# Troubleshooting

Labels: **measured** (we saw it on a GTX 1050 Ti 4 GB machine) and **not tested** (expected from how the tools work, we did not reproduce it).
For the order of steps see [AGENTS.md](../AGENTS.md).

## Setup

| Symptom | Cause | Fix |
|---|---|---|
| `python` is not recognised | Python not installed or not on PATH | Install Python 3.10 or newer, open a new terminal. (not tested) |
| Setup stops without `SETUP_OK` | A download did not finish, a sha256 did not match or an address is dead | Read the `ERROR:` line and run the same `setup.py` command again. Downloads resume from `.part` files. |
| `ERROR: <name>: sha256 mismatch (expected ..., got ...). The partial file was removed; run again.` | The download was damaged; the script already removed it | Run the same command again. If it repeats, do not edit `models.lock.json`; stop and open an issue with the file name and the hash you got. |
| `ERROR: <name>: download failed after <n> tries (...). Run setup again to resume.` | Connection, proxy, firewall | Run the same command again. The sources are Hugging Face and GitHub; both must be reachable. |
| `ERROR: <name>: HTTP <code> for <url>` | The pinned address no longer answers | Running again will not help. Open an issue with the file name and URL. |
| `ERROR: <folder> has <x> GiB free, about <y> GiB more is needed.` | About 11.8 GB are needed for downloads, plus room for the unpacked zips | Free space or pass another drive with `--models-dir` and `--bin-dir`. |

## Engine does not start

| Symptom | Cause | Fix |
|---|---|---|
| Dialog "cudart64_12.dll not found" (or cublas) | CUDA runtime zip not extracted next to `sd-cli.exe` | Re-run `python scripts/setup.py ...` and look for `CUDART_OK`. |
| Dialog about `vcruntime140_1.dll` or `MSVCP140.dll` | Microsoft Visual C++ runtime missing | Install `vc_redist.x64.exe` from https://aka.ms/vs/17/release/vc_redist.x64.exe. |
| `sd-cli.exe --help` prints nothing or crashes | Antivirus blocked the file, or a wrong engine build | Check `ENGINE_OK` in setup; allow the file in your antivirus. Other builds of the engine: not tested. |
| Log shows no CUDA device | Driver too old or no NVIDIA GPU | `nvidia-smi` must work and report CUDA 12.8 or higher. |

## During a run

| Symptom | Cause | Fix |
|---|---|---|
| Log line `VAE decode ran out of memory; retrying with spatial tiling` | At 768x1344 the VAE does not fit in 4 GB in one piece | Nothing: this is normal and measured (the engine decodes in 384x672 tiles itself; 30 to 36 s). |
| Free RAM near zero, the machine feels stuck | The engine process peaked around 10.5-10.9 GB resident on a 16 GB machine; free RAM fell to 331-576 MiB (measured) | Close browsers and other programs before starting; do not run two jobs. Machines with less than 16 GB: not tested. |
| Process killed, out of memory | Not enough free RAM or VRAM, another GPU program running | Close other programs, run alone. Check `Get-Process sd-cli` for a leftover process and end it. |
| Black picture or noise | Not seen in our five runs. Likely a damaged model file or changed settings (not tested) | Re-run `setup.py` to re-verify files; use the default settings (8 steps, cfg 1.0, euler, simple). Do not add a negative prompt; at cfg 1.0 it has no effect according to the model discussion. |
| Very slow start | Model files on a spinning disk | Use an SSD. Only SSD was measured. |
| It takes much longer than about 260 s | Another program uses the GPU or CPU, laptop on battery or power-limited | Close other GPU programs, plug in power. Clock and power behaviour on other machines: not tested. |
| No `IMAGE_OK` line | The engine exited with an error | Open `run.json` and the log in the output folder (`outputs/<time>_<name>/`), read the last lines. |

## Picture quality

| Symptom | Cause | Fix |
|---|---|---|
| Picture does not follow a detail of the prompt | Prompt fidelity is partial (village example: doors came out as separate huts) | Try another `--seed`, simplify the detail, see [PROMPTS.md](PROMPTS.md). |
| A famous place looks inaccurate | The model is not a photograph | Examples are labelled AI-generated; do not present them as real photos. |
| Unreadable text inside the picture | Text in pictures was not tested | Add the text afterwards in an image editor. |

## Reporting a problem

Open an issue with: GPU name and `nvidia-smi` driver version, Windows version, free RAM at start, the command, the last 30 lines of the log and `run.json`.
Do not paste personal paths or names; replace them with `<DIR>`.
