# Suomi (fi): localization notes

Written by: W6 writer agent (Sonnet), 2026-11-14   Read by: R6 reader agent (Sonnet), 2026-11-14   Status: ok

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: informal "sinä" (second person singular: "kokeile", "lue", "voit"). Finnish developer READMEs and documentation use sinuttelu; "te" would sound stiff. Many sentences are impersonal ("Sen voi keskeyttää").
- Register (how technical, how warm): plain, calm, sourced, short sentences. Finnish understatement fits the sourced tone; no enthusiasm words. English words stay where Finnish developers use them (patch, build, README), with Finnish case endings.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
| GPU memory (VRAM) | GPU-muisti; "VRAM-muisti" only in the quotes and their explanation | developers say "VRAM" or "näytönmuisti"; one term is used everywhere |
| text-to-image | tekstistä kuvaksi (text-to-image) | explained in the first sentence, then not repeated |
| tile (VAE tile) | laatta (tile) | "laatta" with the English word in parentheses at the first use and in the options table |
| seed | siemenluku (seed) | "siemenluku" is the common Finnish word; the English word in parentheses once |
| prompt | kehote (prompt) | "kehote" is the established Finnish term; "negatiivinen kehote" for negative prompt |
| quantization | kvantisointi | "matalampi kvantisointi" for lower quantization |
| setup / install | asennus | the script name `setup.py` stays unchanged |
| measured / not tested | mitattu / ei testattu | "ei testattu" for "not tested", the same idea everywhere |
| open source license / NOTICE | lisenssi / `NOTICE`-tiedosto | NOTICE is a file name and stays |
| credit | maininta | "ehto" (condition) for NOTICE, "otetaan ilolla vastaan, mutta sitä ei vaadita" (gladly received, not required) for the credit line |
| patch, build, runtime, README, issue | kept in English, with Finnish case endings (patchit, buildin, README:stä) | the way Finnish developers write them |

## Avoided
- Phrases that sound like advertising in this language/culture: "huikea", "mullistava", "helppo", "paras", "kaikille korteille".
- Literal translations that read wrongly: "pixel for pixel" is "pikseli pikseliltä"; "clean root" is kept as "puhdas juuri" (a test name, not a claim).

## Formatting
- Numbers and decimal separator: the test requires them unchanged. Finnish readers would expect a decimal comma (12,2); the text keeps 12.2 and 6.6 and always puts the unit next to the number. Thousands stay as in the English (10 509, 6,577,440,704). Ranges "29.8 to 36.3" are written with an en dash (29.8–36.3). Digits are ASCII. Slots such as `193–228 s` are unchanged; no Finnish case ending is attached to a slot.
- Script issues (right-to-left, line height, no spaces between words, table widths): none. Finnish compounds make some words long; table cells were kept short. Abbreviations with a colon ending (GPU:n, GB:n, sha256:lla) follow Finnish writing rules.

## Back-translation check
- First paragraph back into English by the reader: "Z-Image-Turbo (Q8_0 GGUF) text to image at 768x1344 on a 4 GB GTX 1050 Ti graphics card (Pascal, sm_61), with stable-diffusion.cpp, on Windows. Measured on a laptop with 16 GB RAM where the process uses about 11 GB RAM. The same seed gives the same pixels, pixel by pixel; measurements and engine patches are published, downloads are locked with sha256 hashes, and an AI-assisted coding agent can do the install step by step. Unofficial. Not affiliated with Tongyi-MAI, leejet or NVIDIA."; differences from the English: none of substance
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes (also checked the Unofficial line, cuDNN paragraph, condition vs request, Limits list, all numbers and slots)

## Open points / corrections welcome
- The model card and README quotes stay in English; each has a short Finnish rendering after it.
- The sample credit line "Based on Sınırsız Foto by ..." stays in English because it is a text to copy.
- The form name "Hardware test report" stays in English, as in the Turkish file.
- The first sentence "tekstistä kuvaksi (text-to-image) koossa 768x1344" is a little heavy; a reader may suggest a lighter wording.
- "tislattu (distilled)" for the model's distillation is my choice; some Finnish developers say "distilloitu".
- Reader (R6): no meaning drift, no softened limit, no added claim; NOTICE is "ehto", the credit line "otetaan ilolla vastaan, mutta sitä ei vaadita". The first sentence reads fine to me; "tislattu (distilled)" is acceptable (the parenthesis covers "distilloitu"). No change made to the README.


## Round 2

- Round 2: «by default» = «oletuksena»; «without sign-in» = «ilman kirjautumista tilille»; «without payment» = «ilman, että maksua pyydetään» (not «ilmainen»); «we found no clause» = «lisenssista löytynyt ehtoa» (first person implied in the verb, kept as «emme»-free passive; reader may check).
- Round 2 reader fix: the passive "lisenssista löytynyt ehtoa" dropped the "we"; now explicit: "emmekä löytäneet lisenssista ehtoa". Greek and Finnish otherwise read calm, nothing from rule 3 implied.
