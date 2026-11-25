# Evidence: copy/compute overlap (engine patch 0030, v0.3.0)

Files behind `docs/MEASUREMENTS.md` Table 4 (development engine, 12 runs) Table 4b (series, development setup) and Table 5 (the release zip through `generate.py`). One machine: GTX 1050 Ti 4 GB laptop, 2026-11-25.

| File | What it is | Supports |
|---|---|---|
| `runs.csv` | the 12 runs of Table 4: arm, clock time, `generate` time, text/sampling/VAE seconds, step 1, mean of steps 2 to 8, `vae_path`, tile fallback, RGB hash (first 12 hex digits), lowest free RAM | Table 4 |
| `logs/A3_v0.2.0_engine_log.txt`, `logs/C2_overlap_on_log.txt`, `logs/C3_overlap_on_log.txt` | verbose engine logs of one arm A run and two arm C runs (terminal escape sequences removed and line endings normalized to LF, nothing else changed). The C logs end with the line `STAGING_PINNED total: ring ... pageable fallback 0` | Table 4, `copy_overlap_used` |
| `tablo_iz_off.md`, `tablo_iz_on.md`, `tablo_o2_iz_on.md` | per-step tables of a device-clock trace (matmul, attention, other ops, gaps, copy time, how much of the gap overlaps a copy) with the switches off and on | "waiting for a weight copy 1.38 s to 0.03 s per step" |
| `source_tree_check.md` | how the patched source tree was compared with the tree the release engine was built from, and the rebuild comparison (commands, result) | Checks table, `patches/README.md` |
| `engine_binaries_sha256.txt` | sha256 of the 7 binaries in the release zip (the same files as the engine of the 12 runs: byte for byte) | Checks table |
| `series_model_kept_loaded.csv` | the 10 pictures of the new series (v0.3.0 engine, model kept loaded, development setup) and the 10 of the earlier v0.2.0 engine series (2026-11-15), seconds per picture | Table 4b |
| `release/` | the Table 5 runs: `run.json` and `log.txt` of each, the memory samples, the setup log | Table 5 |

Notes:
- Paths such as `E:\sinirsiz_foto\...` and `C:\sinirsiz_foto_m` are test folders of this machine, not part of the software.
- No picture files are stored here, only their pixel hashes.
- The trace tool that produced the three tables is a separate engine build (it adds a device-clock event log); it is not part of the release and not in this repository.
