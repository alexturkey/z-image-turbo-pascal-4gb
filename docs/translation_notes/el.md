# Ελληνικά (el): localization notes

Written by: W6 writer agent (Sonnet), 2026-11-14   Read by: R6 reader agent (Sonnet), 2026-11-14   Status: ok

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: informal singular ("εσύ": "δοκίμασέ το", "διάβασέ τα"). Greek open-source READMEs and tutorials mostly speak to one developer in the singular; the plural/polite form reads like a bank or a ministry. Where possible the text avoids pronouns altogether.
- Register (how technical, how warm): plain, calm, sourced; modern demotic Greek, no katharevousa. A little warm in "Start here" and "Contributing", dry in measurements and limits. No advertising words.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
| GPU memory (VRAM) | μνήμη GPU; "VRAM" only in the quotes and their explanation | Greek developers say "VRAM" or "μνήμη της κάρτας γραφικών"; "μνήμη GPU" is short and stays the same everywhere |
| text-to-image | text-to-image (παραγωγή εικόνας από κείμενο) | explained once in the first sentence, then the English term as developers say it |
| tile (VAE tile) | tile | kept in English; "πλακίδιο" is rare among developers |
| seed | seed | kept in English; "σπόρος" sounds odd to developers |
| prompt | prompt | kept in English (plural "prompts") |
| quantization | κβαντισμός | the usual Greek technical word; "χαμηλότερος κβαντισμός" for lower quantization |
| setup / install | εγκατάσταση | the script name `setup.py` stays unchanged |
| measured / not tested | μετρήθηκε / δεν δοκιμάστηκε | "δεν δοκιμάστηκε" says we did not run it, as in the English "not tested" |
| open source license / NOTICE | άδεια χρήσης / αρχείο `NOTICE` | "άδεια" for license; NOTICE stays as a file name |
| patch, build, driver, server, script | kept in English (patches, build, driver) | the way Greek developers write them in running text |
| credit | πίστωση | "προϋπόθεση" (condition) for NOTICE, "ευπρόσδεκτη, αλλά δεν απαιτείται" (welcome, not required) for the credit line |

## Avoided
- Phrases that sound like advertising in this language/culture: "εντυπωσιακό", "επαναστατικό", "απλά και εύκολα", "ό,τι καλύτερο", "για κάθε κάρτα".
- Literal translations that read wrongly: "χωράει άνετα" appears only inside the explanation of the English quote; "clean root" is rendered "καθαρή ρίζα" as a test name, not as a claim.

## Formatting
- Numbers and decimal separator: the test requires them unchanged. Greek readers would expect a decimal comma (12,2); the text keeps 12.2 and 6.6 and always puts the unit next to the number, so it stays clear. Ranges "29.8 to 36.3" are written "29.8 έως 36.3". Digits are ASCII. Slots such as `193–228 s` are unchanged.
- Script issues (right-to-left, line height, no spaces between words, table widths): none; Greek has spaces and normal line height.
- The heading "Check it yourself" became "Επαλήθευση" (verification) because "do it yourself" needs a gendered form in Greek.

## Back-translation check
- First paragraph back into English by the reader: "Z-Image-Turbo (Q8_0 GGUF) text-to-image at 768x1344 on a GTX 1050 Ti 4 GB card (Pascal, sm_61), with stable-diffusion.cpp, on Windows. Measured on a laptop with 16 GB RAM, where the process uses about 11 GB RAM. The same seed gives the same pixels, pixel by pixel; measurements and engine patches are published, downloads are pinned with sha256 and an AI coding assistant can do the install step by step. Unofficial. Not connected with Tongyi-MAI, leejet or NVIDIA."; differences from the English: none of substance
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes (also checked the Unofficial line, cuDNN paragraph, condition vs request, Limits list, all numbers and slots)

## Open points / corrections welcome
- The model card and README quotes stay in English; each has a short Greek rendering after it ("δηλαδή ...").
- The sample credit line "Based on Sınırsız Foto by ..." stays in English because it is a text to copy.
- The form name "Hardware test report" stays in English, as in the Turkish file.
- The heading "Με μια ματιά" and the link-line labels ("Patches", "Prompts") are my choice; a reader may prefer "Επιδιορθώσεις" for patches.
- The final sentence says "μεταφράστηκε και προσαρμόστηκε" (translated and adapted); a reader may prefer "τοπικοποιήθηκε".
- Reader (R6): no meaning drift, no softened limit, no added claim; NOTICE is "προϋπόθεση" and the credit line "ευπρόσδεκτη, αλλά δεν απαιτείται". Agree with the writer choices; "Επιδιορθώσεις" for patches is not needed (patches is what Greek developers write). "μεταφράστηκε και προσαρμόστηκε" is fine. No change made to the README.


## Round 2

- Round 2: «by default» = «από προεπιλογή»; «without sign-in» = «χωρίς σύνδεση σε λογαριασμό»; «without payment» = «χωρίς να ζητηθεί πληρωμή» (not «δωρεάν»); «we found no clause» = «δεν βρήκαμε στην άδεια όρο».
- Round 2 reader (el): pieces 1-3 and the two script-changed lines checked, no change needed.
