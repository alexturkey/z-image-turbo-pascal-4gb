# Bahasa Indonesia (id): localization notes

Written by: W12, 2026-11-14   Read by: R12, 2026-11-14   Status: ok

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: "Anda" (formal-neutral). Indonesian GitHub READMEs vary between "kamu" and "Anda"; "Anda" is safe for an international project README and avoids sounding either stiff-bureaucratic or too chatty. Instructions are imperatives without "silakan" except where it reads as an invitation ("Mohon baca").
- Register (how technical, how warm): standard Indonesian (baku) with English tech terms kept in italics-free plain form where developers use them (patch, build, prompt, seed, tile, driver, GPU, RAM, VAE, latent, text encoder). Calm, factual.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | memori GPU; "VRAM" only inside quotes | |
| text-to-image | text-to-image, with "membuat gambar dari teks" in the title block | English term is common among Indonesian developers |
| tile (VAE tile) | tile | not translated |
| seed | seed | |
| prompt | prompt | |
| quantization | kuantisasi | accepted term |
| setup / install | memasang / pemasangan; `setup.py` | "instalasi" is also used; "pemasangan" chosen for the guide link and requirements |
| measured / not tested | diukur / tidak diuji | same pair everywhere |
| open source license / NOTICE | lisensi / berkas `NOTICE` | NOTICE is "syarat" (condition); credit line "kami hargai, tetapi tidak diwajibkan" |
| unofficial | Tidak resmi. Tidak berafiliasi dengan ... | plain legal-sounding |
| file | berkas | used everywhere (never "file" in prose, "fail" is Malay) |
| steps | langkah (steps) | "steps" in brackets once in the glance section |

## Avoided
- Phrases that sound like advertising in this language/culture: "terbaik", "andal", "mudah banget", "revolusioner", "canggih", "tanpa ribet".
- Literal translations that read wrongly: "fits comfortably" kept as an English quote plus gloss; "tight memory" is "memori sangat mepet" (natural), not "memori ketat".

## Formatting
- Numbers and decimal separator: kept as English (12.2, 261.6), although Indonesian normally writes a decimal comma (12,2) and a thousands point. The test requires the English form; the numbers sit next to units and in tables, so they stay readable. The thousands forms 10 509 and 6,577,440,704 are kept as written.
- Script issues: none (Latin script).

## Back-translation check
- First paragraph back into English by the reader: Z-Image-Turbo (Q8_0 GGUF) for making images from text (text-to-image) at 768x1344 on a GTX 1050 Ti 4 GB (Pascal, sm_61), with stable-diffusion.cpp, on Windows. Measured on a 16 GB RAM laptop where the process uses about 11 GB RAM. Same seed gives the same pixels, pixel by pixel; measurement results and engine patches are published, downloads are pinned with sha256, and an AI coding agent can install it step by step. Unofficial. Not affiliated with Tongyi-MAI, leejet or NVIDIA. Differences from the English: none; quick start, limits (all items, 'tidak diuji' kept), license (NOTICE is 'syarat', credit 'kami hargai, tetapi tidak diwajibkan'; cuDNN optional, NVIDIA's, asked once) match the English. Slots and numbers intact.
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes (all four sections back-translated and compared)

## Open points / corrections welcome
- "Anda" versus "kamu": chosen "Anda"; a reader from the Indonesian developer community may prefer "kamu".
- "Sekilas" for "At a glance" and "Mulai cepat" for "Quick start": check these headings feel natural.
- "Memori sangat mepet" for "Memory is tight": colloquial but common in technical writing; reader to confirm.
- Reader R12: Natural Indonesian developer register. 'Anda' is fine for a project README. No change made.

## Round 2

- Round 2: "by default" is "secara default"; "without payment" is "tanpa diminta pembayaran" (deliberately not "gratis"); "without sign-in" is "tanpa login"; "we found no clause" is "kami tidak menemukan klausul". The NVIDIA sentence is "Lisensi NVIDIA menyatakan bahwa siapa pun yang ... tidak boleh mengunduh, memasang, atau menggunakannya", keeping attribution and all three verbs.
- Round 2 reader: all three pieces and the two script-changed lines read naturally and keep the meaning; no change needed.
