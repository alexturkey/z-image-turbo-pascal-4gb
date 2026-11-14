# Français (fr): localization notes

Written by: W1 (Claude Sonnet 5.5), 2026-11-14   Read by: R1 (Claude Sonnet 5.5), 2026-11-14   Status: ok

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: "vous" (formal plural/polite singular). French open-source READMEs are mostly impersonal or "vous"; "tu" appears in very informal projects. "Vous" is safe for a project that wants to be trusted. Imperatives are soft ("essayez-le d'abord", "fermez les autres programmes").
- Register (how technical, how warm): plain, calm, sourced; no advertising words.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | mémoire GPU; "VRAM" only inside the quotes | French developers say both |
| text-to-image | génération d'images à partir de texte | "texte-vers-image" is used in tools but sounds clumsy in a sentence |
| tile (VAE tile) | tuile | |
| seed | graine | |
| prompt | prompt | the word French developers use; "invite" or "requête" are rare for image models |
| quantization | quantification | |
| setup / install | installation (script name `setup.py` unchanged) | |
| measured / not tested | mesuré / non testé | "non testé" in the limits list, "pas testé" in running text where fitting |
| open source license / NOTICE | licence; fichier `NOTICE` | "condition" for NOTICE, "appréciée, sans être exigée" for the credit line |
| refiner, latent, sampler, scheduler, flash attention, build | kept in English | what developers say |
| not affiliated | Sans lien avec | plain, legal-sounding |

## Avoided
- Phrases that sound like advertising in this language/culture: "incroyable", "facile", "révolutionnaire", "puissant", "sans effort", "performant".
- Literal translations that read wrongly: "Start here" is "Pour commencer"; "At a glance" is "En un coup d'œil"; "Check it yourself" is "Vérifiez par vous-même".

## Formatting
- Numbers and decimal separator: the test requires 12.2, not 12,2; French readers expect a comma, so the point may look English; units sit next to the numbers. Thousands as in the English ("10 509", "6,577,440,704"). Unit symbols are the English ones (GB, not "Go"), as the brief requires; French readers will understand GB, MiB, s, dB.
- Script issues (right-to-left, line height, no spaces between words, table widths): none; Latin script. French typographic spaces before ; : ? ! are written as ordinary spaces (no non-breaking characters, so the invisible-character check stays clean).
- Quotation marks around the cited English sentences are « ... » with ordinary spaces; the English quotes inside stay English.

## Back-translation check
- First paragraph back into English by the reader: "Text-to-image generation with Z-Image-Turbo (Q8_0 GGUF) at 768x1344 on a 4 GB GTX 1050 Ti (Pascal, sm_61), with stable-diffusion.cpp, on Windows. Measured on a laptop with 16 GB RAM, where the process uses about 11 GB. The same seed gives the same pixels, pixel for pixel; measurements and engine patches are published, downloads are pinned by sha256, and an AI coding agent can install it step by step. Unofficial. No link with Tongyi-MAI, leejet or NVIDIA."; differences from the English: none in meaning. One small edit: the gloss of "as little as 4GB of VRAM" was "à partir de" (from 4 GB up) and is now "avec seulement 4 GB".
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes. All limits present, "non testé" kept; NOTICE is the condition, the credit line "appréciée, sans être exigée"; cuDNN is NVIDIA software, optional, asked once. No added claims found.

## Open points / corrections welcome
- "Hardware test report" (issue form name) stays in English.
- The credit example line is translated ("Basé sur ..."); the address stays. The closing quote mark follows a space so the address is not touched.
- "Go" (French for GB) is not used because of the unit rule; a reader may prefer it.
- Reader R1 agrees with the register and term choices; no disagreements.

## Round 2
- Round 2: "by default" = "par défaut"; "without payment or sign-in" = "sans qu'aucun paiement ni aucune connexion ne soit demandé" (avoids "gratuit"); "we found" = "nous n'avons trouvé ... aucune clause"; license sentence kept with "quiconque ... ne doit pas le télécharger, l'installer ni l'utiliser".
- Reader fix: "le passe" (table row and license bullet) replaced by "permet de s'en passer", the natural idiom for skipping something optional; "le passe" read as "hands it over". Everything else read as faithful, calm, no rule-3 implication.
