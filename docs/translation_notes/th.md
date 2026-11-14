# ไทย (th): localization notes

Written by: W10 (Claude), 2026-11-14   Read by: R10 (Claude), 2026-11-14   Status: ok

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: neutral polite "คุณ", used sparingly (most sentences have no pronoun, as is normal in Thai technical docs); no sentence-final particles (ครับ/ค่ะ), because Thai GitHub READMEs are written in plain neutral prose. The first-person plural is "เรา".
- Register (how technical, how warm): plain technical Thai with English terms kept in Latin script where Thai developers write them that way (commit, build, seed, prompt, step, decode, tile family). Calm and sourced; no sales language.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
| GPU memory (VRAM) | VRAM (หน่วยความจำ GPU) | Thai developers say VRAM; the Thai phrase is used in running prose |
| text-to-image | สร้างภาพจากข้อความ | descriptive Thai in the title; the English term is common too |
| tile (VAE tile) | ไทล์ | transliteration used by Thai developers |
| seed | seed | kept in Latin script |
| prompt | prompt | kept in Latin script (the table header and labels use "prompt" too) |
| quantization | quantization | kept in Latin script; the Thai "ควอนไทซ์" is rare in READMEs |
| setup / install | ติดตั้ง | the script name `setup.py` is unchanged |
| measured / not tested | วัด / วัดผลแล้ว / ยังไม่ได้ทดสอบ | "ยังไม่ได้ทดสอบ" keeps the meaning "we did not run it" |
| open source license / NOTICE | สัญญาอนุญาต (license) / ไฟล์ `NOTICE` | "สัญญาอนุญาต" is the usual Thai word for a software license |
| unofficial | ไม่เป็นทางการ | |
| repository | รีโพ (once, in the first paragraph of "Start here"), then "รีโพนี้" | |

## Avoided
- Phrases that sound like advertising in this language/culture: "ที่สุด", "เหนือกว่า", "ง่ายมาก", "สุดยอด", "ปฏิวัติ"; exclamation marks; "ฟรี" used as a sales hook.
- Literal translations that read wrongly: "fits comfortably" is kept as an English quote with a Thai explanation, not translated; "honest limit" became "ข้อจำกัดที่ต้องบอกตรงๆ".

## Formatting
- Numbers and decimal separator: unchanged as the test requires (12.2, ASCII digits). Thai readers also use the point as decimal separator and ASCII digits in technical text, so no workaround is needed. Ranges are written with "ถึง" ("29.8 ถึง 36.3 s"), as the English writes "to".
- Script issues (right-to-left, line height, no spaces between words, table widths): Thai has no spaces between words; a space is used between clauses so lines can wrap. Table cells are kept short. Slots such as `193–228 s` stay as plain text, separated from Thai text by spaces.

## Back-translation check
- First paragraph back into English by the reader: "Text-to-image with Z-Image-Turbo (Q8_0 GGUF) at 768x1344 on a GTX 1050 Ti with 4 GB VRAM (Pascal, sm_61) using stable-diffusion.cpp on Windows. Measured on a 16 GB RAM laptop where the process uses about 11 GB. Same seed gives the same pixels; measurements and engine patches are fully disclosed; downloads pinned by sha256; an AI coding agent can install it step by step. Unofficial, not affiliated with Tongyi-MAI, leejet or NVIDIA." Differences from the English: none in meaning; limits, condition vs request (NOTICE vs credit), and the cuDNN paragraph (NVIDIA's, optional, asked once) are intact.
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes (all four back-translated)

## Open points / corrections welcome
- Machine check: the three tests pass for this file.
- The sentence "ไม่ได้เก็บไว้ที่นี่" and the credit sentence ("เราจะขอบคุณ แต่ไม่ได้บังคับ") keep the condition (NOTICE) versus request (credit) difference; a reader may check the tone.
- "เสมอไป" in "ภาพไม่ได้ทำตาม prompt ครบทุกรายละเอียดเสมอไป" mirrors the English "does not always"; check naturalness.
- Terms left in English (seed, prompt, quantization, refiner, decode, latent) are a deliberate choice; a Thai reader may prefer transliterations.
- Reader R10: no meaning drift, no added praise found. One fix: "แสดงให้ดูเฉยๆ ไม่ได้ขัดขวางอะไร" (casual) changed to the wording used in Quick start ("แสดงให้ดูเท่านั้นและไม่เคยขวางการทำงาน"). Register and terms judged natural.

## Round 2
- "By default" = "โดยค่าเริ่มต้น"; "without payment or sign-in" = "โดยไม่มีการเรียกเก็บเงินและไม่ต้องลงชื่อเข้าใช้" (avoids the everyday word for "free"); "we found no clause" = "เราไม่พบข้อความใดในสัญญาที่จำกัด...". The license sentence keeps "ต้องไม่ดาวน์โหลด ติดตั้ง หรือใช้งาน" attributed to NVIDIA's license.
- Reader R2 fix: in the "one card, one machine" line, added "ส่วน" and a comma after the removed item so the list of untested cases reads as separate items. Pieces 1-3 read correctly: calm, no "free/allowed" implied, "must not" kept.
