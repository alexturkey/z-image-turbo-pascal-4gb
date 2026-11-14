# မြန်မာ (my): localization notes

Written by: W11 (Sonnet 5.5), 2026-11-14   Read by: R11 (Sonnet 5.5), 2026-11-14   Status: ok (reader is not a native Burmese speaker; low-to-medium confidence, native check welcome)

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: polite spoken-written style ending in "ပါတယ်", the style Myanmar developer blogs, community tech pages and tutorials use. The literary "သည်/၏" style would read stiff and old-fashioned in a README. The pronoun "သင်" is used rarely; "ကျွန်တော်တို့" (we, polite male form) is used for the authors, as the project voice. Instructions use the polite particle "ပါ" ("အရင်စမ်းကြည့်ပါ").
- Register (how technical, how warm): plain, calm, sourced. Myanmar developers keep English technical words in Latin script (repository, build, seed, prompt, tile, VAE, latent, decode, quantization, segment, hash, option) and write the grammar in Burmese, so this README does the same.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | GPU မှတ်ဉာဏ်; "VRAM" only inside quotes | "မှတ်ဉာဏ်" is the common word for memory (also used for RAM: "RAM"/"system မှတ်ဉာဏ်") |
| text-to-image | စာသားမှ ပုံဖန်တီးခြင်း (text-to-image) | Burmese phrase first, English term in brackets once |
| tile (VAE tile) | tile | kept in Latin script |
| seed | seed | kept in Latin script |
| prompt | prompt | kept in Latin script |
| quantization | quantization | kept in Latin script; no settled Burmese term |
| setup / install | တပ်ဆင်ခြင်း (install), `setup.py` unchanged | "တပ်ဆင်" is the usual word for installing |
| measured / not tested | တိုင်းတာ / မစမ်းရသေးပါ | "မစမ်းရသေးပါ" (not tried yet) says we did not run it, not that it fails |
| open source license / NOTICE | လိုင်စင်, `NOTICE` unchanged; "စည်းကမ်းချက် (condition)" for NOTICE, "ကျေးဇူးတင်ပါတယ်၊ မဖြစ်မနေ မလိုပါ" (appreciated, not required) for the credit line | the condition/request difference is kept visible |

## Avoided
- Phrases that sound like advertising in this language/culture: "အကောင်းဆုံး" (best), "ပထမဆုံး" (first), "လွယ်ကူ" (easy), "အံ့ဩစရာ" (amazing), "အာမခံ" (guaranteed).
- Literal translations that read wrongly: the model-card sentence stays in English with a Burmese explanation; "not tested" is never turned into "should work".

## Formatting
- Numbers and decimal separator: the test requires them unchanged (12.2 stays 12.2; ASCII digits). Burmese-script digits exist and readers would also accept them, but the file uses only 0-9 next to units (s, MiB, GB, dB); one stray Burmese digit was caught and fixed during writing.
- Script issues (right-to-left, line height, no spaces between words, table widths): Burmese has no spaces between words and needs generous line height (left to the renderer); sentences are kept short, table cells short. Burmese uses "။" as full stop; in this file sentences end with "ပါတယ်။"-type endings or "။" where natural, and a few lines end without it where the line is a list/table item. Latin words sit inside Burmese sentences with a normal space.

## Back-translation check
- First paragraph back into English by the reader: "Z-Image-Turbo (Q8_0 GGUF) text-to-image at 768x1344 on a 4 GB GTX 1050 Ti with stable-diffusion.cpp on Windows; measured on a 16 GB RAM laptop using about 11 GB of RAM; the same seed gives the same pixels, pixel for pixel; results and engine patches are published, downloads are locked with sha256, an AI coding agent can install it step by step. Unofficial, no connection with Tongyi-MAI, leejet or NVIDIA. Differences: none in meaning; no added praise or stronger claim"; none in meaning (the pin word is a loan 'ပင်ထားပါတယ်', understandable to developers).
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes (back-translated all four; limits list complete, 'not tested' kept as 'မစမ်းရသေးပါ'; NOTICE is a 'စည်းကမ်းချက် (condition)' and the credit line is appreciated-not-required; cuDNN is NVIDIA's software, optional; unofficial line plain). Reader confidence in Burmese: moderate, not native.

## Open points / corrections welcome
- Colloquial "ပါတယ်" versus literary "ပါသည်": chosen colloquial for developer READMEs; a reader may disagree.
- "ရိုးရိုးသားသား ကန့်သတ်ချက်" for "Honest limit" and "ဒေသအလိုက် ပြင်ဆင်ထားတာ" for "localized" may need a better word.
- "ပြင်ပအဖွဲ့" for "third-party" is used in the link label and body; check that it is the word developers use.
- The number slots (`193–228` etc.) and their units (s, MiB) stay as in the English; "29 မိနစ်" uses the Burmese word for minutes because the English writes the word "minutes".

## Round 2
- Round 2: "by default" = "မူလအတိုင်း"; "without payment" = "ငွေပေးချေဖို့ မတောင်းဘဲ" (not the word for free); "sign-in" = "account သို့မဟုတ် sign-in မလိုဘဲ"; "anyone who does not accept" = "မလက်ခံသူတွေ"; "we found no clause" = "ပုဒ်မ ကျွန်တော်တို့ မတွေ့ခဲ့ပါဘူး". My wording for "commercial or personal use" (ကူးသန်းရောင်းချမှု / ကိုယ်ပိုင်အသုံးပြုမှု) deserves a native check.
- Round 2 reader fix: "ကူးသန်းရောင်းချမှု" (trading/selling) replaced by "စီးပွားရေးအတွက်ဖြစ်စေ ကိုယ်ပိုင်အတွက်ဖြစ်စေ" (for business or for personal purposes); "ပုဒ်မ" kept for clause.
