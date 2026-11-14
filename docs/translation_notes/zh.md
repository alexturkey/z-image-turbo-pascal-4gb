# Chinese (zh): localization notes

Written by: W8 writer agent, 2026-11-14   Read by: R8 reader agent, 2026-11-14   Status: ok (PASSED)

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: informal "你" (second person singular). Chinese developer READMEs and docs (GitHub, Gitee, technical blogs) use "你", with "您" reserved for customer-service style text. Imperatives are softened with "建议" or "请" where the English suggests ("try it first").
- Register (how technical, how warm): plain, calm, sourced. Simplified Chinese (zh-Hans), mainland usage, because it is the larger developer audience; Traditional Chinese readers can still read it, and a separate zh-TW file can be added later. No advertising words (no "强大", "轻松", "完美", "极速", "革命性"). Chinese and Latin/digit runs are separated by one space, as is usual in Chinese technical writing; full-width punctuation outside code and inside Chinese sentences.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | 显存 (also "GPU 显存" next to nvidia-smi figures); "VRAM" only in quotes | 显存 is what Chinese developers say; "GPU 显存" used where the peak is measured, to be explicit |
| text-to-image | 文生图 | the common term in the Chinese Stable Diffusion community |
| tile (VAE tile) | 分块 | |
| seed | 种子 | |
| prompt | 提示词 | standard term; "negative prompt" = 负面提示词 |
| quantization | 量化 | |
| setup / install | 安装 (for the process), `setup.py` unchanged | |
| measured / not tested | 测量 / 实测 / 未测试 | "未测试" always for "not tested"; never softened to "暂无数据" |
| open source license / NOTICE | 许可证; `NOTICE` file kept as is | "条件" for the NOTICE requirement, "感谢但不是必须" for the credit line |
| refiner | refiner (left in English) | no settled Chinese term in this ecosystem |
| latent | latent (left in English) | same |
| unofficial | 非官方项目 | followed by "均无隶属关系" for "not affiliated" |
| segment (engine slice) | 分段 | "网络的一个切片" explains it once |

## Avoided
- Phrases that sound like advertising in this language/culture: 强大, 轻松, 一键, 极致, 完美, 秒级, 颠覆, 领先; any "首个", "唯一", "最快".
- Literal translations that read wrongly: "fits comfortably" is not rendered as 轻松运行; it stays as an English quote with a plain gloss. "Honest limit" became "坦率的局限" rather than "诚实的限制".

## Formatting
- Numbers and decimal separator: unchanged as the test requires (12.2, 261.6, "10 509", "6,577,440,704"). Chinese readers use the same decimal point and ASCII digits, so no wording workaround is needed. The number slots and the unit symbols (s, MiB, GB, dB) are left exactly as in English; only "minutes" next to `29` is written as 分钟.
- Script issues (right-to-left, line height, no spaces between words, table widths): no spaces between Chinese words; table cells kept short. Headings are short.
- Anchor line `<a id="what-it-runs"></a>` kept above the heading "它运行什么"; the link text "它运行什么" points to `#what-it-runs`.
- The AI-localization sentence is the last line, after the link line.

## Back-translation check
- First paragraph back into English by the reader: "On Windows, with stable-diffusion.cpp, run Z-Image-Turbo (Q8_0 GGUF) on a 4 GB GTX 1050 Ti (Pascal, sm_61), text-to-image at 768x1344. Measured on a 16 GB RAM laptop, process uses about 11 GB RAM. Same seed gives identical pixels, pixel for pixel; measurements and engine patches are public, downloads pinned with sha256, an AI coding assistant can complete the install step by step. Unofficial project, no affiliation with Tongyi-MAI, leejet or NVIDIA."; differences from the English: none of substance
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes (all four back-translated and compared; no meaning drift, no softened limit, no added claim; condition vs request kept distinct; unofficial line plain; cuDNN paragraph keeps NVIDIA software / optional / asked once)

## Open points / corrections welcome
- "Hardware test report" (issue form name) left in English, as in the Turkish file.
- "进程内存" for "process memory" and "分段" for "segment" are my choices; a reader may prefer "进程内存占用" / "片段".
- The village picture alt text is "山坡上的村庄"; the Turkish one is also "hillside". Fine, but check.
- Reader (R8): no disagreement with the decisions above; 进程内存 and 分段 read naturally to a mainland developer. No edits made.

## Round 2
- Round 2 (K-21): "by default" = 默认会安装; "without payment or sign-in" = 不要求付款，也不需要登录账号 (deliberately not 免费); "we found no clause" = 我们没有在许可证中找到...条款; license sentence kept as 写明：不接受其条款的人，不得下载、安装或使用它.
