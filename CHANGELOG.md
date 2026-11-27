# Changelog

Format after [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow [Semantic Versioning](https://semver.org/).
Numbers come from [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md); where a number is not there, it is not claimed here.

## [Unreleased]

- `docs/OTHER_GPUS.md`: the RTX 2060 laptop follow-up through `scripts/generate.py` (section 3b, `[user-reported, issue #7]`: 64.3 s, peak 4871 MiB, `ram_free_min_mib` 7025, same pixel hash as #5) and a short unnamed note about an Apple M4 Pro run in the Draw Things app (section 3c, `[user-reported, issue #4]`, not comparable with our tables). Thanks to MuhammedGUVEN108 for #5 and #7.
- Agent onboarding (kit KL-23): a do-this-first block at the top of `AGENTS_HIZLI.md` and `AGENTS.md` (run `python scripts/tani.py` first, git-ignored `DURUM.md` notebook, NEVER / ASK lists, same error twice stop); a read-only DEVIATIONS section in `tani.py` (tests in `tests/test_tani_sapma.py`); a one-sentence "give this to your agent" block in every README (30 languages); long `AGENTS.md` lines split. Quality and run behaviour unchanged.

## [0.3.0] - 2026-11-25

Faster pictures, same pictures.

**Why it is faster.** The model does not fit into 4 GB of GPU memory, so the engine copies it to the card one part at a time. In v0.2.0 the GPU sat idle while each part was copied. Now, while the GPU is computing the current part, the engine already moves the weights of the next part to the card in the background, so the copy and the computation overlap and the GPU waits much less.

**How much (measured on GTX 1050 Ti 4 GB, 768x1344, 8 steps, seed 42).** Through `generate.py` on a clean copy of the repository, a picture took 188.1 to 192.9 s, and the sampling stage took 158.5 to 161.2 s against 173.8 to 186.3 s in v0.2.0 (`docs/MEASUREMENTS.md`, Table 5). In the same clean copy, one picture took 188.1 s with the overlap and 204.5 s without it (one run each). In our development setup, in 12 alternating runs, the median picture took 177.0 s instead of 199.5 s (Table 4). The VAE stage (the last step, which turns the result into pixels) varies a lot from run to run on this machine (7.5 to 21.7 s), so the total gains less than the sampling in some runs. In our development setup with the models kept loaded (not part of this repository), ten pictures back to back took a median of 163.5 s per picture (pictures 3 to 10) instead of 176.5 s in an earlier series with the v0.2.0 engine (another day, other prompts, times from our work log; not an alternating comparison); picture 2 of that series took 208.0 s, which is not explained yet (Table 4b).

**The pictures are the same.** The pixels are byte-identical to v0.2.0 for the same prompt, seed and settings (checked on eiffel, turkish_tea and village). Steps, cfg, sampler, quantization and size did not change.

**If your RAM is tight.** The overlap uses a 64 MB buffer of page-locked memory, which Windows cannot swap out. We did not measure what that costs on a machine that is short of memory. If yours is, run `python scripts/generate.py --no-overlap`: same picture, longer run.

**Upgrading.** Run `python scripts/setup.py`. It downloads only the new engine zip (about 38 MB). It no longer downloads the 567 MB CUDA runtime again when that file has not changed (before, an upgrade fetched it again).

### Added
- **`patches/sdcpp/0030-weight-copy-overlap.patch`** (MIT): the weight-copy / compute overlap (a worker thread and a small page-locked ring buffer). Off in the engine unless switched on by `SD_PREFETCH_THREAD=1`, `SD_STAGING_PINNED=1`, `SD_STAGING_PINNED_MB=64`; `generate.py` switches it on. Also in the patch and not measured (leave unset): `SD_STAGING_POOL_MB`, `SD_STAGING_PREEVICT`, `SD_PREFETCH_WRAP`; diagnostic: `SD_STAGING_VERIFY`.
- `generate.py --no-overlap`: leave the three switches unset (stock copy path, same picture, longer run; use it when the machine is short of RAM). `run.json` gains `stages.copy_overlap_used`, `overlap_ring_tensors`, `overlap_ring_mib`, `overlap_fallback_tensors`.
- `scripts/pack_engine.py`: packs the release zip the same way every time (same inputs, same bytes), prints the numbers for `models.lock.json`.
- `docs/evidence/overlap/` and Tables 4 and 5 in `docs/MEASUREMENTS.md`; "Compare your build with the release" in `docs/BUILD.md` and "Reproducing the released binaries" in `patches/README.md`.
- `docs/TROUBLESHOOTING.md`: the overlap on a machine short of RAM; `copy_overlap_used` false.

### Added (since v0.2.0, documents and tools)
- `docs/OTHER_GPUS.md`: which path for which card or system (measured by us, community test, not tested), what carries over and what does not, and a community test on an AMD RX 6600 XT with Ubuntu and ROCm, adapted from the report by Hakan ([hknklnc10](https://gist.github.com/hknklnc10/fa19ea3813238bd64853be2a814e4f18)). Thank you.
- Pointers to it in the READMEs (all languages), `AGENTS.md`, `docs/BUILD.md`, `docs/MEASUREMENTS.md` and `CONTRIBUTING.md`.
- `docs/AGENT_METHOD.md`: how an AI agent should run the job for a beginner: hardware inventory first, one project folder, progress notes so nothing is done twice, a stop file, one GPU job at a time, no leftover processes, roles and a second opinion on important decisions, what to ask the user first, evidence labels.
- `docs/OTHER_GPUS.md` section 4: a suggested first path for AMD cards on Windows (upstream prebuilt Vulkan zip, then ROCm), not tested.
- `docs/OTHER_GPUS.md` section 3b: community test on an RTX 2060 laptop 6 GB (Windows 11, unpatched upstream CUDA12 build), reported by @MuhammedGUVEN108 in issue #5; labelled `[user-reported, issue #5]`, not repeated by us. Thank you.
- `python scripts/setup.py --dry-run`: prints what would be downloaded and whether the disk is big enough; writes nothing, creates no folder, opens no network connection. Ends with `DRYRUN_OK` (exit 0) or a disk `ERROR:` line (exit 3). Without the option nothing changes.
- `scripts/denetim.py` (`--hizli`, `--tam`) with `scripts/on_kontrol.cmd`: quick pre-pull-request checks (hidden characters, privacy scan, fixed quality settings, pinned lock file, error code file); `scripts/tani.py`: a local diagnosis report that sends nothing and hides names; `kur.cmd`: double-click launcher for the installer (dry run first).
- `docs/hata_imzalari.json` and an "Error codes" table in `docs/TROUBLESHOOTING.md`: a stable code (`ZIMG-E-...`) and a first step in English and Turkish for each script message; the message text itself is unchanged. `AGENTS_HIZLI.md` (quick card for agents), `llms.txt`, `GEMINI.md`, `.github/copilot-instructions.md`; `AGENTS.md` and `CLAUDE.md` now point to one source.
- `PRIVACY.md`, `SUPPORT.md`, `.github/release.yml`, `.github/dependabot.yml` and a check workflow in report mode (runs on pull_request and on pushes to main, never pull_request_target) (`.github/workflows/denetim.yml`, actions pinned to commit SHAs, read-only permissions).
- `SECURITY.md`: 7-day first-reply target (a goal, not a promise), supported versions, AI agent paragraph. `CONTRIBUTING.md`: first pull request in 5 steps, evidence labels, no-reply e-mail note, one language is enough. README (English and Turkish): "Disk layout and removal"; `AGENTS.md`: "Install layout and agent discipline". The other 27 README translations do not have the new section yet.
- `scripts/repo_kapi.json`: the repository's settings for the repository kit.

### Changed
- **Engine** (`sinirsiz-foto-engine-v0.3.0-win-x64-cuda12.8-sm61.zip`, in this repository's v0.3.0 release): v0.2.0 engine plus patch 0030. `scripts/setup.py` now fetches only the zips whose sha256 changed when you upgrade (the 567 MB CUDA runtime is not downloaded again); `--dry-run` shows the same plan.
- `docs/BUILD.md` and `patches/README.md`: the exact CMake flags (Ninja, Release, ...) and the line-ending trap with the `ggml` submodule (`core.autocrlf` in the submodule).
- `AGENTS.md`: the hard rules about the engine build and memory options are scoped to the released NVIDIA path; quality settings stay fixed everywhere.
- The hardware test report form asks for the operating system, the GPU API and the engine, so reports from Linux, AMD and direct `sd-cli` runs fit.
- The issue chooser no longer offers a blank issue (the forms and the Discussions links cover every case).

### Not changed
- Steps (8), cfg (1.0), sampler, scheduler, quantization (Q8_0), size 768x1344 and the three model files; the pictures of the three examples we re-ran have the same `PIXEL_SHA256` as in v0.2.0.

### Known limits
- Measured only on a GTX 1050 Ti 4 GB laptop; the engine is built for sm_61 only.
- The overlap was not measured with `--vae legacy`, and not on a machine that is short of RAM (the 64 MB page-locked ring cannot be swapped out; use `--no-overlap` there).
- The VAE stage of the same one-piece decode took 7.5 to 21.7 s from run to run in our tests; we do not know why, so the total time moves by that much.

## [0.2.0]

Engine, VAE path, evidence and documents. The pictures of v0.2.0 are not byte-identical to v0.1.0 for the same prompt and seed, because the VAE path changed on purpose.

### Added
- **cuDNN VAE path (installed by default; `--no-cudnn` skips it).** `scripts/setup.py` downloads NVIDIA's official cuDNN archive (9.10.2.21, CUDA 11 build, sha256 pinned in `models.lock.json`) from NVIDIA's server by default, under NVIDIA's license, and copies only eight runtime DLLs next to `sd-cli.exe`. Before the download it prints one line with the license address; `--no-cudnn` skips it. New flags `--no-cudnn`, `--only cudnn` (`--accept-cudnn-license` is still accepted and changes nothing); new lines `CUDNN_OK` and `CUDNN_SKIPPED`. cuDNN is not stored in this repository or its releases. The license text, `mode: default_download_disclosed` and `installed_utc` are recorded locally in `cudnn_license_record.json`.
- With `--only <part>` the last line is `SETUP_PART_OK <part>`; `SETUP_OK` appears only after a full setup.
- **`--vae auto|tiled|legacy`** in `scripts/generate.py`. `auto` (default) decodes the image in one piece when the memory check allows, then in two large tiles, then in small tiles. `legacy` is the v0.1.0 path and is used automatically, with a warning, when the cuDNN DLLs are missing.
- **Preflight block in `scripts/setup.py`**: before downloading, it prints GPU, driver, RAM and free disk space. It only informs; it does not stop the setup.
- Every `ERROR:` line of `setup.py` ends with `Fix: ...`, so each failure says what to do next.
- **`scripts/compare.py`** (standard library only): pixel hash of one picture, or largest difference, mean difference and PSNR of two.
- `generate.py` prints `PIXEL_SHA256 <hex>`; `run.json` gains `vae_mode`, `vae_mode_requested`, `engine_env`, `image_pixel_sha256`, `engine_zips_sha256` and, under `stages`, `vae_path`, `vae_tile`, `vae_full_fell_back`, `vae_quality_drop`, `vae_gate_residual_mib`, `cudnn_used`, `cudnn_workspace_max_kib`.
- **Engine patches published** in `patches/` (MIT) with a README: base commits, apply order, environment switches, CMake flags. `docs/BUILD.md` explains how to build for your own card.
- `docs/MEASUREMENTS.md` restructured: one table per engine and setup, a quality section with the reference definition and its limits, pixel hashes of the five examples, sampling limits. `docs/TROUBLESHOOTING.md` covers the VAE fallbacks and the thin memory margin. `docs/RELATED.md` lists what we looked at.
- `AGENTS.md` rewritten as a step table with acceptance checks on `run.json`; an agent tells the user in one line that setup downloads cuDNN under NVIDIA's license and uses `--no-cudnn` only if the user declines.
- `LICENSE` is now Apache-2.0 with a `NOTICE` file; `ETHICS.md`, `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, issue and pull request templates.
- The README is available in 30 languages (AI-assisted localization; corrections are welcome, see `docs/translation_notes/`).

### Changed
- **Engine** (`sinirsiz-foto-engine-v0.2.0-win-x64-cuda12.8-sm61.zip`, hosted in this repository's v0.2.0 release): the refiner blocks run once per step instead of twice (steps 2 to 8 about 1.3 s faster each, pixel-identical pictures); the VAE can use cuDNN float32 convolutions; the VAE tries the whole image in one piece first and falls back to tiles. Still stable-diffusion.cpp `32d516c`, built for Pascal (sm_61) only.
- `generate.py` runs with `--eager-load` (reads the model pages at the start).
- VAE quality, measured against a CPU float32 one-piece decode of the same latent on 3 pictures: 38 to 43 dB (v0.1.0 path) to 71 to 73 dB (one piece); two large tiles: 45 to 49 dB. Time for the VAE stage and for a whole picture: see `docs/MEASUREMENTS.md` (Table 2).
- Project name in the documents is "Sınırsız Foto"; the repository is `z-image-turbo-pascal-4gb`.

### Not changed
- Steps (8), cfg (1.0), sampler, scheduler, quantization (Q8_0) and the three model files.
- Hardware: still measured only on a GTX 1050 Ti 4 GB laptop with 16 GB RAM. Two runs with the models on a hard disk are in `docs/MEASUREMENTS.md` (325 and 378 s per picture).

### Known limits
- Engine built for sm_61 only; other cards need your own build and were not tested.
- cuDNN CUDA 12 build not measured.
- We have not seen GPU memory run out after the engine's memory check passed, and we did not test what happens then; see `docs/TROUBLESHOOTING.md`.

## [0.1.0] (not published as a release of this repository)

First version, kept here for the record: Z-Image-Turbo Q8_0 for Windows with a 4 GB Pascal GPU, stable-diffusion.cpp `master-1088-32d516c` with four Pascal patches (engine zip from the wan22-pascal-4gb v0.1.0 release), `scripts/setup.py`, `scripts/generate.py`, `scripts/privacy_scan.py`, five example prompts and pictures, measurements on a GTX 1050 Ti 4 GB laptop (250.4 to 258.5 s per picture; clean-root test 261.6 s), MIT license.
