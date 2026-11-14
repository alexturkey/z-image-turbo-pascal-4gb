"""Tests for scripts/generate.py: fixed recipe, argument checks, log parsing (no GPU, no models)."""
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("generate", ROOT / "scripts" / "generate.py")
gen = importlib.util.module_from_spec(spec)
sys.modules["generate"] = gen
spec.loader.exec_module(gen)


def cmd(**kw):
    a = dict(sd_cli="bin/sd-cli.exe", models_dir="models", prompt_file="p.txt", out_png="o/image.png",
             width=768, height=1344, seed=42)
    a.update(kw)
    return gen.build_command(**a)


def value(c, flag):
    return c[c.index(flag) + 1]


class Recipe(unittest.TestCase):
    def test_fixed_flags(self):
        c = cmd()
        self.assertEqual(value(c, "--cfg-scale"), "1.0")
        self.assertEqual(value(c, "--steps"), "8")
        self.assertEqual(value(c, "--sampling-method"), "euler")
        self.assertEqual(value(c, "--scheduler"), "simple")
        self.assertEqual(value(c, "--flash-attn"), "on")
        for f in ("--offload-to-cpu", "--mmap"):
            self.assertIn(f, c)
        self.assertNotIn("--negative-prompt", c)
        self.assertNotIn("--negative-prompt-file", c)

    def test_models_and_size(self):
        c = cmd(width=1344, height=768, seed=7)
        self.assertTrue(value(c, "--diffusion-model").endswith("z_image_turbo-Q8_0.gguf"))
        self.assertTrue(value(c, "--vae").endswith("ae.safetensors"))
        self.assertTrue(value(c, "--llm").endswith("Qwen3-4B-Instruct-2507-Q8_0.gguf"))
        self.assertEqual((value(c, "-W"), value(c, "-H"), value(c, "-s")), ("1344", "768", "7"))
        self.assertTrue(all(isinstance(x, str) for x in c))

    def test_no_personal_strings(self):
        import re
        text = (ROOT / "scripts" / "generate.py").read_text(encoding="utf-8")
        self.assertIsNone(re.search(r"(?i)[A-Z]:[\\/]+Users", text))


class Args(unittest.TestCase):
    def test_defaults(self):
        a = gen.make_parser().parse_args(["--prompt", "x"])
        self.assertEqual((a.width, a.height, a.seed), (768, 1344, 42))

    def test_prompt_required_and_exclusive(self):
        p = gen.make_parser()
        with self.assertRaises(SystemExit):
            p.parse_args([])
        with self.assertRaises(SystemExit):
            p.parse_args(["--prompt", "a", "--prompt-file", "b"])

    def test_size_checks(self):
        self.assertEqual(gen.check_size(768, 1344), ([], []))
        self.assertEqual(gen.check_size(1344, 768), ([], []))
        errors, _ = gen.check_size(770, 1344)
        self.assertEqual(len(errors), 1)
        errors, _ = gen.check_size(128, 1344)
        self.assertEqual(len(errors), 1)
        errors, warnings = gen.check_size(1024, 1536)
        self.assertEqual((errors, len(warnings)), ([], 1))

    def test_slug(self):
        self.assertEqual(gen.slug("Eiffel Tower!"), "eiffel_tower")
        self.assertEqual(gen.slug("***"), "image")

    def test_main_rejects_bad_size_and_missing_engine(self):
        self.assertEqual(gen.main(["--prompt", "x", "--width", "770"]), 2)
        with tempfile.TemporaryDirectory() as t:
            self.assertEqual(gen.main(["--prompt", "x", "--bin-dir", t, "--models-dir", t, "--out", t]), 2)

    def test_help_exits_zero(self):
        with self.assertRaises(SystemExit) as cm:
            gen.main(["--help"])
        self.assertEqual(cm.exception.code, 0)


class LogParse(unittest.TestCase):
    LOG = ("ggml_cuda_init: found 1 CUDA devices\n"
           "[I] loading tensors completed, taking 0.21s (read: 0.00s)\n"
           "[I] get_learned_condition completed, taking 13.94s --- image.cpp:662\n"
           "[I] sampling completed, taking 203.95s --- image.cpp:1037\n"
           "[W] VAE decode ran out of memory; retrying with spatial tiling --- x\n"
           "[I] decode_first_stage completed, taking 34.17s --- image.cpp:757\n"
           "[I] generate_image completed in 252.18s --- image.cpp:1227\n")

    def test_stages(self):
        s = gen.parse_log(self.LOG)
        self.assertEqual(s["text_encode_s"], 13.94)
        self.assertEqual(s["sampling_s"], 203.95)
        self.assertEqual(s["vae_decode_s"], 34.17)
        self.assertEqual(s["generate_total_s"], 252.18)
        self.assertTrue(s["cuda"])
        self.assertTrue(s["vae_tiling_fallback"])

    def test_empty(self):
        s = gen.parse_log("")
        self.assertIsNone(s["sampling_s"])
        self.assertFalse(s["cuda"])


if __name__ == "__main__":
    unittest.main()
