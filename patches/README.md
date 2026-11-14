# Engine patches

Patches for the image engine used by Sinirsiz Foto. All of them are optional switches: with the environment variable unset the stock code path runs (except where the table says "always on").

## Base

| Repository | Commit |
|---|---|
| leejet/stable-diffusion.cpp | `32d516c` (master-1088) |
| ggml submodule (leejet/ggml) | `d803c23` |

## Apply

Apply in this order, ggml patches inside the `ggml/` directory, the others in the stable-diffusion.cpp root:

```
cd ggml
git apply ../patches/ggml/0001-*.patch ../patches/ggml/0002-*.patch ../patches/ggml/0003-*.patch ../patches/ggml/0006-*.patch ../patches/ggml/0009-*.patch
cd ..
git apply patches/sdcpp/0004-*.patch patches/sdcpp/0012-*.patch patches/sdcpp/0022b-*.patch patches/sdcpp/0025-*.patch patches/sdcpp/0027-*.patch patches/sdcpp/0028b-*.patch patches/sdcpp/0029-*.patch
```

Check on a checkout with LF line endings (`git -c core.autocrlf=false clone`). Applying them in this order to a clean base gives exactly the source tree the released engine was built from (checked file by file).

CMake flags of the released engine: `-DSD_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES=61 -DGGML_NATIVE=OFF -DGGML_BACKEND_DL=ON -DSD_BUILD_SHARED_LIBS=ON -DSD_BUILD_SHARED_GGML_LIB=ON -DGGML_CUDA_CUDNN_CONV2D_F32=ON -DCUDNN_INCLUDE_DIR=<cudnn include> -DCUDNN_LIBRARY=<cudnn.lib>`.

## Patches

| Patch | What it does | Environment variable (default) | Quality (pixels) | Roll back | Kind |
|---|---|---|---|---|---|
| ggml/0001 cuda-conv3d-direct-pascal | Pascal implicit-GEMM conv3d kernel (Wan video models; Z-Image does not use it) | `GGML_CUDA_CONV3D_OLD` (unset: new kernel) | bit-identical to stock (development check) | set `GGML_CUDA_CONV3D_OLD` | speed |
| ggml/0002 cuda-mmq-q8_0-dp4a-tile128 | Q8_0 MMQ tile 128x64 on the dp4a path | none (always on, dp4a path only) | same pixels (development check, 3 pictures, with cuDNN off) | none (rebuild without the patch) | speed |
| ggml/0003 cuda-fattn-tile-a3-pascal | hand-written fp32 flash-attention tile kernel (DKQ=DV=128) | `WAN_A3_ORIG` (unset: new kernel) | same pixels (development check, 3 pictures, with cuDNN off) | set `WAN_A3_ORIG` | speed |
| ggml/0006 cuda-im2col-fast | im2col fast path, same values | `GGML_CUDA_IM2COL_FAST=0` selects the old kernel | same pixels (development check, 3 pictures; `test-backend-ops` IM2COL) | `GGML_CUDA_IM2COL_FAST=0` | speed |
| ggml/0009 cuda-cudnn-conv2d-f32 | optional cuDNN F32 conv2d (needs cuDNN at build and run time) | `GGML_CUDA_CUDNN_CONV2D=1` (off), `GGML_CUDA_CUDNN_ALGO`, `GGML_CUDA_CUDNN_WS_MB` (256), `GGML_CUDA_CUDNN_LOG` | changes the VAE pixels on purpose: closer to a CPU float32 reference (tiled 45 to 49 dB instead of 38 to 43 dB, see `docs/MEASUREMENTS.md`) | leave `GGML_CUDA_CUDNN_CONV2D` unset, or `generate.py --vae legacy` (the v0.1.0 VAE path) | quality |
| sdcpp/0004 wan-vae-resample-conv3d-kd1 | Wan VAE resample conv as KD=1 conv3d (Wan video models; Z-Image does not use it) | `SD_WAN_RESAMPLE_CONV3D=0` disables | same as stock for Wan (development check; not used by Z-Image) | `SD_WAN_RESAMPLE_CONV3D=0` | speed |
| sdcpp/0012 vram-margin-env | replaces the VRAM safety margin | `SD_VRAM_MARGIN_MB` (unset) | no effect on pixels (it only changes when memory is moved) | leave `SD_VRAM_MARGIN_MB` unset | measuring tool |
| sdcpp/0022b zimage-refiner-single-pass | refiner blocks run once per step | `SD_ZIMAGE_CONCAT_CUT=1` restores old behavior | same pixels (3 pictures, development check) | `SD_ZIMAGE_CONCAT_CUT=1` | speed |
| sdcpp/0025 vae-tile-floor | memory fallback for VAE tiles: half latent | `SD_VAE_TILE_FLOOR=1` (off) | only matters when a tile does not fit: then smaller tiles give a slightly different picture | leave `SD_VAE_TILE_FLOOR` unset | quality |
| sdcpp/0027 vae-vram-margin | VRAM margin only while the VAE decodes | `SD_VAE_VRAM_MARGIN_MB` (unset) | decides which VAE path fits (tile or one piece); the pixels of a path stay the same | leave `SD_VAE_VRAM_MARGIN_MB` unset (default margin 1024 MiB) | quality |
| sdcpp/0028b vae-try-untiled-first | try one untiled VAE decode before tiling | `SD_VAE_TRY_FULL=1` (off), `SD_VAE_FULL_MARGIN_MB` (256) | changes the VAE pixels on purpose: one piece is closest to the CPU float32 reference (about 71 to 73 dB against 45 to 49 dB for large tiles, `docs/MEASUREMENTS.md`) | leave `SD_VAE_TRY_FULL` unset, or `generate.py --vae tiled` | quality |
| sdcpp/0029 capacity-log | one log line per VRAM capacity check | `SD_CAPACITY_LOG=1` (off) | none (log line only) | leave `SD_CAPACITY_LOG` unset | measuring tool |

## License

Every patch is MIT (`SPDX-License-Identifier: MIT`, header of each file), like the code it modifies. Copyright of the original code stays with its authors (stable-diffusion.cpp: leejet; ggml: the ggml authors).
