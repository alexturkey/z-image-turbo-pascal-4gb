# ខ្មែរ (km): localization notes

Written by: W11 (Sonnet 5.5), 2026-11-14   Read by: R11 (Sonnet 5.5), 2026-11-14   Status: ok (reader is not a native Khmer speaker; low-to-medium confidence, native check welcome)

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: neutral polite written Khmer with no royal or honorific register. The pronoun "អ្នក" (you) is used only where the sentence needs it; most instructions are written without a pronoun ("សូមសាកល្បងវាមុន", "សូមអាន"). Khmer developer pages are mostly written this way and it avoids picking a status level for the reader.
- Register (how technical, how warm): plain, calm, sourced, like the English. Khmer developers mix English technical words into Khmer sentences, so established terms stay in Latin script (repository, build, seed, prompt, tile, VAE, latent, decode, quantization, segment, hash) and Khmer carries the grammar and the explanations. Sentences end with the Khmer full stop "។".

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | អង្គចងចាំ GPU; "VRAM" only inside quotes | Khmer readers say "VRAM" or "memory"; "អង្គចងចាំ" is the standard word for memory. Quotes from the model card keep English VRAM. |
| text-to-image | ការបង្កើតរូបភាពពីអត្ថបទ (text-to-image) | the Khmer phrase first, English term in brackets once |
| tile (VAE tile) | tile | kept in Latin script; no common Khmer word |
| seed | seed | kept in Latin script, as developers write it |
| prompt | prompt | kept in Latin script (also "negative prompt") |
| quantization | quantization | kept in Latin script; no settled Khmer term |
| setup / install | ដំឡើង (install), `setup.py` unchanged | "ដំឡើង" is the usual word for installing software |
| measured / not tested | បានវាស់ / មិនទាន់បានសាកល្បង | "មិនទាន់" ("not yet") says we did not run it; it does not say it fails |
| open source license / NOTICE | អាជ្ញាបណ្ណ (license), `NOTICE` unchanged; "លក្ខខណ្ឌ" (condition) for NOTICE, "ស្វាគមន៍ តែមិនបង្ខំ" (welcome, not forced) for the credit line | the condition/request difference is kept visible |

## Avoided
- Phrases that sound like advertising in this language/culture: superlatives, "ងាយស្រួលបំផុត" (easiest), "ដំបូងគេ" (first), "ល្អបំផុត" (best), "ឥតខ្ចោះ" (flawless).
- Literal translations that read wrongly: "fits comfortably" is not translated as a claim of ours; it stays an English quote with a Khmer explanation. "Not tested" is not softened to "probably fine".

## Formatting
- Numbers and decimal separator: the test requires them unchanged (12.2 stays 12.2; ASCII digits). Khmer-script digits exist but are not used; the text stays in ASCII digits next to units (s, MiB, GB, dB), which Khmer developers also read normally.
- Script issues (right-to-left, line height, no spaces between words, table widths): Khmer has no spaces between words; spaces appear only between phrases. Table cells are kept short. Latin words (commands, terms) sit inside Khmer sentences with a normal space on both sides. Code and file names are in backticks.

## Back-translation check
- First paragraph back into English by the reader: "Z-Image-Turbo (Q8_0 GGUF) text-to-image at 768x1344 on a 4 GB GTX 1050 Ti with stable-diffusion.cpp on Windows; measured on a 16 GB RAM laptop using about 11 GB of RAM; the same seed gives the same pixels, pixel for pixel; results and engine patches are published, downloads are locked with sha256, an AI coding agent can install it step by step. Unofficial, no connection with Tongyi-MAI, leejet or NVIDIA. Differences: none in meaning; no added praise or stronger claim"; the 'once' of the setup time sits oddly in the Khmer word order but the meaning is the same.
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes (back-translated all four; limits list complete with 'not tested' kept as 'មិនទាន់បានសាកល្បង'; NOTICE is a condition and the credit line is welcome-not-forced; cuDNN is NVIDIA's, optional, license typed once as in the code block; unofficial line plain). Reader confidence in Khmer: moderate, not native.

## Open points / corrections welcome
- "ចាក់សោ" (lock) is used for "pinned" (downloads pinned with sha256); a native reader may prefer another word.
- "ទ្រព្យសម្បត្តិរបស់ NVIDIA" for "NVIDIA's property" is legal-sounding; check naturalness.
- The sentence "ទម្រង់បែបបទបញ្ហា" for "issue form" and "ទម្រង់" choices should be checked by a Khmer reader.
- The number slots (`193–228` etc.) and their units (s, MiB) stay as in the English; "29 នាទី" uses the Khmer word for minutes because the English writes the word "minutes".

## Round 2
- Round 2: "by default" = "តាមលំនាំដើម"; "without payment" = "ដោយមិនមានការសុំបង់ប្រាក់" (not the word for free); "sign-in" = "មិនត្រូវការគណនី ឬការចូលប្រើ (sign-in)"; "anyone who" = "អ្នកណាដែល"; "we found no clause" = "យើងរកមិនឃើញខ្សែ...". A Khmer reader may check "ខ្សែ" (clause) for naturalness.
- Round 2 reader fix: "ខ្សែ" (string/line) replaced by "ប្រការ" (clause); "កម្រិត" changed to "ដាក់កម្រិតលើ" (limits on). Rest unchanged.
