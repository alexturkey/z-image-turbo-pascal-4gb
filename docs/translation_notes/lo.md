# ລາວ (lo): localization notes

Written by: W10 (Claude), 2026-11-14   Read by: R10 (Claude), 2026-11-14   Status: ok

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: polite "ທ່ານ", used sparingly (most sentences have no pronoun). Lao developer READMEs are rare and mostly in English or follow Thai conventions, so a neutral polite register was chosen over a chatty one. First-person plural is "ເຮົາ".
- Register (how technical, how warm): plain technical Lao with English terms kept in Latin script where Lao developers use them (build, seed, prompt, step, decode, commit). Calm and sourced; no sales language.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
| GPU memory (VRAM) | VRAM (ໜ່ວຍຄວາມຈຳ GPU) | VRAM in labels, the Lao phrase in running prose |
| text-to-image | ສ້າງຮູບຈາກຂໍ້ຄວາມ | descriptive Lao |
| tile (VAE tile) | ໄທລ໌ | transliteration; may be unfamiliar to readers, see open points |
| seed | seed | kept in Latin script |
| prompt | prompt | kept in Latin script |
| quantization | quantization | kept in Latin script |
| setup / install | ຕິດຕັ້ງ | script name `setup.py` unchanged |
| measured / not tested | ວັດ / ວັດຜົນ / ຍັງບໍ່ໄດ້ທົດສອບ | "ຍັງບໍ່ໄດ້ທົດສອບ" means "not yet tested" |
| open source license / NOTICE | ໃບອະນຸຍາດ (license) / ໄຟລ໌ `NOTICE` | |
| unofficial | ບໍ່ເປັນທາງການ | |
| repository | repository (Latin script) | no common Lao word |

## Avoided
- Phrases that sound like advertising in this language/culture: superlatives ("ທີ່ສຸດ" as a claim), "ງ່າຍຫຼາຍ", "ປະຕິວັດ", exclamation marks.
- Literal translations that read wrongly: model card and README quotes stay in English with a Lao explanation.

## Formatting
- Numbers and decimal separator: unchanged as the test requires (12.2, ASCII digits). Lao readers use ASCII digits in technical text (Lao digits are rarely used in code docs), so no workaround is needed. Ranges are written with "ຫາ".
- Script issues (right-to-left, line height, no spaces between words, table widths): Lao has no spaces between words; a space is used between clauses. Because spaces and punctuation (";", ",", ".") are used between clauses, long lines can wrap. Table cells are kept short.

## Back-translation check
- First paragraph back into English by the reader: "Text-to-image with Z-Image-Turbo (Q8_0 GGUF) at 768x1344 on a GTX 1050 Ti with 4 GB VRAM (Pascal, sm_61) using stable-diffusion.cpp on Windows. Measured on a 16 GB RAM laptop where the process uses about 11 GB. Same seed gives the same pixels; measurements and engine patches fully disclosed, downloads locked by sha256, an AI coding agent can install step by step. Unofficial, no relation to Tongyi-MAI, leejet or NVIDIA." Differences from the English: none in meaning; Limits (all items, 'not tested' kept) and License (NOTICE a condition, credit line 'we would thank, not required'; NVIDIA property) are intact.
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes (all four back-translated)

## Open points / corrections welcome
- Machine check: the three tests pass for this file.
- Lao technical vocabulary is not standardized; the writer is least sure of "ໄທລ໌", "ແພັດ" (patch), "ບິລດ໌" (build) and "ເຂັນຈິນ/ເອັນຈິນ" (engine). A native reader should confirm or replace them, keeping one word per concept.
- Lao is less certain than Thai: a native developer should check naturalness of the whole file, especially the Limits and License sections.
- Reader R10 (not a native Lao speaker; judged by back-translation and consistency): replaced "ຕຶງ" (stretch/taut, used for "pinned" and "tight") with "ກຳນົດຄົງທີ່ໄວ້" (fixed) and "ຄັບແຄບ" (tight); added "(tile)" gloss at the fallback description in How it works. Loanword transliterations (ແພັດ, ເອັນຈິນ, ບິລດ໌, ໄທລ໌) are consistent in the file and left; a native developer should still confirm them.

## Round 2
- "By default" = "ໂດຍຄ່າເລີ່ມຕົ້ນ"; "without payment or sign-in" = "ໂດຍບໍ່ມີການເກັບເງິນ ແລະ ບໍ່ຕ້ອງເຂົ້າສູ່ລະບົບ" (avoids the everyday word for "free"); "we found no clause" = "ເຮົາບໍ່ພົບຂໍ້ຄວາມໃດ...". The license sentence keeps "ຕ້ອງບໍ່ດາວໂຫຼດ, ຕິດຕັ້ງ ຫຼື ນຳໃຊ້" attributed to NVIDIA's license. Lao wording is least certain; a native reader should check.
- Reader R2 fix: "ຣັນ" (rare letter ຣ, looks like a Thai spelling) replaced by "ແລ່ນ" (run a command). "ກໍລະນີ" (case) is a normal, understood Lao word and was kept. The 581.29 line is natural as is. Pieces 1-3 keep the meaning; no "free/allowed" implied.
