# Japanese (ja): localization notes

Written by: W8 writer agent, 2026-11-14   Read by: R8 reader agent, 2026-11-14   Status: ok (PASSED)

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: polite です・ます form, with no explicit "you" (the subject is dropped as is natural in Japanese). Japanese open-source READMEs and docs (Qiita, Zenn, project docs) use です・ます; plain だ・である would read cold, keigo-heavy forms (ございます) would read as customer service. Requests use "〜してください" and "〜いただけるとありがたいです" (for the credit line).
- Register (how technical, how warm): plain, calm, sourced. Technical terms stay in katakana or Latin as developers write them. Full-width punctuation 、。 and full-width ： inside Japanese sentences; no space between Japanese and Latin/digits except where the English has a space in a number or unit (a thin readability space is kept around numbers, as is common in technical docs).

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | VRAM (and "GPU メモリ" for the measured peak) | Japanese developers say VRAM freely; the table row follows nvidia-smi wording "GPU メモリ" |
| text-to-image | テキストから画像への生成 | "text-to-image" in katakana is also common, but the descriptive form reads better in the first line |
| tile (VAE tile) | タイル | |
| seed | シード | |
| prompt | プロンプト | "ネガティブプロンプト" for negative prompt |
| quantization | 量子化 | |
| setup / install | インストール (for the act), `setup.py` unchanged | "セットアップ" avoided to keep one word |
| measured / not tested | 計測 / 未検証 | "未検証" every time for "not tested"; "試していません" used only for "we did not try" statements; never softened |
| open source license / NOTICE | ライセンス; `NOTICE` file kept as is | "条件" for the NOTICE requirement, "ありがたいですが、必須ではありません" for the credit line |
| refiner | refiner (left in English) | no settled Japanese term |
| latent | latent (left in English) | same |
| unofficial | 非公式プロジェクト | "関係ありません" for not affiliated |
| segment (engine slice) | セグメント | explained once as "ネットワークの一部分" |

## Avoided
- Phrases that sound like advertising in this language/culture: 圧倒的, 驚異の, 簡単に, 誰でも, 最強, 爆速, 革新的, 完璧; any "初の", "唯一", "最速".
- Literal translations that read wrongly: "fits comfortably" is not turned into 余裕で動く as a claim of ours; it stays an English quote with a plain gloss. "Honest limit" became "正直な限界".

## Formatting
- Numbers and decimal separator: unchanged as the test requires (12.2, 261.6, "10 509", "6,577,440,704"); Japanese readers use the same decimal point and ASCII digits. The number slots and the unit symbols (s, MiB, GB, dB) stay as in English; only "minutes" next to `29` is 分.
- Script issues (right-to-left, line height, no spaces between words, table widths): no spaces between words; table cells kept short; headings short.
- Anchor line `<a id="what-it-runs"></a>` kept above the heading "何を動かすか"; the link "何を動かすか" points to `#what-it-runs`.
- The AI-localization sentence is the last line, after the link line.

## Back-translation check
- First paragraph back into English by the reader: "On Windows, using stable-diffusion.cpp, run 768x1344 text-to-image with Z-Image-Turbo (Q8_0 GGUF) on a 4 GB VRAM GTX 1050 Ti (Pascal, sm_61). Measured on a 16 GB RAM laptop; the process uses about 11 GB RAM. The same seed gives the same image pixel for pixel. Measurements and engine patches are public, downloads are pinned by sha256, and an AI coding agent can install it following the steps. Unofficial project; no relation to Tongyi-MAI, leejet, NVIDIA."; differences from the English: none of substance
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes (all four back-translated and compared; no meaning drift, no softened limit, no added claim; condition vs request kept distinct; unofficial line plain; cuDNN paragraph keeps NVIDIA software / optional / asked once)

## Open points / corrections welcome
- "Hardware test report" (issue form name) left in English, as in the Turkish file.
- "コントリビュート" for the Contributing heading is the usual katakana form; some projects write "貢献" or "コントリビューション".
- "数字で見る" for "At a glance" is a deliberate localization; a reader may prefer "ひと目でわかる数字".
- Reader (R8): no disagreement. Minor, not changed: 私たち appears often and is slightly translation-flavored in Japanese READMEs, but is acceptable and consistent. No edits made.

## Round 2
- Round 2 (K-21): "by default" = デフォルトで; "without payment or sign-in" = 支払いも、サインインも求められません (deliberately not 無料); "we found no clause" = 文面を読んだ範囲では...見つかりませんでした; license sentence kept as 同意しない人はダウンロード、インストール、使用をしてはならない、と書かれています.
- Reader fix (ja): added 私たちが to keep the explicit "we" in "we found no clause" (brief rule 3); other pieces read natural and unchanged.
