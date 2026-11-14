# Measurements

Every number here was read from a run on one machine. Labels: **measured on GTX 1050 Ti 4 GB** (we ran it) and **not tested** (we did not).
Nothing in this file is a guess; things we did not record are marked "not recorded".

## Machine

| What | Value |
|---|---|
| GPU | GTX 1050 Ti 4 GB (laptop), Pascal, compute capability 6.1 |
| CPU | Intel Core i7-7700HQ |
| RAM | 16 GB |
| OS / driver | Windows 10, NVIDIA driver 581.29 |
| Storage | model files on an SSD |
| Engine | stable-diffusion.cpp `master-1088-32d516c` with four Pascal patches. Main table: **development build**. Clean-root test below: **release zips** |

## Settings (all runs)

Z-Image-Turbo `Q8_0` + Qwen3-4B-Instruct-2507 `Q8_0` + `ae.safetensors`.
`--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --flash-attn on`, seed 42, no negative prompt.
Size 768x1344 unless stated.

## Results

| Picture | Total | Text encoding | Sampling | VAE decode | Peak VRAM | Min free RAM |
|---|---|---|---|---|---|---|
| eiffel | 250.4 s | 13.0 s | 199.5 s | 29.8 s | 2949 MiB | 363 MiB |
| village | 256.2 s | 12.9 s | 200.6 s | 36.3 s | 2949 MiB | 429 MiB |
| turkish_tea | 257.5 s | 13.3 s | 201.3 s | 34.5 s | not recorded | 331 MiB |
| fisherman | 258.5 s | 13.9 s | 204.0 s | 34.2 s | not recorded | 538 MiB |
| istanbul_aerial (1344x768) | 250.7 s | 13.5 s | 199.5 s | 32.6 s | 2951 MiB | 576 MiB |

Range over the five runs: total 250.4 to 258.5 s; peak VRAM 2949 to 2951 MiB where recorded; minimum free RAM 331 to 576 MiB.

Other readings from the four 768x1344 runs:
- GPU utilisation average about 86 %, temperature peak 66 C, CPU average about 20 %.
- GPU power could not be read (laptop `nvidia-smi` reports N/A).
- All runs completed, CUDA was used, no black or NaN picture.
- Model loading plus other overhead is about 8 s (mmap, SSD). Whether a resident server would help: not tested (our estimate, not measured: the gain would be small).
- Engine process resident memory peaked around 10.5 to 10.9 GB (includes memory-mapped model pages).

## VAE tiling

At 768x1344 the VAE decode does not fit in VRAM in one piece. The engine logs
`VAE decode ran out of memory; retrying with spatial tiling` and decodes in 384x672 tiles by itself.
This is normal for this setup, costs 30 to 36 s of the total and did not change success.

## Clean-root test with the release engine

A fresh copy of the repo (without git), then `python scripts/setup.py --models-dir <dir>` and `python scripts/generate.py --prompt-file prompts/turkish_tea.txt` (GPU lock held), 768x1344, seed 42.

| Step | Result |
|---|---|
| `setup.py` | 165 s, exit code 0, `MODEL_OK` x3, `ENGINE_OK`, `CUDART_OK`, `SETUP_OK`. The two big model files were copied beforehand and verified with sha256; `ae.safetensors` (335 MB) and both release zips were really downloaded. |
| `generate.py` | 261.6 s total: text 13.0 s, sampling 198.7 s, VAE 33.7 s. Peak VRAM 2957 MiB, minimum free RAM 488 MiB. The VAE fell back to tiles. `IMAGE_OK`. |
| Picture | **byte-for-byte identical** to the PNG made by the development engine for the same prompt (same pixel md5). |

The release engine took 261.6 s against 257.5 s for the development engine on the same prompt (one run each; the difference is within what we saw between pictures).

## What is not measured

- Other resolutions than 768x1344 and 1344x768 (the 1344x768 picture is a single run).
- Other GPUs, other drivers, machines with less than 16 GB RAM, models on a spinning disk, Linux, macOS.
- Other quantizations (Q4_0 etc.), other step counts, cfg other than 1.0.
- Prompt-following quality beyond the examples (village: the round doors came out as separate huts, not dug into the hill, so prompt match was partial).

## How to add a measurement

Use `outputs/<run>/run.json` (time, stages, peak VRAM from nvidia-smi, the command). Add a row with the machine, seed and engine build,
and mark anything you did not record "not recorded".
