# עברית (he): localization notes

Written by: W7 (Sonnet 5.5), 2026-11-14   Read by: R7 (Sonnet 5.5), 2026-11-14   Status: ok (FIXED, one word)

## Address and tone
- Form of address: plural "you" (אתם) and impersonal forms ("כדאי לנסות", "הריצו", "ראו"). Hebrew developer READMEs avoid the gendered singular; the plural imperative is the neutral, friendly norm, and impersonal sentences are used where the plural would sound forced.
- Register: plain, technical, Israeli developer usage: many English terms written in Latin with a Hebrew prefix and hyphen (ה-seed, ב-float32, ל-GPU). Calm, sourced, no marketing.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | זיכרון GPU | "VRAM" only inside the quotes of the model card / README |
| text-to-image | יצירת תמונות מטקסט | |
| tile (VAE tile) | אריח (tile) | first use gets "(tile)" |
| seed | seed | Israeli developers say "seed"; kept in Latin with ה- prefix |
| prompt | פרומפט | standard in Hebrew developer speech; negative prompt = פרומפט שלילי |
| quantization | קוונטיזציה | |
| setup / install | התקנה | `setup.py` unchanged |
| measured / not tested | נמדד / לא נבדק | "לא נבדק" = not tried; never "נכשל" |
| open source license / NOTICE | רישיון / קובץ `NOTICE` | "התנאי" (condition) for NOTICE vs "תתקבל בברכה, אך אינה חובה" for the credit line |
| refiner, sampler, scheduler, latent, flash attention | kept in Latin | what Israeli developers write |
| unofficial | לא רשמי | |
| landmarks | אתרי ציון | |

## Avoided
- Advertising words (מדהים, מהפכני, קל מאוד, הכי מהיר, הכי טוב); none added.
- A literal translation of "fits comfortably" as our claim: quote stays English with a Hebrew gloss.
- Niqqud (vowel marks); gendered singular address.

## Formatting
- Numbers: unchanged from English (12.2, 261.6, 6,577,440,704, "10 509"), ASCII digits and decimal point, as the check requires; Hebrew readers already use the point and ASCII digits, no conflict.
- Script issues: right-to-left. Commands, files and flags are in backticks, one per phrase, with a hyphen prefix next to Latin words (ה-README, ב-`patches/`). No bidi marks were inserted; mixed lines were rephrased instead. Tables keep Latin version numbers (v0.1.0, v0.2.0) and the units next to digits.
- Number slots `{{...}}` and their unit are plain text, unchanged.

## Back-translation check
- First paragraph back into English by the reader: "Image generation from text with Z-Image-Turbo (Q8_0 GGUF) at 768x1344 on a GTX 1050 Ti with 4 GB (Pascal, sm_61), using stable-diffusion.cpp, on Windows. Measured on a laptop with 16 GB RAM, where the process uses about 11 GB of memory. Same seed gives the same pixels. Measurements and engine patches published, downloads pinned with sha256, an AI coding agent can do the install step by step. Not official. No connection to Tongyi-MAI, leejet or NVIDIA."; differences from the English: none of substance.
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes (back-translated; limits, "not tested", NOTICE condition vs credit request, NVIDIA cuDNN paragraph and numbers all intact)

## Open points / corrections welcome
- Reader to judge: Latin "seed" versus Hebrew "זרע"; "אריח" for tile; "טלאים" for patches (used with "(patches)" once in the first paragraph).
- Prefix hyphen before backticks (ב-`patches/`) and before Latin words: check the rendering.
- The opening of the first paragraph is one very long bold sentence, as in English; the reader can consider splitting it.
- Reader (R7): no changes. "seed", "אריח", "טלאים" are fine. Minor: "ייחוס" is used both for the reference decode and for attribution (the English uses "reference" and "credit"); acceptable in context, no change.

## Round 2
- Round 2: "by default" = "כברירת מחדל"; "without payment or sign-in" = "בלי שמבקשים תשלום ובלי חשבון או התחברות" (avoids "בחינם"); "we found no clause" = "לא מצאנו ... שום סעיף"; license sentence = "הרישיון של NVIDIA אומר שמי שאינו מקבל את תנאיו אסור לו להוריד, להתקין או להשתמש בו".
- Reader round 2 (he): no changes; license URL identical to English; "One card, one machine" and 8-16 s lines fine.
