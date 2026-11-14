[Türkçe](README.tr.md) · **English**

# sinirsiz-foto

**Text-to-image with Z-Image-Turbo on a 4 GB GTX 1050 Ti (Windows).** A small, reproducible setup: pinned model files
with sha256 checks, a prebuilt Pascal-patched engine, two Python scripts (standard library only), and the measurements
behind the settings. One 768x1344 picture takes about four minutes on this card.

- **Who it is for:** owners of an old 4 GB NVIDIA card (Pascal, compute capability 6.1). Only the GTX 1050 Ti 4 GB laptop card was measured; other cards are not tested.
  Also for coding agents: [`AGENTS.md`](AGENTS.md) is a step-by-step install they can follow.
- **What you get:** Z-Image-Turbo (Q8_0) with a Qwen3-4B-Instruct-2507 (Q8_0) text encoder, 8 steps, no negative prompt, portrait 768x1344 by default.
- **What it costs:** time and RAM. About 250-259 s per picture and a free-RAM low point of 331-576 MiB on a 16 GB machine (see [measurements](docs/MEASUREMENTS.md)). Close other programs while it runs.

[Install guide for AI agents](AGENTS.md) · [Measurements](docs/MEASUREMENTS.md) · [Prompts](docs/PROMPTS.md) · [Troubleshooting](docs/TROUBLESHOOTING.md) · [Third-party](THIRD_PARTY.md) · [Changelog](CHANGELOG.md)

## Examples

**AI-generated with this repo** (Z-Image-Turbo Q8_0, seed 42, 8 steps). These are not real photographs; landmarks and details
may be inaccurate. The exact prompts are in [`prompts/`](prompts) and [`docs/PROMPTS.md`](docs/PROMPTS.md).

| | | |
|---|---|---|
| ![Eiffel Tower at golden hour](docs/examples/eiffel.jpg) | ![Turkish tea glass](docs/examples/turkish_tea.jpg) | ![Elderly fisherman](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![Hillside village](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344. The round doors came out as separate huts, not dug into the hill: prompt match was partial. | | |

![Istanbul from the air](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. Not a real photo; landmarks may be inaccurate.

## Quick start

Requirements: Windows 10/11, an NVIDIA GPU with 4 GB, a recent driver (CUDA 12.8 runtime is downloaded for you),
Python 3.10 or newer, about 13 GB free disk (downloads are about 11.8 GB), and 16 GB RAM (what was measured; less is not tested).

```powershell
git clone https://github.com/alexturkey/sinirsiz-foto.git
cd sinirsiz-foto
python scripts/setup.py --models-dir D:\models --bin-dir D:\bin
python scripts/generate.py --prompt-file prompts/eiffel.txt --models-dir D:\models --bin-dir D:\bin
```

- `setup.py` downloads from pinned URLs listed in [`models.lock.json`](models.lock.json) and checks every file with sha256.
  It prints `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK` and finally `SETUP_OK`. Without `--models-dir` and `--bin-dir` it uses `models/` and `bin/` in the repo root; putting the models on an SSD is recommended (measured on an SSD only).
- `generate.py` writes `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png` and `run.json` (time, stages, peak VRAM read from nvidia-smi, the exact command) and prints `IMAGE_OK <path>`.
- Options: `--prompt "<text>"` or `--prompt-file <txt>`, `--width 768 --height 1344 --seed 42 --out outputs/`.
  Use `--width 1344 --height 768` for landscape.

Download size: about 11.8 GB (models 11,193,150,692 bytes, engine zip 37,182,063 bytes, CUDA runtime zip 567,007,257 bytes, from the sizes in `models.lock.json`).

## What it runs

| Part | File | Source |
|---|---|---|
| Diffusion model | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), base [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Text encoder | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), FLUX.1-type autoencoder |
| Engine | `sd-cli.exe`, stable-diffusion.cpp `master-1088-32d516c` with four Pascal patches | zip from the [wan22-pascal-4gb v0.1.0 release](https://github.com/alexturkey/wan22-pascal-4gb/releases/tag/v0.1.0) |
| CUDA runtime | `cudart`, `cublas`, `cublasLt` (12.8), unmodified | same release, separate zip |

Fixed settings (measured, see [measurements](docs/MEASUREMENTS.md)): `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --flash-attn on`.
We do not lower steps, add a negative prompt or enable caching: the model is distilled for 8 steps and does not use negative prompts (model discussion, see [prompts](docs/PROMPTS.md)).

## Measured (summary)

One machine: GTX 1050 Ti 4 GB laptop, i7-7700HQ, 16 GB RAM, Windows 10, driver 581.29, models on an SSD. 768x1344, seed 42.

| Picture | Total | Text encoding | Sampling | VAE decode | Peak VRAM | Min free RAM |
|---|---|---|---|---|---|---|
| eiffel | 250.4 s | 13.0 s | 199.5 s | 29.8 s | 2949 MiB | 363 MiB |
| village | 256.2 s | 12.9 s | 200.6 s | 36.3 s | 2949 MiB | 429 MiB |
| turkish_tea | 257.5 s | 13.3 s | 201.3 s | 34.5 s | not recorded | 331 MiB |
| fisherman | 258.5 s | 13.9 s | 204.0 s | 34.2 s | not recorded | 538 MiB |
| istanbul_aerial (1344x768) | 250.7 s | 13.5 s | 199.5 s | 32.6 s | 2951 MiB | 576 MiB |

No black or NaN pictures in these five runs. At 768x1344 the VAE does not fit in VRAM in one piece; the engine retries
by itself with 384x672 tiles (log line: `VAE decode ran out of memory; retrying with spatial tiling`). The engine process
peaks around 10.5-10.9 GB resident (includes memory-mapped model pages), so free RAM gets very low.
These runs used our development build of the same four patches. Clean-root test with the published release zips (fresh copy of the repo, `setup.py` then `generate.py` with `prompts/turkish_tea.txt`, 768x1344): setup finished in 165 s with all `*_OK` lines and `SETUP_OK` (two big model files were copied beforehand and checked with sha256; `ae.safetensors` and both zips were really downloaded), generation took 261.6 s (text 13.0 s, sampling 198.7 s, VAE 33.7 s), peak VRAM 2957 MiB, minimum free RAM 488 MiB, and the picture is byte-for-byte identical to the one from the development engine.

## Limits (read before you rely on it)

- Measured on one GTX 1050 Ti 4 GB laptop, Windows 10. Other GPUs, drivers, 8 GB RAM machines, Linux and macOS: **not tested**.
- Free RAM drops to a few hundred MiB during a run. Do not open a browser or other heavy program meanwhile.
- Prompt fidelity is partial (see the village example). Text inside pictures and real-world landmarks were not evaluated.
- One run at a time. Speed was not the goal; the settings above are the tested point, not a tuned optimum.

## License

- **This repository's own scripts and docs:** MIT, Copyright (c) 2026 alexturkey ([`LICENSE`](LICENSE)).
- **stable-diffusion.cpp** and **ggml** (engine): MIT. Notices for third-party code compiled into the engine are in [`licenses/`](licenses) and [`THIRD_PARTY.md`](THIRD_PARTY.md).
- **Model files** are not in this repository; they are downloaded from the sources above. Hugging Face lists `license: apache-2.0` for Z-Image-Turbo, the GGUF conversion, Qwen3-4B-Instruct-2507, its GGUF conversion and the Comfy-Org repackage (read via the Hugging Face API on 2026-11-13).
  Apache-2.0 is a license for the model files; **the Z-Image-Turbo model card says nothing about ownership of generated pictures**, and we make no claim about it. Who owns AI output depends on your country; check for yourself.
- The VAE is a FLUX.1-type autoencoder taken from the Comfy-Org repo (tagged Apache-2.0). Whether it is byte-identical to the file in the FLUX.1-schnell and FLUX.1-dev repos was not verified (those repos are gated and their file hashes could not be read).
- **NVIDIA CUDA runtime DLLs** are NVIDIA's property and are not under MIT. They are in a separate unmodified zip under the CUDA Toolkit EULA, Attachment A. Visual C++ runtime and ffmpeg are not included.
- Example pictures are AI-generated with this repo.
