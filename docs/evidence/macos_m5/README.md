# Community evidence: Apple M5 / Metal

Reported by [eburakars](https://github.com/eburakars), run on **2026-11-16**.
One community run, not a maintainer measurement or a repeated-seed test.
Summary: [OTHER_GPUS.md](../../OTHER_GPUS.md#3a-community-test-apple-m5-macos-metal).

- Hardware: MacBook Air, Apple M5, 8 GPU cores, 16 GB unified memory, SSD.
- OS: macOS 26.5.1, arm64.
- Repository at the time: `c7096bc08905e4ecb6a6acdbc1e224a1128b4f8d`.
- Engine: official upstream Metal release `master-1088-32d516c`, commit
  `32d516c0197ed5ca31305b8575e14eb1451fad33`; no Pascal patches or cuDNN.
- Archive: `sd-master-32d516c-bin-Darwin-macOS-26.7.2-arm64.zip`.
- Archive SHA-256: `b6588e81e788d9f2f24498831ba398d7523152e7ec280ff282f39c2009465b77`.
- All three original `models.lock.json` files were size/SHA-256 verified.
- Prompt: `prompts/eiffel.txt`, copied into the run directory without changing its text.
- One run, seed 42, 768x1344, 8 steps, CFG 1.0, Euler/simple, offload, mmap,
  eager load, flash attention on, no negative prompt.

`run.json` is the original wrapper result with only the local repository-root
prefix replaced by `<REPO>` in paths; other recorded fields are unchanged.
`log_excerpt.txt` contains selected original log lines confirming Metal execution
and stage timings, with the same substitution. Missing measurements are not reconstructed.
Image, model and engine binaries are not included.

The actual Python invocation was:

```sh
python3 scripts/generate.py --bin-dir bin/metal --vae legacy --prompt-file prompts/eiffel.txt
```

A local shell wrapper supplied the example prompt when called without arguments.
A local `bin/metal/sd-cli.exe -> sd-cli` symlink let the unchanged Python wrapper
find the native Mac executable. The full engine argv is in `run.json`.

The original PNG was visually checked for a recognisable Eiffel Tower at sunset.
Its decoded RGB SHA-256 was recomputed separately:
`5e64c6759bd3db39955459b8e3e6ec953281daf5a94adf3b596f91bb97527e7e`.
The unredacted files and PNG remain in the contributor's local output folder.

`seconds` is wrapper wall time; `stages.generate_total_s` is the engine's generation
stage. The CUDA detection, RAM/VRAM counters and patched-VAE fields are Windows-specific:
their null/false values do not measure Metal memory or establish a Metal VAE path.
Peak RAM/GPU memory, driver details, repeatability and Windows pixel parity were not recorded.
The direct native command in [MACOS.md](../../../MACOS.md) preserves the model and
sampling options but was not separately timed; its runtime must not be reported as 196.4 s.
