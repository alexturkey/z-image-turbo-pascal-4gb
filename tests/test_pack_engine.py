"""Tests for scripts/pack_engine.py (no network, no GPU, no real engine: tiny fake binaries)."""
import contextlib
import hashlib
import importlib.util
import io
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("pack_engine", ROOT / "scripts" / "pack_engine.py")
pack_engine = importlib.util.module_from_spec(spec)
sys.modules["pack_engine"] = pack_engine
spec.loader.exec_module(pack_engine)


def fake_engine(folder):
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    for i, name in enumerate(pack_engine.BINARIES):
        (folder / name).write_bytes(bytes([i]) * 1000)
    # NVIDIA files next to the binaries must never be packed
    for name in ("cudart64_12.dll", "cudnn64_9.dll"):
        (folder / name).write_bytes(b"nvidia")


class Pack(unittest.TestCase):
    def test_same_inputs_same_bytes_and_no_nvidia_files(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            fake_engine(t / "bin")
            a = pack_engine.pack(t / "bin", "9.9.9", t / "o1")
            b = pack_engine.pack(t / "bin", "9.9.9", t / "o2")
            self.assertEqual(a, b)                                    # name, bytes, sha256
            data = (t / "o1" / a[0]).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), a[2])
            self.assertEqual(data, (t / "o2" / b[0]).read_bytes())
            with zipfile.ZipFile(t / "o1" / a[0]) as z:
                names = z.namelist()
                self.assertEqual(names[:7], pack_engine.BINARIES)
                self.assertIn("README.txt", names)
                self.assertIn("patches/LICENSE-MIT", names)
                self.assertIn("LICENSE", names)
                self.assertFalse([n for n in names if "cudart" in n or "cudnn" in n])
                self.assertTrue(all(i.date_time == pack_engine.FIXED_TIME for i in z.infolist()))
                self.assertIn(b"v9.9.9", z.read("README.txt"))
                self.assertIsNone(z.testzip())
            sidecar = (t / "o1" / (a[0] + ".sha256")).read_text(encoding="utf-8")
            self.assertEqual(sidecar, "%s  %s\n" % (a[2], a[0]))

    def test_name_follows_the_lock_file_pattern(self):
        with tempfile.TemporaryDirectory() as t:
            fake_engine(Path(t) / "bin")
            name = pack_engine.pack(Path(t) / "bin", "0.3.0", Path(t) / "o")[0]
            self.assertEqual(name, "sinirsiz-foto-engine-v0.3.0-win-x64-cuda12.8-sm61.zip")

    def test_missing_binary_is_an_error_with_a_fix(self):
        with tempfile.TemporaryDirectory() as t:
            fake_engine(Path(t) / "bin")
            (Path(t) / "bin" / "ggml-cuda.dll").unlink()
            with contextlib.redirect_stdout(io.StringIO()) as out:
                rc = pack_engine.main(["--engine-dir", str(Path(t) / "bin"), "--version", "1.0.0", "--out", str(Path(t) / "o")])
            self.assertEqual(rc, 1)
            self.assertIn("Fix:", out.getvalue())
            self.assertIn("ggml-cuda.dll", out.getvalue())


if __name__ == "__main__":
    unittest.main()
