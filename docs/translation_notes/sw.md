# Kiswahili (sw): localization notes

Written by: W13, 2026-11-14   Read by: R13, 2026-11-14   Status: ok (FIXED)

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: second person singular "wewe" (verbs in the singular: "kijaribu", "mwelekeze", "usome"). Swahili developer documentation from Kenya and Tanzania is usually plain and direct; a polite but not stiff tone. Plural "ninyi" is avoided because the README addresses one reader at a time.
- Register (how technical, how warm): plain, calm, sourced. Swahili has few settled technical words for this field, so developers use English terms (GPU, driver, prompt, seed, engine, build, log) inside Swahili sentences. The same is done here. No advertising words.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | kumbukumbu ya GPU; "VRAM" only inside quotes | model-card quotes stay English |
| text-to-image | kutengeneza picha kutoka kwa maandishi (text-to-image) | Swahili phrase first, English term in brackets once |
| tile (VAE tile) | tile | kept English |
| seed | seed | kept English |
| prompt | prompt | kept English |
| quantization | quantization | kept English; no settled Swahili term |
| setup / install | usakinishaji / kusakinisha; `setup.py` unchanged | heading "Kuanza haraka" (quick start) |
| measured / not tested | imepimwa / haijajaribiwa | "haijajaribiwa" says we did not run it |
| open source license / NOTICE | leseni; the `NOTICE` file in backticks | condition = "sharti", request = "unakaribishwa kwa shukrani, lakini si wa lazima" |
| picture / image | picha | same word everywhere |
| unofficial | si rasmi | |
| repository | hazina | "repo" avoided in prose; "hazina" is the common Swahili rendering |
| pixel | pikseli | |

## Avoided
- Phrases that sound like advertising in this language/culture: "bora kabisa", "haraka sana", "rahisi", "ya kipekee", "mapinduzi".
- Literal translations that read wrongly: "everything is open" is "kila kitu kiko wazi" (open to see and change), not "bure" (free of charge). "Not real photographs" is "si picha halisi za kamera" so that "picha" (picture) is not confused with a camera photograph.

## Formatting
- Numbers and decimal separator: the test requires them unchanged (12.2 stays 12.2; ASCII digits). Swahili readers in Kenya and Tanzania commonly write a decimal point or comma; the point is understood. Slots such as `193–228 s` and "dakika 29" keep the slot as written.
- Script issues (right-to-left, line height, no spaces between words, table widths): none (Latin script). Swahili words are long; table cells kept short.

## Back-translation check
- Back-translation: 'Text-to-image with Z-Image-Turbo (Q8_0 GGUF) at 768x1344 on a 4 GB GTX 1050 Ti ... Measured on a 16 GB RAM laptop, process uses about 11 GB. Same seed gives same pixels; measurements and engine patches are open; downloads pinned with sha256; an AI coding agent can install it step by step. Unofficial, no relation to Tongyi-MAI, leejet or NVIDIA.' No differences from the English.
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes

## Open points / corrections welcome
- Technical words are mostly English (see above); a Swahili reader may prefer more Swahili terms for "kuendesha", "kupakua", "kujenga".
- "Wakala wa AI wa kuandika msimbo" for "AI coding agent" is a descriptive phrase; "AI coding agent" in English might be what readers search for.
- "Ukurasa huu umetafsiriwa" in the last line says "translated"; "umesanifiwa kwa lugha yako" (adapted) would be closer to localization, reader to decide.
- Reader (R13): changed 'mkimbio' (a run, reads as a sprint) to 'uendeshaji' (running/execution) in 5 places; the rest is unchanged. 'muundo' is used for both 'build' and 'architecture' (minor, left). 'umetafsiriwa' in the last line is acceptable.

## Round 2
- Round 2 (K-21): "by default" = "kwa chaguo-msingi"; "without payment" = "bila kuombwa malipo" (not "bure"); "without sign-in" = "bila kuingia (hakuna akaunti wala login inayohitajika)"; "we found no clause" = "hatukupata kifungu chochote". NVIDIA's sentence kept with "hapaswi kuipakua, kuisakinisha wala kuitumia".
- Reader (Round 2): changed "bila kuingia (hakuna akaunti wala login inayohitajika)" to "bila kuingia kwenye akaunti (hakuna akaunti inayohitajika)" ("login" loanword unnatural/redundant); changed "hapaswi" (ought not, too soft) to "haruhusiwi" (is not permitted, the license-rule force of "must not"). "yeyote" is fine. Other two lines checked, no change.
