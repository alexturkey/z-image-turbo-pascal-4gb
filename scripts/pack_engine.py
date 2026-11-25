#!/usr/bin/env python3
"""Pack the release engine zip the same way every time (standard library only).

  python scripts/pack_engine.py --engine-dir <folder with the 7 binaries> --version 0.3.0 [--out dist]

Writes <out>/sinirsiz-foto-engine-v<version>-win-x64-cuda12.8-sm61.zip and the same name + ".sha256", and prints
  PACK_OK <zip name> <bytes> <sha256>
Same inputs give the same zip, byte for byte: fixed member order, fixed time stamp (1980-01-01), fixed compression.
The numbers go into models.lock.json (name, bytes, sha256).

What goes in: the 7 engine binaries, README.txt (generated here), LICENSE, NOTICE, THIRD_PARTY.md, licenses/ and
patches/LICENSE-MIT from this repository. The NVIDIA DLLs (CUDA runtime, cuDNN) never go in: they are downloaded
separately by scripts/setup.py under NVIDIA's licenses, and the packer copies only the 7 names below.
"""
import argparse
import hashlib
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BINARIES = ["sd-cli.exe", "sd-server.exe", "ggml.dll", "ggml-base.dll", "ggml-cpu.dll", "ggml-cuda.dll",
            "stable-diffusion.dll"]
FIXED_TIME = (1980, 1, 1, 0, 0, 0)
README = """DO NOT DOUBLE-CLICK: sd-cli.exe and sd-server.exe are command-line programs and do not run on their own.

Sinirsiz Foto engine v{version} - prebuilt engine for Windows x64, CUDA 12.8, GPU architecture sm_61 (Pascal, e.g. GTX 10xx).
Based on stable-diffusion.cpp 32d516c + ggml d803c23 (both MIT) plus the patches in the patches/ folder of the Sinirsiz Foto repository (z-image-turbo-pascal-4gb).

What is NOT in this zip (download separately, keep all files in one folder):
  1. NVIDIA CUDA 12.8 runtime DLLs: cudart64_12.dll, cublas64_12.dll, cublasLt64_12.dll (NVIDIA CUDA EULA).
  2. NVIDIA cuDNN 9 DLLs (cudnn64_9.dll and its sub-libraries), only needed for the cuDNN VAE path (NVIDIA cuDNN license).
  3. Microsoft Visual C++ Redistributable x64: https://aka.ms/vs/17/release/vc_redist.x64.exe
  4. An NVIDIA driver that supports CUDA 12.8.
  5. Model files (see the repository docs).

Use it through the scripts of the repository (scripts/setup.py and scripts/generate.py); they set the environment variables for you.
Licenses: LICENSE (Apache-2.0) and NOTICE (author credit), patches/LICENSE-MIT (engine patches), THIRD_PARTY.md, licenses/ (stable-diffusion.cpp, ggml, and the third-party code compiled in).
"""


def members(engine_dir, repo=ROOT, version="0.0.0"):
    """[(archive name, bytes)] in the fixed order; raises FileNotFoundError naming the missing file."""
    out = []
    for name in BINARIES:
        p = Path(engine_dir) / name
        if not p.is_file():
            raise FileNotFoundError("engine binary missing: %s" % p)
        out.append((name, p.read_bytes()))
    out.append(("README.txt", README.format(version=version).encode("utf-8")))
    for name in ("LICENSE", "NOTICE", "THIRD_PARTY.md"):
        out.append((name, (Path(repo) / name).read_bytes()))
    for p in sorted((Path(repo) / "licenses").iterdir()):
        if p.is_file():
            out.append(("licenses/" + p.name, p.read_bytes()))
    out.append(("patches/LICENSE-MIT", (Path(repo) / "patches" / "LICENSE-MIT").read_bytes()))
    return out


def pack(engine_dir, version, out_dir, repo=ROOT):
    name = "sinirsiz-foto-engine-v%s-win-x64-cuda12.8-sm61.zip" % version
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / name
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for arc, data in members(engine_dir, repo, version):
            info = zipfile.ZipInfo(arc, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            info.create_system = 3
            z.writestr(info, data, compresslevel=9)
    sha = hashlib.sha256(target.read_bytes()).hexdigest()
    (out_dir / (name + ".sha256")).write_text("%s  %s\n" % (sha, name), encoding="utf-8")
    return name, target.stat().st_size, sha


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--engine-dir", required=True, help="folder with the 7 engine binaries")
    ap.add_argument("--version", required=True, help="for example 0.3.0 (no leading v)")
    ap.add_argument("--out", default=str(ROOT / "dist"), help="default: ./dist")
    a = ap.parse_args(argv)
    try:
        name, size, sha = pack(a.engine_dir, a.version, a.out)
    except (FileNotFoundError, OSError) as e:
        print("ERROR: %s. Fix: pass --engine-dir with sd-cli.exe, sd-server.exe and the five DLLs of the engine build." % e)
        return 1
    print("PACK_OK %s %d %s" % (name, size, sha))
    return 0


if __name__ == "__main__":
    sys.exit(main())
