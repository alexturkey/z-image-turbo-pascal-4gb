#!/usr/bin/env python3
"""Byte-level privacy scan of a file tree.

Scans every file (text and binary) for personal traces. The script contains NO
personal values: what to look for is passed in at run time.

Built-in generic checks (always on):
  - e-mail address pattern
  - messenger and social-media traces (messenger links or names, X profile links)
  - an absolute Windows user path: <drive>:\\Users\\<name> or <drive>:/Users/<name>
    (the names Public, Default, All Users and <placeholder> forms are ignored)

Patterns you supply (case-insensitive, matched as raw bytes in UTF-8 and UTF-16LE):
  --pattern TEXT          literal text, repeatable (user name, machine name, ...)
  --patterns-file FILE    one literal per line; lines starting with # are skipped.
                          Keep this file outside the tree you scan and out of git.
  env PRIVACY_PATTERNS    literals separated by ';' (alternative to the file)

Output never prints the matched text: it prints the file, the byte offset and the
rule (for supplied patterns, the pattern NUMBER, not its value).

Exit code: 0 clean, 1 findings, 2 usage error.

Usage:
    python privacy_scan.py <tree> [--pattern X ...] [--patterns-file F]
                           [--skip-dir NAME ...] [--max-mb 512] [--scan-licenses]
"""
import argparse
import os
import re
import sys
from pathlib import Path

GENERIC = [
    ("email", re.compile(rb"[A-Za-z0-9._%+\-]{1,64}@[A-Za-z0-9\-]{1,63}(?:\.[A-Za-z0-9\-]{1,63})*\.[A-Za-z]{2,24}")),
    ("messenger", re.compile(rb"(?i)(?:t\.m" rb"e/|tele" rb"gram)")),
    ("x-twitter-handle", re.compile(rb"(?i)(?:x\.com|twitter\.com)/[A-Za-z0-9_]{1,15}")),
    ("windows-user-path", re.compile(
        rb"(?i)[A-Z]:[\\/]+Users[\\/]+(?![<%$\{])(?!(?:Public|Default|All Users|Default User)(?:[\\/]|$))"
        rb"[^\\/\s\"'<>|:*?]{1,64}")),
]
# UTF-16LE variant of the user-path rule (strings embedded in binaries).
GENERIC_U16 = [
    ("windows-user-path (utf-16le)", re.compile(
        rb"(?i)[A-Z]\x00:\x00[\\/]\x00(?:[\\/]\x00)*U\x00s\x00e\x00r\x00s\x00[\\/]\x00"
        rb"(?!<\x00)(?!P\x00u\x00b\x00l\x00i\x00c\x00)(?!D\x00e\x00f\x00a\x00u\x00l\x00t\x00)"
        rb"(?:[A-Za-z0-9_.\-]\x00){2,64}")),
]

DEFAULT_SKIP = {".git"}
# Top-level licenses/ holds upstream license texts verbatim. BSD/MIT licenses require the original
# copyright line, which can contain the upstream author's e-mail. Those are not our personal traces.
# Only the folder directly under the scanned root is skipped (override: --scan-licenses).
UPSTREAM_LICENSES_DIR = "licenses"


def load_literals(args) -> list:
    lits = list(args.pattern or [])
    if args.patterns_file:
        for line in Path(args.patterns_file).read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                lits.append(line)
    env = os.environ.get("PRIVACY_PATTERNS", "")
    lits += [x.strip() for x in env.split(";") if x.strip()]
    return lits


def build_literal_rules(lits):
    rules = []
    for i, lit in enumerate(lits, 1):
        for enc in ("utf-8", "utf-16le"):
            rules.append(("supplied-pattern #%d (%s)" % (i, enc),
                          re.compile(re.escape(lit.encode(enc)), re.IGNORECASE)))
    return rules


def scan_file(path: Path, rules):
    data = path.read_bytes()
    return [(m.start(), name) for name, rx in rules for m in rx.finditer(data)]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("tree", type=Path)
    ap.add_argument("--pattern", action="append")
    ap.add_argument("--patterns-file")
    ap.add_argument("--skip-dir", action="append", default=[])
    ap.add_argument("--scan-licenses", action="store_true",
                    help="also scan <tree>/licenses (skipped by default: verbatim upstream license texts)")
    ap.add_argument("--max-mb", type=int, default=512, help="files larger than this are skipped and reported")
    a = ap.parse_args(argv)

    if not a.tree.exists():
        print("not found: %s" % a.tree, file=sys.stderr)
        return 2
    try:
        lits = load_literals(a)
    except OSError as e:
        print("cannot read patterns file: %s" % e.__class__.__name__, file=sys.stderr)
        return 2

    rules = GENERIC + GENERIC_U16 + build_literal_rules(lits)
    skip = DEFAULT_SKIP | set(a.skip_dir)

    if a.tree.is_file():
        files, base = [a.tree], a.tree.parent
    else:
        files, base = [], a.tree
        for root, dirs, names in os.walk(a.tree):
            dirs[:] = [d for d in dirs if d not in skip
                       and not (not a.scan_licenses and Path(root) == a.tree and d == UPSTREAM_LICENSES_DIR)]
            files += [Path(root) / n for n in names]

    findings = scanned = 0
    skipped_big = []
    for p in sorted(files):
        try:
            if p.stat().st_size > a.max_mb * 1024 * 1024:
                skipped_big.append(p)
                continue
            hits = scan_file(p, rules)
        except OSError as e:
            print("UNREADABLE %s (%s)" % (p.relative_to(base), e.__class__.__name__))
            findings += 1
            continue
        scanned += 1
        for off, name in hits:
            print("%s @%d  %s" % (p.relative_to(base), off, name))
            findings += 1
    for p in skipped_big:
        print("SKIPPED (over %d MB, scan it separately): %s" % (a.max_mb, p.relative_to(base)))
    if a.tree.is_dir() and not a.scan_licenses and (a.tree / UPSTREAM_LICENSES_DIR).is_dir():
        print("NOTE: %s/ not scanned (verbatim upstream license texts); use --scan-licenses to include it" % UPSTREAM_LICENSES_DIR)
    status = "FINDINGS" if findings else ("CLEAN_WITH_SKIPS" if skipped_big else "CLEAN")
    print("%s: %d file(s) scanned, %d finding(s), %d supplied pattern(s)" % (status, scanned, findings, len(lits)))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
