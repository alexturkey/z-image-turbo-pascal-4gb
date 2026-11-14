# Español (es): localization notes

Written by: W1 (Claude Sonnet 5.5), 2026-11-14   Read by: R1 (Claude Sonnet 5.5), 2026-11-14   Status: ok

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: informal "tú" (neutral international Spanish, no voseo, no vosotros). Spanish-language developer READMEs and docs (Hispanic America and Spain) mostly use "tú" or impersonal imperatives; "usted" would sound stiff. Imperatives are soft ("pruébalo primero", "cierra otros programas").
- Register (how technical, how warm): plain, calm, sourced; technical terms as Spanish developers say them (many stay in English). No advertising words.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | memoria de la GPU; "VRAM" only inside the quotes | developers say "VRAM" often; kept in English quotes |
| text-to-image | generación de imágenes a partir de texto; "texto a imagen" is also common | descriptive form used in the first sentence |
| tile (VAE tile) | mosaico (tile) in the options table, "mosaico" elsewhere | "tile" kept once in parentheses because the option is `--vae tiled` |
| seed | semilla | |
| prompt | prompt | the usual word among Spanish-speaking developers; "indicación" is rare |
| quantization | cuantización | |
| setup / install | instalación (script name `setup.py` unchanged) | |
| measured / not tested | medido / no probado | "no probado" says it was not run, not that it failed |
| open source license / NOTICE | licencia; archivo `NOTICE` | "condición" for NOTICE, "se agradece, sin que sea obligatoria" for the credit line |
| refiner, latent, sampler, scheduler, flash attention | kept in English | what developers say |
| not affiliated | Sin relación con | plain, legal-sounding |

## Avoided
- Phrases that sound like advertising in this language/culture: "increíble", "fácil", "revolucionario", "potente", "sin esfuerzo".
- Literal translations that read wrongly: "fits comfortably" was kept as the English quote plus a Spanish gloss; "Start here" is "Empieza aquí", not "Comienza aquí mismo".

## Formatting
- Numbers and decimal separator: the test requires 12.2, not 12,2; Spanish readers expect a comma in Spain, a point in much of Latin America, so the point is acceptable; units are always next to the numbers. Thousands as in the English ("10 509", "6,577,440,704"). Unit symbols GB, MiB, s, dB kept.
- Script issues (right-to-left, line height, no spaces between words, table widths): none; Latin script. Table header words are short.
- The English words "or" inside the options table were changed to "o" between two separate inline codes.

## Back-translation check
- First paragraph back into English by the reader: "Text-to-image generation with Z-Image-Turbo (Q8_0 GGUF) at 768x1344 on a 4 GB GTX 1050 Ti (Pascal, sm_61), with stable-diffusion.cpp, on Windows. Measured on a laptop with 16 GB RAM, where the process uses about 11 GB. The same seed gives the same pixels, pixel by pixel; measurements and engine patches are public, downloads are pinned with sha256, and an AI coding agent can install it step by step. Unofficial. No relation to Tongyi-MAI, leejet or NVIDIA."; differences from the English: none in meaning. One small edit: "retroceso forzado" (odd for "forced fallback") became "se fuerza el paso a la alternativa (fallback)".
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes. Limits all present and "no probado" kept; NOTICE is the condition, the credit line "se agradece, sin que sea obligatoria"; cuDNN is NVIDIA software, optional, asked once. No added claims found.

## Open points / corrections welcome
- "Hardware test report" (issue form name) stays in English.
- The credit example line is translated ("Basado en ..."); the address stays.
- Variant: neutral international Spanish; native speakers from Spain or Latin America may prefer small word changes (for example "portátil" vs "laptop"). "portátil" was chosen.
- Reader R1 agrees with the register and term choices; no disagreements.

## Round 2
- Round 2: "by default" = "por defecto"; "without payment or sign-in" = "sin que se pida ningún pago ni inicio de sesión" (avoids "gratis"); "we found no clause" = "no encontramos ninguna cláusula"; license sentence kept with "quien no acepte ... no debe descargarlo, instalarlo ni usarlo".
- Reader: es read as faithful and calm, no rule-3 implication; no change needed ("lo omite" is natural).
