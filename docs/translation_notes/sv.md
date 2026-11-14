# Svenska (sv): localization notes

Written by: W3 (writer agent), 2026-11-14   Read by: R3 (reader agent), 2026-11-14   Status: ok

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: "du", as everywhere in Swedish (there is no formal address in practice). Advice is phrased as invitations ("prova det först", "stäng andra program").
- Register (how technical, how warm): plain, calm, sourced, understated (lagom). No exclamation marks, no sales language; the numbers carry the message.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | GPU-minne; "VRAM" only inside quotes from the model card | Swedish developers say VRAM or grafikminne; GPU-minne sits well next to "systemminne" |
| text-to-image | text-till-bild | |
| tile (VAE tile) | ruta (plural: rutor) | "kakel" exists but "ruta" is more natural; "rutad avkodning" for tiled |
| seed | seed | not translated ("frö" is not used by developers) |
| prompt | prompt (plural: prompter) | not translated |
| quantization | kvantisering | |
| setup / install | installation; script name `setup.py` unchanged | |
| measured / not tested | uppmätt / inte testat | same wording everywhere |
| open source license / NOTICE | licens / `NOTICE`-fil | condition: "villkoret"; credit: "önskad, inte obligatorisk" |
| refiner, latent, flash attention, scheduler, sampler | kept in English | used as is by Swedish developers; "refinern" gets the Swedish definite ending |
| engine | motor | Swedish developers say motor for a rendering/inference engine |
| unofficial | inofficiellt | |

## Avoided
- Phrases that sound like advertising in this language/culture: "enkelt", "blixtsnabb", "revolutionerande", "perfekt", "fantastisk", superlatives.
- Literal translations that read wrongly: "fits comfortably" is quoted in English and explained; "Honest limit" became "Ärlig gräns"; "Who does what" became "Vem gör vad".

## Formatting
- Numbers and decimal separator: Swedish normally writes 12,2 and a thin space for thousands; the test requires 12.2 and the English thousands form, so those stay. Numbers carry units and sit in tables or plain statements. Slots `193–228 s` etc. are untouched.
- Script issues: none; Latin script. Swedish compounds are written together ("kodagent", "diskutrymme").

## Back-translation check
- First paragraph back into English by the reader: 'Text-to-image with Z-Image-Turbo (Q8_0 GGUF) at 768x1344 on a GTX 1050 Ti with 4 GB (Pascal, sm_61), with stable-diffusion.cpp, on Windows. Measured on a laptop with 16 GB RAM, where the process uses about 11 GB RAM. Same seed gives same pixels...; measurements and engine patches are published, downloads are locked with sha256, an AI coding agent can install it step by step. Unofficial. Not affiliated with Tongyi-MAI, leejet or NVIDIA.' Differences: none after the reader fix (the original 'Inte knutet till' was vaguer than 'not affiliated')
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes (all four back-translated and compared: first paragraph, quick start incl. cuDNN optional/NVIDIA's/asked once, limits with all items and 'not tested', license with NOTICE condition vs credit request)

## Open points / corrections welcome
- "AI-kodagent" for "AI coding agent"; a reader may prefer "AI-kodningsagent".
- "Clean-root-test" kept in English form (no common Swedish term).
- "Erkännande" for the "Credit" section heading (alternative: "Attribution"); "villkoret" vs "önskad" keeps the condition/request difference.
- Reader R3: Reader fixes in README.sv.md: 'Inte knutet till' changed to 'Inte affilierat med' (plain, legal-sounding); 'Minnet är snålt' (snålt = stingy) changed to 'Minnet är knappt'; 'Lediga RAM' changed to 'Ledigt RAM' (neuter, as in 'det lediga RAM:et'). 'Erkännande' is fine (the Swedish CC term for attribution).

## Round 2
- Round 2: "by default" = "som standard"; "without payment" = "utan att någon betalning begärs" (not "gratis"); "without sign-in" = "utan inloggning"; "we found no clause" = "vi hittade ingen klausul"; NVIDIA's rule kept attributed ("säger att den som ... inte får") with all three verbs.
