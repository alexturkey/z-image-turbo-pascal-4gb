# Bahasa Melayu (ms): localization notes

Written by: W12, 2026-11-14   Read by: R12, 2026-11-14   Status: ok

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: "anda" (formal-neutral), the standard in Malaysian technical documents; "kamu"/"awak" would be too casual for a project page. Imperatives are plain ("cuba", "letakkan", "hentikan").
- Register (how technical, how warm): Malaysian Malay (Bahasa Malaysia), standard orthography (Dewan Bahasa style where it is also common among developers: "muat turun", "pemacu", "komputer riba", "fail", "cakera", "lesen", "imej", "perisian"). English technical terms kept where Malaysian developers use them (patch, build, prompt, seed, tile, VAE, latent, text encoder, runtime). Calm and factual, no hype.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | memori GPU; "VRAM" only inside quotes | |
| text-to-image | text-to-image, with "menjana imej daripada teks" in the title block | |
| tile (VAE tile) | jubin (tile) first, then "jubin" | Malaysian texts use "jubin" for tile; the English word is shown once in brackets |
| seed | seed | |
| prompt | prompt | |
| quantization | kuantisasi | |
| setup / install | memasang / pemasangan; `setup.py` | "panduan pemasangan" for the agent install guide |
| measured / not tested | diukur / tidak diuji | same pair everywhere |
| open source license / NOTICE | lesen / fail `NOTICE` | NOTICE is "syarat" (condition); the credit line "amat dihargai, tetapi tidak diwajibkan" |
| unofficial | Tidak rasmi. Tiada kaitan dengan ... | plain, legal-sounding |
| download | muat turun | Malaysian usage (Indonesian uses "unduh") |
| release (GitHub) | keluaran | |
| steps | langkah (steps) | |

## Avoided
- Phrases that sound like advertising in this language/culture: "terbaik", "hebat", "revolusi", "mudah sahaja", "tanpa sebarang masalah".
- Literal translations that read wrongly: Indonesian-only words (berkas, unduh, lisensi, perangkat lunak, gambar for images) are not used; "fits comfortably" stays an English quote with a gloss; "tight memory" is "memori sangat terhad".

## Formatting
- Numbers and decimal separator: kept as in English (12.2, 261.6, 10 509); Malaysian writing uses a decimal point already, so no conflict. ASCII digits.
- Script issues: none (Latin script). The headings say "Had" for limits.

## Back-translation check
- First paragraph back into English by the reader: Z-Image-Turbo (Q8_0 GGUF) for generating images from text (text-to-image) at 768x1344 on a GTX 1050 Ti 4 GB (Pascal, sm_61), with stable-diffusion.cpp, on Windows. Measured on a 16 GB RAM laptop where the process uses about 11 GB RAM. Same seed gives the same pixels; measurement results and engine patches (tampalan) are published, downloads pinned with sha256, and an AI coding agent can install it step by step. Unofficial. No connection with Tongyi-MAI, leejet or NVIDIA. Differences from the English: none of substance; quick start, limits (all items, 'tidak diuji' kept), license (NOTICE a condition, credit 'amat dihargai, tetapi tidak diwajibkan'; cuDNN optional, NVIDIA's, asked once) match the English. Slots and numbers intact.
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes (all four sections back-translated and compared)

## Open points / corrections welcome
- Tile: "jubin" is formal; a reader may prefer plain "tile". It is glossed once and then used consistently.
- "Sepintas lalu" for "At a glance" and "Mula pantas" for "Quick start": check the headings.
- The Malay and Indonesian files were written separately on purpose (different vocabulary: muat turun/unduh, fail/berkas, lesen/lisensi, pemacu/driver, komputer riba/laptop); the reader of ms should check no Indonesian word slipped in.
- Reader R12: Fixed one clumsy sentence in the 'How to read this' paragraph ('sejauh mana dekat ... sejauh mana cantik' became 'betapa dekatnya ... betapa cantiknya rupa'). No Indonesian words found (grep for berkas/unduh/lisensi/perangkat/gambar: none).

## Round 2

- Round 2: "by default" is "secara lalai"; "without payment" is "tanpa bayaran diminta" (deliberately not "percuma"); "without sign-in" is "tanpa log masuk"; "we found no clause" is "kami tidak menemui klausa". The NVIDIA sentence is "Lesen NVIDIA menyatakan bahawa sesiapa yang ... tidak boleh memuat turun, memasang atau menggunakannya", keeping attribution and all three verbs.
- Round 2 reader: all three pieces and the two script-changed lines read naturally and keep the meaning; no change needed.
