"""AGENTS_HIZLI.md, docs/hata_imzalari.json and the scripts must say the same thing (no network, no GPU, no models).

The quick card for AI agents promises exit codes and error codes. This test runs the scripts' cheap paths and
compares what they really print with what the card and the code file promise, so a reworded message or a changed
exit code turns the test red instead of silently making the card wrong.
"""
import contextlib
import importlib.util
import io
import json
import re
import sys
import tempfile
import types
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


setup = load("setup")
gen = load("generate")
CARD = (ROOT / "AGENTS_HIZLI.md").read_text(encoding="utf-8")
CODES = json.loads((ROOT / "docs" / "hata_imzalari.json").read_text(encoding="utf-8"))["kodlar"]
SOURCES = (ROOT / "scripts" / "setup.py").read_text(encoding="utf-8") + (ROOT / "scripts" / "generate.py").read_text(encoding="utf-8")
FAKE_LOCK = {"models": [{"name": "a.gguf", "bytes": 10, "sha256": "0" * 64, "url": "https://x/a.gguf"}],
             "engine": [{"name": "e.zip", "bytes": 10, "sha256": "1" * 64, "url": "https://x/e.zip"}]}


def captured(fn, *args):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = fn(*args)
    return rc, buf.getvalue()


class ErrorCodeFile(unittest.TestCase):
    def test_every_message_piece_is_still_in_the_scripts(self):
        for c in CODES:
            with self.subTest(code=c["kod"]):
                self.assertIn(c["kaynak_parca"], SOURCES)

    def test_examples_match_their_own_signatures(self):
        for c in CODES:
            with self.subTest(code=c["kod"]):
                for ex in c["ornek_log"]:
                    self.assertTrue(any(s.lower() in ex.lower() for s in c["imza"]), ex)

    def test_codes_are_unique_and_prefixed(self):
        names = [c["kod"] for c in CODES]
        self.assertEqual(len(names), len(set(names)))
        for n in names:
            self.assertRegex(n, r"^ZIMG-E-[A-Z]+$")

    def test_card_and_file_name_the_same_codes(self):
        in_card = set(re.findall(r"ZIMG-E-[A-Z]+", CARD))
        self.assertEqual(in_card, {c["kod"] for c in CODES})

    def test_both_languages_for_every_code(self):
        for c in CODES:
            for key in ("baslik_en", "baslik_tr", "ilk_adim_en", "ilk_adim_tr"):
                self.assertTrue(c[key].strip(), c["kod"] + " " + key)

    def test_troubleshooting_lists_every_code(self):
        text = (ROOT / "docs" / "TROUBLESHOOTING.md").read_text(encoding="utf-8")
        for c in CODES:
            self.assertIn(c["kod"], text)


class ExitCodes(unittest.TestCase):
    def test_dry_run_writes_nothing_and_ends_with_dryrun_ok(self):
        with tempfile.TemporaryDirectory() as t:
            models, bin_dir = Path(t) / "m" / "deep", Path(t) / "b"
            rc, out = captured(setup.dry_run, FAKE_LOCK, models, bin_dir, False)
            self.assertEqual(rc, 0)
            self.assertTrue(out.strip().splitlines()[-1].startswith("DRYRUN_OK"))
            self.assertIn("would fetch  a.gguf", out)
            self.assertFalse((Path(t) / "m").exists() or bin_dir.exists(), "the dry run created a folder")

    def test_dry_run_without_disk_is_exit_3_with_a_disk_error(self):
        real = setup.shutil.disk_usage
        setup.shutil.disk_usage = lambda p: types.SimpleNamespace(free=0)
        try:
            with tempfile.TemporaryDirectory() as t:
                rc, out = captured(setup.dry_run, FAKE_LOCK, Path(t) / "m", Path(t) / "b", False)
        finally:
            setup.shutil.disk_usage = real
        self.assertEqual(rc, 3)
        disk = [c for c in CODES if c["kod"] == "ZIMG-E-DISK"][0]
        self.assertTrue(any(s.lower() in out.lower() for s in disk["imza"]))
        self.assertIn("Fix:", out)

    def test_dry_run_flag_through_main(self):
        with tempfile.TemporaryDirectory() as t:
            lock = Path(t) / "lock.json"
            lock.write_text(json.dumps(FAKE_LOCK), encoding="utf-8")
            rc, out = captured(setup.main, ["--dry-run", "--lock", str(lock), "--models-dir", str(Path(t) / "m"),
                                            "--bin-dir", str(Path(t) / "b")])
            self.assertEqual(rc, 0)
            self.assertFalse((Path(t) / "m").exists())

    def test_card_exit_codes_are_real(self):
        for row in ("| `setup.py` | 0 |", "| `setup.py` | 3 |", "| `setup.py` | 2 |", "| `setup.py` | 1 |",
                    "| `generate.py` | 2 |", "| `generate.py` | 1 |"):
            self.assertIn(row, CARD)
        with tempfile.TemporaryDirectory() as t:
            missing = Path(t) / "none.json"
            rc, out = captured(setup.main, ["--lock", str(missing)])
            self.assertEqual(rc, 2)
            kilit = [c for c in CODES if c["kod"] == "ZIMG-E-KILIT"][0]
            self.assertTrue(any(s.lower() in out.lower() for s in kilit["imza"]))

    def test_generate_bad_size_is_exit_2_with_its_code_text(self):
        rc, out = captured(gen.main, ["--prompt", "x", "--width", "770"])
        self.assertEqual(rc, 2)
        boyut = [c for c in CODES if c["kod"] == "ZIMG-E-BOYUT"][0]
        self.assertTrue(any(s.lower() in out.lower() for s in boyut["imza"]))

    def test_generate_missing_engine_is_exit_2_with_its_code_text(self):
        with tempfile.TemporaryDirectory() as t:
            rc, out = captured(gen.main, ["--prompt", "x", "--bin-dir", t, "--models-dir", t, "--out", t])
        self.assertEqual(rc, 2)
        motor = [c for c in CODES if c["kod"] == "ZIMG-E-MOTOR"][0]
        self.assertTrue(any(s.lower() in out.lower() for s in motor["imza"]))


class DenetimAndTani(unittest.TestCase):
    def test_denetim_quick_gates_pass_on_this_copy(self):
        den = load("denetim")
        rc, out = captured(den.main, ["--hizli"])
        self.assertEqual(rc, 0, out)
        self.assertEqual(out.strip().splitlines()[-1].split(" ")[0:2], ["SONUC:", "GECTI"])

    def test_denetim_unicode_gate_sees_a_hidden_character(self):
        den = load("denetim")
        with tempfile.TemporaryDirectory() as t:
            (Path(t) / "x.md").write_text("a" + chr(0x202E) + "b\n", encoding="utf-8")
            old = den.ROOT
            den.ROOT = Path(t)
            try:
                ok, lines = den.gate_unicode()
            finally:
                den.ROOT = old
        self.assertFalse(ok)
        self.assertIn("U+202E", lines[0])

    def test_tani_hides_names_and_finds_codes(self):
        tani = load("tani")
        clean = tani.make_filter(["secretword"])
        text = clean("mail me a" + chr(64) + "b.example.com in %s about SecretWord" % str(Path.home()))
        self.assertNotIn("b.example.com", text)
        self.assertNotIn(str(Path.home()), text)
        self.assertNotIn("secretword", text.lower())
        codes = tani.match_codes("ERROR: x.gguf: sha256 mismatch (expected a, got b).")
        self.assertEqual([c["kod"] for c in codes], ["ZIMG-E-SHA"])


if __name__ == "__main__":
    unittest.main()
