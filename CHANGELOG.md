# Changelog

Format after [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow [Semantic Versioning](https://semver.org/).
Numbers come from [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md); where a number is not there, it is not claimed here.

## [Unreleased]

### Added
- `docs/OTHER_GPUS.md`: which path for which card or system (measured by us, community test, not tested), what carries over and what does not, and a community test on an AMD RX 6600 XT with Ubuntu and ROCm, adapted from the report by Hakan ([hknklnc10](https://gist.github.com/hknklnc10/fa19ea3813238bd64853be2a814e4f18)). Thank you.
- Pointers to it in the READMEs (all languages), `AGENTS.md`, `docs/BUILD.md`, `docs/MEASUREMENTS.md` and `CONTRIBUTING.md`.

### Changed
- The hardware test report form asks for the operating system, the GPU API and the engine, so reports from Linux, AMD and direct `sd-cli` runs fit.

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
