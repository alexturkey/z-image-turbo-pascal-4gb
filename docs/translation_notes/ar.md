# العربية (ar): localization notes

Written by: W7 (Sonnet 5.5), 2026-11-14   Read by: R7 (Sonnet 5.5), 2026-11-14   Status: ok (FIXED, one word)

## Address and tone
- Form of address: impersonal and singular second person ("جرّبها", "ضع النماذج", "يمكنك"), no plural "you" and no honorifics. Arabic developer READMEs (GitHub, technical blogs) use a plain direct imperative or an impersonal passive; this matches the calm, sourced tone of the English.
- Register: Modern Standard Arabic for developers, technical but not literary. Latin technical terms stay where Arab developers write them in Latin (GPU, RAM, SSD, VAE, latent, sampler, scheduler, flash attention, patches in parentheses once).

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | ذاكرة GPU | "VRAM" kept only in quotes of the model card / README |
| text-to-image | توليد الصور من النص | |
| tile (VAE tile) | بلاطة (tile) | first use in the table gets "(tile)"; "تقسيم/مربع" is also seen, "بلاطة" is closest to the literal and consistent |
| seed | البذرة (seed) | first use with the English in brackets |
| prompt | الموجّه (prompt) | "البرومبت" is common in chat but less fitting in a document; negative prompt = موجّه سلبي |
| quantization | التكميم (quantization) | |
| setup / install | التثبيت | script name `setup.py` unchanged |
| measured / not tested | قِيس / لم يُختبر | "لم يُختبر" says not run, not "measured and failed" |
| open source license / NOTICE | ترخيص / ملف `NOTICE` | "الشرط" (condition) for NOTICE vs "موضع تقدير، وليس مطلوبًا" (appreciated, not required) for the credit line |
| refiner | المحسِّن (refiner) | |
| unofficial | غير رسمي | |

## Avoided
- Advertising phrases (رائع، مذهل، ثوري، سهل جدًا، الأسرع، الأفضل); none added.
- Literal "fits comfortably" translation as our claim: the quote stays English with a plain Arabic gloss.
- Diacritics (tashkeel) except where ambiguity would arise; no tatweel.

## Formatting
- Numbers: kept as in English (12.2, 261.6, 6,577,440,704, "10 509"), ASCII digits 0-9 and a decimal point, as the machine check requires. Readers in some countries would expect Arabic-Indic digits or a decimal comma; the text copes by always attaching the Latin unit (s, MiB, GB, dB) and keeping numbers inside tables or next to Latin words.
- Script issues: right-to-left. Commands, file names, flags are in backticks, one per phrase; sentences around them are short. No bidi marks were inserted (a stray RLM was removed after writing). The code blocks, inline code and the language bar are left-to-right content inside an RTL page and rely on the Unicode bidi algorithm. The heading "نظرة سريعة" etc. are short.
- Number slots `{{...}}` and their unit (`193–228 s`) are plain text, unchanged, unspaced.

## Back-translation check
- First paragraph back into English by the reader: "Text-to-image with Z-Image-Turbo (Q8_0 GGUF) at 768x1344 on a GTX 1050 Ti with 4 GB (Pascal, sm_61), via stable-diffusion.cpp and on Windows. Measured on a laptop with 16 GB RAM; the process uses about 11 GB of memory. The same seed gives the same pixels, pixel by pixel. Measurements and engine patches are published, downloads are pinned by sha256, and an AI coding agent can run the install step by step. Unofficial. No connection to Tongyi-MAI, leejet or NVIDIA."; differences from the English: none of substance (the "Unofficial" line is plain, all limits kept).
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes (back-translated; limits, "not tested", NOTICE condition vs credit request, NVIDIA cuDNN paragraph and numbers all intact)

## Open points / corrections welcome
- Reader to judge: "بلاطة" for tile versus a plain English "tile"; "الموجّه" for prompt versus "البرومبت"; "المعالم" for landmarks.
- "بيئة CUDA" for "CUDA runtime" (runtime = بيئة التشغيل); check it reads naturally.
- Mixed-direction lines (the table with Latin version numbers, `stages.vae_path` list) should be checked visually in a renderer.
- Reader (R7): changed "المُعاين" (reads as "inspector") to "أداة أخذ العينات (sampler)" and "المجدوِل" to "الجدولة (scheduler)" in the sentence after the options table. Terms table: sampler/scheduler follow that wording. "بلاطة", "الموجّه", "المعالم", "بيئة CUDA" read naturally; no change.

## Round 2
- Round 2: "by default" = "افتراضيًا"; "without payment or sign-in" = "دون طلب أي دفع ودون حساب أو تسجيل دخول" (avoids "مجانًا"); "we found no clause" = "لم نجد ... أي بند"; license sentence = "ويقول ترخيص NVIDIA إن من لا يقبل شروطه فلا يجوز له تنزيله ولا تثبيته ولا استخدامه".
- Reader round 2 (ar): fixed number agreement "ثماني ملفات" -> "ثمانية ملفات" (piece 1). "و" in the "One card, one machine" line reads correctly, no change. License URL identical to English in both files. he: no changes.
