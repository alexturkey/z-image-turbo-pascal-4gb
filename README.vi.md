[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · **Tiếng Việt** · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**Tạo ảnh từ văn bản (text-to-image) bằng Z-Image-Turbo (Q8_0 GGUF) ở 768x1344 trên GTX 1050 Ti 4 GB (Pascal, sm_61), với stable-diffusion.cpp, trên Windows.** Đã đo trên một laptop 16 GB RAM, nơi tiến trình dùng khoảng 11 GB RAM. Cùng một seed cho ra cùng các điểm ảnh, từng điểm ảnh một; các số đo và bản vá của engine được công khai, các bản tải được ghim bằng sha256, và một AI coding agent có thể cài đặt từng bước.

*Không chính thức. Không liên kết với Tongyi-MAI (Z-Image), leejet (stable-diffusion.cpp) hay NVIDIA.*

## Bắt đầu từ đây

Đã có sẵn một gói dựng sẵn, nên hãy thử nó trước. Nếu phần cứng của bạn khác hoặc một bước bị lỗi, mọi thứ còn lại đều mở: các bản vá, công thức build và các số đo đều nằm trong repository này, nên bạn có thể build cho card của mình hoặc chỉnh lại cho phù hợp.

```
1. nvidia-smi --query-gpu=name,memory.total --format=csv
      expect a line like: NVIDIA GeForce GTX 1050 Ti, 4096 MiB
      NVIDIA card with 4 GB, Windows x64 -> 2        anything else -> 5
2. python scripts/setup.py
      downloads NVIDIA cuDNN by default (NVIDIA's license applies); add --no-cudnn to skip it; both work
      expect the last line: SETUP_OK
3. python scripts/generate.py --prompt-file prompts/eiffel.txt
      expect the last line: IMAGE_OK <path>
4. Open <path>. Done. Compare your numbers: docs/MEASUREMENTS.md
5. Other hardware, or a step failed: everything is open.
      patches/README.md   docs/BUILD.md   docs/MEASUREMENTS.md   docs/TROUBLESHOOTING.md
      Build the engine for your card, or adapt the recipe. AGENTS.md has the exact steps.
```

Bước 2 tải khoảng 12.2 GB và mất 29 phút, một lần, trên đường truyền của chúng tôi; trước tiên nó in ra một khối "Preflight" (GPU, RAM và dung lượng đĩa trống của bạn, đặt cạnh những gì chúng tôi đã đo; chỉ để thông tin).
Chỉ card laptop GTX 1050 Ti 4 GB (Pascal, compute capability 6.1) được đo. Các card khác chưa được thử.
Nếu bạn dùng một AI coding agent (Claude Code, Codex, Cursor và những công cụ tương tự), hãy chỉ cho nó tới [`AGENTS.md`](AGENTS.md).

## Tóm tắt qua số liệu

So với bố cục v0.1.0: một ảnh mất 193–228 s thay vì 261.6 s, giai đoạn VAE mất 8.3–15.9 s thay vì 29.8 đến 36.3 s, cùng một seed cho ra cùng các điểm ảnh, và mỗi con số trong README này đều có một lệnh và một tệp đứng sau.

768x1344, seed 42, 8 bước, cùng một máy. Số của v0.1.0 lấy từ README của v0.1.0 (clean-root test và năm lần chạy); số của v0.2.0 lấy từ clean-root test của bản phát hành này.

| | v0.1.0 (chưa từng được công bố; bố cục cũ) | v0.2.0 |
|---|---|---|
| Thời gian cho một ảnh (một lần chạy `generate.py`) | 261.6 s | 193–228 s |
| Giải mã VAE (giai đoạn cuối) | 29.8 đến 36.3 s | 8.3–15.9 s |
| Độ gần với bản giải mã tham chiếu (PSNR, càng cao càng gần) | 38 đến 43 dB | 71 đến 73 dB |
| Bộ nhớ GPU đỉnh (nvidia-smi) | 2949 đến 2957 MiB | 3057–3059 MiB |
| Bộ nhớ tiến trình, đỉnh | 10.5 đến 10.9 GB (như đã ghi lúc đó) | 10 667–10 915 MiB |
| RAM trống thấp nhất đã thấy | 331 đến 576 MiB | 418–545 MiB |

Cách đọc: bản tham chiếu là chính latent đó được giải mã trên CPU thành một khối float32; PSNR so sánh bản giải mã GPU của chúng tôi với nó (3 ảnh). Nó cho biết giai đoạn VAE gần bản tham chiếu đến mức nào. Nó không cho biết một bức ảnh trông đẹp đến đâu. Ảnh của v0.2.0 không giống từng byte với v0.1.0 cho cùng prompt và seed, vì đường VAE đã được thay đổi có chủ ý. Phương pháp và những phần chưa đo: [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md).

## Ví dụ

**Do AI tạo ra bằng repo này** (Z-Image-Turbo Q8_0, seed 42, 8 bước). Đây không phải ảnh chụp thật; các địa danh và chi tiết
có thể không chính xác, và một ảnh không phải lúc nào cũng bám sát prompt ở mọi chi tiết. Các prompt chính xác nằm trong [`prompts/`](prompts) và [`docs/PROMPTS.md`](docs/PROMPTS.md).

| | | |
|---|---|---|
| ![Tháp Eiffel lúc hoàng hôn vàng](docs/examples/eiffel.jpg) | ![Ly trà Thổ Nhĩ Kỳ](docs/examples/turkish_tea.jpg) | ![Ông lão ngư dân](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![Ngôi làng trên sườn đồi](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![Istanbul nhìn từ trên không](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. Không phải ảnh chụp thật; các địa danh có thể không chính xác.

## Cài đặt nhanh

Yêu cầu: Windows 10/11, một GPU NVIDIA 4 GB, một driver hỗ trợ CUDA 12.8 (đã đo với driver 581.29; các driver cũ hơn chưa được thử; bản thân CUDA runtime sẽ được tải về cho bạn), Python 3.10 trở lên,
git, khoảng 14 GB đĩa trống (các bản tải khoảng 12.2 GB khi có cuDNN; con số đĩa trống chỉ là ước tính), và 16 GB RAM (đây là mức đã đo; ít hơn chưa được thử).

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- Trước tiên `setup.py` in ra một khối "Preflight" (GPU, RAM và dung lượng đĩa trống của bạn, đặt cạnh những gì chúng tôi đã đo; chỉ để thông tin và không bao giờ chặn). Sau đó nó tải từ các địa chỉ được ghim trong [`models.lock.json`](models.lock.json) và kiểm tra từng tệp bằng sha256. Nó in ra `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK`, rồi `CUDNN_OK` hoặc `CUDNN_SKIPPED`, và cuối cùng là `SETUP_OK`.
  Khi không có `--models-dir` và `--bin-dir`, nó dùng `models/` và `bin/` ở thư mục gốc của repo; hãy đặt các model trên SSD (chỉ SSD được đo).
  Bạn có thể dừng bất cứ lúc nào bằng Ctrl+C rồi chạy lại đúng lệnh đó: các bản tải sẽ tiếp tục từ các tệp `.part`.
- **cuDNN được cài đặt theo mặc định và không thuộc repository này.** Đó là phần mềm của NVIDIA theo giấy phép riêng của NVIDIA ([văn bản giấy phép](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)), dành cho hệ thống có GPU NVIDIA. Tệp được tải từ máy chủ của NVIDIA mà không bị yêu cầu thanh toán và không cần đăng nhập (không cần tài khoản), và chúng tôi không tìm thấy điều khoản nào trong giấy phép hạn chế việc sử dụng thương mại hay cá nhân. `setup.py` hiển thị địa chỉ giấy phép, tải tệp và chỉ sao chép tám DLL cạnh `sd-cli.exe`. Giấy phép của NVIDIA nêu rằng ai không chấp nhận các điều khoản của nó thì không được tải xuống, cài đặt hay sử dụng; trong trường hợp đó, hãy chạy `python scripts/setup.py --no-cudnn`. Nếu không có cuDNN, mọi thứ vẫn chạy với đường VAE chậm hơn của v0.1.0 (`--vae legacy`), và `generate.py` sẽ cho bạn biết điều đó.
- `generate.py` ghi `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, `run.json` (thời gian, các giai đoạn, đường VAE nào đã chạy, bộ nhớ GPU đỉnh, lệnh chính xác) và `log.txt`, rồi in `IMAGE_OK <path>`.

## Cách dùng

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| Tùy chọn | Ý nghĩa |
|---|---|
| `--prompt "<text>"` hoặc `--prompt-file <txt>` | prompt (bắt buộc một trong hai) |
| `--width`, `--height` | bội số của 16, từ 256 đến 2048; mặc định 768x1344; đã thử: 768x1344, 1344x768, 1024x1024 |
| `--seed` | mặc định 42 |
| `--out`, `--name` | thư mục gốc của đầu ra (mặc định `outputs/`) và một tên ngắn cho thư mục của lần chạy |
| `--models-dir`, `--bin-dir` | nơi `setup.py` đặt các model và engine |
| `--vae auto` (mặc định) | cuDNN float32; thử một khối trước, rồi hai tile lớn, rồi tile nhỏ mặc định |
| `--vae tiled` | cuDNN float32, luôn dùng hai tile lớn |
| `--vae legacy` | đường của v0.1.0: không cuDNN, tile nhỏ. Tự động được dùng (kèm cảnh báo) khi thiếu các DLL của cuDNN |

Số bước (8), cfg (1.0), sampler và scheduler được cố định có chủ ý; xem [Nó chạy những gì](#what-it-runs).

## Tự kiểm chứng

- `generate.py` in ra `PIXEL_SHA256 <hex>` ở một trong những dòng cuối: mã băm của các điểm ảnh đã giải mã. Chạy cùng một lệnh hai lần và so sánh hai ảnh: `python scripts/compare.py <run A>/image.png <run B>/image.png` phải in ra `SAME_PIXELS`.
- `PIXEL_SHA256` của năm ví dụ trên máy của chúng tôi nằm trong [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md). Mã băm tệp của một PNG có thể khác nhau dù các điểm ảnh giống nhau, vì PNG mang theo các tham số tạo ảnh dưới dạng văn bản; hãy so sánh điểm ảnh, đừng so sánh tệp.
- Giới hạn cần nói thẳng: chúng tôi không đo xem một card hay driver khác có cho ra cùng các điểm ảnh hay không.

## Vì sao nó vừa trong 4 GB

- **Các tác giả model nói gì.** Model card của Z-Image-Turbo nói rằng model "fits comfortably within 16G VRAM consumer devices" (vừa thoải mái trên các thiết bị tiêu dùng có 16 GB VRAM) ([model card](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)). Đó là phát biểu về các card 16 GB. README chính thức cũng liệt kê stable-diffusion.cpp như một lựa chọn của bên thứ ba và trích dẫn nó với "as little as 4GB of VRAM" (chỉ cần 4 GB VRAM) ([README](https://github.com/Tongyi-MAI/Z-Image)); đó là tuyên bố của dự án stable-diffusion.cpp, không phải yêu cầu của nhóm Z-Image.
- **Chúng tôi đã đo gì.** Z-Image-Turbo Q8_0 (một tệp 6.6 GB) với text encoder Qwen3-4B Q8_0, 768x1344: đỉnh GPU, do nvidia-smi lấy mẫu mỗi 2 s (một đợt tăng ngắn có thể bị bỏ sót), là 2949 đến 2957 MiB (engine v0.1.0) và 3057–3059 MiB (engine v0.2.0) trên card 4096 MiB. Các trọng số (10 509 MiB; log của engine in ra là MB) nằm lại trong RAM hệ thống; engine chép mạng sang GPU từng segment một (một lát của mạng): 36 segment, như dòng log `z_image using 36 segments`.
- **Cái giá phải trả.** Thời gian và bộ nhớ hệ thống: 193–228 s mỗi ảnh, và tiến trình engine giữ khoảng 10 667–10 915 MiB RAM (kể cả các trang model ánh xạ bộ nhớ) trên máy 16 GB, nên RAM trống tụt xuống vài trăm MiB trong lúc chạy.
- **Cách cài của người khác.** Những người khác báo cáo chạy Z-Image trên card 4 GB với lượng tử hóa thấp hơn hoặc kích thước nhỏ hơn (ví dụ, trang wiki của stable-diffusion.cpp dành cho card 4 GB khuyên dùng Q3_K hoặc Q4_0 ở 1024x512). Ở những nơi chúng tôi đã tìm (danh sách và ngày trong [`docs/RELATED.md`](docs/RELATED.md)), chúng tôi không thấy cách cài nào đã được công bố mà kết hợp cả bốn điều: card 4 GB, Q8_0, 768x1344 hoặc lớn hơn, và thời gian cùng bộ nhớ GPU đã đo. Đó là phát biểu về những nơi chúng tôi đã tìm, không phải về mọi nơi.
- **Ai làm gì.** Việc vừa trong 4 GB đến từ chính stable-diffusion.cpp: `--offload-to-cpu`, `--mmap`, xử lý theo từng lát, và flash attention (khi tắt nó, một lần chạy cần 4205 MB và không vừa). Các bản vá của chúng tôi dành cho tốc độ và một giai đoạn VAE tốt hơn, không phải để cho vừa. Chúng tôi chưa chạy engine upstream chưa vá trên card này, nên không thể nói liệu nó có vừa hay không.

## Nó hoạt động thế nào

Ba thay đổi trên stable-diffusion.cpp `master-1088-32d516c` (tất cả đều là công tắc; bảng trong [`patches/README.md`](patches/README.md) liệt kê từng thay đổi cùng biến môi trường của nó):

1. **Refiner chạy một lần mỗi bước.** Một tên nhóm bị dùng hai lần, nên bốn khối refiner bị tính lần thứ hai. Sửa lỗi này làm các bước 2 đến 8 nhanh hơn khoảng 1.3 s mỗi bước (22.0 xuống 20.7 s) với ảnh giống hệt từng điểm ảnh (đã kiểm tra 3 ảnh).
2. **VAE qua cuDNN, ở float32.** Giai đoạn cuối (biến latent thành điểm ảnh) giờ dùng phép tích chập float32 của cuDNN từ NVIDIA. Trên card của chúng tôi, nó đưa VAE từ 23 đến 27 s xuống 10 đến 15 s và nâng PSNR so với bản tham chiếu từ 38 đến 43 dB lên 45 đến 49 dB (với tile lớn).
3. **Một khối trước.** Giờ engine thử giải mã cả ảnh trong một khối khi bước kiểm tra bộ nhớ cho là vừa (biên 256 MiB), lùi về hai tile lớn, rồi đến các tile nhỏ. Ở một khối, VAE mất khoảng 8–16 s và PSNR so với bản tham chiếu là 71 đến 73 dB. Nếu buộc phải lùi bước, ảnh có cùng các điểm ảnh với bản dùng tile (đã kiểm tra bằng `PIXEL_SHA256`). Điều đã xảy ra được ghi trong `run.json` (`stages.vae_path`: `full`, `tile`, `floor` hoặc `retry`).

Ngoài ra: `--eager-load` (đọc trước các trang model; 241.2 s xuống 220.3 s trên cùng một ảnh, bản development, mỗi cái một lần chạy) là một phần của lệnh cố định.

<a id="what-it-runs"></a>
## Nó chạy những gì

| Thành phần | Tệp | Nguồn |
|---|---|---|
| Diffusion model | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), bản gốc [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Text encoder | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), autoencoder kiểu FLUX.1 |
| Engine | `sd-cli.exe`, stable-diffusion.cpp `32d516c` kèm các bản vá trong [`patches/`](patches) | bản phát hành v0.2.0 của repository này (`sinirsiz-foto-engine-v0.2.0-win-x64-cuda12.8-sm61.zip`) |
| CUDA runtime | `cudart`, `cublas`, `cublasLt` (12.8), không sửa đổi | tệp zip từ bản phát hành wan22-pascal-4gb v0.1.0 |
| cuDNN (cài đặt theo mặc định; `--no-cudnn` bỏ qua) | 8 DLL, phiên bản 9.10.2.21 (bản build CUDA 11) | máy chủ riêng của NVIDIA, theo giấy phép của NVIDIA; không lưu ở đây |

Các thiết lập cố định: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`.
Chúng tôi không giảm số bước, không thêm negative prompt và không bật caching: model được distill cho 8 bước và không dùng negative prompt (xem [prompt](docs/PROMPTS.md)).

## Giới hạn (đọc trước khi dựa vào nó)

- **Chỉ Windows.** Engine dựng sẵn và các script này chỉ dành cho Windows.
- **Một card, một máy.** Chỉ được đo trên một laptop GTX 1050 Ti 4 GB (i7-7700HQ, 16 GB RAM, Windows 10, driver 581.29, các model trên SSD). Các GPU và driver khác, máy có dưới 16 GB RAM, Linux và macOS: **chưa được thử**.
- Các card và hệ thống khác (có con đường nào, và một bài thử của cộng đồng trên card AMD dưới Linux mà chúng tôi không tự chạy): [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md).
- **Engine chỉ được build cho Pascal (sm_61).** Các kiến trúc khác cần bản build riêng của bạn ([`docs/BUILD.md`](docs/BUILD.md)); chúng tôi chưa thử bản nào.
- **cuDNN:** chúng tôi đo với bản build CUDA 11 của cuDNN 9.10.2.21. Bản build CUDA 12 có các tệp khác và chưa được đo.
- **Bộ nhớ rất chật.** RAM trống tụt xuống vài trăm MiB; hãy đóng các chương trình khác, mỗi lần chỉ tạo một ảnh. Chúng tôi chưa thấy bộ nhớ GPU cạn sau khi bước kiểm tra bộ nhớ của engine đã qua, và chúng tôi chưa thử điều gì xảy ra khi đó.
- **Kích thước:** chỉ 768x1344, 1344x768 và 1024x1024 đã được thử. Kích thước lớn hơn sẽ in cảnh báo và có thể hết bộ nhớ.
- Mức độ bám prompt chỉ một phần: một ảnh không phải lúc nào cũng bám sát prompt ở mọi chi tiết. Chữ trong ảnh và các địa danh có thật chưa được đánh giá.
- Bản tham chiếu của PSNR là bản giải mã CPU của chính engine chúng tôi, không phải một bản cài đặt độc lập.
- Các số trong [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) đến từ mỗi cái một lần chạy, trừ khi có ghi khác.

## Giấy phép và ghi công

- Các script và tài liệu của repository này: [Apache-2.0](LICENSE) kèm một tệp [`NOTICE`](NOTICE). Các bản vá engine trong [`patches/`](patches) theo giấy phép MIT, giống mã mà chúng sửa.
- stable-diffusion.cpp và ggml theo giấy phép MIT. Các thông báo cho mã của bên thứ ba được biên dịch vào engine nằm trong [`licenses/`](licenses) và [`THIRD_PARTY.md`](THIRD_PARTY.md).
- Các tệp model không được lưu ở đây; chúng được tải từ các nguồn ở trên theo giấy phép riêng của từng cái (Hugging Face ghi Apache-2.0 cho tất cả, đọc ngày 2026-11-13). Model card không nói gì về việc ai sở hữu các ảnh được tạo ra, và chúng tôi cũng không đưa ra tuyên bố nào về điều đó.
- **cuDNN và CUDA runtime là tài sản của NVIDIA** và không nằm dưới giấy phép của repository này. cuDNN được tải từ máy chủ của NVIDIA theo giấy phép của NVIDIA (`--no-cudnn` bỏ qua bước này); các DLL của CUDA runtime nằm trong một tệp zip riêng, không sửa đổi (CUDA Toolkit EULA, Attachment A). Chi tiết và những gì chúng tôi chưa thể xác minh: [`THIRD_PARTY.md`](THIRD_PARTY.md).
- **Ghi công.** Giữ tệp `NOTICE` cùng với các bản sao và tác phẩm phái sinh là điều kiện (Apache-2.0, mục 4). Ngoài ra, một dòng như "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey" sẽ được trân trọng, nhưng không bắt buộc.
- Xin đọc [`ETHICS.md`](ETHICS.md): mọi bức ảnh đều là ảnh tổng hợp, và bạn chịu trách nhiệm về những gì mình công bố.

## Đóng góp

Việc hữu ích nhất bạn có thể làm là **thử card của bạn** và cho chúng tôi biết kết quả: tên GPU, driver, RAM, tệp `run.json` và các dòng cuối của log (mẫu issue "Hardware test report"). Các bản sửa cho tài liệu và script cũng được hoan nghênh; xem [`CONTRIBUTING.md`](CONTRIBUTING.md). Báo cáo bảo mật đi qua kênh riêng trong [`SECURITY.md`](SECURITY.md).

[Hướng dẫn cài đặt cho AI agent](AGENTS.md) · [Số đo](docs/MEASUREMENTS.md) · [Khắc phục sự cố](docs/TROUBLESHOOTING.md) · [Build engine](docs/BUILD.md) · [Các bản vá](patches/README.md) · [Prompt](docs/PROMPTS.md) · [Bên thứ ba](THIRD_PARTY.md) · [Nhật ký thay đổi](CHANGELOG.md)

Trang này được bản địa hóa với sự hỗ trợ của AI, và mọi chỉnh sửa đều rất được hoan nghênh; xem [`CONTRIBUTING.md`](CONTRIBUTING.md).
