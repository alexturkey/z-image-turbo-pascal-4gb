# Polski (pl): localization notes

Written by: W5 (Sonnet 5.5), 2026-11-14   Read by: R5 (Sonnet 5.5), 2026-11-14   Status: ok

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: informal "ty" (verbs in the imperative and 2nd person: "wypróbuj", "zamknij", "przeczytałeś"). Polish open-source READMEs mostly address the reader as "ty" or use impersonal forms; "Pan/Pani" would sound like a bank. The one gendered past form ("przeczytałeś") in the cuDNN bullet was replaced by the impersonal "zapoznano się z jej treścią" by the reader.
- Register: plain technical, calm, sourced; no exclamations, no marketing words.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | pamięć GPU; "pamięć graficzna" only in the translated quotes | Polish developers say "VRAM" and "pamięć karty graficznej"; "pamięć GPU" matches nvidia-smi |
| text-to-image | generowanie obrazów z tekstu | |
| tile (VAE tile) | kafelek | "tile" is also used in speech; "kafelek" is the Polish form used in graphics |
| seed | seed | Polish developers say "seed" (ziarno is rare) |
| prompt | prompt | "polecenie" would be confused with a command |
| quantization | kwantyzacja | |
| setup / install | instalacja (script name `setup.py` unchanged) | |
| measured / not tested | zmierzono / nie testowano | "nie testowano" is the usual Polish phrase for "we did not run it" |
| open source license / NOTICE | licencja; plik `NOTICE` | NOTICE is a condition ("warunek"), the credit line a request ("prośba") |
| refiner | refiner | kept in Latin |
| latent | latent | kept in Latin |
| patch | łatka | "patch" also used; one word kept |

## Avoided
- Phrases that sound like advertising in this language/culture: "rewolucyjny", "najlepszy", "niesamowity", "łatwy", "bez wysiłku", "błyskawiczny".
- Literal translations that read wrongly: "gotowa paczka" is acceptable; "uczciwe ograniczenie" kept for "Honest limit" (said plainly, not as a boast).

## Formatting
- Numbers and decimal separator: the test requires them unchanged (12.2 stays 12.2; ASCII digits). Polish readers expect a comma (12,2); the text copes because every number carries a unit and sits in tables or next to a command. Units s, MiB, GB, dB stay Latin as the brief requires. Ranges are written "X do Y" in tables and "X–Y" with an en dash in long sentences where "do ... do" would be ambiguous. Slots `{{...}}` untouched.
- Script issues (right-to-left, line height, no spaces between words, table widths): none; Polish words are longer than English, table cells were kept short.

## Back-translation check
- First paragraph back into English by the reader: "Text-to-image generation with Z-Image-Turbo (Q8_0 GGUF) at 768x1344 on a GTX 1050 Ti with 4 GB (Pascal, sm_61), via stable-diffusion.cpp, on Windows. Measured on a 16 GB RAM laptop; the process uses about 11 GB RAM. Same seed, same pixels; measurements and patches published, downloads pinned by sha256, an AI coding agent can do the install step by step. Unofficial project, not affiliated with Tongyi-MAI, leejet or NVIDIA."; differences from the English: none in meaning. Quick start, limits (all 9 items, 'nie testowano' kept) and license (NOTICE = warunek, credit = prosba, cuDNN = NVIDIA's, optional) also back-translated: no drift, no added claims.
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes

## Open points / corrections welcome
- "Hardware test report" (issue form name) stays in English, as in tr.
- "RAM-u" is colloquial-technical.
- Whether to write "ty" in lowercase everywhere (kept).

## Round 2
- "By default" chosen as the plain adverbial phrase of the language; "without payment or sign-in" rendered as "no payment requested, no account login" (not the everyday word for free). "We found no clause" kept with "we". The license sentence is attributed to NVIDIA's license and keeps "must not" with all three verbs.
- Reader fix: "nie może jej pobierać" -> "nie może go pobierać" ("jej" pointed back at the license; "go" is cuDNN). "kto" kept as the whoever form.
