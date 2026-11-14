# Dansk (da): localization notes

Written by: Writer W4, 2026-11-14   Read by: Reader R4, 2026-11-14   Status: ok

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: informal "du". Danish open-source READMEs and documentation address the reader with "du"; "De" would read as stiff or bureaucratic. Imperatives are kept soft where the English is a suggestion ("prøv den først", "luk andre programmer").
- Register (how technical, how warm): plain, calm, sourced; short sentences. Dry understatement, as Danish developers usually write. No marketing words.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | GPU-hukommelse; "VRAM" only inside the English quotes | Danish developers say "VRAM" or "GPU-hukommelse"; "hukommelse" is the standard word for memory (also "systemhukommelse") |
| text-to-image | tekst-til-billede | descriptive Danish compound; the English term is also common |
| tile (VAE tile) | flise | "tile" is also used by Danish developers; "flise" is kept consistently |
| seed | seed | not translated; this is what Danish developers say |
| prompt | prompt (plural: prompts) | not translated; same reason |
| quantization | kvantisering | |
| setup / install | opsætning (the setup step and the layout), installere (the verb) | the file name `setup.py` stays |
| measured / not tested | målt / ikke testet | "ikke testet" says plainly that we did not run it; "målt" only where a number was taken |
| open source license / NOTICE | licens; NOTICE-fil | `NOTICE` stays in code form |
| refiner | refiner | kept in English |
| unofficial | uofficiel | |

## Avoided
- Phrases that sound like advertising in this language/culture: "fantastisk", "revolutionerende", "nem", "ubesværet", "markedets bedste". Danish readers distrust boasting; understatement is the norm.
- Literal translations that read wrongly: "ready-made package" is "en færdig pakke", not a compound; "fits comfortably" stays an English quote with a plain Danish explanation.

## Formatting
- Numbers and decimal separator: the test requires the English form. Danish normally writes a decimal comma (12,2), but the text keeps 12.2 and the English thousands style; every number carries a unit, so readers cope. The machine check forbids the local form.
- Script issues (right-to-left, line height, no spaces between words, table widths): none; Latin script. Danish compounds make a few table cells longer, kept short by wording.

## Back-translation check
- First paragraph back into English by the reader: "Z-Image-Turbo (Q8_0 GGUF) text-to-image at 768x1344 on a 4 GB GTX 1050 Ti with stable-diffusion.cpp on Windows. Measured on a laptop with 16 GB RAM, process uses about 11 GB RAM. Same seed gives the same pixels, pixel for pixel. Measurements and engine patches are published, downloads pinned with sha256, an AI coding agent can install it step by step. Unofficial. Not affiliated with Tongyi-MAI, leejet or NVIDIA."; differences from the English: none
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes (first paragraph, quick start incl. cuDNN optional/NVIDIA/asked once, limits all items present with 'ikke testet'/'ikke testet', license: NOTICE = condition, credit = appreciated not required)

## Open points / corrections welcome
- Gender of "RAM" (dit/din) varies among Danish developers; "dit RAM" is used.
- "Preflight" is kept in English in quotes, as the script prints it.
- "Hardware test report" is the name of the issue form and stays English.
- Credit: the NOTICE file is "betingelsen" (condition); the credit line is "sætter vi pris på ... men det er ikke et krav" (appreciated, not required).
- Reader R4 (2026-11-14) changed two things in README.da.md: heading 'Hvorfor det kan være i 4 GB' -> 'Hvorfor det passer i 4 GB' (the English states a fact, 'kan være i' was vague); 'alle er kontakter' -> 'alle kan slås til og fra' ('kontakter' reads as electrical plugs/contacts in Danish).

## Round 2

- "By default" = "som standard"; "without payment" = "uden betaling" (not "gratis"), "without sign-in" = "uden login"; "we found no provision" = "vi fandt ingen bestemmelse ... der begrænser"; NVIDIA's sentence kept attributed with "må ikke" (whoever = "den, der").
- Reader fix: "i så fald kør" / "i så fall kjør" (imperative after fronted phrase, stiff) changed to "kører du" / "kjører du". Other pieces and the 8–16 s and "581.29" lines unchanged.
