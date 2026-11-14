# Hindi (hi): localization notes

Written by: W12, 2026-11-14   Read by: R12, 2026-11-14   Status: ok

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: "आप" (polite plural, verb forms such as "आज़माएँ", "देखें"). Indian developer READMEs and docs use "आप"; "तुम" would sound too familiar, "तू" rude. Imperatives are the short polite forms (-एँ/-ें), which read as suggestions.
- Register (how technical, how warm): Devanagari developer register, plain and calm. Hindi sentence frame with the English technical terms kept in Latin script where Indian developers say them (prompt, seed, tile, patch, build, driver, GPU, RAM, VAE, latent). No Sanskritized words where an English term is normal (no "संकेत-पंक्ति" for prompt).

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | GPU मेमोरी; "VRAM" only inside the quotes | Indian developers say "GPU memory" or "VRAM"; quotes stay English |
| text-to-image | text-to-image (टेक्स्ट से इमेज बनाना) | English term first, one-time Hindi gloss in the title block; "इमेज" in prose near the term, "तस्वीर" for pictures |
| tile (VAE tile) | tile | not translated; "टाइल" would be unfamiliar in ML context |
| seed | seed | not translated |
| prompt | prompt | not translated; also in "negative prompt" |
| quantization | quantization | not translated |
| setup / install | इंस्टॉल / `setup.py` | "इंस्टॉल" is what readers say; "सेटअप" for the other-people's-setups bullet |
| measured / not tested | मापा गया / आज़माए नहीं गए | "आज़माए नहीं गए" says "not tried", like "not tested"; never softened |
| open source license / NOTICE | लाइसेंस / `NOTICE` फ़ाइल | NOTICE is a "शर्त" (condition); the credit line is "स्वागत है, पर ज़रूरी नहीं" |
| unofficial | अनौपचारिक (unofficial) | plain, English word kept in brackets so the legal sense is not lost |
| steps / segment / refiner / sampler | kept in Latin | "steps" for diffusion steps, "कदम" only for the numbered decision tree step ("दूसरा कदम") |

## Avoided
- Phrases that sound like advertising in this language/culture: "बेहतरीन", "शानदार", "क्रांतिकारी", "आसान", "बिना किसी झंझट के", "जादुई".
- Literal translations that read wrongly: "fits comfortably" is not rendered as a claim; it stays a quote with a short gloss. "Pixel for pixel" is "पिक्सल दर पिक्सल".

## Formatting
- Numbers and decimal separator: kept exactly as in English (12.2, 261.6, 10 509); ASCII digits 0-9 only, no Devanagari digits (Hindi readers in tech use Western digits anyway). Units s, MiB, GB, dB stay Latin next to the slot (`193–228 s`).
- Script issues (right-to-left, line height, no spaces between words, table widths): none for Devanagari; words are space-separated. The sentence-ending mark is the danda "।" in prose; it is not used after code, commands or inside the quoted English. One exception kept English by design: the credit sentence "Based on ..." and the form name "Hardware test report".

## Back-translation check
- First paragraph back into English by the reader: Z-Image-Turbo (Q8_0 GGUF) text-to-image (making images from text) at 768x1344 on a 4 GB GTX 1050 Ti (Pascal, sm_61) with stable-diffusion.cpp on Windows. Measured on a 16 GB RAM laptop where the process uses about 11 GB RAM. The same seed gives the same pixels, pixel by pixel; measurements and engine patches are public, downloads are pinned with sha256, and an AI coding agent can install it step by step. Unofficial; no affiliation with Tongyi-MAI, leejet or NVIDIA. Differences from the English: none of substance; quick start, limits (all 9 items, 'not tested' kept) and license (NOTICE a condition, credit line welcome but not required; cuDNN optional, NVIDIA's, asked once) match the English. Slots and numbers intact.
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes (all four sections back-translated and compared)

## Open points / corrections welcome
- "text-to-image" is kept in English because that is what Indian developers search for; a Hindi gloss appears once. Reader may judge whether the gloss is natural.
- The mix of "तस्वीर" (picture) and "इमेज" (image): "इमेज" only in the title block and PSNR section where it is the technical object; check consistency.
- Sentence about steps: "दूसरा कदम" for the numbered tree vs "steps" for diffusion steps; deliberately different words for different things.
- Reader R12: Naturalness is good: 'आप', English tech terms kept, no advertising words. 'मापें' as a noun for 'measurements' is slightly unusual (some readers say 'माप' or 'मापन'); left as is, consistent across the file.

## Round 2

- Round 2: "by default" is "डिफ़ॉल्ट रूप से"; "without payment" is "बिना किसी भुगतान की माँग" (no payment is asked), deliberately not "मुफ़्त"; "without sign-in" is "बिना साइन-इन के" (no account, no login); "we found no clause" is "हमें ... कोई धारा नहीं मिली". The NVIDIA sentence keeps "लिखा है" (attributed) and "नहीं करना चाहिए" (a rule stated in the license) with all three verbs.
- Round 2 reader fix: "नहीं करना चाहिए" only means "should not" (advice); changed to "करना मना है" (is prohibited) so the license rule keeps the force of "must not". Lines with 8–16 s and 581.29 read fine, unchanged.
