# Nederlands (nl): localization notes

Written by: W3 (writer agent), 2026-11-14   Read by: R3 (reader agent), 2026-11-14   Status: ok

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: informal "je/jij". Dutch developer READMEs and tech documentation use "je"; "u" would sound distant or bureaucratic. Advice is phrased as invitations ("probeer dat dus eerst", "sluit andere programma's").
- Register (how technical, how warm): plain, calm, sourced; direct and sober, which fits the Dutch style. No exclamation marks, no sales language.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | GPU-geheugen; "VRAM" only inside quotes from the model card | Dutch developers say VRAM or videogeheugen; GPU-geheugen sits well next to "systeemgeheugen" |
| text-to-image | tekst-naar-beeld | "afbeelding" for a picture; "beeld" only inside the compound |
| tile (VAE tile) | tegel | |
| seed | seed | not translated |
| prompt | prompt | not translated; negative prompt is "negatieve prompt" |
| quantization | kwantisatie | |
| setup / install | installatie; script name `setup.py` unchanged | |
| measured / not tested | gemeten / niet getest | same wording everywhere |
| open source license / NOTICE | licentie / `NOTICE`-bestand | condition: "de voorwaarde"; credit: "gewenst, niet verplicht" |
| refiner, latent, flash attention, scheduler, sampler, engine | kept in English | used as is by Dutch developers |
| unofficial | onofficieel | |

## Avoided
- Phrases that sound like advertising in this language/culture: "gemakkelijk", "razendsnel", "revolutionair", "perfect", "geweldig"; Dutch readers react badly to hype, so numbers carry the message.
- Literal translations that read wrongly: "fits comfortably" is quoted in English and explained; "Honest limit" became "Eerlijke grens"; "Who does what" became "Wie wat doet".

## Formatting
- Numbers and decimal separator: Dutch normally writes 12,2; the test requires 12.2, so the point stays. Numbers carry units and sit in tables or in plain statements. Slots `193–228 s` etc. are untouched.
- Script issues: none; Latin script.

## Back-translation check
- First paragraph back into English by the reader: 'Text-to-image with Z-Image-Turbo (Q8_0 GGUF) at 768x1344 on a GTX 1050 Ti with 4 GB (Pascal, sm_61), with stable-diffusion.cpp, on Windows. Measured on a laptop with 16 GB RAM, on which the process uses about 11 GB RAM. Same seed gives the same pixels...; measurements and engine patches are public, downloads are fixed with sha256, and an AI coding agent can install it step by step. Unofficial. Not connected to Tongyi-MAI, leejet or NVIDIA.' Differences: none
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes (all four back-translated and compared: first paragraph, quick start incl. cuDNN optional/NVIDIA's/asked once, limits with all items and 'not tested', license with NOTICE condition vs credit request)

## Open points / corrections welcome
- "AI-codeeragent" for "AI coding agent" (alternatives: "AI-codeerassistent", "coding agent"); a reader may prefer the English term.
- "Clean-root-test" is kept in English form (no common Dutch term).
- "Opzetten van anderen" (English: "Other people's setups") may read slightly stiff; "Setups van anderen" is an alternative.
- Reader R3: No disagreement. Reader suggestion (not changed): the heading "Wat het draait" is slightly literal; "Wat erin draait" or "Waarmee het draait" would be more idiomatic, but it is understandable and the anchor works. "Opzetten van anderen" reads a little stiff; "Setups van anderen" is what many Dutch developers would write.

## Round 2
- Round 2: "by default" = "standaard"; "without payment" = "zonder dat er betaling wordt gevraagd" (not "gratis"); "without sign-in" = "zonder inloggen"; "we found no clause" = "we hebben ... geen bepaling gevonden"; NVIDIA's rule kept attributed ("staat dat wie ... niet mag") with all three verbs.
