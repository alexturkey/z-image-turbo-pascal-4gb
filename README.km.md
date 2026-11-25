[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · **ខ្មែរ** · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**ការបង្កើតរូបភាពពីអត្ថបទ (text-to-image) ដោយ Z-Image-Turbo (Q8_0 GGUF) ទំហំ 768x1344 លើ GTX 1050 Ti (Pascal, sm_61) ទំហំ 4 GB ជាមួយ stable-diffusion.cpp លើ Windows។** បានវាស់លើកុំព្យូទ័រយួរដៃដែលមាន RAM 16 GB ដែលដំណើរការនេះប្រើ RAM ប្រហែល 11 GB។ seed ដូចគ្នាផ្ដល់ភីកសែលដូចគ្នា ភីកសែលទល់នឹងភីកសែល។ លទ្ធផលវាស់ និងបំណះរបស់ម៉ាស៊ីនត្រូវបានបោះពុម្ពផ្សាយ ការទាញយកត្រូវបានចាក់សោដោយ sha256 ហើយភ្នាក់ងារសរសេរកូដ AI អាចដំឡើងវាបានម្ដងមួយជំហាន។

*មិនផ្លូវការ។ មិនមានទំនាក់ទំនងជាមួយ Tongyi-MAI (Z-Image), leejet (stable-diffusion.cpp) ឬ NVIDIA ឡើយ។*

## ចាប់ផ្ដើមនៅទីនេះ

មានកញ្ចប់ដែលរៀបចំរួចរាល់ ដូច្នេះសូមសាកល្បងវាមុន។ បើផ្នែករឹងរបស់អ្នកខុសគ្នា ឬមានជំហានណាមួយបរាជ័យ អ្វីៗផ្សេងទៀតនៅបើកចំហ៖ បំណះ រូបមន្ត build និងលទ្ធផលវាស់ សុទ្ធតែនៅក្នុង repository នេះ ដូច្នេះអ្នកអាច build សម្រាប់កាតរបស់អ្នកផ្ទាល់ ឬកែសម្រួលវាបាន។

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

ជំហាន 2 ទាញយកប្រហែល 12.2 GB ហើយបានចំណាយពេល 29 នាទី ម្ដង លើអ៊ីនធឺណិតរបស់យើង។ វាបោះពុម្ពប្លុក "Preflight" ជាមុន (GPU, RAM និងទំហំថាសទំនេររបស់អ្នក ដាក់ក្បែរតម្លៃដែលយើងបានវាស់ ហើយវាគ្រាន់តែជូនដំណឹង)។
មានតែកាតកុំព្យូទ័រយួរដៃ GTX 1050 Ti 4 GB (Pascal, compute capability 6.1) ប៉ុណ្ណោះដែលត្រូវបានវាស់។ កាតផ្សេងទៀតមិនទាន់បានសាកល្បងទេ។
បើអ្នកប្រើភ្នាក់ងារសរសេរកូដ AI (Claude Code, Codex, Cursor និងស្រដៀងគ្នា) សូមបង្ហាញវាទៅកាន់ [`AGENTS.md`](AGENTS.md)។

## សង្ខេប

ប្រៀបធៀបនឹងទម្រង់ v0.1.0៖ រូបភាពមួយប្រើពេល 188–193 s ជំនួសឱ្យ 261.6 s ដំណាក់កាល VAE ប្រើពេល 12.5–21.7 s ជំនួសឱ្យ 29.8 ដល់ 36.3 s seed ដូចគ្នាផ្ដល់ភីកសែលដូចគ្នា ហើយគ្រប់លេខក្នុង README នេះសុទ្ធតែមានពាក្យបញ្ជា និងឯកសារមួយនៅពីក្រោយ។

768x1344, seed 42, 8 ជំហាន, ម៉ាស៊ីនតែមួយ។ លេខ v0.1.0 មកពី README របស់ v0.1.0 (ការធ្វើតេស្តពី root ស្អាត និងការរត់ប្រាំដង)។ លេខ v0.3.0 មកពីការធ្វើតេស្តពី root ស្អាតនៃកំណែនេះ។

| | v0.1.0 (មិនដែលបានផ្សព្វផ្សាយ; ទម្រង់ចាស់) | v0.3.0 |
|---|---|---|
| ពេលសម្រាប់រូបភាពមួយ (ការរត់ `generate.py` មួយដង) | 261.6 s | 188–193 s |
| VAE decode (ដំណាក់កាលចុងក្រោយ) | 29.8 ដល់ 36.3 s | 12.5–21.7 s |
| ភាពជិតនឹង decode យោង (PSNR, ខ្ពស់ជាង គឺជិតជាង) | 38 ដល់ 43 dB | 71 ដល់ 73 dB |
| អង្គចងចាំ GPU ខ្ពស់បំផុត (nvidia-smi) | 2949 ដល់ 2957 MiB | 3057–3059 MiB |
| អង្គចងចាំដំណើរការ ខ្ពស់បំផុត | 10.5 ដល់ 10.9 GB (ដូចបានកត់ត្រាពេលនោះ) | 10 489–11 203 MiB |
| RAM ទំនេរទាបបំផុតដែលបានឃើញ | 331 ដល់ 576 MiB | 303–532 MiB |

របៀបអាន៖ ឯកសារយោងគឺ latent ដដែលដែលត្រូវបាន decode លើ CPU ជាដុំតែមួយក្នុង float32។ PSNR ប្រៀបធៀប decode លើ GPU របស់យើងជាមួយវា (រូបភាព 3)។ វាប្រាប់ថាដំណាក់កាល VAE ជិតនឹងឯកសារយោងនោះប៉ុនណា។ វាមិនប្រាប់ថារូបភាពមួយស្អាតប៉ុនណាទេ។ រូបភាព v0.2.0 មិនដូច v0.1.0 ដល់កម្រិតបៃទល់នឹងបៃទេ សម្រាប់ prompt និង seed ដូចគ្នា ព្រោះផ្លូវ VAE ត្រូវបានផ្លាស់ប្ដូរដោយចេតនា។ វិធីសាស្ត្រ និងផ្នែកដែលមិនទាន់បានវាស់៖ [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md)។

## ឧទាហរណ៍

**បង្កើតដោយ AI ជាមួយ repository នេះ** (Z-Image-Turbo Q8_0, seed 42, 8 ជំហាន)។ ទាំងនេះមិនមែនជារូបថតពិតទេ។ សំណង់ និងព័ត៌មានលម្អិតអាចមិនត្រឹមត្រូវ ហើយរូបភាពមិនតែងតែធ្វើតាម prompt គ្រប់ព័ត៌មានលម្អិតទេ។ prompt ពេញលេញមាននៅក្នុង [`prompts/`](prompts) និង [`docs/PROMPTS.md`](docs/PROMPTS.md)។

| | | |
|---|---|---|
| ![ប៉មអេហ្វែលនៅម៉ោងមាស](docs/examples/eiffel.jpg) | ![ពែងតែតួកគី](docs/examples/turkish_tea.jpg) | ![អ្នកនេសាទវ័យចំណាស់](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![ភូមិនៅលើជម្រាលភ្នំ](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![អ៊ីស្តង់ប៊ុលពីលើអាកាស](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768។ មិនមែនរូបថតពិតទេ; សំណង់អាចមិនត្រឹមត្រូវ។

## ចាប់ផ្ដើមរហ័ស

តម្រូវការ៖ Windows 10/11, GPU NVIDIA ទំហំ 4 GB, ដ្រាយវើរដែលគាំទ្រ CUDA 12.8 (ដ្រាយវើរ 581.29 ត្រូវបានវាស់; ដ្រាយវើរចាស់ជាងនេះមិនទាន់បានសាកល្បង; CUDA runtime ខ្លួនឯងត្រូវបានទាញយកឱ្យអ្នក), Python 3.10 ឬថ្មីជាងនេះ,
git, ថាសទំនេរប្រហែល 14 GB (ទំហំទាញយកប្រហែល 12.2 GB ជាមួយ cuDNN; តួលេខថាសទំនេរគ្រាន់តែជាការប៉ាន់ស្មាន) និង RAM 16 GB (ទំហំដែលបានវាស់; តិចជាងនេះមិនទាន់បានសាកល្បង)។

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- `setup.py` បោះពុម្ពប្លុក "Preflight" ជាមុន (GPU, RAM និងទំហំថាសទំនេររបស់អ្នក ដាក់ក្បែរតម្លៃដែលយើងបានវាស់; វាគ្រាន់តែជូនដំណឹង ហើយមិនដែលរារាំងអ្វីឡើយ)។ បន្ទាប់មកវាទាញយកពីអាសយដ្ឋានដែលបានចាក់សោក្នុង [`models.lock.json`](models.lock.json) ហើយត្រួតពិនិត្យគ្រប់ឯកសារដោយ sha256។ វាបោះពុម្ព `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK` បន្ទាប់មក `CUDNN_OK` ឬ `CUDNN_SKIPPED` ហើយចុងក្រោយ `SETUP_OK`។
  បើគ្មាន `--models-dir` និង `--bin-dir` វាប្រើ `models/` និង `bin/` ក្នុង root នៃ repository។ សូមដាក់ម៉ូដែលលើ SSD (មានតែ SSD ប៉ុណ្ណោះដែលបានវាស់)។
  អ្នកអាចបញ្ឈប់វាបានគ្រប់ពេលដោយ Ctrl+C ហើយរត់ពាក្យបញ្ជាដដែលម្ដងទៀត៖ ការទាញយកនឹងបន្តពីឯកសារ `.part`។
- **cuDNN ត្រូវបានដំឡើងតាមលំនាំដើម ហើយមិនមែនជាផ្នែកនៃ repository នេះទេ។** វាជាកម្មវិធីរបស់ NVIDIA ក្រោមអាជ្ញាបណ្ណផ្ទាល់ខ្លួនរបស់ NVIDIA ([អត្ថបទអាជ្ញាបណ្ណ](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)) សម្រាប់ប្រព័ន្ធដែលមាន GPU របស់ NVIDIA។ វាត្រូវបានទាញយកពីម៉ាស៊ីនមេរបស់ NVIDIA ដោយមិនមានការសុំបង់ប្រាក់ និងមិនត្រូវការគណនី ឬការចូលប្រើ (sign-in) ហើយយើងរកមិនឃើញប្រការណាមួយក្នុងអាជ្ញាបណ្ណដែលដាក់កម្រិតលើការប្រើប្រាស់ពាណិជ្ជកម្ម ឬផ្ទាល់ខ្លួនទេ។ `setup.py` បង្ហាញអាសយដ្ឋានអាជ្ញាបណ្ណ ទាញយកឯកសារ ហើយចម្លងតែ DLL ប្រាំបីទៅក្បែរ `sd-cli.exe`។ អាជ្ញាបណ្ណរបស់ NVIDIA ចែងថា អ្នកណាដែលមិនទទួលយកលក្ខខណ្ឌរបស់វា មិនត្រូវទាញយក ដំឡើង ឬប្រើវាឡើយ។ ក្នុងករណីនោះ សូមដំណើរការ `python scripts/setup.py --no-cudnn`។ បើគ្មាន cuDNN អ្វីៗនៅតែដំណើរការជាមួយផ្លូវ VAE របស់ v0.1.0 ដែលយឺតជាង (`--vae legacy`) ហើយ `generate.py` នឹងប្រាប់អ្នកអំពីរឿងនេះ។
- `generate.py` សរសេរ `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, `run.json` (ពេលវេលា ដំណាក់កាល ផ្លូវ VAE ណាដែលបានរត់ អង្គចងចាំ GPU ខ្ពស់បំផុត ពាក្យបញ្ជាពេញលេញ) និង `log.txt` ហើយបោះពុម្ព `IMAGE_OK <path>`។

## ការប្រើប្រាស់

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| ជម្រើស | អត្ថន័យ |
|---|---|
| `--prompt "<text>"` ឬ `--prompt-file <txt>` | prompt (ត្រូវការមួយក្នុងពីរ) |
| `--width`, `--height` | ពហុគុណនៃ 16, ពី 256 ដល់ 2048; លំនាំដើម 768x1344; បានសាកល្បង៖ 768x1344, 1344x768, 1024x1024 |
| `--seed` | លំនាំដើម 42 |
| `--out`, `--name` | ថតឫសនៃលទ្ធផល (លំនាំដើម `outputs/`) និងឈ្មោះខ្លីសម្រាប់ថតនៃការរត់ |
| `--models-dir`, `--bin-dir` | កន្លែងដែល `setup.py` ដាក់ម៉ូដែល និងម៉ាស៊ីន |
| `--vae auto` (លំនាំដើម) | cuDNN float32; សាកល្បងជាដុំតែមួយមុន បន្ទាប់មក tile ធំពីរ បន្ទាប់មក tile តូចលំនាំដើម |
| `--vae tiled` | cuDNN float32, tile ធំពីរជានិច្ច |
| `--vae legacy` | ផ្លូវ v0.1.0៖ គ្មាន cuDNN, tile តូច។ ត្រូវបានប្រើដោយស្វ័យប្រវត្តិ (ជាមួយការព្រមាន) ពេលគ្មាន DLL របស់ cuDNN |

ជំហាន (8), cfg (1.0), sampler និង scheduler ត្រូវបានកំណត់ថេរដោយចេតនា។ មើល [អ្វីដែលវាដំណើរការ](#what-it-runs)។

## ពិនិត្យដោយខ្លួនឯង

- `generate.py` បោះពុម្ព `PIXEL_SHA256 <hex>` មួយក្នុងចំណោមបន្ទាត់ចុងក្រោយៗ៖ ជា hash នៃភីកសែលដែលបាន decode។ រត់ពាក្យបញ្ជាដដែលពីរដង ហើយប្រៀបធៀបរូបភាពទាំងពីរ៖ `python scripts/compare.py <run A>/image.png <run B>/image.png` គួរបោះពុម្ព `SAME_PIXELS`។
- `PIXEL_SHA256` នៃឧទាហរណ៍ទាំងប្រាំលើម៉ាស៊ីនរបស់យើងមាននៅក្នុង [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md)។ hash នៃឯកសារ PNG អាចខុសគ្នា ទោះភីកសែលដូចគ្នាក៏ដោយ ព្រោះ PNG ផ្ទុកប៉ារ៉ាម៉ែត្រនៃការបង្កើតជាអត្ថបទ។ សូមប្រៀបធៀបភីកសែល កុំប្រៀបធៀបឯកសារ។
- ដែនកំណត់ដោយស្មោះត្រង់៖ យើងមិនបានវាស់ថាតើកាតផ្សេង ឬដ្រាយវើរផ្សេង ផ្ដល់ភីកសែលដូចគ្នាឬអត់ទេ។

## ហេតុអ្វីបានជាវាសមក្នុង 4 GB

- **អ្វីដែលអ្នកបង្កើតម៉ូដែលនិយាយ។** model card របស់ Z-Image-Turbo និយាយថាម៉ូដែល "fits comfortably within 16G VRAM consumer devices" (សមស្រួលក្នុងឧបករណ៍អ្នកប្រើប្រាស់ដែលមាន VRAM 16 GB) ([model card](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo))។ នោះជាសេចក្ដីថ្លែងអំពីកាត 16 GB។ README ផ្លូវការក៏រាយ stable-diffusion.cpp ជាជម្រើសរបស់ភាគីទីបី ហើយដកស្រង់វាថា "as little as 4GB of VRAM" (VRAM តិចត្រឹម 4 GB) ([README](https://github.com/Tongyi-MAI/Z-Image))។ នោះជាការអះអាងរបស់គម្រោង stable-diffusion.cpp មិនមែនជាតម្រូវការរបស់ក្រុម Z-Image ទេ។
- **អ្វីដែលយើងបានវាស់។** Z-Image-Turbo Q8_0 (ឯកសារទំហំ 6.6 GB) ជាមួយ text encoder Qwen3-4B Q8_0, 768x1344៖ កម្រិតខ្ពស់បំផុតនៃ GPU ដែល nvidia-smi យកគំរូរៀងរាល់ 2 s (កម្រិតកើនខ្លីៗអាចត្រូវខកខាន) គឺ 2949 ដល់ 2957 MiB (ម៉ាស៊ីន v0.1.0) និង 3057–3059 MiB (ម៉ាស៊ីន v0.2.0) លើកាតទំហំ 4096 MiB។ ទម្ងន់ (10 509 MiB; កំណត់ហេតុរបស់ម៉ាស៊ីនបោះពុម្ពវាជា MB) ស្ថិតនៅក្នុង RAM របស់ប្រព័ន្ធ។ ម៉ាស៊ីនចម្លងបណ្ដាញទៅ GPU ម្ដងមួយ segment (ចំណែកមួយនៃបណ្ដាញ)៖ 36 segment ដូចក្នុងបន្ទាត់កំណត់ហេតុ `z_image using 36 segments`។
- **តម្លៃដែលត្រូវបង់។** ពេលវេលា និងអង្គចងចាំរបស់ប្រព័ន្ធ៖ 188–193 s ក្នុងមួយរូបភាព ហើយដំណើរការរបស់ម៉ាស៊ីនកាន់ RAM ប្រហែល 10 489–11 203 MiB (រួមទាំងទំព័រម៉ូដែលដែលផ្គូផ្គងអង្គចងចាំ) លើម៉ាស៊ីន 16 GB ដូច្នេះ RAM ទំនេរធ្លាក់ចុះមកនៅតែប៉ុន្មានរយ MiB ពេលវាកំពុងរត់។
- **ការដំឡើងរបស់អ្នកដទៃ។** អ្នកដទៃរាយការណ៍ថាបានរត់ Z-Image លើកាត 4 GB ដោយប្រើ quantization ទាបជាងនេះ ឬទំហំតូចជាងនេះ (ឧទាហរណ៍ ទំព័រ wiki របស់ stable-diffusion.cpp សម្រាប់កាត 4 GB ណែនាំ Q3_K ឬ Q4_0 ត្រង់ 1024x512)។ នៅកន្លែងដែលយើងបានរកមើល (បញ្ជី និងកាលបរិច្ឆេទក្នុង [`docs/RELATED.md`](docs/RELATED.md)) យើងមិនបានរកឃើញការដំឡើងដែលបានផ្សព្វផ្សាយដែលបញ្ចូលគ្នាទាំងបួនទេ៖ កាត 4 GB, Q8_0, 768x1344 ឬធំជាងនេះ និងពេលវេលា ព្រមទាំងអង្គចងចាំ GPU ដែលបានវាស់។ នោះជាសេចក្ដីថ្លែងអំពីកន្លែងដែលយើងបានរកមើល មិនមែនអំពីគ្រប់កន្លែងទេ។
- **អ្នកណាធ្វើអ្វី។** ការដែលវាសមក្នុង 4 GB មកពី stable-diffusion.cpp ខ្លួនឯង៖ `--offload-to-cpu`, `--mmap`, ការធ្វើការជាចំណែក និង flash attention (ពេលបិទវា ការរត់មួយត្រូវការ 4205 MB ហើយមិនសម)។ បំណះរបស់យើងមានគោលបំណងសម្រាប់ល្បឿន និងដំណាក់កាល VAE ដែលល្អជាងមុន មិនមែនដើម្បីឱ្យវាសមទេ។ យើងមិនបានរត់ម៉ាស៊ីន upstream ដែលគ្មានបំណះលើកាតនេះទេ ដូច្នេះយើងមិនអាចនិយាយថាវាសមឬអត់បានឡើយ។

## របៀបដែលវាដំណើរការ

ការផ្លាស់ប្ដូរបីលើ stable-diffusion.cpp `master-1088-32d516c` (ទាំងអស់ជាកុងតាក់ ហើយតារាងក្នុង [`patches/README.md`](patches/README.md) រាយនីមួយៗជាមួយ environment variable របស់វា)៖

1. **refiner រត់ម្ដងក្នុងមួយជំហាន។** ឈ្មោះក្រុមមួយត្រូវបានប្រើពីរដង ដូច្នេះប្លុក refiner ចំនួនបួនត្រូវបានគណនាម្ដងទៀត។ ការកែនេះធ្វើឱ្យជំហានទី 2 ដល់ 8 លឿនជាងមុនប្រហែល 1.3 s ក្នុងមួយជំហាន (22.0 ដល់ 20.7 s) ដោយរូបភាពដូចគ្នាភីកសែលទល់នឹងភីកសែល (បានពិនិត្យរូបភាព 3)។
2. **VAE តាម cuDNN ក្នុង float32។** ដំណាក់កាលចុងក្រោយ (បម្លែង latent ទៅជាភីកសែល) ឥឡូវប្រើ convolution float32 របស់ cuDNN ពី NVIDIA។ លើកាតរបស់យើង វាបានបន្ថយ VAE ពី 23 ដល់ 27 s មក 10 ដល់ 15 s ហើយបានលើក PSNR ធៀបនឹងឯកសារយោងពី 38 ដល់ 43 dB ទៅ 45 ដល់ 49 dB (ជាមួយ tile ធំ)។
3. **ដុំតែមួយមុន។** ឥឡូវម៉ាស៊ីនព្យាយាម decode រូបភាពទាំងមូលជាដុំតែមួយ ពេលការត្រួតពិនិត្យអង្គចងចាំថាវាសម (រឹម 256 MiB) បើមិនបានទេ ធ្លាក់ទៅ tile ធំពីរ ហើយបន្ទាប់មកទៅ tile តូច។ ក្នុងដុំតែមួយ VAE ប្រើពេលប្រហែល 8–16 s ហើយ PSNR ធៀបនឹងឯកសារយោងគឺ 71 ដល់ 73 dB។ បើមានការធ្លាក់ថយដោយបង្ខំ រូបភាពមានភីកសែលដូចគ្នានឹងរូបភាពដែលធ្វើជា tile (បានពិនិត្យដោយ `PIXEL_SHA256`)។ អ្វីដែលបានកើតឡើងត្រូវបានសរសេរក្នុង `run.json` (`stages.vae_path`: `full`, `tile`, `floor` ឬ `retry`)។

ម្យ៉ាងទៀត៖ `--eager-load` (អានទំព័រម៉ូដែលជាមុន; 241.2 s ទៅ 220.3 s លើរូបភាពតែមួយ កំណែអភិវឌ្ឍន៍ ការរត់ម្ដងម្នាក់) ជាផ្នែកនៃពាក្យបញ្ជាថេរ។

<a id="what-it-runs"></a>
## អ្វីដែលវាដំណើរការ

| ផ្នែក | ឯកសារ | ប្រភព |
|---|---|---|
| ម៉ូដែល diffusion | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), មូលដ្ឋាន [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Text encoder | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), autoencoder ប្រភេទ FLUX.1 |
| ម៉ាស៊ីន | `sd-cli.exe`, stable-diffusion.cpp `32d516c` ជាមួយបំណះក្នុង [`patches/`](patches) | កំណែ v0.3.0 នៃ repository នេះ (`sinirsiz-foto-engine-v0.3.0-win-x64-cuda12.8-sm61.zip`) |
| CUDA runtime | `cudart`, `cublas`, `cublasLt` (12.8) មិនបានកែប្រែ | zip ពីកំណែ v0.1.0 របស់ wan22-pascal-4gb |
| cuDNN (ដំឡើងតាមលំនាំដើម; `--no-cudnn` រំលងវា) | DLL 8, កំណែ 9.10.2.21 (កំណែ build សម្រាប់ CUDA 11) | ម៉ាស៊ីនមេរបស់ NVIDIA ផ្ទាល់ ក្រោមអាជ្ញាបណ្ណរបស់ NVIDIA; មិនត្រូវបានរក្សាទុកនៅទីនេះ |

ការកំណត់ថេរ៖ `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`។
យើងមិនបន្ថយចំនួនជំហាន មិនបន្ថែម negative prompt និងមិនបើក caching ទេ៖ ម៉ូដែលត្រូវបាន distill សម្រាប់ 8 ជំហាន ហើយមិនប្រើ negative prompt (មើល [prompts](docs/PROMPTS.md))។

## ដែនកំណត់ (សូមអានមុនពេលពឹងផ្អែក)

- **Windows តែប៉ុណ្ណោះ។** ម៉ាស៊ីនដែលបានបង្កើតរួច និងស្គ្រីបទាំងនេះសម្រាប់តែ Windows ប៉ុណ្ណោះ។
- **កាតមួយ ម៉ាស៊ីនមួយ។** បានវាស់តែលើកុំព្យូទ័រយួរដៃ GTX 1050 Ti 4 GB មួយប៉ុណ្ណោះ (i7-7700HQ, RAM 16 GB, Windows 10, ដ្រាយវើរ 581.29, ម៉ូដែលលើ SSD)។ GPU និងដ្រាយវើរផ្សេងទៀត ម៉ាស៊ីនដែលមាន RAM តិចជាង 16 GB, Linux និង macOS៖ **មិនទាន់បានសាកល្បង**។
- កាត និងប្រព័ន្ធផ្សេងទៀត (ផ្លូវណាដែលមាន និងការធ្វើតេស្តរបស់សហគមន៍លើកាត AMD ក្នុង Linux ដែលយើងមិនបានដំណើរការដោយខ្លួនឯង)៖ [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md)។
- **ម៉ាស៊ីនត្រូវបាន build សម្រាប់ Pascal (sm_61) តែប៉ុណ្ណោះ។** ស្ថាបត្យកម្មផ្សេងទៀតត្រូវការ build ផ្ទាល់ខ្លួន ([`docs/BUILD.md`](docs/BUILD.md))។ យើងមិនបានសាកល្បងមួយណាទេ។
- **cuDNN៖** យើងបានវាស់ជាមួយកំណែ build សម្រាប់ CUDA 11 នៃ cuDNN 9.10.2.21។ កំណែ build សម្រាប់ CUDA 12 មានឯកសារខុសគ្នា ហើយមិនទាន់បានវាស់។
- **អង្គចងចាំចង្អៀត។** RAM ទំនេរធ្លាក់មកនៅតែប៉ុន្មានរយ MiB។ សូមបិទកម្មវិធីផ្សេងទៀត ហើយបង្កើតម្ដងមួយរូបភាព។ យើងមិនទាន់ឃើញអង្គចងចាំ GPU អស់ បន្ទាប់ពីការត្រួតពិនិត្យអង្គចងចាំរបស់ម៉ាស៊ីនបានជាប់ទេ ហើយយើងមិនបានសាកល្បងថាតើមានអ្វីកើតឡើងពេលនោះឡើយ។
- **ទំហំ៖** មានតែ 768x1344, 1344x768 និង 1024x1024 ប៉ុណ្ណោះដែលបានសាកល្បង។ ទំហំធំជាងនេះបោះពុម្ពការព្រមាន ហើយអាចអស់អង្គចងចាំ។
- ភាពស្មោះត្រង់នឹង prompt គ្រាន់តែមួយផ្នែក៖ រូបភាពមិនតែងតែធ្វើតាម prompt គ្រប់ព័ត៌មានលម្អិតទេ។ អត្ថបទក្នុងរូបភាព និងសំណង់ពិតលើពិភពលោក មិនទាន់ត្រូវបានវាយតម្លៃទេ។
- ឯកសារយោងរបស់ PSNR គឺ decode លើ CPU របស់ម៉ាស៊ីនរបស់យើងផ្ទាល់ មិនមែនជាការអនុវត្តឯករាជ្យទេ។
- លេខក្នុង [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) មកពីការរត់ម្ដងម្នាក់ លុះត្រាតែមានសរសេរផ្សេង។

## អាជ្ញាបណ្ណ និងការផ្ដល់ក្រេឌីត

- ស្គ្រីប និងឯកសាររបស់ repository នេះ៖ [Apache-2.0](LICENSE) ជាមួយឯកសារ [`NOTICE`](NOTICE)។ បំណះម៉ាស៊ីនក្នុង [`patches/`](patches) ជា MIT ដូចកូដដែលពួកវាកែប្រែ។
- stable-diffusion.cpp និង ggml ជា MIT។ សេចក្ដីជូនដំណឹងសម្រាប់កូដភាគីទីបីដែលត្រូវបាន compile ចូលក្នុងម៉ាស៊ីនមាននៅក្នុង [`licenses/`](licenses) និង [`THIRD_PARTY.md`](THIRD_PARTY.md)។
- ឯកសារម៉ូដែលមិនត្រូវបានរក្សាទុកនៅទីនេះទេ។ ពួកវាត្រូវបានទាញយកពីប្រភពខាងលើ ក្រោមអាជ្ញាបណ្ណរបស់ខ្លួនផ្ទាល់ (Hugging Face បង្ហាញ Apache-2.0 សម្រាប់ទាំងអស់ បានអាននៅ 2026-11-13)។ model card មិននិយាយអ្វីអំពីអ្នកដែលជាម្ចាស់រូបភាពដែលបានបង្កើតទេ ហើយយើងក៏មិនអះអាងអ្វីអំពីរឿងនេះដែរ។
- **cuDNN និង CUDA runtime ជាទ្រព្យសម្បត្តិរបស់ NVIDIA** ហើយមិនស្ថិតក្រោមអាជ្ញាបណ្ណរបស់ repository នេះទេ។ cuDNN ត្រូវបានទាញយកពីម៉ាស៊ីនមេរបស់ NVIDIA ក្រោមអាជ្ញាបណ្ណរបស់ NVIDIA (`--no-cudnn` រំលងវា)។ DLL របស់ CUDA runtime នៅក្នុង zip ដាច់ដោយឡែកដែលមិនបានកែប្រែ (CUDA Toolkit EULA, Attachment A)។ ព័ត៌មានលម្អិត និងអ្វីដែលយើងមិនអាចផ្ទៀងផ្ទាត់បាន៖ [`THIRD_PARTY.md`](THIRD_PARTY.md)។
- **ក្រេឌីត។** ការរក្សាឯកសារ `NOTICE` ជាមួយច្បាប់ចម្លង និងស្នាដៃដែលកើតចេញពីវា គឺជាលក្ខខណ្ឌ (Apache-2.0, ផ្នែក 4)។ ក្រៅពីនេះ ឃ្លាដូចជា "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey" ត្រូវបានស្វាគមន៍ តែមិនបង្ខំទេ។
- សូមអាន [`ETHICS.md`](ETHICS.md)៖ រាល់រូបភាពសុទ្ធតែសំយោគ ហើយអ្នកទទួលខុសត្រូវចំពោះអ្វីដែលអ្នកផ្សព្វផ្សាយ។

## ការចូលរួមចំណែក

អ្វីដែលមានប្រយោជន៍បំផុតដែលអ្នកអាចធ្វើបានគឺ **សាកល្បងកាតរបស់អ្នក** ហើយប្រាប់យើងថាមានអ្វីកើតឡើង៖ ឈ្មោះ GPU, ដ្រាយវើរ, RAM, `run.json` និងបន្ទាត់ចុងក្រោយនៃកំណត់ហេតុ (ទម្រង់បែបបទបញ្ហា "Hardware test report")។ ការកែតម្រូវឯកសារ និងស្គ្រីបក៏ត្រូវបានស្វាគមន៍ដែរ។ មើល [`CONTRIBUTING.md`](CONTRIBUTING.md)។ របាយការណ៍សុវត្ថិភាពតាមផ្លូវឯកជននៅក្នុង [`SECURITY.md`](SECURITY.md)។

[មគ្គុទេសក៍ដំឡើងសម្រាប់ភ្នាក់ងារ AI](AGENTS.md) · [លទ្ធផលវាស់](docs/MEASUREMENTS.md) · [ដោះស្រាយបញ្ហា](docs/TROUBLESHOOTING.md) · [ការ build ម៉ាស៊ីន](docs/BUILD.md) · [បំណះ](patches/README.md) · [Prompts](docs/PROMPTS.md) · [ភាគីទីបី](THIRD_PARTY.md) · [កំណត់ហេតុការផ្លាស់ប្ដូរ](CHANGELOG.md)

ទំព័រនេះត្រូវបានធ្វើមូលដ្ឋានីយកម្មដោយមានជំនួយពី AI ហើយយើងស្វាគមន៍ការកែតម្រូវយ៉ាងពិតប្រាកដ៖ មើល [`CONTRIBUTING.md`](CONTRIBUTING.md)។
