[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · **ไทย** · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**สร้างภาพจากข้อความด้วย Z-Image-Turbo (Q8_0 GGUF) ขนาด 768x1344 บน GTX 1050 Ti ที่มี VRAM 4 GB (Pascal, sm_61) ด้วย stable-diffusion.cpp บน Windows** วัดผลบนโน้ตบุ๊กที่มี RAM 16 GB ซึ่งโปรเซสใช้ RAM ประมาณ 11 GB ใช้ seed เดิมได้พิกเซลเดิมทุกพิกเซล ผลการวัดและแพตช์ของเอนจินเปิดเผยไว้ทั้งหมด ไฟล์ที่ดาวน์โหลดล็อกด้วย sha256 และ AI coding agent ติดตั้งให้ทีละขั้นได้

*ไม่เป็นทางการ ไม่มีความเกี่ยวข้องกับ Tongyi-MAI (Z-Image), leejet (stable-diffusion.cpp) หรือ NVIDIA*

> **ใช้เอเจนต์เขียนโค้ด AI (Codex, Claude Code, Gemini, Cursor) อยู่หรือไม่?** ให้ประโยคเดียวนี้แก่เอเจนต์: “อ่าน `AGENTS_HIZLI.md` ให้จบ รัน `python scripts/tani.py` ก่อน บันทึกความคืบหน้าไว้ใน `DURUM.md` และถามฉันก่อนจะลบหรือย้ายสิ่งใด เปลี่ยน Python ของระบบหรือ PATH หรือลดการตั้งค่าคุณภาพ” เอเจนต์จะตรวจวินิจฉัยพีซีเครื่องนี้ เขียนรายการตรวจสอบ และถามคุณทุกครั้งที่ต้องตัดสินใจ

## เริ่มที่นี่

มีแพ็กเกจสำเร็จรูปให้แล้ว ลองใช้ก่อนได้เลย ถ้าฮาร์ดแวร์ของคุณต่างออกไปหรือมีขั้นตอนที่ไม่ผ่าน ส่วนที่เหลือเปิดไว้ทั้งหมด ทั้งแพตช์ สูตรการ build และผลการวัดอยู่ในรีโพนี้ คุณจึงนำไป build สำหรับการ์ดของตัวเองหรือปรับใช้เองได้

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

ขั้นที่ 2 ดาวน์โหลดประมาณ 12.2 GB และใช้เวลา 29 นาทีในครั้งที่เราวัด บนอินเทอร์เน็ตของเรา ขั้นนี้จะพิมพ์บล็อก "Preflight" ก่อน (แสดง GPU, RAM และพื้นที่ดิสก์ว่างของเครื่องคุณเทียบกับค่าที่เราวัดได้ แสดงให้ดูเท่านั้นและไม่เคยขวางการทำงาน)
เราวัดผลเฉพาะโน้ตบุ๊กที่มี GTX 1050 Ti 4 GB (Pascal, compute capability 6.1) เท่านั้น การ์ดรุ่นอื่นยังไม่ได้ทดสอบ
ถ้าคุณใช้ AI coding agent (Claude Code, Codex, Cursor และเครื่องมือทำนองเดียวกัน) ให้ชี้ไปที่ [`AGENTS.md`](AGENTS.md)

## ภาพรวมเป็นตัวเลข

เทียบกับโครงสร้างของ v0.1.0: หนึ่งภาพใช้เวลา 188–193 s แทนที่จะเป็น 261.6 s ขั้น VAE ใช้ 12.5–21.7 s แทนที่จะเป็น 29.8 ถึง 36.3 s ใช้ seed เดิมได้พิกเซลเดิม และทุกตัวเลขใน README นี้มีคำสั่งและไฟล์รองรับ

768x1344, seed 42, 8 steps, เครื่องเดียวกัน ตัวเลขของ v0.1.0 มาจาก README ของ v0.1.0 (การทดสอบจาก clean root และการรัน 5 ครั้ง) ตัวเลขของ v0.3.0 มาจากการทดสอบ clean root ของรุ่นนี้

| | v0.1.0 (ไม่เคยเผยแพร่ โครงสร้างเก่า) | v0.3.0 |
|---|---|---|
| เวลาต่อหนึ่งภาพ (การรัน `generate.py` หนึ่งครั้ง) | 261.6 s | 188–193 s |
| VAE decode (ขั้นสุดท้าย) | 29.8 ถึง 36.3 s | 12.5–21.7 s |
| ความใกล้เคียงกับ reference decode (PSNR ยิ่งสูงยิ่งใกล้) | 38 ถึง 43 dB | 71 ถึง 73 dB |
| VRAM สูงสุด (nvidia-smi) | 2949 ถึง 2957 MiB | 3057–3059 MiB |
| หน่วยความจำของโปรเซส ค่าสูงสุด | 10.5 ถึง 10.9 GB (ตามที่บันทึกไว้ตอนนั้น) | 10 489–11 203 MiB |
| RAM ว่างต่ำสุดที่เห็น | 331 ถึง 576 MiB | 303–532 MiB |

วิธีอ่านตาราง: reference คือ latent ตัวเดียวกันที่ decode บน CPU เป็นก้อนเดียวแบบ float32 PSNR เทียบผลถอดรหัสบน GPU ของเรากับ reference นั้น (3 ภาพ) ค่านี้บอกว่าขั้น VAE ใกล้เคียงกับ reference แค่ไหน ไม่ได้บอกว่าภาพสวยหรือไม่ ภาพของ v0.2.0 ไม่ตรงกับ v0.1.0 ทุกไบต์เมื่อใช้ prompt และ seed เดียวกัน เพราะเราตั้งใจเปลี่ยนเส้นทางของ VAE วิธีวัดและส่วนที่ยังไม่ได้วัดอยู่ที่ [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md)

## ตัวอย่าง

**ภาพที่ AI สร้างด้วยรีโพนี้** (Z-Image-Turbo Q8_0, seed 42, 8 steps) ไม่ใช่ภาพถ่ายจริง สถานที่สำคัญและรายละเอียดอาจไม่ถูกต้อง และภาพไม่ได้ทำตาม prompt ครบทุกรายละเอียดเสมอไป prompt ที่ใช้จริงอยู่ใน [`prompts/`](prompts) และ [`docs/PROMPTS.md`](docs/PROMPTS.md)

| | | |
|---|---|---|
| ![หอไอเฟลตอนแสงทอง](docs/examples/eiffel.jpg) | ![แก้วชาตุรกี](docs/examples/turkish_tea.jpg) | ![ชาวประมงสูงวัย](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![หมู่บ้านบนเนินเขา](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![อิสตันบูลมองจากมุมสูง](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768 ไม่ใช่ภาพถ่ายจริง สถานที่สำคัญอาจไม่ถูกต้อง

## เริ่มใช้งานอย่างรวดเร็ว

สิ่งที่ต้องมี: Windows 10/11, การ์ด NVIDIA ที่มี VRAM 4 GB, ไดรเวอร์ที่รองรับ CUDA 12.8 (วัดผลกับไดรเวอร์ 581.29 ไดรเวอร์รุ่นเก่ากว่านั้นยังไม่ได้ทดสอบ ส่วน CUDA runtime ระบบดาวน์โหลดให้เอง), Python 3.10 ขึ้นไป,
git, พื้นที่ดิสก์ว่างประมาณ 14 GB (ไฟล์ที่ดาวน์โหลดประมาณ 12.2 GB เมื่อรวม cuDNN ตัวเลขพื้นที่ว่างเป็นค่าประมาณ) และ RAM 16 GB (ตามที่วัดไว้ ถ้าน้อยกว่านี้ยังไม่ได้ทดสอบ)

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- `setup.py` พิมพ์บล็อก "Preflight" ก่อน (แสดง GPU, RAM และพื้นที่ดิสก์ว่างของเครื่องคุณเทียบกับค่าที่เราวัดได้ แสดงให้ดูเท่านั้นและไม่เคยขวางการทำงาน) จากนั้นดาวน์โหลดจากที่อยู่ที่ล็อกไว้ใน [`models.lock.json`](models.lock.json) และตรวจทุกไฟล์ด้วย sha256 โดยพิมพ์ `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK` ตามด้วย `CUDNN_OK` หรือ `CUDNN_SKIPPED` และปิดท้ายด้วย `SETUP_OK`
  ถ้าไม่ระบุ `--models-dir` และ `--bin-dir` จะใช้โฟลเดอร์ `models/` และ `bin/` ที่รากของรีโพ ควรวางโมเดลไว้บน SSD (เราวัดผลบน SSD เท่านั้น)
  หยุดได้ทุกเมื่อด้วย Ctrl+C แล้วรันคำสั่งเดิมอีกครั้ง การดาวน์โหลดจะต่อจากไฟล์ `.part`
- **cuDNN จะถูกติดตั้งโดยค่าเริ่มต้น และไม่ได้เป็นส่วนหนึ่งของรีโพนี้** เป็นซอฟต์แวร์ของ NVIDIA ภายใต้สัญญาอนุญาตของ NVIDIA เอง ([ข้อความสัญญาอนุญาต](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)) สำหรับระบบที่มี GPU ของ NVIDIA ดาวน์โหลดจากเซิร์ฟเวอร์ของ NVIDIA โดยไม่มีการเรียกเก็บเงินและไม่ต้องลงชื่อเข้าใช้ และเราไม่พบข้อความใดในสัญญาที่จำกัดการใช้งานเชิงพาณิชย์หรือส่วนตัว `setup.py` จะแสดงที่อยู่ของสัญญาอนุญาต ดาวน์โหลดไฟล์ และคัดลอกเพียงแปดไฟล์ DLL ไปวางข้าง `sd-cli.exe` สัญญาอนุญาตของ NVIDIA ระบุว่าผู้ที่ไม่ยอมรับข้อกำหนดของสัญญาต้องไม่ดาวน์โหลด ติดตั้ง หรือใช้งานซอฟต์แวร์นั้น ในกรณีนั้นให้รัน `python scripts/setup.py --no-cudnn` ถ้าไม่มี cuDNN ทุกอย่างยังทำงานได้ด้วยเส้นทาง VAE แบบ v0.1.0 ที่ช้ากว่า (`--vae legacy`) และ `generate.py` จะแจ้งให้ทราบ
- `generate.py` เขียน `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, `run.json` (เวลา แต่ละขั้น เส้นทาง VAE ที่ใช้ VRAM สูงสุด และคำสั่งที่ใช้จริง) และ `log.txt` แล้วพิมพ์ `IMAGE_OK <path>`

## วิธีใช้

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| ตัวเลือก | ความหมาย |
|---|---|
| `--prompt "<text>"` หรือ `--prompt-file <txt>` | prompt (ต้องระบุอย่างใดอย่างหนึ่ง) |
| `--width`, `--height` | ต้องเป็นพหุคูณของ 16 อยู่ระหว่าง 256 ถึง 2048 ค่าเริ่มต้น 768x1344 ขนาดที่ทดสอบแล้ว: 768x1344, 1344x768, 1024x1024 |
| `--seed` | ค่าเริ่มต้น 42 |
| `--out`, `--name` | โฟลเดอร์รากของผลลัพธ์ (ค่าเริ่มต้น `outputs/`) และชื่อสั้นๆ ของโฟลเดอร์การรันนั้น |
| `--models-dir`, `--bin-dir` | ที่ที่ `setup.py` วางโมเดลและเอนจิน |
| `--vae auto` (ค่าเริ่มต้น) | cuDNN float32 ลองก้อนเดียวก่อน แล้วค่อยใช้ไทล์ใหญ่สองชิ้น แล้วจึงใช้ไทล์เล็กตามค่าเริ่มต้น |
| `--vae tiled` | cuDNN float32 ใช้ไทล์ใหญ่สองชิ้นเสมอ |
| `--vae legacy` | เส้นทางของ v0.1.0 ไม่ใช้ cuDNN ใช้ไทล์เล็ก จะถูกใช้อัตโนมัติ (พร้อมคำเตือน) เมื่อไม่พบ DLL ของ cuDNN |

จำนวน steps (8), cfg (1.0), sampler และ scheduler ตรึงไว้โดยตั้งใจ ดู [สิ่งที่รัน](#what-it-runs)

## ตรวจสอบเอง

- `generate.py` พิมพ์ `PIXEL_SHA256 <hex>` ในบรรทัดท้ายๆ เป็นค่าแฮชของพิกเซลที่ decode แล้ว รันคำสั่งเดิมสองครั้งแล้วเทียบภาพทั้งสอง: `python scripts/compare.py <run A>/image.png <run B>/image.png` ควรพิมพ์ `SAME_PIXELS`
- ค่า `PIXEL_SHA256` ของตัวอย่างทั้งห้าภาพบนเครื่องของเราอยู่ใน [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) แฮชของไฟล์ PNG อาจต่างกันได้แม้พิกเซลเหมือนกัน เพราะ PNG เก็บพารามิเตอร์การสร้างภาพไว้เป็นข้อความ ให้เทียบพิกเซล ไม่ใช่เทียบไฟล์
- ข้อจำกัดที่ต้องบอกตรงๆ: เราไม่ได้วัดว่าการ์ดหรือไดรเวอร์อื่นให้พิกเซลเหมือนกันหรือไม่

## ทำไมจึงใส่ใน 4 GB ได้

- **ผู้สร้างโมเดลบอกว่าอย่างไร** model card ของ Z-Image-Turbo ระบุว่าโมเดล "fits comfortably within 16G VRAM consumer devices" ([model card](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)) หมายถึงการ์ดขนาด 16 GB README ทางการยังระบุ stable-diffusion.cpp เป็นทางเลือกจากบุคคลที่สามและอ้างว่าใช้ "as little as 4GB of VRAM" ([README](https://github.com/Tongyi-MAI/Z-Image)) นั่นเป็นคำกล่าวอ้างของโปรเจกต์ stable-diffusion.cpp ไม่ใช่ข้อกำหนดของทีม Z-Image
- **สิ่งที่เราวัดได้** Z-Image-Turbo Q8_0 (ไฟล์ขนาด 6.6 GB) กับ text encoder Qwen3-4B Q8_0 ที่ 768x1344 ค่าสูงสุดของ GPU ที่ nvidia-smi สุ่มอ่านทุก 2 s (ค่าพุ่งสั้นๆ อาจพลาดได้) อยู่ที่ 2949 ถึง 2957 MiB (เอนจิน v0.1.0) และ 3057–3059 MiB (เอนจิน v0.2.0) บนการ์ดขนาด 4096 MiB น้ำหนักโมเดล (10 509 MiB ล็อกของเอนจินพิมพ์เป็น MB) อยู่ใน RAM ของระบบ เอนจินคัดลอกเน็ตเวิร์กไปที่ GPU ทีละ segment (ชิ้นส่วนของเน็ตเวิร์ก) มี 36 segments ตามบรรทัดล็อก `z_image using 36 segments`
- **ราคาที่ต้องจ่าย** คือเวลาและหน่วยความจำของระบบ: 188–193 s ต่อหนึ่งภาพ และโปรเซสของเอนจินถือ RAM ประมาณ 10 489–11 203 MiB (รวมหน้าโมเดลที่ memory-mapped) บนเครื่อง 16 GB ดังนั้น RAM ว่างจะลดเหลือไม่กี่ร้อย MiB ระหว่างที่รัน
- **วิธีของคนอื่น** มีรายงานว่ารัน Z-Image บนการ์ด 4 GB ได้ด้วย quantization ที่ต่ำกว่าหรือขนาดภาพที่เล็กกว่า (เช่น หน้า wiki ของ stable-diffusion.cpp สำหรับการ์ด 4 GB แนะนำ Q3_K หรือ Q4_0 ที่ 1024x512) ในที่ที่เราไปค้นดู (รายการและวันที่อยู่ใน [`docs/RELATED.md`](docs/RELATED.md)) เราไม่พบวิธีที่เผยแพร่แล้วซึ่งรวมครบทั้งสี่อย่าง คือการ์ด 4 GB, Q8_0, 768x1344 หรือใหญ่กว่า และมีการวัดเวลากับหน่วยความจำ GPU ไว้ นี่เป็นคำกล่าวเกี่ยวกับที่ที่เราค้นดู ไม่ใช่เกี่ยวกับทุกที่
- **ใครทำอะไร** การทำให้ใส่ใน 4 GB ได้มาจาก stable-diffusion.cpp เอง คือ `--offload-to-cpu`, `--mmap`, การทำงานทีละชิ้น และ flash attention (เมื่อปิด flash attention การรันใช้ 4205 MB และใส่ไม่พอ) แพตช์ของเราทำเพื่อความเร็วและขั้น VAE ที่ดีขึ้น ไม่ได้ทำเพื่อให้ใส่ได้ เราไม่ได้รันเอนจิน upstream ที่ไม่มีแพตช์บนการ์ดใบนี้ จึงบอกไม่ได้ว่าใส่ได้หรือไม่

## ทำงานอย่างไร

มีการเปลี่ยนแปลงสามอย่างบน stable-diffusion.cpp `master-1088-32d516c` (ทุกอย่างเป็นสวิตช์ ตารางใน [`patches/README.md`](patches/README.md) ระบุแต่ละอย่างพร้อมตัวแปรสภาพแวดล้อมของมัน):

1. **refiner รันหนึ่งครั้งต่อหนึ่ง step** ชื่อกลุ่มถูกใช้ซ้ำสองครั้ง ทำให้บล็อก refiner สี่บล็อกถูกคำนวณซ้ำอีกรอบ เมื่อแก้แล้ว steps ที่ 2 ถึง 8 เร็วขึ้นประมาณ 1.3 s ต่อ step (จาก 22.0 เป็น 20.7 s) และภาพที่ได้เหมือนเดิมทุกพิกเซล (ตรวจ 3 ภาพ)
2. **VAE ผ่าน cuDNN แบบ float32** ขั้นสุดท้าย (แปลง latent เป็นพิกเซล) ใช้ convolution แบบ float32 ของ cuDNN จาก NVIDIA บนการ์ดของเรา VAE ลดจาก 23 ถึง 27 s เหลือ 10 ถึง 15 s และ PSNR เทียบกับ reference ขยับจาก 38 ถึง 43 dB เป็น 45 ถึง 49 dB (ไทล์ใหญ่)
3. **ลองก้อนเดียวก่อน** ตอนนี้เอนจินจะลอง decode ทั้งภาพเป็นก้อนเดียวเมื่อการตรวจหน่วยความจำบอกว่าใส่ได้ (ส่วนเผื่อ 256 MiB) ถ้าไม่ได้ก็ถอยไปใช้ไทล์ใหญ่สองชิ้น และถ้ายังไม่ได้ก็ใช้ไทล์เล็ก เมื่อ decode เป็นก้อนเดียว VAE ใช้เวลาประมาณ 8–16 s และ PSNR เทียบกับ reference อยู่ที่ 71 ถึง 73 dB ถ้าเกิดการถอยแบบบังคับ ภาพที่ได้มีพิกเซลเหมือนกับแบบไทล์ (ตรวจด้วย `PIXEL_SHA256`) สิ่งที่เกิดขึ้นจริงบันทึกไว้ใน `run.json` (`stages.vae_path`: `full`, `tile`, `floor` หรือ `retry`)

นอกจากนี้: `--eager-load` (อ่านหน้าโมเดลล่วงหน้า จาก 241.2 s เหลือ 220.3 s กับภาพเดียวกัน บิลด์สำหรับพัฒนา รันอย่างละหนึ่งครั้ง) เป็นส่วนหนึ่งของคำสั่งที่ตรึงไว้

<a id="what-it-runs"></a>
## สิ่งที่รัน

| ส่วน | ไฟล์ | แหล่งที่มา |
|---|---|---|
| โมเดล diffusion | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), ฐาน [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Text encoder | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), autoencoder แบบ FLUX.1 |
| เอนจิน | `sd-cli.exe`, stable-diffusion.cpp `32d516c` พร้อมแพตช์ใน [`patches/`](patches) | release v0.3.0 ของรีโพนี้ (`sinirsiz-foto-engine-v0.3.0-win-x64-cuda12.8-sm61.zip`) |
| CUDA runtime | `cudart`, `cublas`, `cublasLt` (12.8) ไม่ได้แก้ไข | zip จาก release wan22-pascal-4gb v0.1.0 |
| cuDNN (ติดตั้งโดยค่าเริ่มต้น; `--no-cudnn` ข้ามขั้นนี้) | DLL 8 ไฟล์ เวอร์ชัน 9.10.2.21 (บิลด์สำหรับ CUDA 11) | เซิร์ฟเวอร์ของ NVIDIA เอง ภายใต้สัญญาอนุญาตของ NVIDIA ไม่ได้เก็บไว้ที่นี่ |

ค่าที่ตรึงไว้: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`
เราไม่ลดจำนวน steps ไม่เพิ่ม negative prompt และไม่เปิด caching เพราะโมเดลถูก distill มาสำหรับ 8 steps และไม่ใช้ negative prompt (ดู [prompts](docs/PROMPTS.md))

## ข้อจำกัด (อ่านก่อนจะพึ่งพา)

- **Windows เท่านั้น** เอนจินที่ build ไว้แล้วและสคริปต์เหล่านี้ใช้ได้กับ Windows เท่านั้น
- **การ์ดหนึ่งใบ เครื่องหนึ่งเครื่อง** วัดผลเฉพาะโน้ตบุ๊ก GTX 1050 Ti 4 GB (i7-7700HQ, RAM 16 GB, Windows 10, ไดรเวอร์ 581.29, โมเดลอยู่บน SSD) ส่วน GPU และไดรเวอร์อื่น, เครื่องที่มี RAM น้อยกว่า 16 GB, Linux และ macOS: **ยังไม่ได้ทดสอบ**
- การ์ดและระบบอื่น (มีเส้นทางใดบ้าง และการทดสอบของชุมชนบนการ์ด AMD ใน Linux ที่เราไม่ได้รันเอง): [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md)
- **เอนจินถูก build สำหรับ Pascal (sm_61) เท่านั้น** สถาปัตยกรรมอื่นต้อง build เอง ([`docs/BUILD.md`](docs/BUILD.md)) เรายังไม่ได้ทดสอบ
- **cuDNN:** เราวัดกับ cuDNN 9.10.2.21 บิลด์สำหรับ CUDA 11 บิลด์สำหรับ CUDA 12 มีไฟล์ต่างออกไปและยังไม่ได้วัด
- **หน่วยความจำตึงมาก** RAM ว่างลดเหลือไม่กี่ร้อย MiB ให้ปิดโปรแกรมอื่นและสร้างทีละภาพ เรายังไม่เคยเห็นหน่วยความจำ GPU หมดหลังจากการตรวจหน่วยความจำของเอนจินผ่านแล้ว และไม่ได้ทดสอบว่าถ้าเกิดขึ้นจะเป็นอย่างไร
- **ขนาดภาพ:** ทดสอบเฉพาะ 768x1344, 1344x768 และ 1024x1024 ขนาดที่ใหญ่กว่านี้จะพิมพ์คำเตือนและอาจหน่วยความจำไม่พอ
- ภาพทำตาม prompt ได้เพียงบางส่วน: ภาพไม่ได้ทำตาม prompt ครบทุกรายละเอียดเสมอไป ตัวอักษรในภาพและสถานที่สำคัญในโลกจริงยังไม่ได้ประเมิน
- reference ของ PSNR คือผล decode บน CPU ของเอนจินเราเอง ไม่ใช่การพัฒนาแยกอิสระ
- ตัวเลขใน [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) มาจากการรันอย่างละหนึ่งครั้ง เว้นแต่จะระบุไว้เป็นอย่างอื่น

## สัญญาอนุญาตและการให้เครดิต

- สคริปต์และเอกสารของรีโพนี้: [Apache-2.0](LICENSE) พร้อมไฟล์ [`NOTICE`](NOTICE) แพตช์ของเอนจินใน [`patches/`](patches) เป็น MIT เช่นเดียวกับโค้ดที่แพตช์ไปแก้
- stable-diffusion.cpp และ ggml เป็น MIT ประกาศของโค้ดบุคคลที่สามที่คอมไพล์รวมอยู่ในเอนจินอยู่ใน [`licenses/`](licenses) และ [`THIRD_PARTY.md`](THIRD_PARTY.md)
- ไฟล์โมเดลไม่ได้เก็บไว้ที่นี่ ดาวน์โหลดจากแหล่งข้างต้นภายใต้สัญญาอนุญาตของแต่ละไฟล์ (Hugging Face ระบุ Apache-2.0 ให้ทุกไฟล์ อ่านเมื่อ 2026-11-13) model card ไม่ได้พูดถึงว่าใครเป็นเจ้าของภาพที่สร้างขึ้น และเราไม่ได้อ้างสิทธิ์เรื่องนี้
- **cuDNN และ CUDA runtime เป็นทรัพย์สินของ NVIDIA** และไม่ได้อยู่ภายใต้สัญญาอนุญาตของรีโพนี้ cuDNN ดาวน์โหลดจากเซิร์ฟเวอร์ของ NVIDIA ภายใต้สัญญาอนุญาตของ NVIDIA (`--no-cudnn` ข้ามขั้นนี้) ส่วน DLL ของ CUDA runtime อยู่ใน zip แยกที่ไม่ได้แก้ไข (CUDA Toolkit EULA, Attachment A) รายละเอียดและสิ่งที่เราตรวจสอบไม่ได้: [`THIRD_PARTY.md`](THIRD_PARTY.md)
- **เครดิต** การเก็บไฟล์ `NOTICE` ไว้กับสำเนาและงานดัดแปลงเป็นเงื่อนไข (Apache-2.0 ข้อ 4) นอกเหนือจากนั้น หากคุณใส่ข้อความทำนอง "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey" เราจะขอบคุณ แต่ไม่ได้บังคับ
- โปรดอ่าน [`ETHICS.md`](ETHICS.md): ทุกภาพเป็นภาพสังเคราะห์ และคุณรับผิดชอบต่อสิ่งที่คุณเผยแพร่

## ร่วมพัฒนา

สิ่งที่มีประโยชน์ที่สุดที่คุณทำได้คือ **ลองกับการ์ดของคุณ** แล้วบอกเราว่าเกิดอะไรขึ้น: ชื่อ GPU, ไดรเวอร์, RAM, `run.json` และบรรทัดท้ายๆ ของล็อก (ฟอร์ม issue "Hardware test report") การแก้ไขเอกสารและสคริปต์ก็ยินดีเช่นกัน ดู [`CONTRIBUTING.md`](CONTRIBUTING.md) การแจ้งปัญหาด้านความปลอดภัยให้ใช้ช่องทางส่วนตัวใน [`SECURITY.md`](SECURITY.md)

[คู่มือติดตั้งสำหรับ AI agent](AGENTS.md) · [ผลการวัด](docs/MEASUREMENTS.md) · [แก้ปัญหา](docs/TROUBLESHOOTING.md) · [การ build เอนจิน](docs/BUILD.md) · [แพตช์](patches/README.md) · [Prompts](docs/PROMPTS.md) · [ซอฟต์แวร์บุคคลที่สาม](THIRD_PARTY.md) · [บันทึกการเปลี่ยนแปลง](CHANGELOG.md)

หน้านี้แปลและปรับให้เหมาะกับผู้อ่านชาวไทยด้วยความช่วยเหลือของ AI หากพบจุดที่ควรแก้ไข ยินดีรับคำแนะนำอย่างยิ่ง ดู [`CONTRIBUTING.md`](CONTRIBUTING.md)
