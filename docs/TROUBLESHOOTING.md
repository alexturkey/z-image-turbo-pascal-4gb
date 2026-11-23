# Troubleshooting

Labels: **measured** (we saw it on a GTX 1050 Ti 4 GB machine) and **not tested** (expected from how the tools work, we did not reproduce it).
For the order of steps see [AGENTS.md](../AGENTS.md). Every message below is printed by `scripts/setup.py` or `scripts/generate.py` or is a line in `log.txt`; `run.json` in the output folder (`outputs/<time>_<name>/`) holds the fields named in the tables.

## Setup

`setup.py` starts with a **Preflight** block: `Preflight (measured on: GTX 1050 Ti 4 GB laptop, ...)`, then your GPU (`GPU      : <name>, <MiB> MiB, driver <version>`), total RAM and free disk. Lines starting with `  WARNING  :` say you are below what we measured (less than 4 GB of GPU memory, less than 16 GB of RAM). They only inform; the setup goes on. Every `ERROR:` line of the scripts ends with `Fix: ...`, which is the first thing to try.

| Symptom | Cause | Fix |
|---|---|---|
| `python` is not recognised | Python not installed or not on PATH | Install Python 3.10 or newer, open a new terminal. (not tested) |
| Setup stops without `SETUP_OK` | A download did not finish, a sha256 did not match or an address is dead | Read the `ERROR:` line and run the same `setup.py` command again. Downloads resume from `.part` files. |
| `ERROR: <name>: sha256 mismatch (expected ..., got ...). The partial file was removed; run again.` | The download was damaged; the script already removed it | Run the same command again. If it repeats, do not edit `models.lock.json`; stop and open an issue with the file name and the hash you got. |
| `ERROR: <name>: download failed after <n> tries (...). Run setup again to resume.` | Connection, proxy, firewall | Run the same command again. The sources are Hugging Face, GitHub and (for cuDNN) NVIDIA; all must be reachable. |
| `ERROR: <name>: HTTP <code> for <url>` | The pinned address no longer answers | Running again will not help. Open an issue with the file name and URL. If it is the cuDNN address, setup can still finish with `--no-cudnn`. |
| `ERROR: <folder> has <x> GiB free, about <y> GiB more is needed.` | About 12 GB are needed for downloads (a little more with cuDNN), plus room for the unpacked files | Free space or pass another drive with `--models-dir` and `--bin-dir`. |
| `CUDNN_SKIPPED (not installed; generate.py will use --vae legacy). To install later: python scripts/setup.py --only cudnn` | You passed `--no-cudnn` (or `--check` found no cuDNN) | Not an error. Pictures are made with the slower v0.1.0 VAE path. To add cuDNN later: `python scripts/setup.py --only cudnn`. It downloads NVIDIA's cuDNN under NVIDIA's license (address in `models.lock.json`, field `cudnn.license_url`; the license says that whoever does not accept it must not download, install or use it). |
| `ERROR: install the engine first (sd-cli.exe not found in <dir>)` | `--only cudnn` was used before the engine was installed | Run `python scripts/setup.py` without `--only` (or `--only engine` first). |
| `ERROR: cuDNN DLLs are incomplete in <dir>` | The archive was unpacked but an expected file is missing | Delete the `cudnn*64_9.dll` files in that folder and run `python scripts/setup.py --only cudnn` again. If it repeats, open an issue. |
| The cuDNN download is about 367 MiB and takes long | It is NVIDIA's official archive; only eight DLLs are kept | Wait, or run again if interrupted (it resumes). The archive is deleted after it is unpacked. |

## Engine does not start

| Symptom | Cause | Fix |
|---|---|---|
| Dialog "cudart64_12.dll not found" (or cublas) | CUDA runtime zip not extracted next to `sd-cli.exe` | Re-run `python scripts/setup.py` and look for `CUDART_OK`. |
| Dialog about `vcruntime140_1.dll` or `MSVCP140.dll` | Microsoft Visual C++ runtime missing | Install `vc_redist.x64.exe` from https://aka.ms/vs/17/release/vc_redist.x64.exe. |
| Dialog about a missing `cudnn...64_9.dll` | cuDNN is partly installed | Delete the `cudnn*64_9.dll` files next to `sd-cli.exe`, then run `python scripts/setup.py --only cudnn` (it downloads cuDNN under NVIDIA's license, see above) or use `--vae legacy`. |
| `sd-cli.exe --help` prints nothing or crashes | Antivirus blocked the file, or a wrong engine build | Check `ENGINE_OK` in setup; allow the file in your antivirus. Other builds of the engine: not tested. |
| Log shows no CUDA device | Driver too old or no NVIDIA GPU | `nvidia-smi` must work and report CUDA 12.8 or higher. Not an NVIDIA card: see [`OTHER_GPUS.md`](OTHER_GPUS.md). |
| `ERROR: sd-cli.exe not found in <dir>. Run: python scripts/setup.py` | `--bin-dir` does not match the folder you gave to setup | Use the same `--bin-dir` for both scripts. |
| `ERROR: missing model file <path>. Run: python scripts/setup.py` | `--models-dir` does not match, or setup did not finish | Use the same `--models-dir` for both scripts and finish setup. |

## The VAE stage (the last stage of a run)

`run.json` says which path ran: `stages.vae_path` is `full` (whole image in one piece), `tile` (the large tile `generate.py` asked for), `floor` or `retry` (smaller tiles after a memory shortfall). `vae_mode` is the mode that was used, `vae_mode_requested` is what you asked for.

| Symptom | Cause | Fix |
|---|---|---|
| `WARNING: cudnn64_9.dll not found in <dir>; using --vae legacy (slower VAE, small tiles). Run: python scripts/setup.py` | The cuDNN DLLs are not next to `sd-cli.exe` | Intended fallback: the picture is made with the v0.1.0 path (`vae_mode` is `legacy` in `run.json`). To get cuDNN, see the setup table above. |
| `NOTE: the one-piece VAE decode did not fit in GPU memory; two large tiles were used instead.` | The memory check before the one-piece decode said no (`stages.vae_full_fell_back` is `true`, `vae_path` is `tile`) | Nothing to fix; this is the planned second step and its pixels match `--vae tiled`. Close other programs that use the GPU if you want the one-piece decode: the margin is thin (see below). |
| `NOTE: the VAE stage ran short of GPU memory and used small tiles` (`vae_quality_drop` is `true`, `vae_path` is `floor` or `retry`) | Even the large tile did not fit | The picture is valid but the VAE is closer to the old v0.1.0 quality (see Quality in [MEASUREMENTS.md](MEASUREMENTS.md)). Close other GPU programs (browser with hardware acceleration, games, a second `sd-cli`) and run again. |
| `NOTE: the log has no cuDNN convolution lines; the VAE may have run on the slow path.` | `stages.cudnn_used` is `false` although cuDNN was requested | Check that the eight `cudnn*64_9.dll` files are next to `sd-cli.exe` and that there is no other `sd-cli.exe` earlier on your PATH. If it stays, run with `--vae legacy` and open an issue with `run.json`. |
| The VAE stage takes minutes | Direct convolution without cuDNN is very slow (about 386 s in one of our tests) | `generate.py` avoids this by switching to `legacy` when cuDNN is missing; do not call `sd-cli` yourself with `--conv-direct` and no cuDNN. |
| Log line `VAE decode ran out of memory; retrying with spatial tiling` | At 768x1344 the VAE does not always fit in 4 GB in one piece | Normal and measured for the v0.1.0 path; the engine retries with tiles by itself. |

**The memory margin is thin.** On the 4 GB card, the memory left over at the one-piece check was about 45 MiB (1024x1024) and 87 to 89 MiB (768x1344, 1344x768) in the development build (a server run). A browser with hardware acceleration, a second GPU job or a different driver can eat that (not tested). The check then fails safely and the engine uses tiles; the cost is quality (see the table above), not a crash.
**A case we did not test:** we have not seen GPU memory run out *after* the engine's memory check passed (for example while cuDNN picks a convolution), and we did not test what happens then. If `generate.py` prints `FAILED: sd-cli exit code <n>`, close other GPU programs and run again; if it repeats, use `--vae tiled` or `--vae legacy` and open an issue with `log.txt`. The largest cuDNN workspace we measured was about 33 MiB (cap 256 MiB).

## During a run

| Symptom | Cause | Fix |
|---|---|---|
| Free RAM near zero, the machine feels stuck | The engine process peaked around 10 667–10 915 MiB resident on a 16 GB machine; free RAM fell to a few hundred MiB (measured) | Close browsers and other programs before starting; do not run two jobs. Machines with less than 16 GB: not tested. `generate.py` warns when less than 8000 MiB are free. |
| The run ends early or disappears while free RAM is a few hundred MiB | Free RAM is very low while the engine runs; one of our runs was stopped this way (see `docs/MEASUREMENTS.md`) | Close other programs and make one picture at a time. |
| Process killed, out of memory | Not enough free RAM or VRAM, another GPU program running | Close other programs, run alone. Check `Get-Process sd-cli` for a leftover process and end it. |
| Black picture or noise | Not seen in our runs. Likely a damaged model file or changed settings (not tested) | Re-run `setup.py` to re-verify files; use the default settings (8 steps, cfg 1.0, euler, simple). Do not add a negative prompt. |
| Very slow start | Model files on a spinning disk | Use an SSD. We measured two runs on one 2 TB laptop hard disk: 325 and 378 s per picture, see `docs/MEASUREMENTS.md`. |
| The first picture after a restart is slower | The model files are read from disk (cold start) | Expected; later pictures start faster. Cold and warm runs are not separated in every row of [MEASUREMENTS.md](MEASUREMENTS.md). |
| It takes much longer than the table in the README | Another program uses the GPU or CPU, the laptop is on battery or power-limited | Close other GPU programs, plug in power. Clock and power behaviour on other machines: not tested. |
| `FAILED: sd-cli exit code <n>. Read <log> and docs/TROUBLESHOOTING.md.` | The engine exited with an error | Open `log.txt` in the output folder and read the last lines; give the last 30 to the user or to an issue. |
| `WARNING: 1344x1344 is larger than the tested sizes ...` (any size above 1024x1024 in pixels) | You asked for more pixels than we tested | It may run out of memory; the tested sizes are 768x1344, 1344x768 and 1024x1024. |
| `WARNING: only <n> MiB RAM free; ...` | Less than 8000 MiB free at start | Close programs first. |

## Going back (rollback options)

| Want | How |
|---|---|
| The v0.1.0 VAE path for one picture | `python scripts/generate.py ... --vae legacy` |
| Always large tiles, never the one-piece try | `--vae tiled` |
| No cuDNN at all | delete the eight `cudnn*64_9.dll` files next to `sd-cli.exe` (`generate.py` then uses `legacy` by itself) |
| The old engine | not supported: the v0.2.0 engine is the one in `models.lock.json` |
| Engine switches (`SD_VAE_TRY_FULL` and others, listed in [`patches/README.md`](../patches/README.md)) | `generate.py` clears them from the environment and sets its own, so a run is reproducible. To experiment, call `sd-cli.exe` yourself (see the exact command in `run.json`). |

## Picture quality

| Symptom | Cause | Fix |
|---|---|---|
| Picture does not follow a detail of the prompt | Prompt fidelity is partial (village example: doors came out as separate huts) | Try another `--seed`, simplify the detail, see [PROMPTS.md](PROMPTS.md). |
| A famous place looks inaccurate | The model is not a photograph | Examples are labelled AI-generated; do not present them as real photos. |
| Unreadable text inside the picture | Text in pictures was not tested | Add the text afterwards in an image editor. |
| Your picture differs from the one in the README for the same prompt and seed | Different VAE path (`vae_path` in `run.json`), different engine or cuDNN build, or different size | Compare `PIXEL_SHA256` only with a run that used the same `vae_path`; use `python scripts/compare.py` to see how far apart two pictures are. |

<a id="error-codes"></a>
## Error codes

The scripts print the message without a code. Each message has a stable code in [`hata_imzalari.json`](hata_imzalari.json) (plain text signatures, a first step in English and Turkish); `python scripts/tani.py --log <file>` looks them up for you. The message pieces are checked against the scripts by `tests/test_agents_hizli.py`.

| Code | You see | First step |
|---|---|---|
| `ZIMG-E-SHA` | `sha256 mismatch` | Run the same command again; if it repeats, do not edit `models.lock.json`, open an issue. |
| `ZIMG-E-INDIRME` | `download failed after 6 tries` | Run the same command again (it resumes); check network, proxy, firewall. |
| `ZIMG-E-HTTP` | `HTTP 404 for <url>` | Running again will not help; open an issue with the file name and address. |
| `ZIMG-E-DISK` | `... GiB is needed` | Free space or use another drive with `--models-dir` and `--bin-dir`. |
| `ZIMG-E-KILIT` | `cannot read lock file` | Run from a complete copy of the repository. |
| `ZIMG-E-MOTOR` | `sd-cli.exe not found in` | `python scripts/setup.py` (or `--only engine`). |
| `ZIMG-E-CUDART` | `cudart64_*.dll not found` | Delete the engine folder, `python scripts/setup.py --only engine`. |
| `ZIMG-E-CUDNN` | `cuDNN DLLs are incomplete` | `python scripts/setup.py --only cudnn`, or `--vae legacy`. |
| `ZIMG-E-MODEL` | `missing model file` | `python scripts/setup.py` with the same `--models-dir`. |
| `ZIMG-E-BOYUT` | `Fix: use the tested size` | Multiples of 16 from 256 to 2048, or no `--width`/`--height`. |
| `ZIMG-E-ISTEM` | `the prompt is empty` / `cannot read prompt file` | Pass `--prompt` or an existing UTF-8 `--prompt-file`. |
| `ZIMG-E-URETIM` | `FAILED: sd-cli exit code` | Read `log.txt` and `run.json` in the output folder; close other programs. |

Check your machine without downloading anything: `python scripts/setup.py --dry-run` (ends with `DRYRUN_OK`, or with a disk `ERROR:` and exit code 3).

## Reporting a problem

Open an issue with: GPU name and `nvidia-smi` driver version, Windows version, free RAM at start, the command, the last 30 lines of the log and `run.json`.
Do not paste personal paths or names; replace them with `<DIR>`. Security reports: [`SECURITY.md`](../SECURITY.md).
