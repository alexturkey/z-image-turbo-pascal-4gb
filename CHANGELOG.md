# Changelog

## Unreleased (first version, not yet tagged)

- Z-Image-Turbo Q8_0 text-to-image for Windows with a 4 GB Pascal GPU, using stable-diffusion.cpp `master-1088-32d516c` with four Pascal patches (engine zip from the wan22-pascal-4gb v0.1.0 release).
- `scripts/setup.py`: downloads three model files and two zips from pinned revisions, verifies sha256, prints `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK`, `SETUP_OK`.
- `scripts/generate.py`: one picture per call, writes `image.png` and `run.json`, prints `IMAGE_OK <path>`.
- `scripts/privacy_scan.py`: checks the repository for personal paths and names before publishing.
- Five example prompts and pictures (AI-generated, seed 42): Eiffel Tower, Turkish tea, fisherman, village, Istanbul aerial.
- Measurements on a GTX 1050 Ti 4 GB laptop: 250.4 to 258.5 s per picture, peak VRAM 2949 to 2951 MiB, minimum free RAM 331 to 576 MiB (see `docs/MEASUREMENTS.md`). Clean-root test with the release zips: setup 165 s, one picture 261.6 s, peak VRAM 2957 MiB, byte-identical to the development-engine picture.
- Docs: README (EN, TR), `AGENTS.md`, `docs/MEASUREMENTS.md`, `docs/PROMPTS.md`, `docs/TROUBLESHOOTING.md`, `THIRD_PARTY.md`.
