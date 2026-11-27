[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · **中文** · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**在 Windows 上，用 stable-diffusion.cpp 在 4 GB 显存的 GTX 1050 Ti（Pascal，sm_61）上运行 Z-Image-Turbo（Q8_0 GGUF），文生图分辨率 768x1344。** 实测环境是一台 16 GB 内存的笔记本，进程大约占用 11 GB 内存。相同的种子会得到完全相同的像素，逐像素一致；测量数据和引擎补丁全部公开，下载文件用 sha256 固定，AI 编程助手可以按步骤完成安装。

*非官方项目，与 Tongyi-MAI（Z-Image）、leejet（stable-diffusion.cpp）和 NVIDIA 均无隶属关系。*

> **正在使用 AI 编程代理（Codex、Claude Code、Gemini、Cursor）吗？** 把下面这一句话交给它：“读完 `AGENTS_HIZLI.md`，先运行 `python scripts/tani.py`，把进度记在 `DURUM.md` 里；在删除或移动任何东西、更改系统 Python 或 PATH、或降低任何质量设置之前，必须先问我。”代理会诊断这台电脑、写出检查清单，并在每个决定处询问你。

## 从这里开始

我们提供了现成的软件包，建议先试它。如果你的硬件不同，或者某一步失败了，其余内容都是公开的：补丁、编译方法和测量数据都在本仓库里，你可以针对自己的显卡重新编译或自行调整。

```
1. nvidia-smi --query-gpu=name,memory.total --format=csv
      expect a line like: NVIDIA GeForce GTX 1050 Ti, 4096 MiB
      NVIDIA card with 4 GB, Windows x64 -> 2        anything else -> 5
2. python scripts/setup.py
      downloads NVIDIA cuDNN by default (NVIDIA's license applies); add --no-cudnn to skip it; both work
      expect the last line: SETUP_OK
3. python scripts/generate.py --prompt-file prompts/eiffel.txt
      expect the last line: IMAGE_OK <path>
4. Open <path>. Done. Compare your numbers: docs/MEASUREMENTS.md
5. Other hardware, or a step failed: everything is open.
      patches/README.md   docs/BUILD.md   docs/MEASUREMENTS.md   docs/TROUBLESHOOTING.md
      Build the engine for your card, or adapt the recipe. AGENTS.md has the exact steps.
```

第 2 步会下载约 12.2 GB 的文件，在我们的网络环境下一次耗时 29 分钟；它会先打印一个 "Preflight" 区块（把你的 GPU、内存和剩余磁盘空间与我们的测量值并排列出，仅作提示）。
只有 GTX 1050 Ti 4 GB 笔记本显卡（Pascal，计算能力 6.1）做过测量，其他显卡未测试。
如果你使用 AI 编程助手（Claude Code、Codex、Cursor 等），请让它读 [`AGENTS.md`](AGENTS.md)。

## 数据一览

与 v0.1.0 的目录结构相比：生成一张图需要 188–193 s，而不是 261.6 s；VAE 阶段需要 12.5–21.7 s，而不是 29.8 到 36.3 s；相同的种子得到相同的像素；本 README 中的每个数字背后都有对应的命令和文件。

768x1344，种子 42，8 步，同一台机器。v0.1.0 的数字来自 v0.1.0 的 README（干净根目录测试和五次运行）；v0.3.0 的数字来自本版本的干净根目录测试。

| | v0.1.0（未发布；旧结构） | v0.3.0 |
|---|---|---|
| 生成一张图的耗时（一次 `generate.py` 运行） | 261.6 s | 188–193 s |
| VAE 解码（最后一个阶段） | 29.8 到 36.3 s | 12.5–21.7 s |
| 与参考解码的接近程度（PSNR，越高越接近） | 38 到 43 dB | 71 到 73 dB |
| GPU 显存峰值（nvidia-smi） | 2949 到 2957 MiB | 3057–3059 MiB |
| 进程内存峰值 | 10.5 到 10.9 GB（按当时的记录） | 10 489–11 203 MiB |
| 观察到的最低空闲内存 | 331 到 576 MiB | 303–532 MiB |

怎么看这张表：参考结果是把同一个 latent 在 CPU 上以 float32 整块解码得到的；PSNR 是拿我们的 GPU 解码结果与它比较（3 张图）。它说明 VAE 阶段与这个参考有多接近，并不说明一张图好不好看。同样的提示词和种子，v0.2.0 的图与 v0.1.0 的图并非逐字节相同，因为 VAE 路径是有意改动的。测量方法和尚未测量的部分见 [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md)。

## 示例

**用本仓库生成的 AI 图像**（Z-Image-Turbo Q8_0，种子 42，8 步）。这些不是真实照片；建筑和细节可能不准确，图像也不一定在每个细节上都符合提示词。完整的提示词在 [`prompts/`](prompts) 和 [`docs/PROMPTS.md`](docs/PROMPTS.md) 中。

| | | |
|---|---|---|
| ![黄金时刻的埃菲尔铁塔](docs/examples/eiffel.jpg) | ![土耳其茶杯](docs/examples/turkish_tea.jpg) | ![年迈的渔夫](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`，768x1344 | `prompts/turkish_tea.txt`，768x1344 | `prompts/fisherman.txt`，768x1344 |
| ![山坡上的村庄](docs/examples/village.jpg) | | |
| `prompts/village.txt`，768x1344 | | |

![空中俯瞰伊斯坦布尔](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`，1344x768。不是真实照片；建筑可能不准确。

## 快速开始

环境要求：Windows 10/11、4 GB 显存的 NVIDIA 显卡、支持 CUDA 12.8 的驱动（实测驱动版本为 581.29；更旧的驱动未测试；CUDA 运行时本身会自动为你下载）、Python 3.10 或更高版本、
git、约 14 GB 的可用磁盘空间（含 cuDNN 的下载量约 12.2 GB；可用磁盘空间的数字是估计值），以及 16 GB 内存（这是实测配置；更少的内存未测试）。

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- `setup.py` 先打印一个 "Preflight" 区块（把你的 GPU、内存和剩余磁盘空间与我们的测量值并排列出；仅作提示，不会阻止任何操作）。然后它从 [`models.lock.json`](models.lock.json) 中固定的地址下载文件，并用 sha256 校验每个文件。它会依次打印 `MODEL_OK <name>`、`ENGINE_OK`、`CUDART_OK`，然后是 `CUDNN_OK` 或 `CUDNN_SKIPPED`，最后是 `SETUP_OK`。
  不指定 `--models-dir` 和 `--bin-dir` 时，使用仓库根目录下的 `models/` 和 `bin/`；请把模型放在固态硬盘（SSD）上（只在 SSD 上测量过）。
  随时可以按 Ctrl+C 中断，再运行同一条命令即可：下载会从 `.part` 文件继续。
- **cuDNN 默认会安装，也不属于本仓库。** 它是 NVIDIA 的软件，适用 NVIDIA 自己的许可证（[许可证全文](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)），面向配有 NVIDIA 显卡的系统。从 NVIDIA 的服务器下载时，不要求付款，也不需要登录账号；我们没有在许可证中找到限制商业或个人使用的条款。`setup.py` 会显示许可证地址，下载文件，并且只把八个 DLL 复制到 `sd-cli.exe` 旁边。NVIDIA 的许可证写明：不接受其条款的人，不得下载、安装或使用它；这种情况下请运行 `python scripts/setup.py --no-cudnn`。没有 cuDNN 也能全部正常运行，只是走较慢的 v0.1.0 VAE 路径（`--vae legacy`），`generate.py` 会明确提示这一点。
- `generate.py` 会写出 `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`、`run.json`（耗时、各阶段、实际使用的 VAE 路径、GPU 显存峰值、完整命令）和 `log.txt`，并打印 `IMAGE_OK <path>`。

## 使用方法

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| 选项 | 含义 |
|---|---|
| `--prompt "<text>"` 或 `--prompt-file <txt>` | 提示词（二选一，必须提供一个） |
| `--width`、`--height` | 16 的倍数，范围 256 到 2048；默认 768x1344；测试过的尺寸：768x1344、1344x768、1024x1024 |
| `--seed` | 默认 42 |
| `--out`、`--name` | 输出目录的根路径（默认 `outputs/`），以及本次运行目录的简短名称 |
| `--models-dir`、`--bin-dir` | `setup.py` 存放模型和引擎的位置 |
| `--vae auto`（默认） | cuDNN float32；先尝试整块解码，再尝试两个大分块，最后用默认的小分块 |
| `--vae tiled` | cuDNN float32，始终使用两个大分块 |
| `--vae legacy` | v0.1.0 的路径：不用 cuDNN，使用小分块。缺少 cuDNN 的 DLL 时会自动采用（并给出警告） |

步数（8）、cfg（1.0）、采样器和调度器是有意固定的；见[它运行什么](#what-it-runs)。

## 自行验证

- `generate.py` 在最后几行之一打印 `PIXEL_SHA256 <hex>`：这是解码后像素的哈希值。把同一条命令运行两次，再比较两张图：`python scripts/compare.py <run A>/image.png <run B>/image.png` 应当打印 `SAME_PIXELS`。
- 五个示例在我们机器上的 `PIXEL_SHA256` 记录在 [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) 中。即使像素相同，PNG 的文件哈希也可能不同，因为 PNG 以文本形式保存了生成参数；请比较像素，而不是比较文件。
- 坦率的局限：换一张显卡或换一个驱动是否得到相同的像素，我们没有测量过。

## 为什么 4 GB 显存够用

- **模型作者怎么说。** Z-Image-Turbo 的模型卡写道，该模型 "fits comfortably within 16G VRAM consumer devices"（可以轻松放进 16 GB 显存的消费级设备）（[模型卡](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)）。这说的是 16 GB 显卡。官方 README 还把 stable-diffusion.cpp 列为第三方方案，并引述其 "as little as 4GB of VRAM"（最低只需 4 GB 显存）（[README](https://github.com/Tongyi-MAI/Z-Image)）；这是 stable-diffusion.cpp 项目自己的说法，不是 Z-Image 团队提出的要求。
- **我们测到了什么。** Z-Image-Turbo Q8_0（一个 6.6 GB 的文件）搭配 Qwen3-4B Q8_0 文本编码器，768x1344：由 nvidia-smi 每 2 s 采样一次的 GPU 显存峰值（短暂的尖峰可能漏掉），在 4096 MiB 的显卡上是 2949 到 2957 MiB（v0.1.0 引擎）和 3057–3059 MiB（v0.2.0 引擎）。权重（10 509 MiB；引擎日志中把它写作 MB）留在系统内存中；引擎每次把网络的一个分段（网络的一个切片）复制到 GPU：共 36 段，正如日志行 `z_image using 36 segments` 所示。
- **代价是什么。** 时间和系统内存：每张图 188–193 s，在 16 GB 的机器上引擎进程占用约 10 489–11 203 MiB 内存（包括内存映射的模型页面），所以运行期间空闲内存会降到几百 MiB。
- **别人的配置。** 也有人报告在 4 GB 显卡上跑 Z-Image，用的是更低的量化或更小的尺寸（例如 stable-diffusion.cpp wiki 中针对 4 GB 显卡的页面，建议在 1024x512 下使用 Q3_K 或 Q4_0）。在我们查过的地方（清单和日期见 [`docs/RELATED.md`](docs/RELATED.md)），没有找到同时满足这四项的公开配置：4 GB 显卡、Q8_0、768x1344 或更大的尺寸，以及实测的耗时和 GPU 显存。这只是对我们查过的范围的陈述，不代表所有地方。
- **谁做了什么。** 能放进 4 GB 靠的是 stable-diffusion.cpp 本身：`--offload-to-cpu`、`--mmap`、分段处理，以及 flash attention（关闭它时，一次运行需要 4205 MB，放不下）。我们的补丁是为了速度和更好的 VAE 阶段，不是为了放得下。我们没有在这张显卡上运行未打补丁的上游引擎，所以无法说它能否放得下。

## 工作原理

在 stable-diffusion.cpp `master-1088-32d516c` 之上做了三处改动（全部是开关；[`patches/README.md`](patches/README.md) 中的表格列出了每一项及其环境变量）：

1. **refiner 每一步只运行一次。** 原先一个分组名被重复使用，导致四个 refiner 块被多算了一遍。修复后，第 2 到 8 步每步快约 1.3 s（从 22.0 s 到 20.7 s），图像像素完全相同（检查了 3 张图）。
2. **VAE 通过 cuDNN，使用 float32。** 最后一个阶段（把 latent 变成像素）现在使用 NVIDIA cuDNN 的 float32 卷积。在我们的显卡上，VAE 耗时从 23 到 27 s 降到 10 到 15 s，与参考结果的 PSNR 从 38 到 43 dB 提高到 45 到 49 dB（大分块）。
3. **先尝试整块解码。** 当显存检查认为放得下时（余量 256 MiB），引擎现在会先尝试把整张图一次解码；不行就退回到两个大分块，再不行就退回到小分块。整块解码时 VAE 耗时约 8–16 s，与参考结果的 PSNR 为 71 到 73 dB。如果被强制退回，得到的图与分块结果的像素相同（用 `PIXEL_SHA256` 检查过）。实际发生了什么会写进 `run.json`（`stages.vae_path`：`full`、`tile`、`floor` 或 `retry`）。

另外：`--eager-load`（预先读入模型页面；同一张图从 241.2 s 降到 220.3 s，开发版本，各运行一次）是固定命令的一部分。

<a id="what-it-runs"></a>
## 它运行什么

| 组成部分 | 文件 | 来源 |
|---|---|---|
| 扩散模型 | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF)，基础模型 [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| 文本编码器 | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo)，FLUX.1 类型的自编码器 |
| 引擎 | `sd-cli.exe`，stable-diffusion.cpp `32d516c` 加上 [`patches/`](patches) 中的补丁 | 本仓库的 v0.3.0 发布版（`sinirsiz-foto-engine-v0.3.0-win-x64-cuda12.8-sm61.zip`） |
| CUDA 运行时 | `cudart`、`cublas`、`cublasLt`（12.8），未经修改 | wan22-pascal-4gb v0.1.0 发布版中的 zip |
| cuDNN（默认安装；`--no-cudnn` 则跳过） | 8 个 DLL，版本 9.10.2.21（CUDA 11 构建） | NVIDIA 自己的服务器，适用 NVIDIA 的许可证；不存放在本仓库 |

固定的设置：`--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`。
我们不降低步数、不加负面提示词、不启用缓存：该模型是为 8 步蒸馏的，不使用负面提示词（见[提示词](docs/PROMPTS.md)）。

## 局限（依赖它之前请先读）

- **仅限 Windows。** 预编译的引擎和这些脚本只支持 Windows。
- **一张显卡，一台机器。** 只在一台 GTX 1050 Ti 4 GB 笔记本上测量过（i7-7700HQ，16 GB 内存，Windows 10，驱动 581.29，模型放在 SSD 上）。其他 GPU 和驱动、内存小于 16 GB 的机器、Linux 和 macOS：**未测试**。
- 其他显卡和系统(有哪条路可走,以及一项我们自己未运行的、在 Linux 下 AMD 显卡上的社区测试):[docs/OTHER_GPUS.md](docs/OTHER_GPUS.md)。
- **引擎只为 Pascal（sm_61）编译。** 其他架构需要你自己编译（[`docs/BUILD.md`](docs/BUILD.md)）；我们没有测试过。
- **cuDNN：** 我们使用 cuDNN 9.10.2.21 的 CUDA 11 构建进行测量。CUDA 12 构建的文件不同，也没有测量过。
- **内存很紧张。** 空闲内存会降到几百 MiB；请关闭其他程序，一次只生成一张图。引擎的显存检查通过之后，我们没有遇到过 GPU 显存耗尽的情况，也没有测试过耗尽时会发生什么。
- **尺寸：** 只测试过 768x1344、1344x768 和 1024x1024。更大的尺寸会打印警告，并可能内存不足。
- 对提示词的遵循只是部分的：图像不一定在每个细节上都符合提示词。图像中的文字和现实世界的建筑没有评估过。
- PSNR 的参考结果是我们自己引擎的 CPU 解码结果，不是独立的实现。
- [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) 中的数字，除非另有说明，都只来自各一次运行。

## 许可证与署名

- 本仓库的脚本和文档：[Apache-2.0](LICENSE)，附带 [`NOTICE`](NOTICE) 文件。[`patches/`](patches) 中的引擎补丁与其所修改的代码一样，采用 MIT 许可证。
- stable-diffusion.cpp 和 ggml 采用 MIT 许可证。编译进引擎的第三方代码的声明在 [`licenses/`](licenses) 和 [`THIRD_PARTY.md`](THIRD_PARTY.md) 中。
- 模型文件不存放在这里；它们从上面列出的来源下载，适用各自的许可证（Hugging Face 上全部标注为 Apache-2.0，读取日期 2026-11-13）。模型卡没有说明生成图像的归属，我们对此也不作任何主张。
- **cuDNN 和 CUDA 运行时归 NVIDIA 所有**，不适用本仓库的许可证。cuDNN 从 NVIDIA 的服务器下载，适用 NVIDIA 的许可证（`--no-cudnn` 则跳过）；CUDA 运行时的 DLL 放在一个单独的、未经修改的 zip 中（CUDA Toolkit EULA，附件 A）。详情以及我们未能核实的部分见 [`THIRD_PARTY.md`](THIRD_PARTY.md)。
- **署名。** 在副本和衍生作品中保留 `NOTICE` 文件是条件（Apache-2.0，第 4 条）。除此之外，如果你愿意写一行类似 "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey" 的话，我们会很感谢，但这不是必须的。
- 请阅读 [`ETHICS.md`](ETHICS.md)：每一张图都是合成的，你对自己发布的内容负责。

## 参与贡献

最有帮助的是**测试你自己的显卡**并告诉我们结果：GPU 名称、驱动、内存、`run.json`，以及日志的最后几行（"Hardware test report" 问题表单）。也欢迎修正文档和脚本；见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。安全问题请通过 [`SECURITY.md`](SECURITY.md) 中的私密渠道报告。

[AI 助手安装指南](AGENTS.md) · [测量数据](docs/MEASUREMENTS.md) · [故障排查](docs/TROUBLESHOOTING.md) · [编译引擎](docs/BUILD.md) · [补丁](patches/README.md) · [提示词](docs/PROMPTS.md) · [第三方](THIRD_PARTY.md) · [更新日志](CHANGELOG.md)

本页面在 AI 的协助下完成本地化，欢迎随时指出并纠正问题，详见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。
