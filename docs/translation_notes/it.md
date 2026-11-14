# Italiano (it): localization notes

Written by: W2 (Sonnet), 2026-11-14   Read by: R2 (Sonnet), 2026-11-14   Status: ok

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: informal "tu" (imperatives such as "provalo", "chiudi", "leggi"). Italian developer READMEs and GitHub documentation address the reader as "tu"; the formal "Lei" would read as a manual or a bank letter.
- Register (how technical, how warm): plain, calm, sourced; technical but not stiff. Established English terms are kept where Italian developers say them (prompt, seed, tile, patch, log, build, scheduler, sampler). No promotional words.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | memoria GPU ("VRAM" only inside the model-card quote) | Italians say "VRAM" and "memoria video"; "memoria GPU" matches the nvidia-smi context |
| text-to-image | generazione di immagini da testo | descriptive form in the first sentence; "text encoder" stays English (the component name) |
| tile (VAE tile) | tile | kept in English, as Italian developers say; plural "tile" (invariable) |
| seed | seed | "seme" is not used in this field |
| prompt | prompt | universal; "negative prompt" also kept |
| quantization | quantizzazione | |
| setup / install | installazione (the script name `setup.py` unchanged) | "avvio rapido" for the quick start section |
| measured / not tested | misurato / non testato | "non testato" is the normal phrase for "not tested" in Italian |
| open source license / NOTICE | licenza; file `NOTICE` | "condizione" for NOTICE, "gradita, non obbligatoria" for the credit line |
| refiner, latent, patch, sampler, scheduler, flash attention, encoder | kept in English | usual in Italian technical text |
| pixel for pixel | pixel per pixel | |
| unofficial | non ufficiale | |

## Avoided
- Phrases that sound like advertising in this language/culture: "straordinario", "rivoluzionario", "semplicissimo", "potentissimo", "il migliore"; no exclamation marks.
- Literal translations that read wrongly: "esecuzione pulita di radice" for "clean-root" (written "test a radice pulita"); "bilanciamento" for "margin" (written "margine"); "un pezzo" for "one piece" (written "un unico blocco").

## Formatting
- Numbers and decimal separator: Italian readers would normally expect a decimal comma (6,6) and a space or dot for thousands. The test requires the English forms, so 12.2 and 261.6 stay with a point. The numbers always carry a unit and sit in tables or short phrases, so the point is understandable; "da X a Y" wording is used for ranges instead of "X to Y" with a hyphen of its own.
- Script issues (right-to-left, line height, no spaces between words, table widths): none; Latin script. Table cells kept short. The `{{...}}` slots and their units are untouched.

## Back-translation check
- First paragraph back into English by the reader: Back-translated from the Italian only: "Text-to-image generation with Z-Image-Turbo (Q8_0 GGUF) at 768x1344 on a 4 GB GTX 1050 Ti (Pascal, sm_61), with stable-diffusion.cpp, on Windows. Measured on a laptop with 16 GB RAM, where the process uses about 11 GB RAM. The same seed gives the same pixels, pixel for pixel; the measurements and engine patches are public, downloads are pinned with sha256, and an AI coding agent can run the installation step by step. Unofficial. No tie to Tongyi-MAI, leejet or NVIDIA." Differences from the English: none in meaning.
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes (first paragraph, quick start, limits, license all checked)

## Open points / corrections welcome
- "Hardware test report" (issue form name) kept in English, as in the Turkish example.
- "In breve" chosen for "At a glance"; "Avvio rapido" for "Quick start"; "Crediti" for "credit". The reader may prefer "Panoramica" for the first.
- "Il modello ... è distillato per 8 passi": "distillato" (the term used in Italian ML texts) kept.
- Reader (R2) agrees with the form of address (tu), terms and the "In breve" heading. cuDNN paragraph keeps: NVIDIA software, optional, asks once. Condition (NOTICE) vs. appreciated (credit line) stays distinct. No added or softened claims found. Number format stays English by test requirement; acceptable.

## Round 2
- Round 2: "per impostazione predefinita" for "by default"; "senza registrazione né accesso" for "without sign-in"; "senza che venga richiesto alcun pagamento" (not "gratis"); "abbiamo trovato" kept with "noi"; "non deve ... né ... né" keeps the force of "must not".
- Round 2 reader check: three pieces and the two script-changed lines (256 MiB, 581.29) read natively; meaning, calm tone and rule 3 and 4 fine; no change needed.
