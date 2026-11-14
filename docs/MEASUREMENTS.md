# Measurements

Every number here was read from a run on one machine. Labels: **measured on GTX 1050 Ti 4 GB** (we ran it) and **not tested** (we did not).
Nothing in this file is a guess; things we did not record are marked "not recorded".
The tables are separate on purpose: each one names the engine and the setup it comes from, and numbers from different tables must not be mixed.

## Machine

| What | Value |
|---|---|
| GPU | GTX 1050 Ti 4 GB (laptop), Pascal, compute capability 6.1 |
| CPU | Intel Core i7-7700HQ |
| RAM | 16 GB (15.9 GiB reported by Windows) |
| OS / driver | Windows 10, NVIDIA driver 581.29 |
| Storage | model files on an SSD |
| CUDA runtime | 12.8 (`cudart`, `cublas`, `cublasLt`) |
| cuDNN | 9.10.2.21, **CUDA 11 build** from NVIDIA's archive (the only build measured) |

## Settings (all runs)

Z-Image-Turbo `Q8_0` + Qwen3-4B-Instruct-2507 `Q8_0` + `ae.safetensors`.
`--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --flash-attn on`, seed 42, no negative prompt.
Since v0.2.0 the command also has `--eager-load`; the v0.1.0 tables below were taken without it. Size 768x1344 unless stated.

## How the numbers were taken

- Times come from the engine's verbose log (`sd-cli -v`) and from `run.json`; "total" is the wall-clock time of `generate.py`.
- **GPU memory peak** is read from `nvidia-smi` every 2 seconds by `generate.py` (class `Monitor`), and so is the lowest free RAM. A spike shorter than the interval can be missed, so read these as "sampled peak" and "sampled low point".
- Process memory is the engine's resident set; it includes memory-mapped model pages.
- Most rows are single runs. Where a number is a range, the range is over the pictures listed, not over repeated runs of one picture.
- The first run after a reboot or a long idle time reads the model files from disk and can be slower than later runs. Rows say when we know a run was cold.

## Table 1: v0.1.0 layout (never released as a build of this repository)

Engine: stable-diffusion.cpp `master-1088-32d516c` with four Pascal patches, VAE in 384x672 tiles, no cuDNN, no `--eager-load`. Main table: development build; the clean-root line: the published v0.1.0 release zips.

| Picture | Total | Text encoding | Sampling | VAE decode | Peak VRAM | Min free RAM |
|---|---|---|---|---|---|---|
| eiffel | 250.4 s | 13.0 s | 199.5 s | 29.8 s | 2949 MiB | 363 MiB |
| village | 256.2 s | 12.9 s | 200.6 s | 36.3 s | 2949 MiB | 429 MiB |
| turkish_tea | 257.5 s | 13.3 s | 201.3 s | 34.5 s | not recorded | 331 MiB |
| fisherman | 258.5 s | 13.9 s | 204.0 s | 34.2 s | not recorded | 538 MiB |
| istanbul_aerial (1344x768) | 250.7 s | 13.5 s | 199.5 s | 32.6 s | 2951 MiB | 576 MiB |

Clean-root test with the v0.1.0 release zips (fresh copy of the repo, `setup.py` then `generate.py` with `prompts/turkish_tea.txt`): setup 165 s; one picture 261.6 s (text 13.0 s, sampling 198.7 s, VAE 33.7 s), peak VRAM 2957 MiB, minimum free RAM 488 MiB.
In these runs the engine process peaked around 10.5 to 10.9 GB resident (as recorded then; the unit was not re-checked, and a later reading of the same kind, 10 947 MiB, suggests it was GiB). At 768x1344 the VAE did not fit in one piece and the engine retried with tiles (`VAE decode ran out of memory; retrying with spatial tiling`).
No black or NaN pictures in these runs.

## Table 2: v0.2.0, clean-root test (one `generate.py` run per row)

Engine: the v0.2.0 release zip (`sinirsiz-foto-engine-v0.2.0-win-x64-cuda12.8-sm61.zip`), cuDNN installed by `setup.py`, `--vae auto`, models from an SSD. A fresh copy of the repository in an empty folder; setup took 1733 s (28.9 minutes, 20:28:48 to 20:57:41 by the clock) including the check of an interrupted download (the check itself and the pause around it cost about 3 minutes). The setup time was measured with the folders on a hard disk (the downloads ran at 8.7 to 9 MiB/s; we read that as limited by the network, but we did not test it). The timing rows of this table were taken from an SSD.
Logs and `run.json` files: `docs/evidence/clean_root/` (`ssd_models/` for this table, `hdd_models/` for the hard-disk runs, `setup/` for the setup logs, `checks/` for the comparisons). Process memory peak is the largest resident size of `sd-cli.exe` seen by sampling `tasklist` every 2 s (a short peak can be missed). The first row ran right after the sha256 check of the model files; its first step (36 s) and VAE stage (15.9 s) were slower than in the other four rows (27.5 to 29.5 s and 8.3 to 12.2 s).

| Picture | Total | Text encoding | Sampling | VAE decode | `vae_path` | Peak VRAM | Min free RAM | Process memory peak |
|---|---|---|---|---|---|---|---|---|
| eiffel (first run after the sha256 check) | 228.4 s | 5.0 s | 186.3 s | 15.9 s | `full` | 3059 MiB | 441 MiB | 10 763 MiB |
| turkish_tea | 197.4 s | 3.4 s | 173.8 s | 12.0 s | `full` | 3057 MiB | 418 MiB | 10 667 MiB |
| fisherman | 208.1 s | 3.8 s | 178.6 s | 12.2 s | `full` | 3057 MiB | 545 MiB | 10 915 MiB |
| village | 193.1 s | 3.2 s | 175.8 s | 8.7 s | `full` | 3057 MiB | 476 MiB | 10 859 MiB |
| istanbul_aerial (1344x768) | 196.0 s | 3.2 s | 178.1 s | 8.3 s | `full` | 3059 MiB | 491 MiB | 10 852 MiB |

The ranges in the README (time per picture, VAE decode, peak GPU memory, process memory, lowest free RAM) are over all five rows of this table, the first run (eiffel) included. That run came right after the model files were hashed and is the slowest of the five; a first run on your machine can look like it.

The three VAE modes on the same picture (`prompts/eiffel.txt`, seed 42), also from the clean-root test:

| `--vae` | Total | VAE decode | `vae_path` | Note |
|---|---|---|---|---|
| `auto` | 228.4 s | 15.9 s | `full` | default (first run after the sha256 check) |
| `tiled` | 205.6 s | 14.0 s | `tile` (768x1024) | two large tiles |
| `legacy` | 216.5 s | 22.8 s | not reported by the engine in this mode (small default tiles, 384x672; `vae_quality_drop` true) | the v0.1.0 path. Measured in a second fresh copy of the repository, set up with `--no-cudnn` (so `auto` became `legacy`), models read from the same SSD files |
| `auto`, forced fallback (`SD_VAE_FULL_MARGIN_MB` set large) | 199.1 s | 12.4 s | `tile` (768x1024), `vae_full_fell_back` true | one-piece try does not fit, falls back to the requested tile |

Values seen earlier with a development build of the same engine, one run each (taken before the clean-root test, so not part of the table above; kept for the record): generate stage 186.2 s (768x1344), VAE 7.5 to 11.3 s (the 11.3 s run was the first, cold one), sampled peak VRAM 3057 to 3105 MiB, free RAM low point 475 to 582 MiB, process memory peak 10 790 to 11 167 MiB.

One run of the clean-root test (the third SSD run) was stopped when free RAM was low (the engine was running with a few hundred MiB free). We think the tool that started it ended its background processes (not verified). The engine log shows no error line (no match for an error, out-of-memory or abort message), and the run was repeated. Read it as a warning, not as a measurement: keep other heavy programs closed while the engine runs.

Memory and the one-piece VAE: the engine checks GPU memory before the one-piece VAE decode and keeps a margin (`SD_VAE_FULL_MARGIN_MB`, default 256 MiB). In the development build the memory left over at that check was about 45 MiB for 1024x1024 and 87 to 89 MiB for 768x1344 and 1344x768 (that was a server run, not a repo setup). That is a thin margin: another program holding GPU memory can push the decode to tiles (`vae_path` `tile`, `floor` or `retry`), which is the intended fallback.

## Models on a hard disk (two runs)

By accident the model files of the clean-root test were on a hard disk (a 2 TB laptop hard disk, model ST2000LM007; the system drive is an SSD), so we have two runs from it. Same engine, same settings as Table 2, `--vae auto`. The download and the sha256 check were tested in the folder on the hard disk; the timing rows of Table 2 were measured again with the same, sha256-verified files on the SSD (see the evidence files in `docs/evidence/clean_root/`).

| Run | Total | First step | Steps 2 to 8 (each) | VAE decode | Loading tensors | Peak VRAM | Process memory peak | Min free RAM |
|---|---|---|---|---|---|---|---|---|
| eiffel (the files had just been read by the sha256 check, so they were probably cached) | 324.8 s | 143 s | 21.1 s | 13.7 s | 0.62 s | 3059 MiB | 10 239 MiB | 321 MiB |
| turkish_tea | 378.0 s | 114 s | 21.4 s | 67.0 s | 27.3 s | 3057 MiB | 10 868 MiB | 591 MiB |

What we measured: steps 2 to 8 took the same time as on the SSD; the extra time is in the first step, in loading, and (in one of the two runs) in the VAE stage.
What we think, but did not test: the slowdown comes from model pages being read from the disk again while the process runs. We did not run a check that separates this from other causes.
Two runs, one disk: do not generalize to other hard disks. If you have a hard disk, the numbers above are the only ones we have; an SSD is what we recommend.

## Checks (clean-root test)

Each row is one check made in the clean-root test of this release. The evidence files are in `docs/evidence/clean_root/` (see the `README.md` there).

| Check | Command or method | Result | Evidence file |
|---|---|---|---|
| Repeat | two pairs on the `auto` path: `prompts/eiffel.txt` and `prompts/turkish_tea.txt`, seed 42. Each pair: two separate processes, the model files (same sha256) once on a hard disk and once on an SSD; `scripts/compare.py` on the two pictures of a pair (`SAME_PIXELS` or `DIFFERENT`) | `SAME_PIXELS` for both pairs: `PIXEL_SHA256` equal, largest difference 0, PSNR infinite (eiffel `bf39b8c5...`, turkish_tea `d939afdc...`) | `docs/evidence/clean_root/checks/g15_repeat_hdd_vs_ssd_*.txt` |
| Released zip = development engine | the 7 binaries in the release zip have the same sha256 as the development engine build all development measurements were taken with (a comparison of files, not of pictures; equal bytes are a stronger statement than equal pictures) | 7 of 7 equal (`sd-cli.exe`, `sd-server.exe`, `stable-diffusion.dll`, `ggml.dll`, `ggml-base.dll`, `ggml-cpu.dll`, `ggml-cuda.dll`; installed by `setup.py` from the release zip, compared with the `-hiz-0028` engine folder) | `docs/evidence/clean_root/checks/zip_vs_development_engine_sha256.txt` |
| Forced fallback | `SD_VAE_FULL_MARGIN_MB` set large: `vae_path` must be `tile`; are the pixels the same as the `--vae tiled` picture? | yes: `vae_path` `tile`, `vae_full_fell_back` true, gate residual -99653 MB; same pixels as the `--vae tiled` picture (`PIXEL_SHA256` `c7e5ed4b...`, `SAME_PIXELS`, largest difference 0) | `docs/evidence/clean_root/checks/g19_forced_fallback_vs_tiled.txt`, `g19_note.txt` |
| `--vae tiled` and `--vae legacy` against `--vae auto` | `scripts/compare.py`: largest difference and PSNR | against the one-piece `auto` picture (eiffel): `tiled` 41.06 dB, largest difference 106 (mean 1.09), not the same pixels; `legacy` 35.61 dB, largest difference 176 (mean 2.20), not the same pixels | `docs/evidence/clean_root/checks/tiled_vs_auto.txt`, `legacy_vs_auto.txt` |
| Interrupted setup resumes | a download was cut off and `setup.py` run again: does the `.part` file continue and is the sha256 right? | yes, for the cuDNN download with the current `setup.py`: stopped at 62 914 560 of 384 728 540 bytes, run again: it continued from the `.part` file (44 s, first progress line already at 20%), then `CUDNN_OK` and `SETUP_PART_OK cudnn` (the script checks the sha256 before `CUDNN_OK`). A first attempt was stopped when the file was already complete, so it only tested the hash check; it is listed in the evidence for honesty. The engine and CUDA runtime downloads were interrupted and resumed earlier, with the `setup.py` of that time (`setup_engine_resume.log`) | `docs/evidence/clean_root/setup/g12_*`, `setup_engine_resume.log` |
| Commands from a fresh copy to the first picture | number of commands | 2 commands: `python scripts/setup.py` and `python scripts/generate.py --prompt-file prompts/eiffel.txt` (with `--lock`, `--bin-dir`, `--models-dir` in this test). Setup took 4 min 6 s, the picture 238 s (`PIXEL_SHA256` `bf39b8c5...`, the same as the other eiffel runs). In this test the engine zip came from a local file and the model files were the ones already downloaded and verified (so the 12 GB download was not repeated; its time is above), on the hard disk. The first attempt of the picture step was stopped by the host's memory manager and repeated; both are in the evidence | `docs/evidence/clean_root/g11_fresh_copy/` |
| `sd-cli.exe --help` | flag names the commands use | every sd-cli flag that `generate.py` passes appears in the help text (checked with a script over the list of flags); version line `master-1088-32d516c` | `docs/evidence/clean_root/setup/sd-cli_help.txt` |

## Table 3: development setup with the model held open (not in this repository)

This table comes from our development setup, a long-running engine server with the models kept loaded. **This setup is not part of the repository**; you cannot reproduce these times with `generate.py`. It is here because it shows what each change was worth on one fixed picture. Do not compare it with Table 1 or 2: it skips the model loading and the engine start, which are part of every `generate.py` run.

First request of a series, a 1024x1024 picture, seed 42, 8 steps:

| Engine state | Time for the picture |
|---|---|
| before the changes below (development engine, faster im2col only) | 219.7 s |
| refiner computed once per step | 205.3 s |
| + cuDNN float32 VAE in large tiles | 196.9 s |
| + one-piece VAE first (this release) | 191.5 s |

Later pictures in the same series were faster (174 to 186 s per picture with the current engine; the first picture pays for warming up). Pictures: the refiner change gave pixel-identical pictures (the PNG files were identical too); the two VAE changes change the pixels on purpose (see Quality).

## Quality: closeness of the VAE stage to a reference

**What "reference" means here.** For one picture we saved the latent (the data just before the VAE) and decoded it on the CPU, in float32, as one piece. That decode is the reference. PSNR (peak signal-to-noise ratio, in dB, higher is closer; identical pixels give infinity) and the largest single-pixel difference (0 to 255) compare each GPU decode path with it. Both are computed on decoded pixels with `scripts/compare.py` logic: the PNG files carry the generation parameters as text, so file hashes differ even for identical pixels.

| Picture | `--vae legacy` (small tiles, v0.1.0 path) | cuDNN, two large tiles (`--vae tiled`) | cuDNN, one piece (`--vae auto`, full path) |
|---|---|---|---|
| 768x1344 (picture 1) | 39.19 dB, max diff 94 | 47.41 dB, max diff 52 | 70.96 dB, max diff 1 |
| 1024x1024 (picture 2) | 42.91 dB, max diff 76 | 48.81 dB, max diff 29 | 72.93 dB, max diff 1 |
| 1344x768 (picture 3) | 38.21 dB, max diff 66 | 45.70 dB, max diff 46 | 70.88 dB, max diff 1 |

Reading it: the one-piece decode is practically the reference (a largest difference of 1 out of 255); the tile paths are further away because tile seams change the normalization statistics and the edges. Falling back from one piece to tiles lands on the tiled number.
When a forced fallback happened, the picture had the same pixels as the one made with the tiled path directly (`PIXEL_SHA256` equal).

**Limits of this table, plainly:**
- The reference is a decode by our own engine on the CPU, **not an independent reference** (for example not the original PyTorch decoder).
- Three pictures, one seed each. PSNR measures closeness to the reference decode, not how a picture looks to a person.
- The three test pictures use prompts that are not among the five examples; their prompts are not published in `prompts/`, and the saved latents and the CPU reference pictures are kept only in the development workshop (not in this repository, because the latents are large and the test pictures are not among the examples).
- Whether you can repeat the table with the published package: **No, not with the published package.** Saving a latent and decoding it alone on the CPU uses a development patch (0008) that is not part of the published patch set, and the published `sd-cli.exe` has no option for it. The numbers in this table were measured with a development build of the same engine; the values are reproduced here as measured, not re-measured with the zip. What the zip does reproduce is the pixel hashes in the tables above (same prompt, seed and VAE mode give the same pixels).

## Example pictures: pixel hashes

Each example was generated with the v0.2.0 clean-root setup, seed 42, 8 steps. `PIXEL_SHA256` is the SHA-256 of the decoded RGB bytes that `generate.py` prints, so you can check your run against it.

| Example | Size | Command | `PIXEL_SHA256` |
|---|---|---|---|
| eiffel | 768x1344 | `python scripts/generate.py --prompt-file prompts/eiffel.txt --seed 42` | `bf39b8c5388599c4a85f195782e089f28bad56ef91882d95c1f2c90971f2ab2e` |
| turkish_tea | 768x1344 | `python scripts/generate.py --prompt-file prompts/turkish_tea.txt --seed 42` | `d939afdc5dce90c041bbe8e5ab7b7ba22b811285fcc5ce25c01a058411d982b2` |
| fisherman | 768x1344 | `python scripts/generate.py --prompt-file prompts/fisherman.txt --seed 42` | `5734101c2b0d39bff430880355791cff643798e937a95a3727af299d06af0ea1` |
| village | 768x1344 | `python scripts/generate.py --prompt-file prompts/village.txt --seed 42` | `bba30730994222bd0e72ea97a352129009c011e1f65698002fba60af2263e93e` |
| istanbul_aerial | 1344x768 | `python scripts/generate.py --prompt-file prompts/istanbul_aerial.txt --seed 42 --width 1344 --height 768` | `da6dc93adc61f5df875365488bed72c3bbec5c2f5411bcd7c7f3ac01faae0369` |

Add `--models-dir` and `--bin-dir` if you used them in setup. The hash holds for the same VAE path (`stages.vae_path` in `run.json`): the one-piece path and the tiled path give different pixels. To compare two of your own runs: `python scripts/compare.py <A>/image.png <B>/image.png` prints `SAME_PIXELS` or `DIFFERENT` with the largest difference and the PSNR.
The same prompt, seed and setup gave identical pixels in repeated runs: two pairs on the `auto` path (eiffel and turkish_tea; separate processes, the model files with the same sha256 once on a hard disk and once on an SSD). For `--vae tiled` and `--vae legacy` we did not repeat runs. This is not a statistical test.

**The condition behind "the same seed gives the same pixels"** (README): the same setup and the same VAE path. If the path changes, for example after a forced fallback or when another program holds GPU memory and the one-piece try no longer fits, the pixels change too; `stages.vae_path` in `run.json` says which path ran.

## What is not measured

- Other resolutions than 768x1344, 1344x768 and 1024x1024 (the 1344x768 picture is a single run).
- Other GPUs, other drivers, machines with less than 16 GB RAM, other hard disks than the one in the section "Models on a hard disk", Linux, macOS.
- cuDNN CUDA 12 build (its files differ from the CUDA 11 build we used; speed and pixels may differ).
- Other quantizations (Q4_0 etc.), other step counts, cfg other than 1.0.
- The unpatched upstream engine on this card: we did not run it, so we cannot say whether it fits or how fast it is.
- Prompt-following quality beyond the examples (village: the round doors came out as separate huts, not dug into the hill, so prompt match was partial).
- Repeated runs for a spread: most rows are single runs.
- GPU power draw (laptop `nvidia-smi` reports N/A). Earlier readings, development build: GPU utilisation about 86 %, temperature peak 66 C, clock about 1544 to 1582 MHz median with a software power cap in part of the samples.

## How to add a measurement

Use `outputs/<run>/run.json` (time, stages, which VAE path ran, sampled peak GPU memory, `image_pixel_sha256`, the exact command). Open a "measurement report" issue or a pull request with the machine, seed and engine build,
and mark anything you did not record "not recorded".
