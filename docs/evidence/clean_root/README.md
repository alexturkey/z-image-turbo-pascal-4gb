# Evidence of the clean-root test (v0.2.0)

Files behind the numbers in `docs/MEASUREMENTS.md` (Table 2, the VAE modes table and the "Checks" table). All of it was produced on one machine (GTX 1050 Ti 4 GB laptop) on 2026-11-14.

| Folder | What it is | Checks / tables it supports |
|---|---|---|
| `ssd_models/` | `run.json`, `log.txt` and the memory sampling of every run with the model files read from the SSD (five examples, `--vae tiled`, forced fallback), plus `models_check.txt` (3 x `MODEL_OK`) and `_sira.log` (run start and end times) | Table 2, VAE modes table (`auto`, `tiled`, forced fallback), Repeat |
| `hdd_models/` | the first two runs, with the model files on a hard disk (same sha256) | the hard-disk table, Repeat |
| `legacy_reader/` | `run.json`, `log.txt` and `command.txt` of the `legacy` run. It came from a second fresh copy of the repository set up with `--no-cudnn`, not from the folder of the other runs; the model files were the same SSD files | VAE modes table (`legacy`), `--vae tiled` and `--vae legacy` against `--vae auto` |
| `setup/` | setup logs. `setup_engine*.log`, `setup_cudnn.log`, `setup_models_speed.log`: the first install (engine, interrupted and resumed engine download, cuDNN, models), made with the `setup.py` of that time, before cuDNN became the default download. `g12_*`: the interrupted-download check with the current `setup.py` (attempt 1: the file was already complete when the process was stopped, so it only tested hashing; attempt 2: stopped at 62 914 560 of 384 728 540 bytes, then resumed). `sd-cli_help.txt`: the output of `sd-cli.exe --help` | setup time, "Interrupted setup resumes", `sd-cli.exe --help` |
| `g11_fresh_copy/` | the "commands from a fresh copy to the first picture" check with the current `setup.py`: `setup_command1.out` (command 1), `generate_command2.out` (command 2), `g11.log` (times), the `run.json` and `log.txt` of the picture, and the log of the first, stopped attempt (`20261114_220543_eiffel_killed_by_host`, see the notes) | "Commands from a fresh copy to the first picture" |
| `checks/` | outputs of `scripts/compare.py` for each pair of pictures (`g15_repeat_*`, `tiled_vs_auto`, `legacy_vs_auto`, `g19_*`) and the sha256 table of the 7 engine binaries (`zip_vs_development_engine_sha256.txt`) | Repeat, forced fallback, `--vae tiled` and `--vae legacy` against `--vae auto`, released zip = development engine |

Notes:
- The folder `ssd_models/20261114_212254_fisherman` is a run that was stopped from outside (the host's memory manager ended the process tree while memory was low; `KILLED_BY_HOST_NOT_ENGINE.txt`). The log has no error line, there is no `image.png` or `run.json`. The run was repeated (`20261114_212743_fisherman`); only the repeated run is in the tables.
- `g11_fresh_copy/20261114_220543_eiffel_killed_by_host` is the first attempt of command 2; the host's memory manager stopped it (about 22:08, not an engine error). It was repeated at 22:09:11.
- `G19` (forced fallback): `SD_VAE_FULL_MARGIN_MB` was set to 100000 in the environment; `run.json` does not list that variable, the effect is visible in `stages.vae_full_fell_back` and `stages.vae_gate_residual_mib` (`checks/g19_note.txt`).
- Log files: terminal escape sequences removed and line endings normalized to LF, nothing else changed.
- Paths such as `E:\t\...` and `C:\sinirsiz_foto_m` are the test folders of this machine, not part of the software.
- No picture files are stored here, only their pixel hashes (`image_pixel_sha256` in each `run.json`).
