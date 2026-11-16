# Claude Code notes

Install and verification steps: see `AGENTS.md` (the same rules apply to every agent). Fixed quality (the steps and
cfg in `scripts/generate.py` are not lowered for speed), one GPU job at a time, tell the user in one line about NVIDIA
cuDNN before you run `scripts/setup.py` (it downloads cuDNN by default under NVIDIA's license; `--no-cudnn` skips it;
see `AGENTS.md`), stop when a sha256 does not match, do not edit `scripts/`.
Working method (hardware first, one folder, notes, stop file, GPU lock, second opinion): `docs/AGENT_METHOD.md`.
