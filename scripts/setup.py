#!/usr/bin/env python3
"""Download and verify everything needed to run sinirsiz-foto (Windows, Python 3.10+, standard library only).

What it does (reads models.lock.json in the repo root):
  * downloads the three model files from pinned Hugging Face commits  -> <models-dir>
  * downloads the engine zip and the CUDA runtime zip from our release -> <bin-dir>
  * resumes interrupted downloads (<name>.part), checks size and sha256 of every file
  * never uses "main" / "latest": the lock file pins commits and release tags

Usage:
  python scripts/setup.py [--models-dir DIR] [--bin-dir DIR] [--lock FILE] [--only models|engine] [--check]

Defaults: models/ and bin/ in the repo root. The models are about 11 GB: put --models-dir on an SSD.
Success lines: MODEL_OK <name>, ENGINE_OK, CUDART_OK, final line SETUP_OK. Exit code 0 on success.
Stop with Ctrl+C; run the same command again to continue where it stopped.
"""
import argparse
import hashlib
import json
import shutil
import sys
import time
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHUNK = 1024 * 1024
RETRIES = 6
USER_AGENT = "sinirsiz-foto-setup/1"


def load_lock(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    for key in ("models", "engine"):
        if not isinstance(data.get(key), list) or not data[key]:
            raise ValueError("lock file has no '%s' list" % key)
    return data


def sha256_file(path, label=None, quiet=False):
    h = hashlib.sha256()
    total = Path(path).stat().st_size
    done = 0
    next_mark = 10
    with open(path, "rb") as f:
        while True:
            b = f.read(8 * CHUNK)
            if not b:
                break
            h.update(b)
            done += len(b)
            if not quiet and total > 200 * CHUNK and done * 100 // total >= next_mark:
                print("  hashing %s ... %d%%" % (label or Path(path).name, done * 100 // total), flush=True)
                next_mark += 10
    return h.hexdigest()


def is_verified(path, entry):
    p = Path(path)
    if not p.is_file() or p.stat().st_size != entry["bytes"]:
        return False
    return sha256_file(p, entry["name"]) == entry["sha256"]


def _open(url, start):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    if start > 0:
        req.add_header("Range", "bytes=%d-" % start)
    return urllib.request.urlopen(req, timeout=60)


def download(url, dest, size, sha256, label=None):
    """Download url to dest through dest+'.part' (resumable). Returns True when verified.

    Raises RuntimeError on a hash mismatch (the bad file is removed) or when retries run out.
    """
    dest = Path(dest)
    label = label or dest.name
    part = dest.with_name(dest.name + ".part")
    dest.parent.mkdir(parents=True, exist_ok=True)
    last_err = None
    for attempt in range(1, RETRIES + 1):
        have = part.stat().st_size if part.exists() else 0
        if have > size:
            part.unlink()
            have = 0
        try:
            if have < size:
                with _open(url, have) as r:
                    status = getattr(r, "status", 200)
                    if have and status != 206:
                        have = 0                      # server ignored Range: start over
                    mode = "ab" if have else "wb"
                    got = have
                    next_mark = (got * 100 // size // 10 + 1) * 10 if size else 100
                    t0 = time.time()
                    with open(part, mode) as out:
                        while True:
                            b = r.read(CHUNK)
                            if not b:
                                break
                            out.write(b)
                            got += len(b)
                            if size and got * 100 // size >= next_mark:
                                rate = (got - have) / max(time.time() - t0, 1e-6) / CHUNK
                                print("  %s %d%% (%.1f MiB/s)" % (label, got * 100 // size, rate), flush=True)
                                next_mark += 10
            if part.stat().st_size != size:
                raise OSError("incomplete: %d of %d bytes" % (part.stat().st_size, size))
            break
        except urllib.error.HTTPError as e:
            if e.code == 416 and part.exists() and part.stat().st_size == size:
                break                                 # already complete
            if e.code in (401, 403, 404):
                raise RuntimeError("%s: HTTP %d for %s" % (label, e.code, url))
            last_err = e
        except (urllib.error.URLError, OSError, TimeoutError) as e:
            last_err = e
        if attempt == RETRIES:
            raise RuntimeError("%s: download failed after %d tries (%s). Run setup again to resume." % (label, RETRIES, last_err))
        wait = min(60, 3 * attempt * attempt)
        print("  %s: %s; retry %d/%d in %d s" % (label, last_err.__class__.__name__, attempt, RETRIES - 1, wait), flush=True)
        time.sleep(wait)

    got_hash = sha256_file(part, label)
    if got_hash != sha256:
        part.unlink()
        raise RuntimeError("%s: sha256 mismatch (expected %s, got %s). The partial file was removed; run again." % (label, sha256, got_hash))
    part.replace(dest)
    return True


def safe_extract(zip_path, target):
    """Extract a zip refusing paths that escape the target folder. Returns the list of extracted files."""
    target = Path(target).resolve()
    target.mkdir(parents=True, exist_ok=True)
    out = []
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            dest = (target / info.filename).resolve()
            if target != dest and target not in dest.parents:
                raise RuntimeError("unsafe path in zip: %s" % info.filename)
            z.extract(info, target)
            if not info.is_dir():
                out.append(dest)
    return out


def find_sd_cli(bin_dir):
    bin_dir = Path(bin_dir)
    direct = bin_dir / "sd-cli.exe"
    if direct.is_file():
        return direct
    for p in sorted(bin_dir.rglob("sd-cli.exe")):
        return p
    return None


def has_cudart(bin_dir):
    bin_dir = Path(bin_dir)
    return any(bin_dir.rglob("cudart64_*.dll"))


def check_disk(path, need_bytes):
    Path(path).mkdir(parents=True, exist_ok=True)
    free = shutil.disk_usage(path).free
    if free < need_bytes:
        print("ERROR: %s has %.1f GiB free, about %.1f GiB more is needed." % (path, free / 2**30, need_bytes / 2**30))
        return False
    return True


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--models-dir", default=str(ROOT / "models"), help="where the model files go (default: ./models; an SSD is recommended)")
    ap.add_argument("--bin-dir", default=str(ROOT / "bin"), help="where sd-cli.exe and the CUDA DLLs go (default: ./bin)")
    ap.add_argument("--lock", default=str(ROOT / "models.lock.json"), help="lock file (default: models.lock.json)")
    ap.add_argument("--only", choices=("models", "engine"), help="do only one half")
    ap.add_argument("--check", action="store_true", help="verify files that are already there; download nothing")
    a = ap.parse_args(argv)

    try:
        lock = load_lock(a.lock)
    except (OSError, ValueError) as e:
        print("ERROR: cannot read lock file: %s" % e)
        return 2
    models_dir, bin_dir = Path(a.models_dir), Path(a.bin_dir)
    do_models = a.only in (None, "models")
    do_engine = a.only in (None, "engine")

    try:
        if do_models:
            need = 0
            for m in lock["models"]:
                if not (models_dir / m["name"]).is_file():
                    part = models_dir / (m["name"] + ".part")
                    need += m["bytes"] - (part.stat().st_size if part.exists() else 0)
            if need and not a.check and not check_disk(models_dir, need + 512 * CHUNK):
                return 2
            for m in lock["models"]:
                dest = models_dir / m["name"]
                if is_verified(dest, m):
                    print("MODEL_OK %s" % m["name"])
                    continue
                if a.check:
                    print("MODEL_MISSING_OR_BAD %s" % m["name"])
                    return 1
                if dest.exists():
                    print("  %s is present but does not match the lock; downloading again" % m["name"])
                    dest.unlink()
                print("Downloading %s (%.2f GiB)" % (m["name"], m["bytes"] / 2**30), flush=True)
                download(m["url"], dest, m["bytes"], m["sha256"], m["name"])
                print("MODEL_OK %s" % m["name"])

        if do_engine:
            marker = bin_dir / ".engine_installed.json"
            wanted = {e["name"]: e["sha256"] for e in lock["engine"]}
            try:
                installed = json.loads(marker.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                installed = None
            if installed != wanted or not find_sd_cli(bin_dir) or not has_cudart(bin_dir):
                if a.check:
                    print("ENGINE_MISSING_OR_OLD")
                    return 1
                zips = []
                for e in lock["engine"]:
                    zp = bin_dir / "_downloads" / e["name"]
                    if not is_verified(zp, e):
                        if zp.exists():
                            zp.unlink()
                        if not check_disk(bin_dir, e["bytes"] * 2 + 256 * CHUNK):
                            return 2
                        print("Downloading %s (%.1f MiB)" % (e["name"], e["bytes"] / 2**20), flush=True)
                        download(e["url"], zp, e["bytes"], e["sha256"], e["name"])
                    zips.append(zp)
                for zp in zips:
                    safe_extract(zp, bin_dir)
                shutil.rmtree(bin_dir / "_downloads", ignore_errors=True)   # install source only
                marker.write_text(json.dumps(wanted, indent=1), encoding="utf-8")
            if not find_sd_cli(bin_dir):
                print("ERROR: sd-cli.exe not found in %s" % bin_dir)
                return 1
            print("ENGINE_OK")
            if not has_cudart(bin_dir):
                print("ERROR: cudart64_*.dll not found in %s" % bin_dir)
                return 1
            print("CUDART_OK")
    except RuntimeError as e:
        print("ERROR: %s" % e)
        return 1
    except KeyboardInterrupt:
        print("Interrupted. Run the same command again to continue.")
        return 130

    print("SETUP_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
