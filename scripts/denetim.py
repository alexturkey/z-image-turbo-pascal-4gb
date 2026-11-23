#!/usr/bin/env python3
"""Repository check before a pull request: python -I -X utf8 scripts/denetim.py --hizli

Quick gates (seconds, no network, no GPU, writes nothing, opens no window):
  unicode   no invisible or bidirectional characters and no control bytes in text files (Trojan Source, hidden text)
  gizlilik  scripts/privacy_scan.py on the whole tree (personal paths, e-mail addresses, messenger traces)
  sabitler  the fixed quality settings in scripts/generate.py are unchanged (8 steps, cfg 1.0)
  kilit     models.lock.json is valid JSON and every address is pinned (no "main", no "latest")
  imzalar   docs/hata_imzalari.json is valid and its message pieces still exist in the scripts
--tam additionally runs the unit tests (python -B -m unittest discover -s tests); that takes longer.

Exit code: 0 all gates passed, 1 at least one gate is red, 3 input or environment missing (not run from a repository
copy), 6 a gate could not run. The last line is a single line: SONUC: GECTI (passed) or SONUC: KIRMIZI (red) or
SONUC: CALISMADI (a gate could not run).
Not run here: engine, models, GPU. A passed check is a hygiene check, not proof that the repository works on your card.
"""
import argparse
import json
import re
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
TEXT_SUFFIXES = {".py", ".md", ".json", ".yml", ".yaml", ".txt", ".cmd", ".toml", ".cfg", ".gitignore", ".gitattributes", ".lock"}
SKIP_DIRS = {".git", "models", "bin", "outputs", "__pycache__", ".venv", ".pytest_cache"}
# code points that can hide text: zero width, bidirectional controls, soft hyphen, BOM, line/paragraph separators
HIDDEN = set(range(0x200B, 0x2010)) | set(range(0x202A, 0x202F)) | set(range(0x2060, 0x206A)) | \
    {0x00AD, 0xFEFF, 0x2028, 0x2029, 0x061C, 0x180E}
NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)


def text_files():
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        parts = set(path.relative_to(ROOT).parts)
        if parts & SKIP_DIRS:
            continue
        if path.suffix.lower() in TEXT_SUFFIXES or path.name in (".gitignore", ".gitattributes"):
            yield path


def gate_unicode():
    bad = []
    for path in text_files():
        try:
            text = path.read_bytes().decode("utf-8")
        except UnicodeDecodeError:
            bad.append("%s: not valid UTF-8" % path.relative_to(ROOT).as_posix())
            continue
        found = sorted({"U+%04X" % ord(ch) for ch in text
                        if ord(ch) in HIDDEN or (ord(ch) < 32 and ch not in "\n\r\t") or ord(ch) == 0x7F})
        if found:
            bad.append("%s: %s" % (path.relative_to(ROOT).as_posix(), " ".join(found)))
    return not bad, bad or ["no hidden characters in text files"]


def gate_privacy():
    scan = ROOT / "scripts" / "privacy_scan.py"
    if not scan.is_file():
        raise RuntimeError("scripts/privacy_scan.py not found")
    r = subprocess.run([sys.executable, "-I", "-X", "utf8", str(scan), str(ROOT)], capture_output=True, text=True,
                       timeout=300, creationflags=NO_WINDOW)
    last = (r.stdout.strip().splitlines() or ["(no output)"])[-1]
    if r.returncode not in (0, 1):
        raise RuntimeError("privacy_scan.py exit code %d" % r.returncode)
    return r.returncode == 0, [last]


def gate_constants():
    src = (ROOT / "scripts" / "generate.py").read_text(encoding="utf-8")
    ok = re.search(r"^STEPS = 8$", src, re.M) is not None and re.search(r'^CFG = "1\.0"$', src, re.M) is not None
    return ok, ["STEPS = 8 and CFG = \"1.0\" in scripts/generate.py" if ok else
                "the fixed quality settings changed (STEPS must be 8, CFG must be \"1.0\"): image quality is never lowered"]


def gate_lock():
    lock = json.loads((ROOT / "models.lock.json").read_text(encoding="utf-8"))
    entries = list(lock["models"]) + list(lock["engine"]) + ([lock["cudnn"]] if isinstance(lock.get("cudnn"), dict) else [])
    floating = [e["name"] for e in entries if re.search(r"/(main|master|latest)(/|$)", e["url"])]
    if floating:
        return False, ["a floating reference (main/latest) in the download address of: " + ", ".join(floating)]
    return True, ["models.lock.json is valid and every download address is pinned"]


def gate_signatures():
    path = ROOT / "docs" / "hata_imzalari.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    sources = "".join((ROOT / "scripts" / n).read_text(encoding="utf-8") for n in ("setup.py", "generate.py"))
    missing = [c["kod"] for c in data["kodlar"] if c["kaynak_parca"] not in sources]
    return not missing, missing and ["message piece no longer in the scripts: " + ", ".join(missing)] or \
        ["%d error codes, all message pieces found" % len(data["kodlar"])]


def gate_tests():
    r = subprocess.run([sys.executable, "-B", "-X", "utf8", "-m", "unittest", "discover", "-s", "tests"], cwd=str(ROOT),
                       capture_output=True, text=True, timeout=1800, creationflags=NO_WINDOW)
    tail = (r.stderr.strip().splitlines() or r.stdout.strip().splitlines() or ["(no output)"])[-1]
    return r.returncode == 0, [tail]


def main(argv=None):
    ap = argparse.ArgumentParser(description="Repository check (hygiene gates).")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--hizli", action="store_true", help="quick gates (default)")
    g.add_argument("--tam", action="store_true", help="quick gates and the unit tests")
    a = ap.parse_args(argv)
    for need in ("scripts/generate.py", "models.lock.json"):
        if not (ROOT / need).is_file():
            print("ERROR: %s not found. Fix: run from a complete copy of the repository." % need)
            print("SONUC: CALISMADI (exit 3)")
            return 3
    gates = [("unicode", gate_unicode), ("gizlilik", gate_privacy), ("sabitler", gate_constants),
             ("kilit", gate_lock), ("imzalar", gate_signatures)]
    if a.tam:
        gates.append(("testler", gate_tests))
    red = broken = 0
    for name, fn in gates:
        try:
            ok, lines = fn()
        except (OSError, ValueError, KeyError, RuntimeError, subprocess.SubprocessError) as e:
            broken += 1
            print("CALISMADI  %-9s %s" % (name, e.__class__.__name__ + ": " + str(e)[:160]))
            continue
        print("%-10s %-9s %s" % ("GECTI" if ok else "KIRMIZI", name, lines[0]))
        for extra in lines[1:6]:
            print("           %s" % extra)
        red += 0 if ok else 1
    if broken:
        print("SONUC: CALISMADI (%d gate could not run, %d red; exit 6)" % (broken, red))
        return 6
    if red:
        print("SONUC: KIRMIZI (%d gate red; exit 1)" % red)
        return 1
    print("SONUC: GECTI (%d gates passed; exit 0)" % len(gates))
    return 0


if __name__ == "__main__":
    sys.exit(main())
