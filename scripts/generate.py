#!/usr/bin/env python3
"""Generate one image with Z-Image-Turbo (Q8_0) through sd-cli on a 4 GB Pascal GPU.

Runs the fixed recipe (README.md / AGENTS.md): 8 steps, cfg 1.0, euler + simple, no negative prompt,
--offload-to-cpu --mmap --flash-attn on. Quality settings are fixed on purpose. Python 3.10+, standard library only.

Examples (Windows):
  python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
  python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7

Output: <out>/<YYYYmmdd_HHMMSS>_<name>/image.png + run.json (seconds, stages, VRAM peak from nvidia-smi, command).
Last line on success: IMAGE_OK <path>.
Measured on GTX 1050 Ti 4 GB, 768x1344: about 250-260 s per image; the process uses about 10.5 GB of RAM.
Close browsers and other heavy programs first.
"""
import argparse
import ctypes
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODEL_FILES = {
    "diffusion": "z_image_turbo-Q8_0.gguf",
    "vae": "ae.safetensors",
    "llm": "Qwen3-4B-Instruct-2507-Q8_0.gguf",
}
STEPS = 8
CFG = "1.0"
DEFAULT_SEED = 42
DEFAULT_W, DEFAULT_H = 768, 1344           # portrait; landscape is 1344x768
TESTED_PIXELS = 768 * 1344
LOW_RAM_MIB = 8000
NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)


def fwd(p):
    return str(p).replace("\\", "/")


def build_command(sd_cli, models_dir, prompt_file, out_png, width, height, seed):
    """The fixed sd-cli command line (list of strings). The tests pin this recipe."""
    m = Path(models_dir)
    return [
        str(sd_cli),
        "--diffusion-model", fwd(m / MODEL_FILES["diffusion"]),
        "--vae", fwd(m / MODEL_FILES["vae"]),
        "--llm", fwd(m / MODEL_FILES["llm"]),
        "--prompt-file", fwd(prompt_file),
        "--cfg-scale", CFG, "--steps", str(STEPS),
        "--sampling-method", "euler", "--scheduler", "simple",
        "--offload-to-cpu", "--mmap", "--flash-attn", "on",
        "-s", str(seed), "-W", str(width), "-H", str(height),
        "-v", "-o", fwd(out_png),
    ]


def make_parser():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--prompt", help="prompt text (natural language; the example prompts in this repo are English)")
    g.add_argument("--prompt-file", help="UTF-8 text file with the prompt")
    ap.add_argument("--width", type=int, default=DEFAULT_W, help="pixels, multiple of 16 (default %d)" % DEFAULT_W)
    ap.add_argument("--height", type=int, default=DEFAULT_H, help="pixels, multiple of 16 (default %d)" % DEFAULT_H)
    ap.add_argument("--seed", type=int, default=DEFAULT_SEED, help="default %d" % DEFAULT_SEED)
    ap.add_argument("--out", default=str(ROOT / "outputs"), help="output root (default: ./outputs)")
    ap.add_argument("--name", help="short name in the output folder (default: prompt file name, or 'image')")
    ap.add_argument("--models-dir", default=str(ROOT / "models"), help="default: ./models")
    ap.add_argument("--bin-dir", default=str(ROOT / "bin"), help="default: ./bin (sd-cli.exe and CUDA DLLs)")
    return ap


def check_size(width, height):
    """Return (errors, warnings) for the requested size."""
    errors, warnings = [], []
    for label, v in (("width", width), ("height", height)):
        if v < 256 or v > 2048 or v % 16:
            errors.append("--%s %d: must be a multiple of 16 between 256 and 2048" % (label, v))
    if not errors and width * height > TESTED_PIXELS:
        warnings.append("%dx%d is larger than the tested 768x1344 (not tested on 4 GB; it may run out of memory)" % (width, height))
    return errors, warnings


def slug(text):
    s = re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_").lower()
    return s[:40] or "image"


def find_sd_cli(bin_dir):
    bin_dir = Path(bin_dir)
    if (bin_dir / "sd-cli.exe").is_file():
        return bin_dir / "sd-cli.exe"
    for p in sorted(bin_dir.rglob("sd-cli.exe")):
        return p
    return None


def free_ram_mib():
    if os.name != "nt":
        return None

    class MS(ctypes.Structure):
        _fields_ = [("l", ctypes.c_ulong), ("load", ctypes.c_ulong), ("total", ctypes.c_ulonglong),
                    ("avail", ctypes.c_ulonglong), ("tp", ctypes.c_ulonglong), ("ap", ctypes.c_ulonglong),
                    ("tv", ctypes.c_ulonglong), ("av", ctypes.c_ulonglong), ("ae", ctypes.c_ulonglong)]
    ms = MS()
    ms.l = ctypes.sizeof(MS)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(ms)):
        return None
    return int(ms.avail // (1024 * 1024))


def gpu_used_mib():
    exe = shutil.which("nvidia-smi")
    if not exe:
        return None
    try:
        r = subprocess.run([exe, "--query-gpu=memory.used", "--format=csv,noheader,nounits"],
                           capture_output=True, text=True, timeout=10, creationflags=NO_WINDOW)
        return int(r.stdout.strip().splitlines()[0]) if r.returncode == 0 and r.stdout.strip() else None
    except (OSError, ValueError, subprocess.SubprocessError, IndexError):
        return None


class Monitor(threading.Thread):
    """Samples GPU memory (nvidia-smi) and free RAM every 2 s while sd-cli runs."""

    def __init__(self):
        super().__init__(daemon=True)
        self.stop_event = threading.Event()
        self.vram_peak = None
        self.ram_free_min = None
        self.baseline = gpu_used_mib()

    def run(self):
        while not self.stop_event.is_set():
            v = gpu_used_mib()
            if v is not None and (self.vram_peak is None or v > self.vram_peak):
                self.vram_peak = v
            r = free_ram_mib()
            if r is not None and (self.ram_free_min is None or r < self.ram_free_min):
                self.ram_free_min = r
            self.stop_event.wait(2.0)

    def finish(self):
        self.stop_event.set()
        self.join(timeout=10)


def parse_log(text):
    """Pull stage times (seconds) out of the sd-cli verbose log."""
    def sec(pattern):
        m = re.search(pattern + r" completed(?: in|, taking) ([0-9.]+)\s*(ms|s)\b", text)
        if not m:
            return None
        v = float(m.group(1))
        return round(v / 1000 if m.group(2) == "ms" else v, 2)
    return {
        "text_encode_s": sec(r"get_learned_condition"),
        "sampling_s": sec(r"sampling"),
        "vae_decode_s": sec(r"decode_first_stage"),
        "generate_total_s": sec(r"generate_image"),
        "cuda": "ggml_cuda_init: found" in text,
        "vae_tiling_fallback": "retrying with spatial tiling" in text,
    }


def main(argv=None):
    a = make_parser().parse_args(argv)
    errors, warnings = check_size(a.width, a.height)
    if errors:
        for e in errors:
            print("ERROR: " + e)
        return 2

    sd_cli = find_sd_cli(a.bin_dir)
    if sd_cli is None:
        print("ERROR: sd-cli.exe not found in %s. Run: python scripts/setup.py" % a.bin_dir)
        return 2
    for f in MODEL_FILES.values():
        if not (Path(a.models_dir) / f).is_file():
            print("ERROR: missing model file %s. Run: python scripts/setup.py" % (Path(a.models_dir) / f))
            return 2
    if a.prompt_file:
        try:
            prompt = Path(a.prompt_file).read_text(encoding="utf-8").strip()
        except OSError as e:
            print("ERROR: cannot read prompt file (%s)" % e.__class__.__name__)
            return 2
    else:
        prompt = a.prompt.strip()
    if not prompt:
        print("ERROR: the prompt is empty")
        return 2
    for w in warnings:
        print("WARNING: " + w)
    ram = free_ram_mib()
    if ram is not None and ram < LOW_RAM_MIB:
        print("WARNING: only %d MiB RAM free; the run uses about 10.5 GB of process memory (measured). Close other programs." % ram)

    name = slug(a.name or (Path(a.prompt_file).stem if a.prompt_file else "image"))
    out = (Path(a.out) / ("%s_%s" % (time.strftime("%Y%m%d_%H%M%S"), name))).resolve()
    out.mkdir(parents=True, exist_ok=True)
    prompt_path = out / "prompt.txt"
    prompt_path.write_text(prompt, encoding="utf-8")
    image = out / "image.png"
    cmd = build_command(sd_cli, a.models_dir, prompt_path, image, a.width, a.height, a.seed)
    (out / "command.txt").write_text(subprocess.list2cmdline(cmd) + "\n", encoding="utf-8")
    env = dict(os.environ)
    env["PATH"] = str(sd_cli.parent) + os.pathsep + env.get("PATH", "")

    print("%dx%d seed=%d steps=%d -> %s" % (a.width, a.height, a.seed, STEPS, out))
    print("Started. Expected about 4-5 minutes on a GTX 1050 Ti (measured). Log: %s" % (out / "log.txt"), flush=True)
    mon = Monitor()
    mon.start()
    t0 = time.time()
    try:
        with open(out / "log.txt", "w", encoding="utf-8", errors="replace") as log:
            p = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT, env=env, creationflags=NO_WINDOW)
            try:
                rc = p.wait()
            except KeyboardInterrupt:
                p.terminate()
                print("Interrupted; a generation cannot resume, start it again.")
                return 130
    finally:
        mon.finish()
    secs = round(time.time() - t0, 1)

    try:
        stages = parse_log((out / "log.txt").read_text(encoding="utf-8", errors="replace"))
    except OSError:
        stages = {}
    ok = rc == 0 and image.is_file() and image.stat().st_size > 0
    info = {
        "result": "OK" if ok else "FAILED", "exit_code": rc, "seconds": secs,
        "width": a.width, "height": a.height, "seed": a.seed, "steps": STEPS, "cfg": float(CFG),
        "stages": stages,
        "gpu_memory_used_peak_mib": mon.vram_peak, "gpu_memory_used_before_mib": mon.baseline,
        "ram_free_min_mib": mon.ram_free_min,
        "command": cmd,
    }
    (out / "run.json").write_text(json.dumps(info, indent=1), encoding="utf-8")
    if not ok:
        print("FAILED: sd-cli exit code %s. Read %s and docs/TROUBLESHOOTING.md." % (rc, out / "log.txt"))
        return 1
    print("%.0f s" % secs)
    print("IMAGE_OK %s" % image)
    return 0


if __name__ == "__main__":
    sys.exit(main())
