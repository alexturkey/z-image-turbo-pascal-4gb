# Other GPUs and systems: which path to take

This repository was built and measured on **one machine: a GTX 1050 Ti 4 GB laptop (NVIDIA Pascal, sm_61), 16 GB RAM, Windows 10**.
The release engine, `scripts/setup.py` and `scripts/generate.py` are for Windows and NVIDIA only.
This page is for everyone else, and for their AI agents: read it **before** you download about 12 GB, so you know which path exists for your card, what carries over from this repository and what does not.

Three labels are used here and they are never mixed:

| Label | Meaning |
|---|---|
| **measured by us** | we ran it on the machine above; the numbers are in [`MEASUREMENTS.md`](MEASUREMENTS.md) |
| **community test** | someone else ran it on their machine and published it; we did **not** repeat it |
| **not tested** | nobody we know of has reported it; at most, an upstream document says it is supported |

## 1. Which path for my card

| Your system | Path | Label |
|---|---|---|
| GTX 1050 Ti 4 GB, Windows | The normal setup in the [README](../README.md) | measured by us (one card) |
| Other NVIDIA Pascal card (sm_61, for example GTX 1050, 1060, 1070, 1080), Windows | The same setup; the prebuilt engine zip targets sm_61 | not tested |
| Other NVIDIA card, Windows | Build the engine from our patches with your CUDA architecture: [`BUILD.md`](BUILD.md). Several patches are tuned for Pascal; read "What may not carry over" there | not tested |
| NVIDIA card, Linux | Build the engine yourself: our patches with [`BUILD.md`](BUILD.md) (its steps are written for Windows), or upstream "Build with CUDA" | not tested |
| AMD card, Linux (ROCm) | Section 3 below: unpatched upstream engine, built with HIP, run directly with `sd-cli` | community test (one RX 6600 XT 8 GB) |
| AMD card, Windows (ROCm / HIP SDK) | Upstream build guide, section "Build with HIPBLAS", Windows part: [docs/build.md](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/build.md) | not tested |
| AMD, Intel or other card through Vulkan (Windows or Linux) | Upstream build guide, section "Build with Vulkan" | not tested |
| Intel Arc through SYCL | Upstream build guide, section "Build with SYCL" | not tested |
| Apple Silicon Mac (Metal) | Upstream build guide, section "Build with Metal" | not tested |
| No GPU | Upstream lists a CPU backend; speed with these 10 GB of model files unknown | not tested |

The backend list (CPU, CUDA, Vulkan, Metal, OpenCL, SYCL) is from the upstream [stable-diffusion.cpp README](https://github.com/leejet/stable-diffusion.cpp); HIP (AMD) has its own section in the upstream build guide. Both were read on 2026-11-16. Upstream says these backends exist; it does not say how fast Z-Image-Turbo Q8_0 runs on them.

If your card is in a "not tested" row and you try it, please report it (section 5): that is how a row moves to "community test".

## 2. What carries over from this repository, and what does not

**Carries over (any system):**
- **The model files.** [`models.lock.json`](../models.lock.json) lists the three files (Z-Image-Turbo Q8_0, Qwen3-4B-Instruct-2507 Q8_0, `ae.safetensors`, about 10.4 GiB together) with pinned addresses, byte sizes and SHA-256. Download them from those addresses and check the hashes; the community test in section 3 used exactly these files. `python scripts/setup.py --only models --models-dir <folder>` downloads and verifies only these three files with the Python standard library; outside Windows it is not tested (it prints a GPU warning first and does not stop).
- **The settings.** `--steps 8 --cfg-scale 1.0 --sampling-method euler --scheduler simple`, seed 42 for comparison, no negative prompt. The model is distilled for 8 steps; lowering them is not a speed fix. A base `sd-cli` command for any backend (not tested by us outside our own engine; add the backend and memory options from your build guide or from section 3):
  ```bash
  sd-cli --diffusion-model models/z_image_turbo-Q8_0.gguf --llm models/Qwen3-4B-Instruct-2507-Q8_0.gguf \
    --vae models/ae.safetensors --offload-to-cpu --mmap \
    --sampling-method euler --scheduler simple --steps 8 --cfg-scale 1.0 --seed 42 \
    --width 768 --height 1344 --output outputs/test.png -p "<your prompt>"
  ```
- **The prompts** in `prompts/` and the advice in [`PROMPTS.md`](PROMPTS.md).
- **The comparison tool.** `scripts/compare.py` uses only the Python standard library (pixel hash, largest difference, PSNR of two pictures). Running it outside Windows: not tested.

**Does not carry over:**
- **The release engine zip:** a Windows build for sm_61 only.
- **`scripts/setup.py` (full setup):** it warns when there is no NVIDIA GPU but does not stop, and then downloads the Windows engine zip and NVIDIA files you cannot use elsewhere. Use `--only models` instead (above).
- **`scripts/generate.py`:** it looks for `sd-cli.exe`, reads GPU memory with `nvidia-smi`, sets environment switches that only our patched engine reads and uses the cuDNN VAE path when present. On another system it stops with `ERROR: sd-cli.exe not found ...` or measures the wrong thing.
- **Do not edit these scripts to make them run elsewhere**; call `sd-cli` directly instead, as in section 3.
- **The patches in [`patches/`](../patches/README.md):** most are written for Pascal. Whether any of them helps another card is not tested.
- **Our timings and pixel hashes:** they hold for our card, our engine and the same VAE path. Different hardware or engine means different pixels; that alone is not an error.

## 3. Community test: AMD RX 6600 XT 8 GB, Ubuntu 24.04, ROCm 7.2.4

> **Community test, not ours.** Run and written by **Hakan (GitHub [hknklnc10](https://github.com/hknklnc10))** on 2026-11-15 and published as a technical report: [gist.github.com/hknklnc10/fa19ea3813238bd64853be2a814e4f18](https://gist.github.com/hknklnc10/fa19ea3813238bd64853be2a814e4f18) (the revision we read: [5b292f9](https://gist.github.com/hknklnc10/fa19ea3813238bd64853be2a814e4f18/5b292f9bd15a7eb19b918b56a85db1e44c2d64b4)). The report invites the maintainer to reuse or adapt it; this section is our shortened adaptation. The full report has more detail, including GPU profiling.
> **What it is:** unpatched upstream stable-diffusion.cpp at commit `01c463a` (ggml `eeda9ec`), built with HIP, run directly with `sd-cli`. It is **not** our patched engine (`32d516c` plus `patches/`), and none of our scripts were used.
> **What it is not:** a measurement by us, a statement about other AMD cards, or a supported release. One machine; every number is a single run.

Thank you, Hakan, for the careful work and for marking its limits so clearly.

### Machine

| Part | Tested |
|---|---|
| OS | Ubuntu 24.04.5 LTS (Xubuntu), x86_64 |
| GPU | AMD Radeon RX 6600 XT 8 GB (physically `gfx1032`, run as `gfx1030` with `HSA_OVERRIDE_GFX_VERSION=10.3.0`) |
| CPU, RAM | Ryzen 5 3600, 31 GiB RAM + 8 GiB swap |
| ROCm | 7.2.4 |
| Build tools | gcc/g++ 13.3.0, cmake 3.31.6, git 2.43.0 |
| Engine | upstream `01c463a223203f374f70b2a0aa83c1301cdbcaae`, ggml `eeda9ec`, `-DSD_HIPBLAS=ON` |

### Steps (condensed from the report)

The commands below are the report's, shortened: flags joined on fewer lines, the prompt replaced by a placeholder, and the report's extra checks (`--version`, `ldd`, the CMake cache check) and `--batch-count 1 --verbose` left out. If something differs on your machine, compare with the full report.

Work in one folder with a clone of this repository (`z-image-turbo-pascal-4gb/`, for `models.lock.json`), `stable-diffusion.cpp/`, `models/` and `outputs/`.

1. Check that ROCm sees the card:
   ```bash
   ls -l /dev/kfd /dev/dri/renderD128
   HSA_OVERRIDE_GFX_VERSION=10.3.0 rocminfo
   ```
2. Get the engine at the tested commit:
   ```bash
   git clone https://github.com/leejet/stable-diffusion.cpp.git ./stable-diffusion.cpp
   git -C ./stable-diffusion.cpp checkout 01c463a223203f374f70b2a0aa83c1301cdbcaae
   git -C ./stable-diffusion.cpp submodule update --init --depth 1 -- ggml
   ```
3. Build with HIP (`gfx1030` is the target the report used for its RX 6600 XT; see "Read with care"):
   ```bash
   export ROCM_PATH=/opt/rocm
   export PATH="$ROCM_PATH/bin:$PATH"
   export LD_LIBRARY_PATH="$ROCM_PATH/lib:$ROCM_PATH/lib64${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
   export HSA_OVERRIDE_GFX_VERSION=10.3.0

   cmake -S ./stable-diffusion.cpp -B ./stable-diffusion.cpp/build-hip -G 'Unix Makefiles' \
     -DCMAKE_BUILD_TYPE=Release -DSD_HIPBLAS=ON \
     -DGPU_TARGETS=gfx1030 -DCMAKE_HIP_ARCHITECTURES=gfx1030 \
     -DCMAKE_HIP_COMPILER="$ROCM_PATH/llvm/bin/clang++" \
     -DCMAKE_C_COMPILER="$(command -v gcc)" -DCMAKE_CXX_COMPILER="$(command -v g++)" \
     -DCMAKE_PREFIX_PATH="$ROCM_PATH" \
     -DSD_CUDA=OFF -DSD_VULKAN=OFF -DSD_WEBP=OFF -DSD_WEBM=OFF -DSD_SERVER_BUILD_FRONTEND=OFF
   cmake --build ./stable-diffusion.cpp/build-hip --config Release --target sd-cli --parallel 2
   ./stable-diffusion.cpp/build-hip/bin/sd-cli --list-devices
   ```
   Expected: a line naming `ROCm0` and the card.
4. Download the three model files into `models/` from the addresses in `models.lock.json` (the report used its own resumable `curl` script with a size and hash check; the full report has it), or try `python3 z-image-turbo-pascal-4gb/scripts/setup.py --only models --models-dir models` (not tested on Linux; it also creates an empty `bin/` folder). Then check them (hashes from `models.lock.json`):
   ```bash
   sha256sum -c <<'EOF'
   df1c5baa86d1398c979495a6072dbcee79444fdb884a2445582ba0769c44e9a1  models/z_image_turbo-Q8_0.gguf
   391c1e410fd9f4cf2de2b510273b56a84c19ce18f4fa3bfb3774031dac4ef068  models/Qwen3-4B-Instruct-2507-Q8_0.gguf
   afc8e28272cd15db3919bacdb6918ce9c1ed22e96cb12c4d5ed0fba823529e38  models/ae.safetensors
   EOF
   ```
5. Generate (the faster of the two reported setups: text encoder on CPU, diffusion and VAE on the GPU, a 6 GiB budget):
   ```bash
   export HSA_OVERRIDE_GFX_VERSION=10.3.0
   export LD_LIBRARY_PATH="/opt/rocm/lib:/opt/rocm/lib64${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
   ./stable-diffusion.cpp/build-hip/bin/sd-cli \
     --diffusion-model ./models/z_image_turbo-Q8_0.gguf \
     --llm ./models/Qwen3-4B-Instruct-2507-Q8_0.gguf \
     --vae ./models/ae.safetensors \
     --backend diffusion=ROCm0,te=cpu,vae=ROCm0 \
     --offload-to-cpu --mmap --flash-attn off,diffusion=on --max-vram ROCm0=6 \
     --sampling-method euler --scheduler simple --steps 8 --cfg-scale 1.0 --seed 42 \
     --width 1024 --height 1024 --output ./outputs/test_1024.png -p "<your prompt>"
   ```
   The slower setup keeps the VAE on the CPU: `--backend diffusion=ROCm0,te=cpu,vae=cpu` and no `--max-vram`. `--max-vram ROCm0=6` was chosen for this 8 GB card; other memory sizes: not tested.

### Reported numbers (community test, one run each, 2026-11-15)

Same prompt (a living room), seed 42, 8 steps. Seconds for the whole picture; in brackets: text encoder / diffusion / VAE.

| Size | VAE on CPU, no `--max-vram` | VAE on GPU, `--max-vram ROCm0=6` |
|---|---|---|
| 512x512 | 51.21 s (4.12 / 29.66 / 15.61) | 15.04 s (1.24 / 11.44 / 1.39) |
| 768x768 | 58.98 s (1.28 / 20.39 / 36.23) | 26.56 s (1.27 / 22.21 / 1.99) |
| 1024x1024 | 109.13 s (1.28 / 38.12 / 68.40) | 53.88 s (1.26 / 42.28 / 9.05) |

Peak process RAM: up to 16.89 GiB with the VAE on the CPU, 10.42–10.43 GiB with the VAE on the GPU. At 1024x1024 the one-piece GPU VAE did not fit the 6 GiB budget and the engine fell back to 9 tiles by itself; that picture differs slightly from the CPU-VAE one (PSNR 44.12 dB), at 512 and 768 the difference is smaller (54.26 and 54.71 dB).

The report also lists what did **not** help on this card: a `GGML_CUDA_FORCE_CUBLAS=ON` build (512x512 took 27.62 s instead of 15.04 s and the picture changed, PSNR 24.96 dB), `--disable-prefetch` (no change), `GGML_CUDA_DISABLE_GRAPHS=1` (55.63 s instead of 53.88 s, one run), and `--max-vram ROCm0=6.5` (no change, still 9 tiles).

### Read with care (our notes, from reading the report; we did not run it)

- **Two changes at once.** The faster setup moves the VAE to the GPU *and* adds `--max-vram`, which per the report also split diffusion into 36 segments instead of 1; the report itself warns not to credit the GPU VAE alone and names cold-start effects. At 768 and 1024 the gain is almost all in the VAE stage (36.23 → 1.99 s, 68.40 → 9.05 s); diffusion was not faster there (20.39 → 22.21 s and 38.12 → 42.28 s). The 512x512 baseline was the first, cold run (text encoder 4.12 s against about 1.3 s later), so in our reading "51 → 15 s" overstates the gain at that size.
- **Not comparable with our tables.** Different engine (no patches), different card, different sizes (our standard size 768x1344 was not run there), different attention setting (`--flash-attn off,diffusion=on` there, `--flash-attn on` and `--eager-load` in our scripts).
- **`HSA_OVERRIDE_GFX_VERSION=10.3.0` and `gfx1030` were chosen for this card.** The report uses them so that the RX 6600 XT (`gfx1032`) runs kernels built for `gfx1030`. Our reading, not tested: another AMD card may need a different value or none; check AMD's ROCm documentation for your card before copying them. The report kept the variable in the shell it ran in, not system-wide.
- **Same seed, same pixels** holds only within one setup and one VAE path, here as in our own tests.

### If it does not work (from the report's troubleshooting table)

| What you see | Likely cause, per the report | What the report did |
|---|---|---|
| `rocminfo` fails, or permission denied on `/dev/kfd` | no read/write access to `/dev/kfd` and `/dev/dri/renderD128`, or a restricted container | check `ls -l /dev/kfd /dev/dri/renderD128`; add your user to the `render` and `video` groups if your system needs it |
| `sd-cli --list-devices` shows only `CPU`, or crashes | `HSA_OVERRIDE_GFX_VERSION` or `LD_LIBRARY_PATH` not set in this shell | export both, as in step 5 |
| `vae segment 1/1 (graph) failed during weight preparation` at 1024x1024 | the one-piece VAE needs more than the 6 GiB budget | expected; the engine retries with 9 tiles by itself and finishes |
| Out of GPU memory | another program holds GPU memory, or `--max-vram` is unset or too high with `vae=ROCm0` | close browsers and games; the report required at least 6.75 GiB free GPU memory before a run with `--max-vram ROCm0=6` |
| System RAM runs out | the CPU-VAE setup peaked at 16.89 GiB | use the GPU-VAE setup (10.42–10.43 GiB) |

### Not covered by the report

How to install ROCm 7.2.4 (see AMD's [ROCm installation guide](https://rocm.docs.amd.com/en/latest/install/rocm.html)), adding your user to the `render` and `video` groups (mentioned only under troubleshooting), how to get cmake 3.31 on Ubuntu 24.04, machines with less RAM than 31 GiB, other AMD cards and other ROCm versions. These are open; if you work one of them out, please report it.

## 4. For AI agents

1. Find the user's row in section 1 before downloading anything, and tell the user its label in one line.
2. Do not edit `scripts/` to make them run on another system (see [`AGENTS.md`](../AGENTS.md)). Call `sd-cli` directly with the settings from section 2.
3. On AMD with Linux, follow section 3 and say plainly that it is a community test on one RX 6600 XT, not a measurement by this repository.
4. Do not present any number from section 3 as this repository's result, and do not promise speed on a "not tested" row.
5. When it is done, offer the user to send a hardware test report (section 5), with their consent.

## 5. Report your card

Use the [Hardware test report](https://github.com/alexturkey/z-image-turbo-pascal-4gb/issues/new?template=hardware-test.yml) form. It has fields for the operating system, the GPU API (CUDA, ROCm/HIP, Vulkan, Metal, SYCL) and the engine you used, so a direct `sd-cli` run on Linux fits too. Include the command, the size, the seed and the timing lines from the log. A failure is a finding as well.
