# Русский (ru): localization notes

Written by: W5 (Sonnet 5.5), 2026-11-14   Read by: R5 (Sonnet 5.5), 2026-11-14   Status: ok

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: "вы" (lowercase, plural/polite), imperative-polite verbs ("попробуйте", "закройте"). Russian developer READMEs and docs use "вы"; "ты" is only for chats and very informal projects. The project's English is neutral, so the polite form fits.
- Register: plain technical, calm, sourced. Short sentences, no exclamations, no marketing words.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | память GPU; "видеопамять" only in the translated quotes | Russian developers say both "видеопамять" and "VRAM"; "память GPU" matches nvidia-smi output |
| text-to-image | генерация изображений по тексту | "text-to-image" is also common, but the descriptive form is clearer in the first sentence |
| tile (VAE tile) | тайл | common in Russian ML/graphics usage; "плитка" would read oddly |
| seed | сид | "seed" is used too; "сид" is the common spoken/written form |
| prompt | промпт | "запрос" would be ambiguous; "промпт" is the community word |
| quantization | квантизация | "квантование" also exists; one root kept everywhere |
| setup / install | установка (script name `setup.py` unchanged) | |
| measured / not tested | измерялось / не проверялось | "не проверялось" says we did not run it, not that it fails |
| open source license / NOTICE | лицензия; файл `NOTICE` | credit is a condition (условие) for NOTICE, a request (просьба) for the credit line |
| refiner | refiner | left in Latin, as Russian developers do |
| latent | латент | |

## Avoided
- Phrases that sound like advertising in this language/culture: "уникальный", "революционный", "легко", "мощный", "лучший", "бесплатно и без ограничений".
- Literal translations that read wrongly: "ширина по умолчанию" for "default"; "нуль потерь"; word-for-word "fits comfortably" (kept as English quote with a Russian gloss).

## Formatting
- Numbers and decimal separator: the test requires them unchanged (12.2 stays 12.2; ASCII digits). Russian readers expect a comma (12,2); the text copes because every number carries a unit and sits in tables or next to a command. Units s, MiB, GB, dB stay Latin as the brief requires (not "с", "МиБ"). Ranges "X to Y" are written "от X до Y" in prose and tables; in the long sentences "X–Y" with an en dash is used. Slots `{{...}}` untouched.
- Script issues (right-to-left, line height, no spaces between words, table widths): none; Cyrillic words are longer than English, table cells were kept short.

## Back-translation check
- First paragraph back into English by the reader: "Text-to-image generation with Z-Image-Turbo (Q8_0 GGUF) at 768x1344 on a GTX 1050 Ti with 4 GB (Pascal, sm_61), via stable-diffusion.cpp, on Windows. Measured on a 16 GB RAM laptop, process uses about 11 GB RAM. Same seed gives the same pixels; measurements and engine patches are published, downloads pinned by sha256, an AI coding agent can run the install step by step. Unofficial project, not affiliated with Tongyi-MAI, leejet or NVIDIA."; differences from the English: none in meaning. Quick start, limits (all 9 items, 'не проверялось' kept) and license (NOTICE = condition, credit line = request, cuDNN = NVIDIA's, optional) also back-translated: no drift, no added claims.
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes

## Open points / corrections welcome
- "Hardware test report" (issue form name) stays in English, as in tr.
- "Compute capability" kept in English as a term of NVIDIA documentation.
- Reader fixes: removed "у нас на нашем" (doubled); "форма обращения" (form of address, wrong) replaced by "шаблон обращения ... в разделе issues"; added the dash in three "X — это Y" sentences. Reader suggestion left open: "сид" vs "seed" both fine.
- Headings: "Коротко в цифрах" for "At a glance"; "Лицензия и упоминание авторства" for "License and credit" (keeps the condition/request split in the credit bullet).

## Round 2
- "By default" chosen as the plain adverbial phrase of the language; "without payment or sign-in" rendered as "no payment requested, no account login" (not the everyday word for free). "We found no clause" kept with "we". The license sentence is attributed to NVIDIA's license and keeps "must not" with all three verbs.
- Reader check: no mixed Latin/Cyrillic words found; "тот, кто" is correct and natural. No change.
