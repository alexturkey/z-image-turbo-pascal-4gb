# 한국어 (ko): localization notes

Written by: W9 (Claude Sonnet 5.5), 2026-11-14   Read by: R9 (Claude Sonnet 5.5), 2026-11-14   Status: ok (FIXED, one small correction)

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: formal polite (합니다체 for statements, 하세요 for instructions). Korean open-source READMEs and docs for a public audience are usually written in 합니다/하세요 or 해요; 합니다체 keeps the calm, sourced tone and avoids both bluntness (반말) and chatty warmth. The reader is addressed lightly ("내 GPU", "내 카드"), subject pronouns (당신) are dropped as usual in Korean.
- Register (how technical, how warm): plain technical, calm, not promotional. Instructions are polite requests ("먼저 그것을 써 보세요"), limits are stated flatly.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | GPU 메모리; "VRAM" only inside the English quotes | Korean developers say both VRAM and GPU 메모리; quotes stay English so VRAM appears there |
| text-to-image | 텍스트-이미지 변환 | "텍스트 투 이미지" / "text-to-image" also common; hyphenated Korean form chosen for the first sentence |
| tile (VAE tile) | 타일 | usual loanword |
| seed | 시드 | |
| prompt | 프롬프트 | standard loanword |
| quantization | 양자화 | |
| setup / install | 설치 (`setup.py` stays) | |
| measured / not tested | 측정했습니다 / 테스트하지 않았습니다 | "테스트" is what Korean developers say; "측정" for numbers only, so an unmeasured claim is never worded as measured |
| open source license / NOTICE | 라이선스 / `NOTICE` 파일 | "조건" (condition) for NOTICE; "감사하겠지만 필수는 아닙니다" (appreciated, not required) for the credit line |
| unofficial | 비공식 | |
| refiner / latent / float32 / flash attention | 리파이너(refiner) at first use / latent / float32 / flash attention | English terms kept where Korean developers use them untranslated |
| picture / image | 이미지 | one word throughout (not 사진 except "실제 사진" = real photograph) |
| step / segment | 스텝 / 세그먼트 | |

## Avoided
- Phrases that sound like advertising in this language/culture: "획기적", "놀라운", "손쉽게", "누구나", "최고", "혁신적", "완벽".
- Literal translations that read wrongly: "fits comfortably" is given as quote plus a plain gloss; "unofficial" is 비공식 with a plain "제휴 관계가 없습니다" (not affiliated), no softening.

## Formatting
- Numbers and decimal separator: unchanged as required (12.2, 261.6, ASCII digits); Korean uses a point as decimal separator anyway. Ranges keep the English form ("2949 ~ 2957 MiB"), thousands separators as in English ("10 509").
- Slots `{{...}}` kept with their unit symbol (`193–228 s`, `3057–3059 MiB`); "29분" attaches the Korean counter directly to the slot.
- Script issues: none (spaces between words, left-to-right). Table cells are short.

## Back-translation check
- First paragraph back into English by the reader: "Runs Z-Image-Turbo (Q8_0 GGUF) text-to-image conversion at 768x1344 on a 4 GB GTX 1050 Ti (Pascal, sm_61) with stable-diffusion.cpp on Windows. Measured on a 16 GB RAM laptop; the process uses about 11 GB of RAM. The same seed produces the same pixels pixel for pixel. Measurements and engine patches are public, downloads are pinned by sha256, and an AI coding agent can walk through the install step by step. Unofficial project; no affiliation with Tongyi-MAI, leejet or NVIDIA." Differences from the English: none in meaning.
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes. Limits: all nine items present, "테스트하지 않았습니다" kept, nothing softened. License: NOTICE is a condition (조건), credit line is appreciated-not-required; NVIDIA property kept. cuDNN: NVIDIA software, optional, asked once: kept.
- One fix: in the cuDNN bullet "그러면 파일을 ... 내려받아" (ambiguous after "--no-cudnn skips") became "건너뛰지 않으면 파일을 ...", matching "The file is then downloaded".

## Open points / corrections welcome
- "Hardware test report" (issue form name) is left in English because the form title is English.
- The cuDNN paragraph says "한 번 묻습니다" (asks once), "선택 사항" (optional) and "NVIDIA 소프트웨어" explicitly.
- Reader agrees with the 합니다체 choice, the term table and the loanword "클린 루트 테스트" (acceptable for developers); no open disagreement.
- Unsure points: (1) 합니다체 versus 해요체; (2) "텍스트-이미지 변환" versus "텍스트 투 이미지"; (3) "클린 루트 테스트" (clean-root test) as a loanword phrase.


## Round 2
- "by default" = "기본으로 설치되며" (not 선택 사항); "without payment or sign-in" = "결제나 로그인 없이" (deliberately not 무료); "we found no clause" = "저희가 찾지 못했습니다"; the license sentence is kept as 적혀 있습니다 + 해서는 안 된다 (three verbs). The license link is placed after the "found" sentence.
- Reader check: all three pieces and both script-edited lines (256 MiB, 581.29) read natively; no fix needed, nothing from rule 3 implied.
