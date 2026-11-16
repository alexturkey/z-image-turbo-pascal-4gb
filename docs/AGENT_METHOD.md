# AGENT_METHOD.md: how an AI agent should run this job for a beginner

This page is for an AI coding agent (Claude Code, OpenAI Codex, Google Antigravity, Cursor, Gemini CLI or similar)
that a user has pointed at this repository, often with one sentence such as "set this up and make a picture".
Assume the user may never have used an agent before. Your job is to get them a working picture **without harming their
computer**, and to leave behind a folder that anyone (the user, you in a later session, another agent) can understand.

This page is the **working method**. The **steps** are elsewhere and are not repeated here:
- NVIDIA 4 GB Pascal on Windows: [`AGENTS.md`](../AGENTS.md).
- Any other card or system: [`OTHER_GPUS.md`](OTHER_GPUS.md) (which path exists for which card, with labels; AMD on Windows is its section 4).

The method is how this repository itself was built and checked: on one 4 GB laptop card, with every number measured and every important decision checked twice.

## 0. Start here (first session)

1. Talk to the user in **their language**, in plain words. Explain each technical word the first time you use it.
2. Read this page to the end.
3. Do the hardware inventory (section 1).
4. Choose the project folder (section 2) and clone this repository into it: `git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git repo`.
5. Read the local `repo\AGENTS.md` section 0. If the card is not an NVIDIA 4 GB Pascal card on Windows, read `repo\docs\OTHER_GPUS.md` and find the user's row.
6. Tell the user in three or four lines what you will do, how much will be downloaded (about 12 GB on the NVIDIA path; about 10.4 GiB of model files plus an engine zip on other paths), and which steps will need their approval (section 7).

If your tool cannot open web pages, ask the user to download the repository as a zip from its GitHub page and unpack it into `repo\`.

## 1. Know where you are: hardware first

Hardware decides everything else. Before any download or install, inventory the machine with **read-only** commands (PowerShell) and write the result to `notes\HARDWARE.md`:

| What | Read-only command |
|---|---|
| GPU name and driver version | `Get-CimInstance Win32_VideoController \| Select-Object Name,DriverVersion` |
| GPU memory | NVIDIA: `nvidia-smi --query-gpu=name,memory.total --format=csv`. Any card: `dxdiag /t notes\dxdiag.txt`, then read "Dedicated Memory" in that file (`Win32_VideoController.AdapterRAM` is wrong above 4 GB) |
| CPU | `Get-CimInstance Win32_Processor \| Select-Object Name,NumberOfCores` |
| RAM | `Get-CimInstance Win32_ComputerSystem \| Select-Object TotalPhysicalMemory` |
| Free disk per drive, SSD or HDD | `Get-PSDrive -PSProvider FileSystem`, `Get-PhysicalDisk \| Select-Object FriendlyName,MediaType,Size` |
| Windows version | `Get-CimInstance Win32_OperatingSystem \| Select-Object Caption,Version` |
| Python, Git | `python --version`, `git --version` (missing: see `AGENTS.md` P3 and P4; installing needs the user's approval) |

Compare it with what the user told you; if they differ, trust the commands and tell the user. Check every later decision
against this file (enough disk? enough memory? the right engine for this card?). Re-read it at the start of every session.

## 2. One project folder

Use the folder the agent was opened in, if its path is short, has no spaces or non-English letters and is on an SSD with at least 20 GB free. Otherwise propose one (for example `C:\ZImage`) and ask the user. Inside it:

```
<project>\
  repo\      this repository (git clone)
  engine\    the sd-cli build you use (one sub-folder per build, e.g. engine\vulkan\)
  models\    the three model files, and nowhere else
  outputs\   pictures
  logs\      console output of every run, process list, GPU lock
  notes\     HARDWARE.md, STATUS.md, DECISIONS.md, JOURNAL.md, MEASUREMENTS.md
```

- Model files are downloaded **once, into `models\`**: `python repo\scripts\setup.py --only models --models-dir models`, run from the project folder (it checks size and SHA-256 against `models.lock.json`; it may also create an empty `repo\bin\`, which is harmless). Before any download, check whether the file is already there and its hash matches. No second copy, no copy in Downloads.
- Do not write, move or delete anything outside this folder without asking (section 7).

## 3. Memory: never do the same work twice

Your chat memory ends with the session; the folder does not. Keep four files in `notes\`:

| File | What goes in | Rule |
|---|---|---|
| `STATUS.md` | where we are, what is done, the next step and its exact command | only the present; rewrite it after every step |
| `DECISIONS.md` | date, question, options, evidence, decision, who checked it | append only |
| `JOURNAL.md` | one line per finished step: time, step, result, output path | append only; take the time from a command (`Get-Date`), never guess it |
| `MEASUREMENTS.md` | command, date, number of runs, the number, which log it came from | append only |

At the start of **every** session, read `STATUS.md`, `DECISIONS.md` and the last lines of `JOURNAL.md` first, and continue
from there. Do not repeat a finished step. If the user says "continue", that means: read `STATUS.md`.

## 4. Stoppable and resumable work

- Long work is split into small steps; each step writes its result to disk before the next one starts.
- If a file named `STOP` appears in the project folder (the user can create it), finish the current small step, write `continue with: <command>` into `STATUS.md`, and stop. Do not kill processes halfway unless the user asks.
- Downloads resume and are verified at the end: `setup.py` resumes its own `.part` files when run again; for other files use `curl.exe -L -C - -o <file> <url>` and check `Get-FileHash <file> -Algorithm SHA256`. A partial file is never treated as finished.

## 5. The machine stays clean

- **Start the engine hidden and tracked**, so the window, the log and the process ID are handled in one step: `Start-Process -FilePath <sd-cli.exe> -ArgumentList '<arguments>' -WindowStyle Hidden -PassThru -RedirectStandardOutput logs\<run>.txt -RedirectStandardError logs\<run>.err`. Keep the returned object; its `.Id` is the process ID. (`OTHER_GPUS.md` section 4 has a complete example.)
- **One GPU job at a time.** Before GPU work, look at `logs\gpu.lock`. If it exists and the process ID in it is still running (`Get-Process -Id <id>`), wait. If that process is gone, the lock is stale: delete it and note that in `JOURNAL.md`. Otherwise write the **engine's** process ID (not your shell's) and the job name into the lock, and delete the lock when the engine exits. Also check that no game or other heavy program uses the GPU, and tell the user if one does.
- **No zombie processes.** Write the name and process ID of everything you start to `logs\processes.txt`. When a job ends, close it. At the end of the session `Get-Process sd-cli -ErrorAction SilentlyContinue` must return nothing; report anything still running.
- **No surprise windows.** Background work runs hidden; do not take over the user's screen, mouse or keyboard.

## 6. A team, and no decision rests on one agent

Split the work into roles. If your tool can start sub-agents, give each role its own agent; if not, play the roles one after another and say which one you are in:

| Role | Does |
|---|---|
| Hardware | inventory, driver and disk checks, `notes\HARDWARE.md` |
| Setup | clone, downloads, SHA-256 checks |
| Engine | chooses and tests the `sd-cli` build for this card |
| Reviewer | checks the others: evidence, notes, stale locks, leftover processes, nothing changed outside the folder |

**Important decisions** are: which engine path to use, installing a program, changing a setting, deleting anything, accepting a result as done. For each one:
1. Write the proposal and its evidence in `DECISIONS.md`.
2. Get an **independent second opinion**. With sub-agents: give one only the question and the files, not your own answer. Without sub-agents: answer this checklist as the Reviewer, in writing: did I read the source, is the command in a document, can it be undone, does it need the user's approval, is there another way? (If the user is comfortable with it, a new empty session in the same folder can do the review: "check the last decision in notes\DECISIONS.md".)
3. Put the two views side by side like a short meeting; the stronger evidence wins; write the outcome and who checked it.

## 7. Ask the user first

Always ask, in one plain sentence with the reason, before you:
- spend money, sign in to or change an account;
- install or remove a program or driver, change a system setting, the registry, the antivirus or the firewall;
- run anything as administrator;
- delete or overwrite anything, or write outside the project folder;
- download something not named in this repository's documents;
- commit, push or publish anything, or send a report.

Never disable security software. If an installer wants administrator rights, explain why before the user clicks yes.
Before anything is shared (a hardware report, a log), remove the user's name and personal paths from it.

## 8. Evidence, not guesses

- Label every claim: **measured** (you ran it here), **read in a document** (give the file or address), **guess**. Never show a number from another machine as this machine's result, and never promise speed.
- If you said something and it turns out wrong, say so plainly and correct it.
- **Same error twice, stop.** If a step fails twice the same way, do not try it a third time and do not invent a fix. Stop, show the last 30 lines of the log, and give the user 2 or 3 options with their cost and risk, and recommend one.

## 9. "It will not work" is a starting point, not an answer

When something "does not fit", "is not supported" or "is too slow", go through this list before you conclude:
1. **Measure:** which stage takes how long and how much memory?
2. **Split it:** tiles, stages, smaller pieces.
3. **Move it:** GPU or CPU (offload), which part where.
4. **Another way:** another prebuilt release, another backend (CUDA, Vulkan, ROCm/HIP), building from source.
5. **Solved before?** This repository's documents, the upstream documents and issues, community tests.
6. **Otherwise build it**, after asking the user.

**The limit:** quality settings are not lowered quietly. The model files (Q8_0), `--steps 8`, `--cfg-scale 1.0`, euler, simple and no negative prompt stay the same on every card. Memory and backend options (offload, mmap, tiling, flash attention, `--max-vram`, `--backend`) may change on other hardware, but only with a before/after measurement on the same seed and a look at both pictures. If quality and speed conflict, quality wins and the user decides.

## 10. End of the session

Report to the user, in their language:
- the picture's path (show it if you can), the engine path you used, the timing lines from the log;
- what you decided and who checked it (short summary of `DECISIONS.md`);
- that no process is left running and the GPU lock is gone;
- what is not tested.

Update `STATUS.md` and `JOURNAL.md`. If it worked, or failed in an interesting way, offer the user to send a
[hardware test report](https://github.com/alexturkey/z-image-turbo-pascal-4gb/issues/new?template=hardware-test.yml), with their consent; a failure is a finding too.
