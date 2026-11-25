# Source tree and rebuild check (v0.3.0 engine)

Question: is the release engine built from what `patches/` says? Two checks, on the machine that built the engine, 2026-11-25.

## 1. Source tree: patches against the tree the engine was built from

1. Clean checkout of the two base commits: `stable-diffusion.cpp` `32d516c` and `ggml` `d803c23` (cloned from GitHub; line endings LF, see the note in `patches/README.md`).
2. The patches in the order of `patches/README.md`: ggml `0001 0002 0003 0006 0009`, then sdcpp `0004 0012 0022b 0025 0027 0028b 0029 0030`. Every `git apply` succeeded.
3. File by file comparison (`diff -rq --strip-trailing-cr`, without `.git`, `build`, `thirdparty`, `assets`, the web front-end folder) with the source folder of the engine build:

| Result | Files |
|---|---|
| different | `ggml/src/ggml-cuda/ggml-cuda.cu`: the engine folder has a trace block (a device-clock event log) that was added after the release engine was built (file time 12:44, engine built 12:02 to 12:03) and is not in the release engine |
| different | `src/model_manager.cpp`: two comment lines (the working copy has Turkish "hiz ekibi" where the patches say "speed work"); no code differs |
| equal | everything else |

The engine files of the 12 runs of Table 4 and the files in the v0.3.0 zip are the same bytes (`engine_binaries_sha256.txt`).

## 2. Rebuild

A second build of the same tree does not give the same file hashes. What differs, found by comparing the v0.2.0 engine with the v0.3.0 engine, whose shared sources are identical (`ggml.dll`: 40 bytes): the PE time stamp, the debug directory, the absolute source path inside text strings (`E:\b\sdcpp_<name>\...`), and, when the source folder is a git checkout, the commit hash that CMake writes into the version strings (`stable-diffusion.cpp commit`, `ggml commit`; the release engine was built from a folder without `.git`, so both say `unknown`).

Method of the comparison: build the clean tree of step 1 in a folder whose path has the same length as the engine's (`E:\b\sdcpp_repro_02\src` against `E:\b\sdcpp_ortusme2\src`), without `.git`, with the flags of `patches/README.md`; then replace the path in the release binary, zero the PE time stamp, checksum and debug directory in both, compare the bytes.

Result: see the section "Result of the rebuild" below.

## Result of the rebuild

Built once from the clean tree (step 1, no `.git`, the flags of `patches/README.md`, `E:\b\sdcpp_repro_02`, 337 build steps), then compared with the release binaries as described above:

| File | Result |
|---|---|
| `ggml.dll` | equal |
| `ggml-cpu.dll` | equal |
| `ggml-base.dll` | differs (14 089 bytes, in the code of a few functions and their unwind tables) |
| `ggml-cuda.dll` | differs |
| `stable-diffusion.dll` | differs (67 616 bytes) |
| `sd-cli.exe` | differs (24 243 bytes) |
| `sd-server.exe` | differs (44 086 bytes) |

So the release binaries were **not** reproduced byte for byte. What we found out about the difference, and what we ruled out:
- Not the line endings: the sources of the release build have CRLF, the first rebuild had LF, a second rebuild of `ggml-base` with CRLF gave the same `ggml-base.dll` as the LF one.
- Not the commit string: with `.git` removed both say `unknown` (with `.git` present the first rebuild embedded the ggml commit and differed more).
- Not the CMake settings: the two `CMakeCache.txt` files differ only in the path of `git.exe`.
- Object by object, most `ggml-base` objects differ only by a few dozen bytes (time stamps and debug records); three do more (`ggml-backend-meta.cpp.obj` 26 090 bytes, `ggml-backend.cpp.obj` and `ggml-ext.cpp.obj` differ by one byte in size). We have not found the reason (same compiler, same flags, same source text, a source folder name of the same length but not the same letters).
- The source trees are equal (step 1), so the difference is in the build, not in the patches.

What this does and does not show: the patched sources are the sources of the release engine (step 1, file by file); the binaries come from one build of those sources, the one that was measured and packed. A second build was not run and not measured; anyone who builds it gets working code from the same sources but not the same file hashes. For a pixel check of your own build use `PIXEL_SHA256` (`docs/MEASUREMENTS.md`, example hashes).
