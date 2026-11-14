# AGENTS.md: install and verify for an AI coding agent (Claude Code, Codex, Cursor...)

You are setting up **Z-Image-Turbo text-to-image on a Windows 10/11 PC with an NVIDIA 4 GB Pascal GPU (only the GTX 1050 Ti 4 GB laptop card was measured)**.
Follow the steps in order. Each step has **Command**, **Expected** and **If it fails**. Do not skip a check; if an
expectation fails, use the step's fix or the troubleshooting table at the end instead of improvising.
Messages to the user may be in the user's language; commands are language-neutral.
Evidence labels used here: "measured on GTX 1050 Ti 4 GB" (we ran it) and "not tested" (we did not).

## 0. Decide first

```
1. NVIDIA GPU with 4 GB, Windows x64?     nvidia-smi --query-gpu=name,memory.total --format=csv
   yes -> go to 2          no / other card -> go to 5
2. python scripts/setup.py                expect the last line: SETUP_OK
                                          (it downloads NVIDIA cuDNN by default and says so before the download; --no-cudnn skips it: read section 1 and S3 before you run it)
3. python scripts/generate.py --prompt-file prompts/eiffel.txt
                                          expect the last line: IMAGE_OK <path>
4. Open <path>. Done.
5. Not this hardware, or a step failed: do not improvise. Read patches/README.md, docs/BUILD.md,
   docs/MEASUREMENTS.md and docs/TROUBLESHOOTING.md, then tell the user what you found and what the options are.
```

If the card is not a 4 GB Pascal card, say so to the user before you download anything (about 12 GB): the engine in this repository is built for compute capability 6.1 only and other cards are not tested.

## 1. Hard rules (do not do these, with reasons)

| Do not | Why |
|---|---|
| **Hide cuDNN from the user, or choose for them that the license does not matter** | `setup.py` downloads NVIDIA cuDNN by default, under NVIDIA's own license (address printed by `setup.py` and in `models.lock.json`, field `cudnn.license_url`), and prints one line about it before the download. NVIDIA's license text says that whoever does not accept all its terms must not download, install or use the SDK. So tell the user in one line before you run it, with the address. Use `--no-cudnn` only if the user declines (see step S3). |
| Edit anything in `scripts/` | The scripts are the tested recipe. If a script seems wrong, stop and report it. |
| Change the sd-cli settings (`--steps 8`, `--cfg-scale 1.0`, euler, simple, offload, mmap, flash-attn) | They are the tested point (measured on GTX 1050 Ti 4 GB). The model is a distilled 8-step model. Do not lower steps for speed and do not add a negative prompt. |
| Edit `models.lock.json` hashes or URLs to make a check pass | A mismatch means a different or damaged file. Stop and tell the user; re-download once, never edit the lock. |
| Run two generations at the same time | One 4 GB GPU and very little free RAM; the second job would run out of memory or slow both. |
| Open a browser or other heavy program during a run | Free RAM fell to a few hundred MiB during measured runs (16 GB machine). The engine process peaked around 10 667–10 915 MiB. |
| Replace the engine with another build | The engine zip carries the Pascal patches. Other builds: not tested. |
| Put models on a spinning disk | Measured twice on one 2 TB laptop hard disk: 325 s and 378 s per picture (see `docs/MEASUREMENTS.md`); use an SSD. Other hard disks: not tested. |
| Claim results for other GPUs, less than 16 GB RAM, Linux or macOS | Not tested. |
| Delete or move files outside the folders you were given | Use only the repo folder, `--models-dir`, `--bin-dir` and `outputs/`. |
| Commit, push or publish for the user | Only the user decides that. |

## 2. Prerequisites

| # | Need | Check command | Expected | If missing |
|---|---|---|---|---|
| P1 | NVIDIA GPU, 4 GB or more | `nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader` | e.g. `NVIDIA GeForce GTX 1050 Ti, 4096 MiB, 581.29` | No NVIDIA GPU: stop, this setup is CUDA only. |
| P2 | Driver | `nvidia-smi`, note the "Driver Version" and "CUDA Version" in the header | information only: we measured with driver 581.29; older drivers were not tested | Write both values in your report to the user. If the engine later fails to start and the driver is old, suggest updating it; do not block on the value. |
| P3 | Python 3.10+ on PATH | `python --version` | `Python 3.10` or newer | `winget install Python.Python.3.12` |
| P4 | Git | `git --version` | `git version 2.x` | `winget install Git.Git` |
| P5 | Microsoft Visual C++ runtime (x64) | `powershell -NoProfile -Command 'Test-Path $env:WINDIR\System32\vcruntime140_1.dll'` | `True` | Download `https://aka.ms/vs/17/release/vc_redist.x64.exe` and run it (we do not ship it). |
| P6 | Free disk | the `Get-PSDrive` command below | at least 14 GB free on the drive (downloads about 12.2 GB with cuDNN, plus unpacked files; an estimate), plus a few MB per picture | Free space or choose another drive. `setup.py` prints `ERROR: ... more is needed` when space is short. |
| P7 | Free RAM | `powershell -NoProfile -Command '[math]::Round((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory/1MB,1)'` | as high as possible; the measured machine has 16 GB in total | Close programs. Machines with less than 16 GB RAM: not tested; tell the user. |
| P8 | Model drive type | the `Get-PhysicalDisk` command below | the drive you will use for models is `SSD` | Warn the user: on one 2 TB laptop hard disk a picture took 325 s and 378 s (two runs, `docs/MEASUREMENTS.md`); an SSD is recommended. |

Run these in PowerShell (copy them as they are; they are written for PowerShell, not for `cmd`):
```powershell
Get-PSDrive -PSProvider FileSystem | Select-Object Name, @{n='FreeGB';e={[math]::Round($_.Free/1GB,1)}}
Get-PhysicalDisk | Select-Object FriendlyName, MediaType
```
If you run them from a tool that wraps commands in `powershell -Command "..."`, put the whole command in single quotes or save it to a `.ps1` file, because `$_` and `$env` are expanded by the outer shell inside double quotes.

## 3. Steps

Pick two folders (examples; replace them): models on an SSD, e.g. `D:\models`, and the engine in e.g. `D:\bin`.
Every command below that takes `--models-dir` and `--bin-dir` must get the same two folders.

| # | Command | Expected | Check | If it fails |
|---|---|---|---|---|
| S1 | `git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git` then `cd z-image-turbo-pascal-4gb`. If you are already inside the repository folder, skip `git clone` | folders `scripts`, `prompts`, `docs`, `tests`, `patches`, `licenses` and a file `models.lock.json` | `dir` shows them | Check the network; keep the path short and ASCII-only. |
| S2 | `python scripts/setup.py --help` and `python scripts/generate.py --help` | usage text, exit code 0, no traceback | `--models-dir` and `--bin-dir` appear in both | `python --version` must be 3.10 or newer. The scripts use only the standard library; do not install packages. |
| S3 | Tell the user in one line about cuDNN (see below), then `python scripts/setup.py --models-dir D:\models --bin-dir D:\bin` (add `--no-cudnn` only if the user declines) | lines `MODEL_OK z_image_turbo-Q8_0.gguf`, `MODEL_OK Qwen3-4B-Instruct-2507-Q8_0.gguf`, `MODEL_OK ae.safetensors`, `ENGINE_OK`, `CUDART_OK`, then `CUDNN_OK` (default) or `CUDNN_SKIPPED` (`--no-cudnn`), and the last line `SETUP_OK` | last line is `SETUP_OK` | see the `ERROR:` table after this one. `--only models` and `--only engine` install one part each and end with `SETUP_PART_OK <part>` (not `SETUP_OK`: one part is not the whole setup) |
| S4 | `D:\bin\sd-cli.exe --help` | usage text, exit code 0, no "dll not found" dialog | exit code 0 | A missing `cudart64_12.dll` or similar: re-run S3. A missing `vcruntime140_1.dll` or `MSVCP140.dll`: install the runtime from P5. |
| S5 | `python scripts/generate.py --prompt-file prompts/eiffel.txt --models-dir D:\models --bin-dir D:\bin` | the last lines are, in this order, `<n> s` (seconds), `PIXEL_SHA256 <hex>` and `IMAGE_OK <path>` | see section 4 (acceptance) | see the troubleshooting table |
| S6 | Look at the picture (open it or ask the user) | a recognisable Eiffel Tower at sunset | not black, not noise | see the troubleshooting table |

**About cuDNN (S3).** cuDNN is optional NVIDIA software; it is not in this repository. With it, the last stage (VAE) is faster and closer to a reference decode (see `docs/MEASUREMENTS.md`). Without it everything still works with the slower v0.1.0 VAE path.
1. Tell the user in one line, before you run `setup.py`: it downloads NVIDIA cuDNN from NVIDIA's server by default (about 367 MiB) and copies 8 DLLs next to `sd-cli.exe`; cuDNN is under NVIDIA's license (address: `cudnn.license_url` in `models.lock.json`), it downloads without payment or sign-in, and we found no clause in the license that limits commercial or personal use; NVIDIA's license text says that whoever does not accept all its terms must not download, install or use the SDK; `--no-cudnn` skips it. Say no more than this: do not call it free, allowed or safe.
2. Run the command without `--no-cudnn`. If the user declines, add `--no-cudnn`. You can install cuDNN later with `python scripts/setup.py --only cudnn --models-dir ... --bin-dir ...`.
3. `--accept-cudnn-license` is still accepted for old command lines and changes nothing. Before the download `setup.py` prints one line (the license address and `Use --no-cudnn to skip.`) and records the license text, `mode: default_download_disclosed` and `installed_utc` in `cudnn_license_record.json` (the file records a disclosed default, not a decision by the user).
4. Do not edit the record or the license file. If the user does not want cuDNN, use `--no-cudnn`; everything still works with the slower v0.1.0 VAE path (`CUDNN_SKIPPED`).

Run S3 and S5 detached or with a tool timeout of at least 60 minutes for S3 (downloads are about 12.2 GB; it took 29 minutes once, on our connection) and at least 15 minutes for S5 (one picture took 193–228 s when measured). Do not start anything else on the machine meanwhile.
Downloads use `.part` files and resume: running the same command again continues an interrupted download. Revisions are pinned in `models.lock.json`; never `main` or `latest`.

### The Preflight block (S3)

Before any download `setup.py` prints `Preflight (measured on: GTX 1050 Ti 4 GB laptop, ...)` followed by `  GPU      : <name>, <MiB> MiB, driver <version>`, `  RAM      : <MiB> MiB total` and `  Disk     : <GiB> GiB free for models in <dir>` (and one for the engine folder). Lines that start with `  WARNING  :` mean your machine is below what we measured (less than 4 GB of GPU memory, less than 16 GB of RAM, little disk). It only informs and never stops the setup: read it, **tell the user about every WARNING before the downloads go on**, and let the user decide.

### `ERROR:` lines from `setup.py`

Every `ERROR:` line from `setup.py`, `generate.py` and `compare.py` ends with `Fix: ...`; do what it says first.


| Message (as printed; `<...>` varies) | Meaning | What to do |
|---|---|---|
| `ERROR: <name>: sha256 mismatch (expected ..., got ...). The partial file was removed; run again. Fix: run the same command again (downloads resume); if it repeats, see docs/TROUBLESHOOTING.md.` | The download was damaged; the script already removed it | Run the same command again. If the same message repeats, stop and tell the user; do not edit `models.lock.json`. |
| `ERROR: <name>: download failed after 6 tries (<reason>). Run setup again to resume. Fix: run the same command again (downloads resume); if it repeats, see docs/TROUBLESHOOTING.md.` | Network problem | Run the same command again (it resumes). Behind a proxy or without Hugging Face, GitHub or NVIDIA access: stop and ask the user. |
| `ERROR: <name>: HTTP <code> for <url>. Fix: run the same command again (downloads resume); if it repeats, see docs/TROUBLESHOOTING.md.` | The pinned address no longer answers (for example 404) | Running again will not help when the code is 404. Stop and tell the user which file and URL. |
| `ERROR: <folder> has <x> GiB free, about <y> GiB is needed. Fix: free disk space, or choose another drive with --models-dir / --bin-dir, then run the same command again.` | Not enough disk space | Do what the message says. |
| `ERROR: sd-cli.exe not found in <dir> after unpacking. Fix: delete that folder and run python scripts/setup.py --only engine again.` (also `cudart64_*.dll not found ...`) | The engine zip did not unpack as expected | Do what the message says; if it repeats, stop and tell the user. |
| `ERROR: sd-cli.exe not found in <dir>. Fix: install the engine first with python scripts/setup.py --only engine` | `--only cudnn` before the engine | Do what the message says. |
| `ERROR: cuDNN DLLs are incomplete in <dir>. Fix: run python scripts/setup.py --only cudnn again; see docs/TROUBLESHOOTING.md.` | cuDNN unpacked partly | Do what the message says. |
| `ERROR: cannot read lock file: <reason>. Fix: run from a complete copy of the repository, or pass --lock FILE.` | `models.lock.json` missing or damaged | Do what the message says; do not write a lock file yourself. |
| last line is not `SETUP_OK` | The setup is incomplete (a `SETUP_PART_OK <part>` line after `--only` is not `SETUP_OK` either) | Do not go on to S5. |

## 4. Acceptance: read `run.json`

After S5 open the newest `outputs/<YYYYmmdd_HHMMSS>_eiffel/run.json`. Accept the run only when:

| Field | Expected | Meaning if different |
|---|---|---|
| `result` | `"OK"` | `"FAILED"`: read `log.txt` in the same folder |
| `vae_mode` | `"auto"` if cuDNN was installed (the default); `"legacy"` if you used `--no-cudnn` | `vae_mode_requested` is `auto` but `vae_mode` is `legacy`: the cuDNN DLLs are missing; tell the user, then run `python scripts/setup.py --only cudnn` |
| `stages.vae_path` | `"full"` (whole image in one piece), `"tile"` is also fine | `"floor"` or `"retry"`: the VAE ran short of GPU memory and used small tiles; the picture is valid but lower quality. Close other GPU programs and run again; see `docs/TROUBLESHOOTING.md` |
| `stages.cudnn_used` | `true` when `vae_mode` is not `legacy` | `false`: the VAE may have run on the slow path; tell the user |
| `stages.vae_quality_drop` | `false` | `true`: same as `floor`/`retry` above |
| `image_pixel_sha256` | the same value as the `PIXEL_SHA256` line | Different: stop, something is wrong with the file |

Tell the user the path to `image.png` and the seconds from `run.json`. For the same prompt, seed and size, two runs on the same setup and on the same VAE path give identical pixels: `python scripts/compare.py <image A> <image B>` prints `SAME_PIXELS`.
Pixels depend on the VAE path (`vae_path`), so a picture made with `--vae legacy` is not pixel-identical to one made with `--vae auto`.

## 5. Rollback and other options

| Want | Command |
|---|---|
| Go back to the v0.1.0 VAE path (no cuDNN) for one picture | add `--vae legacy` to the `generate.py` command |
| Always use two large tiles | add `--vae tiled` |
| Remove cuDNN | delete the eight `cudnn*64_9.dll` files and `NVIDIA_cuDNN_LICENSE.txt`, `cudnn_license_record.json` next to `sd-cli.exe` (only after you list them to the user and the user agrees); `generate.py` then uses `legacy` by itself |
| More pictures | `python scripts/generate.py --prompt "<text>" --models-dir D:\models --bin-dir D:\bin`; landscape: `--width 1344 --height 768`; other seed: `--seed <n>`; other folder: `--out <dir>` |

Width and height must be multiples of 16 between 256 and 2048; `generate.py` rejects anything else with an `ERROR:` line. Sizes with more pixels than 1024x1024 print a warning (not tested on 4 GB; may run out of memory). Sizes other than 768x1344, 1344x768 and 1024x1024 are not tested.
Prompt writing tips: `docs/PROMPTS.md`. One generation at a time.

## 6. If the hardware does not fit

Different card, less than 16 GB RAM, Linux or macOS: do not try to make this work by editing the scripts. Everything the engine needs is open:
- `patches/README.md`: the engine patches, their order, the CMake flags of the released engine.
- `docs/BUILD.md`: how to build for another card, and what we did and did not test.
- `docs/MEASUREMENTS.md`: what was measured, so the user can compare.
Tell the user plainly what is untested and let them choose.

## Troubleshooting

More cases in `docs/TROUBLESHOOTING.md`.

| Symptom | Likely cause | Fix |
|---|---|---|
| `python` not found | Python not on PATH | Install Python 3.10+, reopen the shell |
| Setup ends without `SETUP_OK` | Incomplete download, checksum mismatch or a dead address | Read the `ERROR:` line; run the same command again; do not edit `models.lock.json` |
| `WARNING: cudnn64_9.dll not found ...; using --vae legacy` | cuDNN was not installed (`--no-cudnn` or a failed download) | Not an error. To install: tell the user in one line (see section 1), then `python scripts/setup.py --only cudnn` |
| `NOTE: the one-piece VAE decode did not fit in GPU memory; two large tiles were used instead.` | Planned fallback | Nothing to fix; `run.json` has `stages.vae_full_fell_back: true` |
| `NOTE: the VAE stage ran short of GPU memory and used small tiles` | Another program holds GPU memory | Close it, run again |
| Dialog "cudart64_12.dll not found" | CUDA runtime zip not extracted | Re-run `setup.py` and look for `CUDART_OK` |
| Dialog about `vcruntime140_1.dll` / `MSVCP140.dll` | Visual C++ runtime missing | Install `vc_redist.x64` (P5) |
| Out of memory error or the process is killed | Free RAM or VRAM too low; another program running | Close other programs, run again alone; check that no second `sd-cli.exe` is running (`Get-Process sd-cli`) |
| Black or all-noise picture | A damaged model file or a changed setting | Re-run `setup.py` (it re-verifies hashes); do not change the sd-cli settings |
| Very slow start | Models on a spinning disk | Measured twice on one 2 TB laptop hard disk: 325 and 378 s per picture, see `docs/MEASUREMENTS.md`; move models to an SSD (`--models-dir`) |
| `IMAGE_OK` missing, no traceback | The engine exited with an error | Open `run.json` and `log.txt` in the output folder; give the last 30 lines to the user |
| Picture does not match the prompt | Prompt fidelity is partial | See `docs/PROMPTS.md`; try another seed |

## Maintenance

- A change to settings, engine or models is accepted only with a before/after measurement on the same seed and a human look at the pictures. Record it in `docs/MEASUREMENTS.md` with the label "measured on ..." or "not tested".
- Do not add personal paths, names, e-mail addresses or machine-specific names to any file; run `python scripts/privacy_scan.py .` before the user commits. By default it does not scan `licenses/` (verbatim upstream texts) and prints `CLEAN: <n> file(s) scanned, 0 finding(s)`. With `--scan-licenses` it reports exactly one finding, an e-mail address in the upstream author's copyright line in `licenses/LICENSE-oniguruma-BSD-2-Clause.txt`; the BSD license requires us to keep it, so it is not a problem. Report any other finding to the user.
