#!/usr/bin/env python3
"""Local diagnosis report you can paste into an issue: python scripts/tani.py [--log FILE ...] [--kart-satiri]

What it does: collects a short report (operating system, Python, GPU from nvidia-smi, RAM, free disk, the repository
version, the dry run of scripts/setup.py) and, if you name log files with --log, matches their text against
docs/hata_imzalari.json (plain substrings) and lists the stable error codes with the first step.
What it never does: it sends NOTHING (no network, it does not upload or post anything), writes no file, installs nothing,
opens no window. It only prints.
Privacy filter: your user name, computer name, home folder and e-mail addresses are replaced with <...> markers before
anything is shown; folder paths under your home become <HOME>. The filter is a rough pattern: READ the report before
you paste it; it is not a guarantee. Extra words to hide: --gizle word1 word2.
--kart-satiri prints one line (GPU, memory, driver, RAM, OS) for an issue title.
Exit code: 0 the report was made (even if errors were found in a log), 6 it could not run.
"""
import argparse
import getpass
import json
import os
import platform
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

ROOT = Path(__file__).resolve().parent.parent
NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)
EMAIL = re.compile(r"[A-Za-z0-9._%+\-]{1,64}@[A-Za-z0-9\-]{1,63}(?:\.[A-Za-z0-9\-]{1,63})*\.[A-Za-z]{2,24}")
TOKEN = re.compile(r"\b(?:ghp|gho|ghs|github_pat|hf)_[A-Za-z0-9_]{20,}\b")


def hide_words(extra):
    words = []
    for w in [safe(getpass.getuser), os.environ.get("USERNAME"), os.environ.get("COMPUTERNAME"), safe(platform.node)] + list(extra):
        if w and len(w.strip()) >= 3 and w.strip() not in words:
            words.append(w.strip())
    return words


def safe(fn):
    try:
        return fn()
    except Exception:  # noqa: BLE001 - a missing user name must never stop the report
        return None


def make_filter(extra):
    words = hide_words(extra)
    home = str(Path.home())
    homes = {home, home.replace("\\", "/")}

    def clean(text):
        for h in sorted(homes, key=len, reverse=True):
            text = re.sub(re.escape(h), "<HOME>", text, flags=re.I)
        text = EMAIL.sub("<EMAIL>", text)
        text = TOKEN.sub("<TOKEN>", text)
        for w in words:
            text = re.sub(re.escape(w), "<NAME>", text, flags=re.I)
        # 8.3 short names such as USERNA~1 hide a user name too
        text = re.sub(r"\b[A-Za-z0-9_]{1,8}~\d\b", "<SHORT>", text)
        return text
    return clean


def run(cmd, timeout=60):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, creationflags=NO_WINDOW)
        return r.returncode, (r.stdout or "") + (r.stderr or "")
    except (OSError, subprocess.SubprocessError):
        return None, ""


def gpu_line():
    exe = shutil.which("nvidia-smi")
    if not exe:
        return None
    rc, out = run([exe, "--query-gpu=name,memory.total,driver_version", "--format=csv,noheader"], 15)
    return out.strip().splitlines()[0] if rc == 0 and out.strip() else None


def ram_mib():
    if os.name != "nt":
        try:
            for line in Path("/proc/meminfo").read_text().splitlines():
                if line.startswith("MemTotal"):
                    return int(line.split()[1]) // 1024
        except OSError:
            return None
        return None
    try:
        import ctypes

        class MS(ctypes.Structure):
            _fields_ = [("l", ctypes.c_ulong), ("load", ctypes.c_ulong), ("total", ctypes.c_ulonglong),
                        ("avail", ctypes.c_ulonglong), ("tp", ctypes.c_ulonglong), ("ap", ctypes.c_ulonglong),
                        ("tv", ctypes.c_ulonglong), ("av", ctypes.c_ulonglong), ("ae", ctypes.c_ulonglong)]
        ms = MS()
        ms.l = ctypes.sizeof(MS)
        if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(ms)):
            return int(ms.total // (1024 * 1024))
    except (OSError, AttributeError):
        pass
    return None


def version():
    try:
        for line in (ROOT / "CHANGELOG.md").read_text(encoding="utf-8").splitlines():
            m = re.match(r"## \[(\d[^\]]*)\]", line)
            if m:
                return m.group(1)
    except OSError:
        pass
    return "unknown"


def card_line():
    g = gpu_line() or "no NVIDIA GPU found"
    r = ram_mib()
    return "%s | RAM %s | %s %s" % (g, "%d MiB" % r if r else "unknown", platform.system(), platform.release())


def match_codes(text):
    path = ROOT / "docs" / "hata_imzalari.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []
    low = text.lower()
    return [c for c in data["kodlar"] if any(s.lower() in low for s in c["imza"])]


def main(argv=None):
    ap = argparse.ArgumentParser(description="Local diagnosis report (sends nothing).")
    ap.add_argument("--log", nargs="*", default=[], help="log files to match against the error codes (e.g. outputs/<run>/log.txt)")
    ap.add_argument("--gizle", nargs="*", default=[], help="extra words to hide")
    ap.add_argument("--kart-satiri", action="store_true", help="one line for an issue title")
    ap.add_argument("--atla-kuru", action="store_true", help="skip the setup.py --dry-run part")
    a = ap.parse_args(argv)
    clean = make_filter(a.gizle)
    if a.kart_satiri:
        print(clean(card_line()))
        return 0
    lines = ["# zimg diagnosis (local; nothing was sent)", "repository version : %s" % version(),
             "OS                 : %s %s (%s)" % (platform.system(), platform.release(), platform.version()),
             "Python             : %s" % platform.python_version(),
             "GPU                : %s" % (gpu_line() or "no NVIDIA GPU found (nvidia-smi missing or silent)"),
             "RAM                : %s" % ("%d MiB total" % ram_mib() if ram_mib() else "unknown"),
             "free disk (repo)   : %.1f GiB" % (shutil.disk_usage(ROOT).free / 2**30)]
    found_text = ""
    if not a.atla_kuru:
        rc, out = run([sys.executable, "-I", "-X", "utf8", str(ROOT / "scripts" / "setup.py"), "--dry-run"], 60)
        lines += ["", "## setup.py --dry-run (exit code %s; writes nothing)" % rc] + out.strip().splitlines()
        found_text += out
    for name in a.log:
        p = Path(name)
        try:
            body = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            lines += ["", "## log %s: cannot be read" % p.name]
            continue
        tail = body.strip().splitlines()[-30:]
        lines += ["", "## last lines of %s" % p.name] + tail
        found_text += body
    codes = match_codes(found_text)
    lines += ["", "## error codes found (docs/hata_imzalari.json)"]
    if codes:
        for c in codes:
            lines += ["%s: %s" % (c["kod"], c["baslik_en"]), "   first step: %s" % c["ilk_adim_en"]]
    else:
        lines.append("none matched")
    print(clean("\n".join(lines)))
    print("\nRead this before you paste it: names, e-mail addresses and your home folder were replaced, but the filter is not a guarantee.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:  # noqa: BLE001
        print("ERROR: the report could not be made (%s). Fix: run it from a complete copy of the repository." % e.__class__.__name__)
        sys.exit(6)
