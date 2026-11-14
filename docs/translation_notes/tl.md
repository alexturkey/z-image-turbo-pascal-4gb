# Tagalog (tl): localization notes

Written by: W13, 2026-11-14   Read by: R13, 2026-11-14   Status: ok (PASSED)

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: informal "mo / ka" (second person singular, no "po"). Filipino developer READMEs and docs are usually written in a friendly, direct register; "po" would sound like customer service. Imperatives are softened with "subukan mo", "ituro mo".
- Register (how technical, how warm): plain, calm, sourced. Many technical words stay in English the way Filipino developers write them (Taglish): the sentence frame is Tagalog, the technical nouns are English. No advertising words.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | memorya ng GPU; "VRAM" only inside quotes | readers say "VRAM" or "GPU memory"; the quotes from the model card stay English, so VRAM appears there |
| text-to-image | text-to-image | readers use the English term; the long Tagalog phrase "paglikha ng larawan mula sa teksto" sounds stiff |
| tile (VAE tile) | tile | kept English; "tile" has no common Tagalog developer word |
| seed | seed | kept English |
| prompt | prompt | kept English |
| quantization | quantization | kept English |
| setup / install | pag-install (heading "Mabilis na pag-install"); `setup.py` unchanged | |
| measured / not tested | nasukat / hindi pa nasubukan | "hindi pa nasubukan" says we did not run it, not that it fails |
| open source license / NOTICE | lisensya; the `NOTICE` file is kept in backticks | condition = "kondisyon", request = "malugod na tatanggapin, ngunit hindi kinakailangan" |
| picture / image | larawan | same word everywhere |
| unofficial | hindi opisyal | |

## Avoided
- Phrases that sound like advertising in this language/culture: "pinakamahusay", "napakabilis", "madali lang", "walang kapantay", "rebolusyonaryo".
- Literal translations that read wrongly: "comfortably fits" was not turned into a boast; it is kept as an English quote plus a plain explanation. "Open" in "everything is open" is "bukas" (open to use and change), not "libre".

## Formatting
- Numbers and decimal separator: the test requires them unchanged (12.2 stays 12.2; ASCII digits). Filipino readers write the decimal point as a point, so no conflict. Slots such as `193–228 s` are kept exactly with the unit.
- Script issues (right-to-left, line height, no spaces between words, table widths): none (Latin script). Tagalog words are long, so table cells were kept short.

## Back-translation check
- Back-translation: 'Z-Image-Turbo text-to-image at 768x1344 on a 4 GB GTX 1050 Ti ... measured on a 16 GB RAM laptop, process uses about 11 GB. Same seed gives same pixels; measurements and patches open; downloads pinned with sha256; an AI coding agent can install it step by step. Unofficial, not affiliated with Tongyi-MAI, leejet or NVIDIA.' No differences from the English.
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes

## Open points / corrections welcome
- "pixel por pixel" uses the Spanish-derived "por" that is common in Filipino speech; a reader may prefer "bawat pixel".
- The Taglish balance (English technical nouns, Tagalog frame) is a judgement; readers from the Philippines are asked to confirm.
- "Isinalokal" (localized) in the last line is a formal word; "isinalin" (translated) would be less exact.
- Reader (R13): agree with the notes; 'pixel por pixel' is acceptable Taglish, no change. No claim drift found; cuDNN (NVIDIA's, optional, asked once) and NOTICE condition vs credit request are intact.

## Round 2
- Round 2 (K-21): "by default" = "bilang default" (ini-install); "without payment" = "nang hindi humihingi ng bayad" (not "libre"); "without sign-in" = "walang sign-in (hindi kailangan ng account o login)"; "we found no clause" = "wala kaming nakitang sugnay". NVIDIA's own sentence kept as "hindi dapat mag-download, mag-install o gumamit".
- Reader (Round 2): "sinumang" is natural for "whoever"; "sign-in"/"login" loanwords are common in Filipino tech writing and understood, left unchanged. Line "8–16 s" and "One card, one machine" checked, no change.
