# Experimental Apple Silicon / Metal setup

This community setup uses the **unpatched upstream Metal engine**, not the
Windows/Pascal release. The [community report](docs/OTHER_GPUS.md#3a-community-test-apple-m5-macos-metal)
records the hardware, date, one measured run and its limits. Other Macs and macOS
versions are not tested by that report.

The original model files, 8 steps, CFG 1.0, Euler/simple and no negative prompt
are preserved. The Pascal patches and cuDNN are not used.

## 1. Check the machine and folder

You need an Apple Silicon Mac, Git and Python 3.10 or newer. Before downloading:

```sh
uname -m
sw_vers
python3 --version
git --version
df -h .
```

Expected architecture: `arm64`. Use an SSD with room for the model files
(about 10.4 GiB), the engine archive, extracted files and outputs.
The reported machine has 16 GB of unified memory; less memory is not tested.
Clone the repository, or use an existing clone, and run the rest from its root:

```sh
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
```

Run one engine process at a time. Stop any existing generation or web server
before unpacking an engine or starting another one.

## 2. Download and verify the models

```sh
python3 scripts/setup.py --only models
```

This standard-library downloader resumes `.part` files and verifies the sizes
and SHA-256 values in `models.lock.json`. It ends with `SETUP_PART_OK models`,
not the full Windows `SETUP_OK`. Its preflight NVIDIA warning comes from the
Windows hardware probe; check Metal separately below. Use **only** the models
option: full setup downloads the Windows engine and NVIDIA libraries.
For existing files, `python3 scripts/setup.py --only models --check` verifies
them without downloading anything.

## 3. Install the pinned upstream Mac package

The [upstream release](https://github.com/leejet/stable-diffusion.cpp/releases/tag/master-1088-32d516c)
is `master-1088-32d516c`, commit `32d516c0197ed5ca31305b8575e14eb1451fad33`.
Check the archive against its published SHA-256 before extracting it:

```sh
python3 - <<'PY'
import sys
from pathlib import Path

sys.path.insert(0, str(Path('scripts').resolve()))
from setup import download, is_verified, safe_extract

name = 'sd-master-32d516c-bin-Darwin-macOS-26.7.2-arm64.zip'
entry = {
    'name': name,
    'url': 'https://github.com/leejet/stable-diffusion.cpp/releases/download/master-1088-32d516c/' + name,
    'bytes': 38105745,
    'sha256': 'b6588e81e788d9f2f24498831ba398d7523152e7ec280ff282f39c2009465b77',
}
archive = Path('bin/_downloads') / name
if not is_verified(archive, entry):
    download(entry['url'], archive, entry['bytes'], entry['sha256'])
target = Path('bin/metal')
safe_extract(archive, target)
for executable in ('sd-cli', 'sd-server'):
    (target / executable).chmod(0o755)
print('METAL_ENGINE_OK')
PY
```

Continue only after the Python command exits successfully and prints
`METAL_ENGINE_OK`. If verification or extraction fails, stop; do not use an
older installation's help output as evidence that this installation succeeded.

```sh
bin/metal/sd-cli --help
bin/metal/sd-cli --list-devices
```

Keep all extracted files together. Expected: `METAL_ENGINE_OK`, successful help
output, then a Metal device such as `MTL0 Apple M5`. CPU/Accelerate alone does not
verify Metal. Sandboxed agent tools may hide the GPU; use the tool's normal
permission flow to obtain GPU access. On a hash mismatch, stop; do not change
the expected hash. The asset name does not establish a minimum macOS version.

## 4. Generate directly with the native CLI

Use `sd-cli` directly, as described in [OTHER_GPUS.md](docs/OTHER_GPUS.md):

```sh
mkdir -p outputs
bin/metal/sd-cli \
  --diffusion-model models/z_image_turbo-Q8_0.gguf \
  --vae models/ae.safetensors \
  --llm models/Qwen3-4B-Instruct-2507-Q8_0.gguf \
  --prompt-file prompts/eiffel.txt \
  --cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple \
  --offload-to-cpu --mmap --eager-load --flash-attn on \
  -s 42 -W 768 -H 1344 -v -o outputs/macos_eiffel.png \
  > outputs/macos_cli.log 2>&1
```

Wait for exit code 0 and the log's successful image-save message. Open the PNG:
it should show a recognisable Eiffel Tower, not black pixels or noise.
Stage timings are in `outputs/macos_cli.log`. The native CLI does not create
`run.json` or print the Python wrapper's `IMAGE_OK` marker.

The historical report used an unchanged Python wrapper with a Mac-only
executable-name symlink. Its [recorded engine argv](docs/evidence/macos_m5/run.json)
has the same model and sampling options. The direct command above uses the
original prompt file and was not separately timed; do not attribute the
reported wrapper wall time to this shell command.

## 5. Optional web UI

Start the native server instead of the CLI:

```sh
bin/metal/sd-server \
  --listen-ip 127.0.0.1 --listen-port 7860 --max-pending-jobs 1 \
  --model-dir models \
  --diffusion-model models/z_image_turbo-Q8_0.gguf \
  --vae models/ae.safetensors \
  --llm models/Qwen3-4B-Instruct-2507-Q8_0.gguf \
  --offload-to-cpu --mmap --eager-load --flash-attn on \
  --steps 8 --cfg-scale 1.0 --sampling-method euler --scheduler simple \
  -s 42 -W 768 -H 1344
```

Keep that terminal open and visit [the local UI](http://127.0.0.1:7860).
The startup model and settings are preloaded. Enter a prompt, click **Generate**,
then **Download**. Stop the server with **Ctrl+C** before CLI generation; its
model context stays loaded while it is running. It binds only to loopback.
The community setup also exercised Generate/Download; its different prompt and
timing are not part of the single CLI timing report.

No before/after benchmark, repeated-seed test, or pixel/quality parity test with
the patched Windows path was performed. Windows-only memory and VAE-path
instrumentation does not measure Metal. Follow [AGENT_METHOD.md](docs/AGENT_METHOD.md)
for process tracking, one GPU job at a time, and consent before publishing logs.
