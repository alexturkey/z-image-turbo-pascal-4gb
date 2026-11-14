# Building the engine for your own card

The release zip contains an engine built for **NVIDIA Pascal, compute capability 6.1 (sm_61)** only. If you have a different card, or you want to check what is in the zip, build it yourself from the sources and the patches in this repository.
**What we tested:** one build for sm_61, on the measured GTX 1050 Ti laptop. **What we did not test:** any other architecture, Linux, macOS, Vulkan or ROCm builds. Read "What may not carry over" before you spend an hour compiling.

## What you need

| Need | Version we used | Note |
|---|---|---|
| Windows 10/11 x64 | Windows 10 | |
| Visual Studio Build Tools (MSVC) | 14.44 | C++ x64 tools |
| CUDA Toolkit | 12.8 | the runtime DLLs in the release are the 12.8 ones |
| CMake and Ninja | any recent version (version not recorded) | we built with `Release` and Ninja |
| Git | 2.x | clone with LF line endings (see below) |
| cuDNN development files | 9.10.2.21 | only for the optional cuDNN convolution; headers and `cudnn.lib` |
| Disk and time | a full build took about 55 minutes on the measured laptop (one build, our development setup) | |

## Base sources

| Repository | Commit |
|---|---|
| leejet/stable-diffusion.cpp | `32d516c` (master-1088) |
| ggml submodule (leejet/ggml) | `d803c23` |

```powershell
git -c core.autocrlf=false clone https://github.com/leejet/stable-diffusion.cpp.git sdcpp
cd sdcpp
git checkout 32d516c
git submodule update --init --recursive
git -C ggml checkout d803c23
```

Line endings matter: the patches apply to LF files. Use `core.autocrlf=false` as above.
Both commits are as recorded in [`patches/README.md`](../patches/README.md) (table "Base").

## Apply the patches

Order and details are in [`patches/README.md`](../patches/README.md). In short, from the stable-diffusion.cpp folder (adjust the path to this repository's `patches/`):

```powershell
cd ggml
git apply <repo>\patches\ggml\0001-*.patch <repo>\patches\ggml\0002-*.patch <repo>\patches\ggml\0003-*.patch <repo>\patches\ggml\0006-*.patch <repo>\patches\ggml\0009-*.patch
cd ..
git apply <repo>\patches\sdcpp\0004-*.patch <repo>\patches\sdcpp\0012-*.patch <repo>\patches\sdcpp\0022b-*.patch <repo>\patches\sdcpp\0025-*.patch <repo>\patches\sdcpp\0027-*.patch <repo>\patches\sdcpp\0028b-*.patch <repo>\patches\sdcpp\0029-*.patch
```

Applying them in this order to a clean base gives the source tree the released engine was built from (checked file by file by comparing a tree built from the patches with the one we built from). If `git apply` complains, your base is not the commit above or the line endings changed.

## Configure and build

Use the "x64 Native Tools" prompt of your Visual Studio, with CUDA 12.8 on the path. The flags of the released engine, as recorded in [`patches/README.md`](../patches/README.md) ("CMake flags of the released engine"):

```
cmake -B build ^
  -DSD_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES=61 ^
  -DGGML_NATIVE=OFF -DGGML_BACKEND_DL=ON ^
  -DSD_BUILD_SHARED_LIBS=ON -DSD_BUILD_SHARED_GGML_LIB=ON ^
  -DGGML_CUDA_CUDNN_CONV2D_F32=ON ^
  -DCUDNN_INCLUDE_DIR=<cudnn include> -DCUDNN_LIBRARY=<cudnn.lib>
cmake --build build
```

(`^` continues a line in `cmd`; in PowerShell use a backtick or one long line. The generator and the build type are not recorded there; choose your own, for example `-G Ninja -DCMAKE_BUILD_TYPE=Release`.) The cuDNN headers and import library come from an NVIDIA cuDNN 9 archive; which build was used at compile time is not recorded here.
Without cuDNN, leave out the last three flags: the engine then runs without the cuDNN VAE path and `generate.py` uses `--vae legacy`.

The engine ends up as `sd-cli.exe` and a few DLLs in `build/bin`. Put them in a folder together with the CUDA runtime DLLs (`cudart64_12.dll`, `cublas64_12.dll`, `cublasLt64_12.dll`) and, if you built with cuDNN, the eight cuDNN DLLs, and give that folder to `generate.py` with `--bin-dir`.

## Other cards: what may not carry over

- `-DCMAKE_CUDA_ARCHITECTURES=<your value>` is the obvious change (for example `75` for Turing, `86` for Ampere). We have **no** card other than the GTX 1050 Ti and never ran such a build.
- Several patches are written for Pascal: the Q8_0 matrix-multiply tile on the `dp4a` path (`ggml/0002`), the hand-written flash-attention tile kernel (`ggml/0003`, tuned for the register and shared-memory budget of sm_61) and the conv3d kernel (`ggml/0001`). On a newer architecture they may compile and still be slower than the stock kernels, or not be selected. Each can be switched off by its environment variable (table in `patches/README.md`). We did not measure this.
- The memory fallbacks (`sdcpp/0025`, `0027`, `0028b`) are generic and are the part most likely to help on another small card, but the default margin of the one-piece try (256 MiB, `SD_VAE_FULL_MARGIN_MB`) was chosen for 4 GB.
- cuDNN: we measured the CUDA 11 build of cuDNN 9.10.2.21. Its CUDA 12 build contains different files; whether speed and pixels match was not measured.

## Check your build

1. `sd-cli.exe --help` runs without a missing-DLL dialog.
2. `python scripts/generate.py --prompt-file prompts/eiffel.txt --bin-dir <your folder>` prints `IMAGE_OK` and `run.json` has `"result": "OK"`.
3. Compare `PIXEL_SHA256` with the table in [`MEASUREMENTS.md`](MEASUREMENTS.md). The same value is expected only on the same card family, the same cuDNN build and the same `stages.vae_path`; a different value does not by itself mean something is wrong. `python scripts/compare.py` shows how far apart two pictures are. If your numbers differ a lot, a "measurement report" issue is welcome.
