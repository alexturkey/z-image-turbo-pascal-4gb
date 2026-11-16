[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · **ລາວ** · [Kiswahili](README.sw.md)

# Sınırsız Foto

**ສ້າງຮູບຈາກຂໍ້ຄວາມດ້ວຍ Z-Image-Turbo (Q8_0 GGUF) ຂະໜາດ 768x1344 ເທິງ GTX 1050 Ti ທີ່ມີ VRAM 4 GB (Pascal, sm_61) ດ້ວຍ stable-diffusion.cpp ເທິງ Windows.** ວັດຜົນເທິງແລັບທັອບທີ່ມີ RAM 16 GB ເຊິ່ງໂປຣເຊສໃຊ້ RAM ປະມານ 11 GB. ໃຊ້ seed ດຽວກັນຈະໄດ້ພິກເຊວດຽວກັນທຸກພິກເຊວ; ຜົນການວັດ ແລະ ແພັດຂອງເອັນຈິນເປີດເຜີຍໄວ້ທັງໝົດ, ໄຟລ໌ທີ່ດາວໂຫຼດຖືກລັອກດ້ວຍ sha256, ແລະ AI coding agent ຕິດຕັ້ງໃຫ້ໄດ້ເທື່ອລະຂັ້ນ.

*ບໍ່ເປັນທາງການ. ບໍ່ມີຄວາມກ່ຽວຂ້ອງກັບ Tongyi-MAI (Z-Image), leejet (stable-diffusion.cpp) ຫຼື NVIDIA.*

## ເລີ່ມຕົ້ນທີ່ນີ້

ມີແພັກເກດສຳເລັດຮູບໃຫ້ແລ້ວ, ລອງໃຊ້ກ່ອນໄດ້ເລີຍ. ຖ້າຮາດແວຂອງທ່ານແຕກຕ່າງ ຫຼື ມີຂັ້ນຕອນທີ່ບໍ່ຜ່ານ, ສ່ວນທີ່ເຫຼືອເປີດໄວ້ທັງໝົດ: ແພັດ, ສູດການ build ແລະ ຜົນການວັດຢູ່ໃນ repository ນີ້, ທ່ານຈຶ່ງ build ສຳລັບກາດຂອງຕົນເອງ ຫຼື ດັດແປງໃຊ້ໄດ້.

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

ຂັ້ນທີ 2 ດາວໂຫຼດປະມານ 12.2 GB ແລະ ໃຊ້ເວລາ 29 ນາທີໃນຄັ້ງທີ່ເຮົາວັດ, ເທິງອິນເຕີເນັດຂອງເຮົາ; ມັນຈະສະແດງບລັອກ "Preflight" ກ່ອນ (GPU, RAM ແລະ ພື້ນທີ່ດິດວ່າງຂອງເຄື່ອງທ່ານ ທຽບກັບຄ່າທີ່ເຮົາວັດໄດ້; ສະແດງໃຫ້ເບິ່ງເທົ່ານັ້ນ).
ເຮົາວັດຜົນສະເພາະແລັບທັອບທີ່ມີ GTX 1050 Ti 4 GB (Pascal, compute capability 6.1) ເທົ່ານັ້ນ. ກາດຮຸ່ນອື່ນຍັງບໍ່ໄດ້ທົດສອບ.
ຖ້າທ່ານໃຊ້ AI coding agent (Claude Code, Codex, Cursor ແລະ ເຄື່ອງມືທຳນອງດຽວກັນ), ໃຫ້ຊີ້ໄປທີ່ [`AGENTS.md`](AGENTS.md).

## ພາບລວມເປັນຕົວເລກ

ທຽບກັບໂຄງສ້າງຂອງ v0.1.0: ໜຶ່ງຮູບໃຊ້ເວລາ 193–228 s ແທນທີ່ຈະເປັນ 261.6 s, ຂັ້ນ VAE ໃຊ້ 8.3–15.9 s ແທນທີ່ຈະເປັນ 29.8 ຫາ 36.3 s, ໃຊ້ seed ດຽວກັນໄດ້ພິກເຊວດຽວກັນ, ແລະ ທຸກຕົວເລກໃນ README ນີ້ມີຄຳສັ່ງ ແລະ ໄຟລ໌ຮອງຮັບ.

768x1344, seed 42, 8 steps, ເຄື່ອງດຽວກັນ. ຕົວເລກຂອງ v0.1.0 ມາຈາກ README ຂອງ v0.1.0 (ການທົດສອບຈາກ clean root ແລະ ການຣັນ 5 ຄັ້ງ); ຕົວເລກຂອງ v0.2.0 ມາຈາກການທົດສອບ clean root ຂອງຮຸ່ນນີ້.

| | v0.1.0 (ບໍ່ເຄີຍເຜີຍແຜ່; ໂຄງສ້າງເກົ່າ) | v0.2.0 |
|---|---|---|
| ເວລາຕໍ່ໜຶ່ງຮູບ (ການຣັນ `generate.py` ໜຶ່ງຄັ້ງ) | 261.6 s | 193–228 s |
| VAE decode (ຂັ້ນສຸດທ້າຍ) | 29.8 ຫາ 36.3 s | 8.3–15.9 s |
| ຄວາມໃກ້ຄຽງກັບ reference decode (PSNR, ຍິ່ງສູງຍິ່ງໃກ້) | 38 ຫາ 43 dB | 71 ຫາ 73 dB |
| VRAM ສູງສຸດ (nvidia-smi) | 2949 ຫາ 2957 MiB | 3057–3059 MiB |
| ໜ່ວຍຄວາມຈຳຂອງໂປຣເຊສ, ຄ່າສູງສຸດ | 10.5 ຫາ 10.9 GB (ຕາມທີ່ບັນທຶກໄວ້ຕອນນັ້ນ) | 10 667–10 915 MiB |
| RAM ວ່າງຕ່ຳສຸດທີ່ເຫັນ | 331 ຫາ 576 MiB | 418–545 MiB |

ວິທີອ່ານ: reference ແມ່ນ latent ອັນດຽວກັນທີ່ decode ເທິງ CPU ເປັນກ້ອນດຽວແບບ float32; PSNR ທຽບຜົນ decode ເທິງ GPU ຂອງເຮົາກັບ reference ນັ້ນ (3 ຮູບ). ຄ່ານີ້ບອກວ່າຂັ້ນ VAE ໃກ້ຄຽງກັບ reference ແຄ່ໃດ. ມັນບໍ່ໄດ້ບອກວ່າຮູບງາມຫຼືບໍ່. ຮູບຂອງ v0.2.0 ບໍ່ຕົງກັບ v0.1.0 ທຸກໄບຕ໌ເມື່ອໃຊ້ prompt ແລະ seed ດຽວກັນ, ເພາະເຮົາຕັ້ງໃຈປ່ຽນເສັ້ນທາງຂອງ VAE. ວິທີວັດ ແລະ ສ່ວນທີ່ຍັງບໍ່ໄດ້ວັດຢູ່ທີ່ [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md).

## ຕົວຢ່າງ

**ຮູບທີ່ AI ສ້າງດ້ວຍ repository ນີ້** (Z-Image-Turbo Q8_0, seed 42, 8 steps). ບໍ່ແມ່ນຮູບຖ່າຍຈິງ; ສະຖານທີ່ສຳຄັນ ແລະ ລາຍລະອຽດອາດບໍ່ຖືກຕ້ອງ, ແລະ ຮູບບໍ່ໄດ້ເຮັດຕາມ prompt ຄົບທຸກລາຍລະອຽດສະເໝີໄປ. prompt ທີ່ໃຊ້ຈິງຢູ່ໃນ [`prompts/`](prompts) ແລະ [`docs/PROMPTS.md`](docs/PROMPTS.md).

| | | |
|---|---|---|
| ![ຫໍເອັບເຟວຕອນແສງທອງ](docs/examples/eiffel.jpg) | ![ແກ້ວຊາຕວກກີ](docs/examples/turkish_tea.jpg) | ![ຊາວປະມົງສູງອາຍຸ](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![ບ້ານເທິງເນີນພູ](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![ອິສຕັນບູນເບິ່ງຈາກທາງອາກາດ](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. ບໍ່ແມ່ນຮູບຖ່າຍຈິງ; ສະຖານທີ່ສຳຄັນອາດບໍ່ຖືກຕ້ອງ.

## ເລີ່ມໃຊ້ງານໄວ

ສິ່ງທີ່ຕ້ອງມີ: Windows 10/11, ກາດ NVIDIA ທີ່ມີ VRAM 4 GB, ໄດເວີທີ່ຮອງຮັບ CUDA 12.8 (ວັດຜົນກັບໄດເວີ 581.29; ໄດເວີຮຸ່ນເກົ່າກວ່ານັ້ນຍັງບໍ່ໄດ້ທົດສອບ; ສ່ວນ CUDA runtime ລະບົບດາວໂຫຼດໃຫ້ເອງ), Python 3.10 ຂຶ້ນໄປ,
git, ພື້ນທີ່ດິດວ່າງປະມານ 14 GB (ໄຟລ໌ທີ່ດາວໂຫຼດປະມານ 12.2 GB ເມື່ອລວມ cuDNN; ຕົວເລກພື້ນທີ່ວ່າງເປັນຄ່າປະມານ), ແລະ RAM 16 GB (ຕາມທີ່ວັດໄວ້; ຖ້ານ້ອຍກວ່ານີ້ຍັງບໍ່ໄດ້ທົດສອບ).

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- `setup.py` ສະແດງບລັອກ "Preflight" ກ່ອນ (GPU, RAM ແລະ ພື້ນທີ່ດິດວ່າງຂອງເຄື່ອງທ່ານ ທຽບກັບຄ່າທີ່ເຮົາວັດໄດ້; ສະແດງໃຫ້ເບິ່ງເທົ່ານັ້ນ ແລະ ບໍ່ເຄີຍຂັດຂວາງ). ຈາກນັ້ນດາວໂຫຼດຈາກທີ່ຢູ່ທີ່ລັອກໄວ້ໃນ [`models.lock.json`](models.lock.json) ແລະ ກວດທຸກໄຟລ໌ດ້ວຍ sha256. ມັນພິມ `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK`, ຕາມດ້ວຍ `CUDNN_OK` ຫຼື `CUDNN_SKIPPED`, ແລະ ປິດທ້າຍດ້ວຍ `SETUP_OK`.
  ຖ້າບໍ່ລະບຸ `--models-dir` ແລະ `--bin-dir` ຈະໃຊ້ `models/` ແລະ `bin/` ທີ່ຮາກຂອງ repository; ຄວນວາງໂມເດວໄວ້ເທິງ SSD (ເຮົາວັດຜົນເທິງ SSD ເທົ່ານັ້ນ).
  ຢຸດໄດ້ທຸກເວລາດ້ວຍ Ctrl+C ແລ້ວຣັນຄຳສັ່ງເດີມອີກຄັ້ງ: ການດາວໂຫຼດຈະສືບຕໍ່ຈາກໄຟລ໌ `.part`.
- **cuDNN ຖືກຕິດຕັ້ງໂດຍຄ່າເລີ່ມຕົ້ນ ແລະ ບໍ່ໄດ້ເປັນສ່ວນໜຶ່ງຂອງ repository ນີ້.** ມັນເປັນຊອບແວຂອງ NVIDIA ພາຍໃຕ້ໃບອະນຸຍາດຂອງ NVIDIA ເອງ ([ຂໍ້ຄວາມໃບອະນຸຍາດ](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)) ສຳລັບລະບົບທີ່ມີ GPU ຂອງ NVIDIA. ມັນດາວໂຫຼດຈາກເຊີບເວີຂອງ NVIDIA ໂດຍບໍ່ມີການເກັບເງິນ ແລະ ບໍ່ຕ້ອງເຂົ້າສູ່ລະບົບ, ແລະ ເຮົາບໍ່ພົບຂໍ້ຄວາມໃດໃນໃບອະນຸຍາດທີ່ຈຳກັດການນຳໃຊ້ທາງການຄ້າ ຫຼື ສ່ວນຕົວ. `setup.py` ຈະສະແດງທີ່ຢູ່ຂອງໃບອະນຸຍາດ, ດາວໂຫຼດໄຟລ໌ ແລະ ສຳເນົາພຽງແປດໄຟລ໌ DLL ໄປວາງຂ້າງ `sd-cli.exe`. ໃບອະນຸຍາດຂອງ NVIDIA ລະບຸວ່າຜູ້ທີ່ບໍ່ຍອມຮັບເງື່ອນໄຂຂອງມັນຕ້ອງບໍ່ດາວໂຫຼດ, ຕິດຕັ້ງ ຫຼື ນຳໃຊ້ມັນ; ໃນກໍລະນີນັ້ນໃຫ້ແລ່ນ `python scripts/setup.py --no-cudnn`. ຖ້າບໍ່ມີ cuDNN ທຸກຢ່າງຍັງໃຊ້ງານໄດ້ດ້ວຍເສັ້ນທາງ VAE ແບບ v0.1.0 ທີ່ຊ້າກວ່າ (`--vae legacy`), ແລະ `generate.py` ຈະແຈ້ງໃຫ້ຮູ້.
- `generate.py` ຂຽນ `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, `run.json` (ເວລາ, ແຕ່ລະຂັ້ນ, ເສັ້ນທາງ VAE ທີ່ໃຊ້, VRAM ສູງສຸດ, ຄຳສັ່ງທີ່ໃຊ້ຈິງ) ແລະ `log.txt`, ແລ້ວພິມ `IMAGE_OK <path>`.

## ວິທີໃຊ້

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| ຕົວເລືອກ | ຄວາມໝາຍ |
|---|---|
| `--prompt "<text>"` ຫຼື `--prompt-file <txt>` | prompt (ຕ້ອງລະບຸຢ່າງໃດຢ່າງໜຶ່ງ) |
| `--width`, `--height` | ຕ້ອງເປັນຜົນຄູນຂອງ 16, ຢູ່ລະຫວ່າງ 256 ຫາ 2048; ຄ່າເລີ່ມຕົ້ນ 768x1344; ຂະໜາດທີ່ທົດສອບແລ້ວ: 768x1344, 1344x768, 1024x1024 |
| `--seed` | ຄ່າເລີ່ມຕົ້ນ 42 |
| `--out`, `--name` | ໂຟນເດີຮາກຂອງຜົນລັບ (ຄ່າເລີ່ມຕົ້ນ `outputs/`) ແລະ ຊື່ສັ້ນໆຂອງໂຟນເດີການຣັນນັ້ນ |
| `--models-dir`, `--bin-dir` | ບ່ອນທີ່ `setup.py` ວາງໂມເດວ ແລະ ເອັນຈິນ |
| `--vae auto` (ຄ່າເລີ່ມຕົ້ນ) | cuDNN float32; ລອງກ້ອນດຽວກ່ອນ, ແລ້ວໃຊ້ໄທລ໌ໃຫຍ່ສອງຊິ້ນ, ແລ້ວຈຶ່ງໃຊ້ໄທລ໌ນ້ອຍຕາມຄ່າເລີ່ມຕົ້ນ |
| `--vae tiled` | cuDNN float32, ໃຊ້ໄທລ໌ໃຫຍ່ສອງຊິ້ນສະເໝີ |
| `--vae legacy` | ເສັ້ນທາງຂອງ v0.1.0: ບໍ່ໃຊ້ cuDNN, ໃຊ້ໄທລ໌ນ້ອຍ. ຖືກໃຊ້ອັດຕະໂນມັດ (ພ້ອມຄຳເຕືອນ) ເມື່ອບໍ່ພົບ DLL ຂອງ cuDNN |

ຈຳນວນ steps (8), cfg (1.0), sampler ແລະ scheduler ຖືກກຳນົດຄົງທີ່ໄວ້ໂດຍຕັ້ງໃຈ; ເບິ່ງ [ສິ່ງທີ່ຣັນ](#what-it-runs).

## ກວດສອບດ້ວຍຕົນເອງ

- `generate.py` ພິມ `PIXEL_SHA256 <hex>` ໃນແຖວທ້າຍໆ: ເປັນຄ່າແຮຊຂອງພິກເຊວທີ່ decode ແລ້ວ. ຣັນຄຳສັ່ງເດີມສອງຄັ້ງແລ້ວທຽບຮູບທັງສອງ: `python scripts/compare.py <run A>/image.png <run B>/image.png` ຄວນພິມ `SAME_PIXELS`.
- ຄ່າ `PIXEL_SHA256` ຂອງຕົວຢ່າງທັງຫ້າຮູບເທິງເຄື່ອງຂອງເຮົາຢູ່ໃນ [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md). ແຮຊຂອງໄຟລ໌ PNG ອາດຕ່າງກັນໄດ້ ເຖິງວ່າພິກເຊວຈະຄືກັນ, ເພາະ PNG ເກັບພາຣາມິເຕີການສ້າງຮູບໄວ້ເປັນຂໍ້ຄວາມ; ໃຫ້ທຽບພິກເຊວ, ບໍ່ແມ່ນທຽບໄຟລ໌.
- ຂໍ້ຈຳກັດທີ່ຕ້ອງບອກຕົງໆ: ເຮົາບໍ່ໄດ້ວັດວ່າກາດ ຫຼື ໄດເວີອື່ນໃຫ້ພິກເຊວຄືກັນຫຼືບໍ່.

## ເປັນຫຍັງຈຶ່ງໃສ່ໄດ້ໃນ 4 GB

- **ຜູ້ສ້າງໂມເດວບອກວ່າແນວໃດ.** model card ຂອງ Z-Image-Turbo ລະບຸວ່າໂມເດວ "fits comfortably within 16G VRAM consumer devices" ([model card](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)). ນັ້ນໝາຍເຖິງກາດຂະໜາດ 16 GB. README ທາງການຍັງລະບຸ stable-diffusion.cpp ເປັນທາງເລືອກຈາກບຸກຄົນທີສາມ ແລະ ອ້າງເຖິງ "as little as 4GB of VRAM" ([README](https://github.com/Tongyi-MAI/Z-Image)); ນັ້ນເປັນຄຳກ່າວອ້າງຂອງໂປຣເຈັກ stable-diffusion.cpp, ບໍ່ແມ່ນຂໍ້ກຳນົດຂອງທີມ Z-Image.
- **ສິ່ງທີ່ເຮົາວັດໄດ້.** Z-Image-Turbo Q8_0 (ໄຟລ໌ຂະໜາດ 6.6 GB) ກັບ text encoder Qwen3-4B Q8_0 ທີ່ 768x1344: ຄ່າສູງສຸດຂອງ GPU ທີ່ nvidia-smi ສຸ່ມອ່ານທຸກ 2 s (ຄ່າພຸ່ງສັ້ນໆອາດພາດໄດ້) ຢູ່ທີ່ 2949 ຫາ 2957 MiB (ເອັນຈິນ v0.1.0) ແລະ 3057–3059 MiB (ເອັນຈິນ v0.2.0) ເທິງກາດຂະໜາດ 4096 MiB. ນ້ຳໜັກໂມເດວ (10 509 MiB; ລັອກຂອງເອັນຈິນພິມເປັນ MB) ຢູ່ໃນ RAM ຂອງລະບົບ; ເອັນຈິນສຳເນົາເຄືອຂ່າຍໄປທີ່ GPU ເທື່ອລະ segment (ຊິ້ນສ່ວນຂອງເຄືອຂ່າຍ): ມີ 36 segments, ຕາມແຖວລັອກ `z_image using 36 segments`.
- **ລາຄາທີ່ຕ້ອງຈ່າຍ.** ແມ່ນເວລາ ແລະ ໜ່ວຍຄວາມຈຳຂອງລະບົບ: 193–228 s ຕໍ່ໜຶ່ງຮູບ, ແລະ ໂປຣເຊສຂອງເອັນຈິນຖື RAM ປະມານ 10 667–10 915 MiB (ລວມໜ້າໂມເດວທີ່ memory-mapped) ເທິງເຄື່ອງ 16 GB, ດັ່ງນັ້ນ RAM ວ່າງຈະຫຼຸດເຫຼືອບໍ່ເທົ່າໃດຮ້ອຍ MiB ລະຫວ່າງທີ່ຣັນ.
- **ວິທີຂອງຄົນອື່ນ.** ມີລາຍງານວ່າຣັນ Z-Image ເທິງກາດ 4 GB ໄດ້ດ້ວຍ quantization ທີ່ຕ່ຳກວ່າ ຫຼື ຂະໜາດຮູບທີ່ນ້ອຍກວ່າ (ຕົວຢ່າງ ໜ້າ wiki ຂອງ stable-diffusion.cpp ສຳລັບກາດ 4 GB ແນະນຳ Q3_K ຫຼື Q4_0 ທີ່ 1024x512). ໃນບ່ອນທີ່ເຮົາໄປຄົ້ນເບິ່ງ (ລາຍການ ແລະ ວັນທີຢູ່ໃນ [`docs/RELATED.md`](docs/RELATED.md)) ເຮົາບໍ່ພົບວິທີທີ່ເຜີຍແຜ່ແລ້ວທີ່ລວມຄົບທັງສີ່ຢ່າງ: ກາດ 4 GB, Q8_0, 768x1344 ຫຼື ໃຫຍ່ກວ່າ, ແລະ ມີການວັດເວລາກັບໜ່ວຍຄວາມຈຳ GPU ໄວ້. ນີ້ເປັນຄຳກ່າວກ່ຽວກັບບ່ອນທີ່ເຮົາຄົ້ນເບິ່ງ, ບໍ່ແມ່ນກ່ຽວກັບທຸກບ່ອນ.
- **ໃຜເຮັດຫຍັງ.** ການໃສ່ໄດ້ໃນ 4 GB ມາຈາກ stable-diffusion.cpp ເອງ: `--offload-to-cpu`, `--mmap`, ການເຮັດວຽກເທື່ອລະຊິ້ນ, ແລະ flash attention (ເມື່ອປິດ flash attention ການຣັນໃຊ້ 4205 MB ແລະ ໃສ່ບໍ່ພໍ). ແພັດຂອງເຮົາເຮັດເພື່ອຄວາມໄວ ແລະ ຂັ້ນ VAE ທີ່ດີຂຶ້ນ, ບໍ່ໄດ້ເຮັດເພື່ອໃຫ້ໃສ່ໄດ້. ເຮົາບໍ່ໄດ້ຣັນເອັນຈິນ upstream ທີ່ບໍ່ມີແພັດເທິງກາດໃບນີ້, ຈຶ່ງບອກບໍ່ໄດ້ວ່າໃສ່ໄດ້ຫຼືບໍ່.

## ເຮັດວຽກແນວໃດ

ມີການປ່ຽນແປງສາມຢ່າງເທິງ stable-diffusion.cpp `master-1088-32d516c` (ທັງໝົດເປັນສະວິດ; ຕາຕະລາງໃນ [`patches/README.md`](patches/README.md) ລະບຸແຕ່ລະຢ່າງພ້ອມຕົວແປສະພາບແວດລ້ອມຂອງມັນ):

1. **refiner ຣັນໜຶ່ງຄັ້ງຕໍ່ໜຶ່ງ step.** ຊື່ກຸ່ມຖືກໃຊ້ຊ້ຳສອງເທື່ອ, ເຮັດໃຫ້ບລັອກ refiner ສີ່ບລັອກຖືກຄິດໄລ່ຊ້ຳອີກຮອບ. ເມື່ອແກ້ແລ້ວ steps ທີ 2 ຫາ 8 ໄວຂຶ້ນປະມານ 1.3 s ຕໍ່ step (ຈາກ 22.0 ເປັນ 20.7 s) ແລະ ຮູບທີ່ໄດ້ຄືເກົ່າທຸກພິກເຊວ (ກວດ 3 ຮູບ).
2. **VAE ຜ່ານ cuDNN ແບບ float32.** ຂັ້ນສຸດທ້າຍ (ປ່ຽນ latent ເປັນພິກເຊວ) ໃຊ້ convolution ແບບ float32 ຂອງ cuDNN ຈາກ NVIDIA. ເທິງກາດຂອງເຮົາ VAE ຫຼຸດຈາກ 23 ຫາ 27 s ເຫຼືອ 10 ຫາ 15 s ແລະ PSNR ທຽບກັບ reference ຂະຫຍັບຈາກ 38 ຫາ 43 dB ເປັນ 45 ຫາ 49 dB (ໄທລ໌ໃຫຍ່).
3. **ລອງກ້ອນດຽວກ່ອນ.** ດຽວນີ້ເອັນຈິນຈະລອງ decode ທັງຮູບເປັນກ້ອນດຽວເມື່ອການກວດໜ່ວຍຄວາມຈຳບອກວ່າໃສ່ໄດ້ (ສ່ວນເຜື່ອ 256 MiB), ຖ້າບໍ່ໄດ້ກໍຖອຍໄປໃຊ້ໄທລ໌ (tile) ໃຫຍ່ສອງຊິ້ນ, ແລະ ຖ້າຍັງບໍ່ໄດ້ກໍໃຊ້ໄທລ໌ນ້ອຍ. ເມື່ອ decode ເປັນກ້ອນດຽວ VAE ໃຊ້ເວລາປະມານ 8–16 s ແລະ PSNR ທຽບກັບ reference ຢູ່ທີ່ 71 ຫາ 73 dB. ຖ້າເກີດການຖອຍແບບບັງຄັບ, ຮູບທີ່ໄດ້ມີພິກເຊວຄືກັບແບບໄທລ໌ (ກວດດ້ວຍ `PIXEL_SHA256`). ສິ່ງທີ່ເກີດຂຶ້ນຈິງບັນທຶກໄວ້ໃນ `run.json` (`stages.vae_path`: `full`, `tile`, `floor` ຫຼື `retry`).

ນອກຈາກນີ້: `--eager-load` (ອ່ານໜ້າໂມເດວລ່ວງໜ້າ; ຈາກ 241.2 s ເຫຼືອ 220.3 s ກັບຮູບດຽວກັນ, ບິລດ໌ສຳລັບພັດທະນາ, ຣັນຢ່າງລະໜຶ່ງຄັ້ງ) ເປັນສ່ວນໜຶ່ງຂອງຄຳສັ່ງທີ່ກຳນົດຄົງທີ່ໄວ້.

<a id="what-it-runs"></a>
## ສິ່ງທີ່ຣັນ

| ສ່ວນ | ໄຟລ໌ | ແຫຼ່ງທີ່ມາ |
|---|---|---|
| ໂມເດວ diffusion | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), ຖານ [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Text encoder | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), autoencoder ແບບ FLUX.1 |
| ເອັນຈິນ | `sd-cli.exe`, stable-diffusion.cpp `32d516c` ພ້ອມແພັດໃນ [`patches/`](patches) | release v0.2.0 ຂອງ repository ນີ້ (`sinirsiz-foto-engine-v0.2.0-win-x64-cuda12.8-sm61.zip`) |
| CUDA runtime | `cudart`, `cublas`, `cublasLt` (12.8), ບໍ່ໄດ້ແກ້ໄຂ | zip ຈາກ release wan22-pascal-4gb v0.1.0 |
| cuDNN (ຕິດຕັ້ງໂດຍຄ່າເລີ່ມຕົ້ນ; `--no-cudnn` ຂ້າມຂັ້ນນີ້) | DLL 8 ໄຟລ໌, ເວີຊັນ 9.10.2.21 (ບິລດ໌ສຳລັບ CUDA 11) | ເຊີບເວີຂອງ NVIDIA ເອງ, ພາຍໃຕ້ໃບອະນຸຍາດຂອງ NVIDIA; ບໍ່ໄດ້ເກັບໄວ້ທີ່ນີ້ |

ຄ່າທີ່ກຳນົດຄົງທີ່ໄວ້: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`.
ເຮົາບໍ່ຫຼຸດຈຳນວນ steps, ບໍ່ເພີ່ມ negative prompt ແລະ ບໍ່ເປີດ caching: ໂມເດວຖືກ distill ມາສຳລັບ 8 steps ແລະ ບໍ່ໃຊ້ negative prompt (ເບິ່ງ [prompts](docs/PROMPTS.md)).

## ຂໍ້ຈຳກັດ (ອ່ານກ່ອນຈະເພິ່ງພາ)

- **Windows ເທົ່ານັ້ນ.** ເອັນຈິນທີ່ build ໄວ້ແລ້ວ ແລະ ສະຄຣິບເຫຼົ່ານີ້ໃຊ້ໄດ້ກັບ Windows ເທົ່ານັ້ນ.
- **ກາດໜຶ່ງໃບ, ເຄື່ອງໜຶ່ງເຄື່ອງ.** ວັດຜົນສະເພາະແລັບທັອບ GTX 1050 Ti 4 GB (i7-7700HQ, RAM 16 GB, Windows 10, ໄດເວີ 581.29, ໂມເດວຢູ່ເທິງ SSD). GPU ແລະ ໄດເວີອື່ນ, ເຄື່ອງທີ່ມີ RAM ໜ້ອຍກວ່າ 16 GB, Linux ແລະ macOS: **ຍັງບໍ່ໄດ້ທົດສອບ**.
- ກາດ ແລະ ລະບົບອື່ນ (ມີທາງໃດແດ່ ແລະ ການທົດສອບຂອງຊຸມຊົນເທິງກາດ AMD ໃນ Linux ທີ່ພວກເຮົາບໍ່ໄດ້ແລ່ນເອງ): [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md).
- **ເອັນຈິນຖືກ build ສຳລັບ Pascal (sm_61) ເທົ່ານັ້ນ.** ສະຖາປັດຕະຍະກຳອື່ນຕ້ອງ build ເອງ ([`docs/BUILD.md`](docs/BUILD.md)); ເຮົາຍັງບໍ່ໄດ້ທົດສອບ.
- **cuDNN:** ເຮົາວັດກັບ cuDNN 9.10.2.21 ບິລດ໌ສຳລັບ CUDA 11. ບິລດ໌ສຳລັບ CUDA 12 ມີໄຟລ໌ຕ່າງອອກໄປ ແລະ ຍັງບໍ່ໄດ້ວັດ.
- **ໜ່ວຍຄວາມຈຳຄັບແຄບຫຼາຍ.** RAM ວ່າງຫຼຸດເຫຼືອບໍ່ເທົ່າໃດຮ້ອຍ MiB; ໃຫ້ປິດໂປຣແກຣມອື່ນ ແລະ ສ້າງເທື່ອລະຮູບ. ເຮົາຍັງບໍ່ເຄີຍເຫັນໜ່ວຍຄວາມຈຳ GPU ໝົດຫຼັງຈາກການກວດໜ່ວຍຄວາມຈຳຂອງເອັນຈິນຜ່ານແລ້ວ, ແລະ ບໍ່ໄດ້ທົດສອບວ່າຖ້າເກີດຂຶ້ນຈະເປັນແນວໃດ.
- **ຂະໜາດຮູບ:** ທົດສອບສະເພາະ 768x1344, 1344x768 ແລະ 1024x1024. ຂະໜາດທີ່ໃຫຍ່ກວ່ານີ້ຈະພິມຄຳເຕືອນ ແລະ ອາດໜ່ວຍຄວາມຈຳບໍ່ພໍ.
- ຮູບເຮັດຕາມ prompt ໄດ້ພຽງບາງສ່ວນ: ຮູບບໍ່ໄດ້ເຮັດຕາມ prompt ຄົບທຸກລາຍລະອຽດສະເໝີໄປ. ຕົວອັກສອນໃນຮູບ ແລະ ສະຖານທີ່ສຳຄັນໃນໂລກຈິງຍັງບໍ່ໄດ້ປະເມີນ.
- reference ຂອງ PSNR ແມ່ນຜົນ decode ເທິງ CPU ຂອງເອັນຈິນເຮົາເອງ, ບໍ່ແມ່ນການພັດທະນາແຍກອິດສະຫຼະ.
- ຕົວເລກໃນ [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) ມາຈາກການຣັນຢ່າງລະໜຶ່ງຄັ້ງ ເວັ້ນແຕ່ຈະລະບຸໄວ້ເປັນຢ່າງອື່ນ.

## ໃບອະນຸຍາດ ແລະ ການໃຫ້ເຄຣດິດ

- ສະຄຣິບ ແລະ ເອກະສານຂອງ repository ນີ້: [Apache-2.0](LICENSE) ພ້ອມໄຟລ໌ [`NOTICE`](NOTICE). ແພັດຂອງເອັນຈິນໃນ [`patches/`](patches) ເປັນ MIT ເຊັ່ນດຽວກັບໂຄ້ດທີ່ແພັດໄປແກ້.
- stable-diffusion.cpp ແລະ ggml ເປັນ MIT. ປະກາດຂອງໂຄ້ດບຸກຄົນທີສາມທີ່ຄອມໄພລ໌ລວມຢູ່ໃນເອັນຈິນຢູ່ໃນ [`licenses/`](licenses) ແລະ [`THIRD_PARTY.md`](THIRD_PARTY.md).
- ໄຟລ໌ໂມເດວບໍ່ໄດ້ເກັບໄວ້ທີ່ນີ້; ດາວໂຫຼດຈາກແຫຼ່ງຂ້າງເທິງພາຍໃຕ້ໃບອະນຸຍາດຂອງແຕ່ລະໄຟລ໌ (Hugging Face ລະບຸ Apache-2.0 ໃຫ້ທຸກໄຟລ໌, ອ່ານເມື່ອ 2026-11-13). model card ບໍ່ໄດ້ກ່າວເຖິງວ່າໃຜເປັນເຈົ້າຂອງຮູບທີ່ສ້າງຂຶ້ນ, ແລະ ເຮົາບໍ່ໄດ້ອ້າງສິດເລື່ອງນີ້.
- **cuDNN ແລະ CUDA runtime ເປັນຊັບສິນຂອງ NVIDIA** ແລະ ບໍ່ໄດ້ຢູ່ພາຍໃຕ້ໃບອະນຸຍາດຂອງ repository ນີ້. cuDNN ດາວໂຫຼດຈາກເຊີບເວີຂອງ NVIDIA ພາຍໃຕ້ໃບອະນຸຍາດຂອງ NVIDIA (`--no-cudnn` ຂ້າມຂັ້ນນີ້); ສ່ວນ DLL ຂອງ CUDA runtime ຢູ່ໃນ zip ແຍກທີ່ບໍ່ໄດ້ແກ້ໄຂ (CUDA Toolkit EULA, Attachment A). ລາຍລະອຽດ ແລະ ສິ່ງທີ່ເຮົາກວດສອບບໍ່ໄດ້: [`THIRD_PARTY.md`](THIRD_PARTY.md).
- **ເຄຣດິດ.** ການເກັບໄຟລ໌ `NOTICE` ໄວ້ກັບສຳເນົາ ແລະ ງານດັດແປງເປັນເງື່ອນໄຂ (Apache-2.0 ຂໍ້ 4). ນອກເໜືອຈາກນັ້ນ, ຖ້າທ່ານໃສ່ຂໍ້ຄວາມທຳນອງ "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey" ເຮົາຈະຂອບໃຈ, ແຕ່ບໍ່ໄດ້ບັງຄັບ.
- ກະລຸນາອ່ານ [`ETHICS.md`](ETHICS.md): ທຸກຮູບເປັນຮູບສັງເຄາະ, ແລະ ທ່ານຮັບຜິດຊອບຕໍ່ສິ່ງທີ່ທ່ານເຜີຍແຜ່.

## ການຮ່ວມພັດທະນາ

ສິ່ງທີ່ມີປະໂຫຍດທີ່ສຸດທີ່ທ່ານເຮັດໄດ້ແມ່ນ **ລອງກັບກາດຂອງທ່ານ** ແລ້ວບອກເຮົາວ່າເກີດຫຍັງຂຶ້ນ: ຊື່ GPU, ໄດເວີ, RAM, `run.json` ແລະ ແຖວທ້າຍໆຂອງລັອກ (ຟອມ issue "Hardware test report"). ການແກ້ໄຂເອກະສານ ແລະ ສະຄຣິບກໍຍິນດີຮັບເຊັ່ນກັນ; ເບິ່ງ [`CONTRIBUTING.md`](CONTRIBUTING.md). ການແຈ້ງບັນຫາດ້ານຄວາມປອດໄພໃຫ້ໃຊ້ຊ່ອງທາງສ່ວນຕົວໃນ [`SECURITY.md`](SECURITY.md).

[ຄູ່ມືຕິດຕັ້ງສຳລັບ AI agent](AGENTS.md) · [ຜົນການວັດ](docs/MEASUREMENTS.md) · [ແກ້ບັນຫາ](docs/TROUBLESHOOTING.md) · [ການ build ເອັນຈິນ](docs/BUILD.md) · [ແພັດ](patches/README.md) · [Prompts](docs/PROMPTS.md) · [ຊອບແວບຸກຄົນທີສາມ](THIRD_PARTY.md) · [ບັນທຶກການປ່ຽນແປງ](CHANGELOG.md)

ໜ້ານີ້ແປ ແລະ ປັບໃຫ້ເໝາະກັບຜູ້ອ່ານຊາວລາວດ້ວຍຄວາມຊ່ວຍເຫຼືອຂອງ AI; ຖ້າພົບຈຸດທີ່ຄວນແກ້ໄຂ ຍິນດີຮັບຄຳແນະນຳຢ່າງຍິ່ງ, ເບິ່ງ [`CONTRIBUTING.md`](CONTRIBUTING.md).
