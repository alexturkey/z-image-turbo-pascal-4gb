# Tiếng Việt (vi): localization notes

Written by: W13, 2026-11-14   Read by: R13, 2026-11-14   Status: ok (PASSED)

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: "bạn" (neutral second person) for the reader, "chúng tôi" for the authors. Vietnamese developer READMEs and technical docs use "bạn" as the standard neutral form; "anh/chị" would be too personal and "quý vị" too formal.
- Register (how technical, how warm): plain, calm, sourced. Vietnamese developers keep many English terms (prompt, seed, tile, engine, build, log, patch); they are kept, with Vietnamese for the explaining words. No advertising words.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | bộ nhớ GPU; "VRAM" only inside quotes | readers say "VRAM" or "bộ nhớ GPU"; the model-card quotes stay English |
| text-to-image | tạo ảnh từ văn bản (text-to-image) | Vietnamese phrase first, English term in brackets once, since readers know both |
| tile (VAE tile) | tile | kept English |
| seed | seed | kept English |
| prompt | prompt | kept English; "lời nhắc" exists but is rare among developers |
| quantization | lượng tử hóa | the usual Vietnamese term |
| setup / install | cài đặt (heading "Cài đặt nhanh"); `setup.py` unchanged | |
| measured / not tested | đã đo / chưa được thử | "chưa được thử" says we did not run it |
| open source license / NOTICE | giấy phép; the `NOTICE` file in backticks | condition = "điều kiện", request = "được trân trọng, nhưng không bắt buộc" |
| picture / image | ảnh | same word everywhere (not "hình" or "bức ảnh" except once as a classifier) |
| unofficial | không chính thức | |
| pixel | điểm ảnh | |

## Avoided
- Phrases that sound like advertising in this language/culture: "tuyệt vời", "siêu nhanh", "dễ dàng", "đỉnh cao", "hoàn hảo", "cách mạng".
- Literal translations that read wrongly: "everything is open" is "mọi thứ còn lại đều mở", not "miễn phí" (free). The "AI coding agent" stays as an English phrase; no Vietnamese equivalent is common.

## Formatting
- Numbers and decimal separator: the test requires them unchanged (12.2 stays 12.2; ASCII digits). Vietnamese normally writes a decimal comma (12,2), so a Vietnamese reader may notice the point; the numbers carry units and sit in tables, so it should not confuse. Thousands (6,577,440,704, 10 509) are as in the English.
- Script issues (right-to-left, line height, no spaces between words, table widths): Latin script with tone marks; line height is the renderer's job. Table cells kept short.

## Back-translation check
- Back-translation: 'Text-to-image with Z-Image-Turbo (Q8_0 GGUF) at 768x1344 on a 4 GB GTX 1050 Ti ... Measured on a 16 GB RAM laptop, process uses about 11 GB. Same seed gives same pixels, pixel by pixel; measurements and patches public; downloads pinned by sha256; an AI coding agent can install step by step. Not official, not affiliated with Tongyi-MAI, leejet or NVIDIA.' No differences from the English.
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes

## Open points / corrections welcome
- "Tóm tắt qua số liệu" for "At a glance" is a free rendering ("summary by the numbers"); a reader may prefer a shorter heading.
- "Ghi công" (credit) versus "ghi nhận": "ghi công" is the usual open-source word for attribution.
- "mỗi cái một lần chạy" ("one run each") is colloquial; check that it reads naturally.
- Reader (R13): agree with the notes; 'mỗi cái một lần chạy' is understandable but slightly clumsy, left as is. No claim drift; limits all present; condition vs request kept.

## Round 2
- Round 2 (K-21): "by default" = "theo mặc định"; "without payment" = "mà không bị yêu cầu thanh toán" (not "miễn phí"); "without sign-in" = "không cần đăng nhập (không cần tài khoản)"; "we found no clause" = "chúng tôi không tìm thấy điều khoản nào". NVIDIA's sentence kept with "không được tải xuống, cài đặt hay sử dụng".
- Reader (Round 2): "ai ... thì không được" is the natural form for "whoever"; "đăng nhập" is native, no loanword issue. "8–16 s" and "Một card, một máy" lines checked, no change.
