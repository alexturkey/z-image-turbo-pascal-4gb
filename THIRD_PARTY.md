# Third-party material

This repository's own scripts and docs are MIT (see `LICENSE`). Model files and the engine are downloaded by `scripts/setup.py`
from the pinned sources in `models.lock.json` and are **not stored in this repository**. Each keeps its own license.

License labels below were read from the Hugging Face API (`license` field) and the repositories' files on 2026-11-13. Check the originals.

| Component | Use | License | Source |
|---|---|---|---|
| Z-Image-Turbo (Tongyi-MAI) | Base image model | Apache-2.0 | https://huggingface.co/Tongyi-MAI/Z-Image-Turbo (card: `license: apache-2.0`; the Z-Image GitHub repo has an Apache-2.0 LICENSE) |
| `z_image_turbo-Q8_0.gguf` (leejet) | GGUF conversion, downloaded by the user | Apache-2.0 (the page says the quantized files follow the original model's license) | https://huggingface.co/leejet/Z-Image-Turbo-GGUF |
| Qwen3-4B-Instruct-2507 (Qwen) | Text encoder, base model | Apache-2.0 | https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507 |
| `Qwen3-4B-Instruct-2507-Q8_0.gguf` (unsloth) | GGUF conversion, downloaded by the user | Apache-2.0 | https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF |
| `ae.safetensors` (Comfy-Org repackage) | VAE, a FLUX.1-type autoencoder | Apache-2.0 (repo tag and card) | https://huggingface.co/Comfy-Org/Z-Image-Turbo |
| stable-diffusion.cpp (leejet), `master-1088-32d516c` | Engine (`sd-cli.exe`) | MIT | https://github.com/leejet/stable-diffusion.cpp |
| ggml (leejet fork) | Tensor library inside the engine | MIT | https://github.com/leejet/ggml |
| wan22-pascal-4gb v0.1.0 release zips | Prebuilt engine with four Pascal patches, and the CUDA runtime zip | patches and scripts MIT; CUDA runtime under NVIDIA's EULA (below) | https://github.com/alexturkey/wan22-pascal-4gb/releases/tag/v0.1.0 |
| NVIDIA CUDA 12.8 runtime DLLs (`cudart`, `cublas`, `cublasLt`) | Needed by the engine; unmodified, in a separate zip | NVIDIA CUDA Toolkit EULA, Attachment A (redistributable) | https://docs.nvidia.com/cuda/eula/index.html |

Notices for third-party code compiled into the engine (Oniguruma, utf8proc, darts-clone, nlohmann/json, stb, miniz/zip) and their license texts are in `licenses/`.

## Things we could not verify

- **Ownership of generated pictures.** The Z-Image-Turbo model card and README contain no sentence about who owns generated pictures (searched for "rights", "generated content", "commercial"). We make no claim in either direction.
- **VAE identity.** The `ae.safetensors` we use comes from the Comfy-Org repo (Apache-2.0 tagged; sha256 `afc8e28272cd15db3919bacdb6918ce9c1ed22e96cb12c4d5ed0fba823529e38`). FLUX.1-schnell is tagged Apache-2.0 and FLUX.1-dev is under a non-commercial license. Whether the `ae.safetensors` files in those two repos are the same bytes as ours was not verified (the repositories are gated and their file hashes could not be read). If you need certainty about the VAE's terms, check the FLUX.1 repositories yourself.
- Apache-2.0 asks you to keep the license text and notices when you redistribute the model files. This repository does not redistribute them.

Microsoft Visual C++ runtime and ffmpeg are not included.
