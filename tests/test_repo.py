"""Tests for scripts/compare.py and for repository-wide promises (no network, no GPU, no models).

Promises checked here:
  * compare.py decodes PNG pixels itself and reports the same numbers for every PNG filter type
  * every ERROR line printed by the scripts tells the user what to do next
  * the setup preflight only informs and never raises
  * every patch file is plain LF text with an SPDX line, and patches/README.md names each of them
  * relative links in the Markdown files point at files that exist
"""
import contextlib
import hashlib
import importlib.util
import io
import math
import re
import struct
import sys
import tempfile
import unittest
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


compare = load("compare")
setup = load("setup")


def paeth(a, b, c):
    p = a + b - c
    pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
    return a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)


def write_png(path, width, height, rgb, filter_type=0, alpha=False, text=None):
    """Minimal PNG writer for the tests: 8-bit RGB or RGBA, one filter type for all rows."""
    bpp = 4 if alpha else 3
    rows = []
    for y in range(height):
        row = bytearray()
        for x in range(width):
            row += rgb[(y * width + x) * 3:(y * width + x) * 3 + 3]
            if alpha:
                row.append(255)
        rows.append(row)
    raw = bytearray()
    prev = bytearray(width * bpp)
    for row in rows:
        out = bytearray(len(row))
        for i in range(len(row)):
            a = row[i - bpp] if i >= bpp else 0
            b = prev[i]
            c = prev[i - bpp] if i >= bpp else 0
            pred = (0, a, b, (a + b) >> 1, paeth(a, b, c))[filter_type]
            out[i] = (row[i] - pred) & 255
        raw.append(filter_type)
        raw += out
        prev = row

    def chunk(kind, body):
        return struct.pack(">I", len(body)) + kind + body + struct.pack(">I", zlib.crc32(kind + body))

    data = compare.PNG_SIGNATURE + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 6 if alpha else 2, 0, 0, 0))
    if text:
        data += chunk(b"tEXt", b"parameters\x00" + text.encode("latin-1"))
    half = len(raw) // 2
    packed = zlib.compress(bytes(raw))
    data += chunk(b"IDAT", packed[:half]) + chunk(b"IDAT", packed[half:]) + chunk(b"IEND", b"")
    Path(path).write_bytes(data)


def sample(width, height, seed=1):
    return bytes((x * 7 + y * 13 + c * 29 + seed * 31) % 256 for y in range(height) for x in range(width) for c in range(3))


class Compare(unittest.TestCase):
    def test_every_filter_and_alpha_decode_to_the_same_pixels(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            rgb = sample(17, 9)
            want = hashlib.sha256(rgb).hexdigest()
            for f in range(5):
                for alpha in (False, True):
                    p = t / ("f%d_%d.png" % (f, alpha))
                    write_png(p, 17, 9, rgb, f, alpha)
                    self.assertEqual(compare.pixel_sha256(p), (want, 17, 9), (f, alpha))

    def test_text_chunk_changes_the_file_but_not_the_pixels(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            rgb = sample(8, 8)
            write_png(t / "a.png", 8, 8, rgb, 4, text="tile 384")
            write_png(t / "b.png", 8, 8, rgb, 1, text="no tile")
            r = compare.compare(t / "a.png", t / "b.png")
            self.assertFalse(r["file_sha256_equal"])
            self.assertTrue(r["same_pixels"])
            self.assertEqual(r["max_abs_diff"], 0)
            self.assertEqual(r["psnr_db"], math.inf)
            with contextlib.redirect_stdout(io.StringIO()) as out:
                self.assertEqual(compare.main([str(t / "a.png"), str(t / "b.png")]), 0)
            self.assertEqual(out.getvalue().strip().splitlines()[-1], "SAME_PIXELS")

    def test_psnr_and_max_difference(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            a = bytearray(sample(10, 10))
            b = bytearray(a)
            b[0] = (a[0] + 10) % 256 if a[0] <= 245 else a[0] - 10      # one channel of one pixel differs by 10
            write_png(t / "a.png", 10, 10, bytes(a))
            write_png(t / "b.png", 10, 10, bytes(b), 2)
            r = compare.compare(t / "a.png", t / "b.png")
            self.assertEqual(r["max_abs_diff"], 10)
            self.assertEqual(r["psnr_db"], round(10 * math.log10(255 * 255 / (100 / 300)), 2))
            with contextlib.redirect_stdout(io.StringIO()) as out:
                self.assertEqual(compare.main([str(t / "a.png"), str(t / "b.png")]), 1)
            self.assertEqual(out.getvalue().strip().splitlines()[-1], "DIFFERENT")

    def test_bad_input_is_an_error_with_a_fix(self):
        with tempfile.TemporaryDirectory() as t:
            p = Path(t) / "x.png"
            p.write_bytes(b"not a png")
            with contextlib.redirect_stdout(io.StringIO()) as out:
                self.assertEqual(compare.main([str(p), str(p)]), 2)
            self.assertIn("Fix:", out.getvalue())


class Messages(unittest.TestCase):
    """Every ERROR the scripts can print names the next step: a command (Run:/Fix:) or a document."""

    def test_error_lines_carry_a_fix(self):
        for name in ("setup.py", "generate.py", "compare.py"):
            text = (ROOT / "scripts" / name).read_text(encoding="utf-8")
            # a print(...) call that starts an ERROR message, up to the closing parenthesis of the statement
            for m in re.finditer(r'print\(\s*"ERROR:.*?\n(?=\s*(?:return|sys\.exit|raise)\b)', text, re.S):
                block = m.group(0)
                self.assertTrue(re.search(r"Fix:|Run:|docs/", block), "%s: no next step in: %s" % (name, block.strip()[:120]))

    def test_there_are_error_lines_to_check(self):
        text = (ROOT / "scripts" / "setup.py").read_text(encoding="utf-8")
        self.assertGreaterEqual(len(re.findall(r'print\(\s*"ERROR:', text)), 5)


class Preflight(unittest.TestCase):
    def test_reports_and_never_raises(self):
        with tempfile.TemporaryDirectory() as t:
            lines = []
            info = setup.preflight(Path(t) / "m", Path(t) / "b", out=lines.append)
            self.assertIn("gpu", info)
            self.assertTrue(lines[0].startswith("Preflight"))
            self.assertEqual(len([x for x in lines if "Disk" in x]), 2)


class Patches(unittest.TestCase):
    def patches(self):
        return sorted((ROOT / "patches").rglob("*.patch"))

    def test_patch_files_are_clean_text_with_a_license_line(self):
        files = self.patches()
        self.assertGreaterEqual(len(files), 12)
        for p in files:
            data = p.read_bytes()
            self.assertNotIn(b"\x00", data, p.name)
            self.assertNotIn(b"\r\n", data, "%s must keep LF line ends (git apply fails on CRLF)" % p.name)
            self.assertIn(b"SPDX-License-Identifier: MIT", data[:2000], p.name)
            self.assertIn(b"\ndiff --git ", data, p.name)

    def test_readme_names_every_patch(self):
        readme = (ROOT / "patches" / "README.md").read_text(encoding="utf-8")
        for p in self.patches():
            number, rest = p.stem.split("-", 1)
            self.assertTrue(p.name in readme or (number + " " + rest) in readme, p.name)
        self.assertTrue((ROOT / "patches" / "LICENSE-MIT").is_file())


class Links(unittest.TestCase):
    def test_relative_markdown_links_exist(self):
        skip = (".git", "models", "bin", "outputs", ".venv")
        for md in ROOT.rglob("*.md"):
            if any(part in skip for part in md.relative_to(ROOT).parts):
                continue
            text = md.read_text(encoding="utf-8")
            for target in re.findall(r"\]\(([^)\s]+)\)", text):
                if re.match(r"^(https?:|mailto:|#)", target) or target.startswith("../"):
                    continue
                path = (md.parent / target.split("#")[0]).resolve()
                self.assertTrue(path.exists(), "%s links to missing %s" % (md.relative_to(ROOT), target))


if __name__ == "__main__":
    unittest.main()
