# Deutsch (de): localization notes

Written by: W3 (writer agent), 2026-11-14   Read by: R3 (reader agent), 2026-11-14   Status: ok

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: informal "du". German open-source READMEs and developer docs overwhelmingly use "du" today (GitHub projects, Rust/Python community docs in German); "Sie" would sound like corporate software documentation. Suggestions are phrased as invitations ("probiere es zuerst aus", "lege die Modelle auf eine SSD").
- Register (how technical, how warm): plain, calm, sourced; technical but not stiff. No exclamation marks, no marketing words. Limits are as visible as results.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | GPU-Speicher; "VRAM" only inside quotes from the model card | German developers say VRAM or Grafikspeicher; GPU-Speicher reads cleanly next to "Arbeitsspeicher" (system RAM) |
| text-to-image | Text-zu-Bild | common in the German AI community, also used as is |
| tile (VAE tile) | Kachel | "Kachel" is the usual German word for tiled decoding |
| seed | Seed | not translated; "Startwert" exists but nobody in this community says it |
| prompt | Prompt | not translated; "negative prompt" becomes "Negativ-Prompt" |
| quantization | Quantisierung | |
| setup / install | Installation / Einrichtung; script name `setup.py` unchanged | "Schritt 2" is the setup script; text avoids a third word |
| measured / not tested | gemessen / nicht getestet | "nicht getestet" kept the same everywhere; says we did not run it, not that it fails |
| open source license / NOTICE | Lizenz / `NOTICE`-Datei | condition: "ist die Bedingung"; credit: "erwünscht, aber nicht vorgeschrieben" |
| refiner, latent, flash attention, scheduler, sampler | kept in English | used as is by German developers |
| engine | Engine | as used in German developer texts |
| unofficial | Inoffiziell | |

## Avoided
- Phrases that sound like advertising in this language/culture: "mühelos", "einfach", "blitzschnell", "revolutionär", "bahnbrechend", "perfekt", superlatives of any kind.
- Literal translations that read wrongly: "fits comfortably" is quoted in English and explained as "passt bequem auf Consumer-Karten"; "Honest limit" became "Ehrliche Grenze", which is natural; "Who does what" became "Wer was macht".

## Formatting
- Numbers and decimal separator: German normally writes 12,2 and 6,6 GB; the test requires the English form, so 12.2 stays. Numbers carry units and sit in tables, so readers are not confused. The slots `193–228 s` etc. are untouched.
- Script issues (right-to-left, line height, no spaces between words, table widths): none; Latin script. German words are long, so table headings are kept short. Quotation marks in German text are „…“ except around the credit sentence, where plain ASCII quotes are used because the curly closing quote merges with the URL in the machine check.

## Back-translation check
- First paragraph back into English by the reader: Unofficial-line fixed; 'Text-to-image with Z-Image-Turbo (Q8_0 GGUF) at 768x1344 on a 4 GB GTX 1050 Ti (Pascal, sm_61), with stable-diffusion.cpp, on Windows. Measured on a laptop with 16 GB RAM, where the process occupies about 11 GB RAM. The same seed gives the same pixels, pixel for pixel; measurements and engine patches are published, downloads are pinned by sha256, and an AI coding agent can carry out the installation step by step. Unofficial. Not connected with Tongyi-MAI, leejet or NVIDIA.' Differences: none (no added praise, no softened limit)
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes (all four back-translated and compared: first paragraph, quick start incl. cuDNN optional/NVIDIA's/asked once, limits with all items and 'not tested', license with NOTICE condition vs credit request)

## Open points / corrections welcome
- "Sicherheitsmeldungen gehen über den privaten Weg" and the issue form name "Hardware test report" (kept in English as the form's own name).
- "Clean-Root-Test" is kept as an English-based compound, since no common German term exists; reader may suggest "Test im sauberen Stammordner".
- "Setups anderer" heading of the fourth bullet (English: "Other people's setups"): "Setups anderer" is colloquial and fitting, but a reader may prefer "Aufbauten anderer".
- Reader R3: No disagreement. Naturalness: informal du, VRAM/GPU-Speicher, Kachel, Engine all fit German developer READMEs. "Setups anderer" is fine; "Clean-Root-Test" acceptable.

## Round 2
- Round 2: "by default" = "standardmäßig"; "without payment" = "ohne dass eine Zahlung verlangt wird" (not "kostenlos"); "without sign-in" = "ohne Anmeldung" (no account or login needed); "we found no clause" = "wir haben ... keine Klausel gefunden"; NVIDIA's rule kept attributed ("besagt, dass niemand ... darf") with all three verbs.
