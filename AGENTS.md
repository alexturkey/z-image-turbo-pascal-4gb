# AGENTS.md: install and verify for an AI coding agent (Claude Code, Codex, Cursor...)

You are setting up **Z-Image-Turbo text-to-image on a Windows 10/11 PC with an NVIDIA 4 GB Pascal GPU (only the GTX 1050 Ti 4 GB laptop card was measured)**.
Follow the steps in order. Each step has **Command**, **Expected** and **If it fails**. Do not skip a check; if an
expectation fails, use the step's fix or the troubleshooting table at the end instead of improvising.
Messages to the user may be in the user's language; commands are language-neutral.
Evidence labels used here: "measured on GTX 1050 Ti 4 GB" (we ran it) and "not tested" (we did not).

## Hard rules (do not do these, with reasons)

| Do not | Why |
|---|---|
| Change the sd-cli settings (`--steps 8`, `--cfg-scale 1.0`, euler, simple, offload, mmap, flash-attn) | They are the tested point (measured on GTX 1050 Ti 4 GB). The model is a distilled 8-step model. Do not lower steps for speed and do not add a negative prompt (it is not used at cfg 1.0). |
| Run two generations at the same time | One 4 GB GPU and very little free RAM; the second job would run out of memory or slow both. |
| Open a browser or other heavy program during a run | Free RAM fell to 331-576 MiB during measured runs (16 GB machine). The engine process peaked around 10.5-10.9 GB resident. |
| Edit `models.lock.json` hashes or URLs to make a check pass | A mismatch means a different or damaged file. Re-download instead. |
| Replace the engine with another build | The engine zip carries the Pascal patches. Other builds: not tested. |
| Put models on a spinning disk | Only SSD was measured. A spinning disk: not tested. |
| Claim results for other GPUs, 8 GB RAM, Linux or macOS | Not tested. |
| Delete or move files outside the folders you were given | Use only the repo folder, `--models-dir`, `--bin-dir` and `outputs/`. |
| Commit, push or publish for the user | Only the user decides that. |

## 0. Prerequisites

| Need | Check command | Expected | If missing |
|---|---|---|---|
| NVIDIA GPU, 4 GB or more | `nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader` | e.g. `NVIDIA GeForce GTX 1050 Ti, 4096 MiB, 581.29` | No NVIDIA GPU: stop, this setup is CUDA only. |
| Driver new enough for CUDA 12.8 | `nvidia-smi` and read "CUDA Version" in the header | `12.8` or higher | Ask the user to update the NVIDIA driver. |
| Python 3.10+ on PATH | `python --version` | `Python 3.10` or newer | `winget install Python.Python.3.12` |
| Git | `git --version` | `git version 2.x` | `winget install Git.Git` |
| Microsoft Visual C++ runtime (x64) | `powershell -NoProfile -Command 'Test-Path $env:WINDIR\System32\vcruntime140_1.dll'` | `True` | Download `https://aka.ms/vs/17/release/vc_redist.x64.exe` and run it (we do not ship it). |
| Free disk | the `Get-PSDrive` command in the block below | at least 13 GB free on the drive (downloads are about 11.8 GB; extra room for the unpacked zips; estimate) plus a few MB per picture | Free space or choose another drive. `setup.py` also prints `ERROR: ... more is needed` when space is short. |
| Free RAM | `powershell -NoProfile -Command '[math]::Round((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory/1MB,1)'` | as high as possible; the measured machine has 16 GB total | Close programs. Machines with less than 16 GB RAM: not tested; tell the user. |
| Model drive type | the `Get-PhysicalDisk` command in the block below | the drive you will use for models is `SSD` | Warn the user: only SSD was measured. |

Run these in PowerShell (copy them as they are; they are written for PowerShell, not for `cmd`):
```powershell
Get-PSDrive -PSProvider FileSystem | Select-Object Name, @{n='FreeGB';e={[math]::Round($_.Free/1GB,1)}}
Get-PhysicalDisk | Select-Object FriendlyName, MediaType
```
If you run them from a tool that wraps commands in `powershell -Command "..."`, put the whole command in single quotes or save it to a `.ps1` file, because `$_` and `$env` are expanded by the outer shell inside double quotes.

## 1. Get the repository

Command:
```powershell
git clone https://github.com/alexturkey/sinirsiz-foto.git
cd sinirsiz-foto
```
Expected: folders `scripts`, `prompts`, `docs`, `tests`, `licenses`, and a file `models.lock.json`.
If it fails: check the network; keep the path short and ASCII-only.

## 2. Check the scripts start

Command: `python scripts/setup.py --help` and `python scripts/generate.py --help`
Expected: usage text, exit code 0, no traceback. `--models-dir`, `--bin-dir` appear in both.
If it fails: `python --version` must be 3.10 or newer. The scripts use only the standard library, so do not install packages.

## 3. Download and verify models and engine

Pick two folders (examples; replace them): models on an SSD, e.g. `D:\models`, and the engine in e.g. `D:\bin`.
Command:
```powershell
python scripts/setup.py --models-dir D:\models --bin-dir D:\bin
```
Expected (these exact lines, in this order of kinds): `MODEL_OK z_image_turbo-Q8_0.gguf`, `MODEL_OK Qwen3-4B-Instruct-2507-Q8_0.gguf`, `MODEL_OK ae.safetensors`, `ENGINE_OK`, `CUDART_OK`, and the last line `SETUP_OK`.
Download size is about 11.8 GB (models 11,193,150,692 bytes; engine zip 37,182,063 bytes; CUDA runtime zip 567,007,257 bytes); allow 20 to 60 minutes depending on the connection (estimate, not measured).
Downloads use `.part` files and resume; running the command again continues an interrupted download. Never `main` or `latest`: revisions are pinned in `models.lock.json`.
If it fails:
- `ERROR: <name>: sha256 mismatch (expected ..., got ...). The partial file was removed; run again.`: the script already removed the bad download. Run the same command again. If the same message repeats, stop and tell the user; do not edit `models.lock.json`.
- `ERROR: <name>: download failed after <n> tries (...). Run setup again to resume.`: a network problem. Run the same command again (it resumes from the `.part` file). Behind a proxy or without Hugging Face / GitHub access: stop and ask the user.
- `ERROR: <name>: HTTP <code> for <url>` (for example 404): the pinned address no longer answers. Running again will not help; stop and tell the user which file and URL.
- `ERROR: <folder> has <x> GiB free, about <y> GiB more is needed.`: free space or use another drive, then run again.
- The last line is not `SETUP_OK`: the setup is incomplete; do not go on to step 5.

## 4. Check that the engine starts

Command: `D:\bin\sd-cli.exe --help`
Expected: usage text, exit code 0, no "dll not found" dialog.
If it fails: a missing `cudart64_12.dll` or similar means the CUDA runtime zip was not extracted next to `sd-cli.exe`; re-run step 3. A missing `vcruntime140_1.dll` or `MSVCP140.dll` means the Visual C++ runtime from step 0 is missing.

## 5. First picture

Command:
```powershell
python scripts/generate.py --prompt-file prompts/eiffel.txt --models-dir D:\models --bin-dir D:\bin
```
Run it detached or with a tool timeout of at least 15 minutes: one picture took 250 to 259 seconds when measured, plus first-time disk reads (not measured separately). Do not start anything else on the machine meanwhile.
Expected: the last line is `IMAGE_OK <path>`, where `<path>` is an absolute path ending in `<YYYYmmdd_HHMMSS>_<name>\image.png` inside the `outputs` folder; next to it a `run.json` with the time, stages, peak VRAM and the exact command.
Measured on GTX 1050 Ti 4 GB at 768x1344: total 250.4-258.5 s with the development engine, 261.6 s with the release engine (clean-root test); peak VRAM 2949-2957 MiB.
A normal log line (not an error): `VAE decode ran out of memory; retrying with spatial tiling`. The engine retries by itself with smaller tiles.
If it fails: see the troubleshooting table below.

## 6. Check the result

Command: `powershell -NoProfile -Command "Get-Item outputs\*\image.png | Select FullName,Length"`
Expected: the file exists and is not empty (the script already checks this before it prints `IMAGE_OK`).
Then look at the picture (open it, or ask the user). A fully black picture means a failed run (see the table).
Tell the user the path and the elapsed time from `run.json`.

## 7. More pictures

- Your own prompt: `python scripts/generate.py --prompt "<text>" --models-dir D:\models --bin-dir D:\bin`
- Landscape: add `--width 1344 --height 768`. Other seed: `--seed <n>`. Other output folder: `--out <dir>`.
- Width and height must be multiples of 16 between 256 and 2048; `generate.py` rejects anything else with an `ERROR:` line. Sizes with more pixels than 768x1344 print a warning (not tested on 4 GB; may run out of memory). Sizes other than 768x1344 and 1344x768 are not tested.
- Prompt writing tips: `docs/PROMPTS.md`. One generation at a time.

## Troubleshooting

More cases in `docs/TROUBLESHOOTING.md`.

| Symptom | Likely cause | Fix |
|---|---|---|
| `python` not found | Python not on PATH | Install Python 3.10+, reopen the shell |
| Setup ends without `SETUP_OK` | Incomplete download, checksum mismatch or a dead address | Read the `ERROR:` line; run the same command again (step 3 explains each message); do not edit `models.lock.json` |
| Dialog "cudart64_12.dll not found" | CUDA runtime zip not extracted | Re-run `setup.py` and check for `CUDART_OK` |
| Dialog about `vcruntime140_1.dll` / `MSVCP140.dll` | Visual C++ runtime missing | Install `vc_redist.x64` (step 0) |
| Out of memory error or the process is killed | Free RAM or VRAM too low; another program running | Close other programs, run again alone; check that no second `sd-cli.exe` is running (`Get-Process sd-cli`) |
| Black or all-noise picture | A damaged model file or a changed setting | Re-run `setup.py` (it re-verifies hashes); do not change the sd-cli settings |
| Very slow start | Models on a spinning disk | Move models to an SSD (`--models-dir`) |
| `IMAGE_OK` missing, no traceback | The engine exited with an error | Open `run.json` and the log in the output folder; give the last 30 lines to the user |
| Picture does not match the prompt | Prompt fidelity is partial | See `docs/PROMPTS.md`; try another seed |

## Maintenance

- A change to settings, engine or models is accepted only with a before/after measurement on the same seed and a human look at the pictures. Record it in `docs/MEASUREMENTS.md` with the label "measured on ..." or "not tested".
- Do not add personal paths, names, e-mail addresses or machine-specific names to any file; run `python scripts/privacy_scan.py .` before the user commits. Expected finding that is not a problem: the upstream author's copyright line (with an e-mail address) in `licenses/LICENSE-oniguruma-BSD-2-Clause.txt`, which the BSD license requires us to keep. Report any other finding to the user.
