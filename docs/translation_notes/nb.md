# Norsk bokmål (nb): localization notes

Written by: Writer W4, 2026-11-14   Read by: Reader R4, 2026-11-14   Status: ok

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: informal "du". Norwegian developer READMEs and docs address the reader with "du"; "De" is practically unused. Soft suggestions where the English suggests ("prøv den først", "lukk andre programmer").
- Register (how technical, how warm): plain, calm, sourced; short sentences, a little more relaxed than the Danish. Written in Bokmål. No marketing words.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | GPU-minne; "VRAM" only inside the English quotes | Norwegian developers say "VRAM" or "GPU-minne"; "minne" is the standard word (also "systemminne") |
| text-to-image | tekst-til-bilde | Norwegian "bilde" (Danish "billede") |
| tile (VAE tile) | flis (plural: flis) | "tile" is also common among developers; "flis" kept consistently |
| seed | seed | not translated |
| prompt | prompt (plural: prompter) | not translated; Bokmål plural "prompter" |
| quantization | kvantisering | |
| setup / install | oppsett (setup, layout), installere (verb) | the file name `setup.py` stays |
| measured / not tested | målt / ikke testet | "ikke testet" = we did not run it |
| open source license / NOTICE | lisens; NOTICE-fil | `NOTICE` stays in code form |
| refiner | refiner | kept in English |
| unofficial | uoffisiell | |

## Avoided
- Phrases that sound like advertising in this language/culture: "fantastisk", "revolusjonerende", "enkelt", "kjempebra", "markedets beste". Understatement fits Norwegian developer culture.
- Literal translations that read wrongly: "ready-made package" is "en ferdig pakke"; "fits comfortably" stays an English quote with a plain Norwegian explanation. "repoet" (common short form) is used rather than "repositoriet".

## Formatting
- Numbers and decimal separator: the test requires the English form. Norwegian normally writes a decimal comma (12,2), but the text keeps 12.2 and the English thousands style; every number carries a unit. The machine check forbids the local form.
- Script issues (right-to-left, line height, no spaces between words, table widths): none; Latin script (letters æ ø å present).

## Back-translation check
- First paragraph back into English by the reader: "Z-Image-Turbo (Q8_0 GGUF) text-to-image at 768x1344 on a 4 GB GTX 1050 Ti with stable-diffusion.cpp on Windows. Measured on a laptop with 16 GB RAM, process uses about 11 GB RAM. Same seed gives the same pixels, pixel for pixel. Measurements and engine patches are published, downloads pinned with sha256, an AI coding agent can install it step by step. Unofficial. Not affiliated with Tongyi-MAI, leejet or NVIDIA."; differences from the English: none
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes (first paragraph, quick start incl. cuDNN optional/NVIDIA/asked once, limits all items present with 'ikke testet'/'ikke testet', license: NOTICE = condition, credit = appreciated not required)

## Open points / corrections welcome
- "Preflight" is kept in English in quotes, as the script prints it.
- "Hardware test report" is the name of the issue form and stays English.
- Credit: the NOTICE file is "betingelsen" (condition); the credit line is "setter vi pris på ... men det er ikke et krav" (appreciated, not required).
- Shared with da: address and terms; differs in spelling (bilde/billede, minne/hukommelse, flis/flise, repoet/repository).
- Reader R4 (2026-11-14): no change needed; terms and register natural for Norwegian developers ('repoet', 'bryter', 'får plass').

## Round 2

- "By default" = "som standard"; "without payment" = "uten betaling" (not "gratis"), "without sign-in" = "uten innlogging"; "we found no provision" = "vi fant ingen bestemmelse ... som begrenser"; NVIDIA's sentence kept attributed with "må ikke" (whoever = "den som").
- Reader fix: "i så fall kjør" (stiff imperative after fronted phrase) changed.
