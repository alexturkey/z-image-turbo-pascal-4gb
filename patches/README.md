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
git apply patches/sdcpp/0004-*.patch patches/sdcpp/0012-*.patch patches/sdcpp/0022b-*.patch patches/sdcpp/0025-*.patch patches/sdcpp/0027-*.patch patches/sdcpp/0028b-*.patch patches/sdcpp/0029-*.patch patches/sdcpp/0030-*.patch
```

Check on a checkout with LF line endings. `git -c core.autocrlf=false clone` is not enough on Windows: the `ggml` submodule is checked out by a second git process that ignores that option when your system-wide git config has `core.autocrlf=true`. Set `core.autocrlf` to `false` in the ggml folder too (`git -C ggml config core.autocrlf false`), then check the files out again (or clone with the environment variables `GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.autocrlf GIT_CONFIG_VALUE_0=false`). Applying them in this order to a clean base gives exactly the source tree the released engine was built from (checked file by file).

CMake flags of the released engine (generator Ninja, build type Release): `-G Ninja -DCMAKE_BUILD_TYPE=Release -DSD_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES=61 -DGGML_NATIVE=OFF -DGGML_BACKEND_DL=ON -DSD_BUILD_SHARED_LIBS=ON -DSD_BUILD_SHARED_GGML_LIB=ON -DSD_WEBP=OFF -DSD_WEBM=OFF -DSD_BUILD_EXAMPLES=ON -DGGML_BUILD_TESTS=OFF -DSD_CUDA_CUTLASS_PATH= -DGGML_CUDA_CUDNN_CONV2D_F32=ON -DCUDNN_INCLUDE_DIR=<cudnn include> -DCUDNN_LIBRARY=<cudnn.lib>`, targets `sd-cli sd-server stable-diffusion ggml ggml-base ggml-cpu ggml-cuda`.

## Patches

0030 bundles former development patches (staging pool, prefetch worker thread, step-wrap prefetch, pre-evict, pinned ring; in our work log 0011, 0016, 0018, 0021, 0023, 0023b). Those numbers are not in this repository: the comments in the patch that mention them refer to that history; the one patch file is the whole change.

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
| sdcpp/0030 weight-copy-overlap | copies the weights of the next model part to the GPU through a small page-locked ring, from a worker thread, while the current part is computed (the bundle of five earlier steps: staging pool, prefetch thread, step wrap, pre-evict, pinned ring) | `SD_PREFETCH_THREAD=1` and `SD_STAGING_PINNED=1` (+ `SD_STAGING_PINNED_MB`, default 64) switch it on (unset: stock path; `generate.py` sets all three, `--no-overlap` leaves them unset). Also in the patch, **not measured, leave unset**: `SD_STAGING_POOL_MB`, `SD_STAGING_PREEVICT`, `SD_PREFETCH_WRAP`; `SD_STAGING_VERIFY=N` is a diagnostic that reads the copies back and compares them | same pixels (12 of 12 pictures with the same RGB hash on and off, `docs/MEASUREMENTS.md` Table 4); only the order of copy and compute changes | `generate.py --no-overlap`, or leave the three variables unset | speed |

## Reproducing the released binaries

Applying the patches in the order above to the two base commits gives the source tree the released engine was built from. A second build of the same tree does **not** give the same file hashes: the compiler writes a time stamp into every DLL and exe and embeds the absolute path of the source folder in text strings. To compare a rebuild with the release anyway, build in a folder whose path has the same length as the one in the release (the engine strings show it) and compare after replacing that path and zeroing the PE time stamp; our comparison for this release (2 of 7 binaries equal, the other 5 differ for a reason we did not find) is in `docs/MEASUREMENTS.md` (Checks) and `docs/evidence/overlap/source_tree_check.md`. Comparing pictures needs no such care: same prompt, seed and settings give the same pixel hash.

## License

Every patch is MIT (`SPDX-License-Identifier: MIT`, header of each file), like the code it modifies. Copyright of the original code stays with its authors (stable-diffusion.cpp: leejet; ggml: the ggml authors).
