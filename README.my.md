[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · **မြန်မာ** · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**Windows ပေါ်မှာ၊ 4 GB GTX 1050 Ti (Pascal, sm_61) တစ်ခုပေါ်က stable-diffusion.cpp နဲ့ Z-Image-Turbo (Q8_0 GGUF) ကို သုံးပြီး စာသားမှ ပုံဖန်တီးခြင်း (text-to-image) ကို 768x1344 အရွယ်အစားနဲ့ လုပ်ပါတယ်။** RAM 16 GB ရှိတဲ့ လက်ပ်တော့တစ်လုံးပေါ်မှာ တိုင်းထားတာဖြစ်ပြီး ဒီ process က RAM ကို ခန့်မှန်းခြေ 11 GB သုံးပါတယ်။ seed တူရင် pixel တူပါတယ်၊ pixel တစ်ခုချင်း တူပါတယ်။ တိုင်းတာမှုတွေနဲ့ engine patch တွေကို ထုတ်ပြန်ထားပြီး download တွေကို sha256 နဲ့ ပင်ထားပါတယ်။ AI coding agent တစ်ခုက အဆင့်ဆင့် တပ်ဆင်ပေးနိုင်ပါတယ်။

*တရားဝင်မဟုတ်ပါ။ Tongyi-MAI (Z-Image)၊ leejet (stable-diffusion.cpp) သို့မဟုတ် NVIDIA တို့နဲ့ ဆက်စပ်မှု မရှိပါ။*

## ဒီမှာ စတင်ပါ

အသင့်ပြင်ထားတဲ့ package တစ်ခု ရှိတာမို့ အရင်စမ်းကြည့်ပါ။ သင့်ဟာ့ဒ်ဝဲ မတူရင် ဒါမှမဟုတ် အဆင့်တစ်ခု မအောင်မြင်ရင် ကျန်တာအားလုံး ဖွင့်ထားပါတယ်။ patch တွေ၊ build လုပ်နည်းနဲ့ တိုင်းတာမှုတွေက ဒီ repository ထဲမှာ ရှိတာမို့ သင့်ကတ်အတွက် ကိုယ်တိုင် build လုပ်နိုင်တယ်၊ ပြင်ဆင်သုံးနိုင်ပါတယ်။

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

အဆင့် 2 က ခန့်မှန်းခြေ 12.2 GB ကို download လုပ်ပြီး ကျွန်တော်တို့ရဲ့ အင်တာနက်မှာ တစ်ကြိမ်လုပ်တုန်းက 29 မိနစ် ကြာခဲ့ပါတယ်။ အရင်ဆုံး "Preflight" ဆိုတဲ့ block တစ်ခု ထုတ်ပြပါတယ် (သင့် GPU၊ RAM နဲ့ disk လွတ်နေတဲ့နေရာကို ကျွန်တော်တို့ တိုင်းထားတဲ့တန်ဖိုးဘေးမှာ ပြပေးတာဖြစ်ပြီး အသိပေးရုံပါပဲ)။
GTX 1050 Ti 4 GB လက်ပ်တော့ကတ် (Pascal, compute capability 6.1) ကိုသာ တိုင်းထားပါတယ်။ တခြားကတ်တွေကို မစမ်းရသေးပါ။
AI coding agent (Claude Code, Codex, Cursor စတာတွေ) သုံးရင် [`AGENTS.md`](AGENTS.md) ဆီ ညွှန်ပေးလိုက်ပါ။

## တစ်ချက်ကြည့်

v0.1.0 ပုံစံနဲ့ နှိုင်းယှဉ်ရင်၊ ပုံတစ်ပုံက 261.6 s အစား 193–228 s ကြာပါတယ်၊ VAE အဆင့်က 29.8 ကနေ 36.3 s အစား 8.3–15.9 s ကြာပါတယ်၊ seed တူရင် pixel တူပါတယ်၊ ဒီ README ထဲက ကိန်းဂဏန်းတိုင်းရဲ့ နောက်မှာ command နဲ့ ဖိုင်တစ်ခု ရှိပါတယ်။

768x1344၊ seed 42၊ 8 steps၊ စက်တူတူ။ v0.1.0 ကိန်းတွေက v0.1.0 README က (root သန့်သန့်နဲ့ စမ်းသပ်မှုနဲ့ ငါးကြိမ်ပြေးမှု) ဖြစ်ပါတယ်။ v0.2.0 ကိန်းတွေက ဒီ release ရဲ့ root သန့်သန့်နဲ့ စမ်းသပ်မှုက ဖြစ်ပါတယ်။

| | v0.1.0 (ထုတ်ပြန်ခဲ့ဖူးခြင်း မရှိ၊ ဟောင်းတဲ့ပုံစံ) | v0.2.0 |
|---|---|---|
| ပုံတစ်ပုံအတွက် အချိန် (`generate.py` တစ်ကြိမ်ပြေးမှု) | 261.6 s | 193–228 s |
| VAE decode (နောက်ဆုံးအဆင့်) | 29.8 ကနေ 36.3 s | 8.3–15.9 s |
| ကိုးကားထားတဲ့ decode နဲ့ ဆင်တူမှု (PSNR၊ မြင့်ရင် ပိုဆင်တူ) | 38 ကနေ 43 dB | 71 ကနေ 73 dB |
| GPU မှတ်ဉာဏ် အမြင့်ဆုံး (nvidia-smi) | 2949 ကနေ 2957 MiB | 3057–3059 MiB |
| process မှတ်ဉာဏ် အမြင့်ဆုံး | 10.5 ကနေ 10.9 GB (အဲဒီတုန်းက မှတ်ထားတဲ့အတိုင်း) | 10 667–10 915 MiB |
| တွေ့ခဲ့တဲ့ အနိမ့်ဆုံး RAM လွတ် | 331 ကနေ 576 MiB | 418–545 MiB |

ဘယ်လိုဖတ်မလဲ။ ကိုးကားချက်ဆိုတာ latent တစ်ခုတည်းကို CPU ပေါ်မှာ float32 အပိုင်းတစ်ခုတည်းအဖြစ် decode လုပ်ထားတာပါ။ PSNR က ကျွန်တော်တို့ရဲ့ GPU decode ကို အဲဒါနဲ့ နှိုင်းယှဉ်ပါတယ် (ပုံ 3 ပုံ)။ VAE အဆင့်က အဲဒီကိုးကားချက်နဲ့ ဘယ်လောက်ဆင်တူလဲဆိုတာကို ပြောပါတယ်။ ပုံတစ်ပုံ ဘယ်လောက်လှလဲဆိုတာကို မပြောပါဘူး။ v0.2.0 ပုံတွေက prompt နဲ့ seed တူတာတောင် v0.1.0 နဲ့ byte တစ်ခုချင်း မတူပါဘူး၊ VAE လမ်းကြောင်းကို ရည်ရွယ်ချက်ရှိရှိ ပြောင်းထားလို့ပါ။ နည်းလမ်းနဲ့ မတိုင်းရသေးတာတွေ: [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md)။

## နမူနာများ

**ဒီ repo နဲ့ AI ဖန်တီးထားတာ** (Z-Image-Turbo Q8_0၊ seed 42၊ 8 steps)။ ဒါတွေက တကယ့်ဓာတ်ပုံ မဟုတ်ပါဘူး။ အဆောက်အအုံတွေနဲ့ အသေးစိတ်တွေ မမှန်နိုင်ပါဘူး၊ ပုံတစ်ပုံက prompt ကို အသေးစိတ်အားလုံးမှာ အမြဲမလိုက်ပါဘူး။ prompt အပြည့်အစုံက [`prompts/`](prompts) နဲ့ [`docs/PROMPTS.md`](docs/PROMPTS.md) ထဲမှာ ရှိပါတယ်။

| | | |
|---|---|---|
| ![ရွှေရောင်အချိန်က Eiffel Tower](docs/examples/eiffel.jpg) | ![တူရကီလက်ဖက်ရည်ခွက်](docs/examples/turkish_tea.jpg) | ![အသက်ကြီးတဲ့ ငါးဖမ်းသမား](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![တောင်စောင်းက ရွာ](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![ကောင်းကင်ကနေ မြင်ရတဲ့ အစ္စတန်ဘူလ်](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768။ တကယ့်ဓာတ်ပုံ မဟုတ်ပါ။ အဆောက်အအုံတွေ မမှန်နိုင်ပါ။

## အမြန်စတင်ခြင်း

လိုအပ်ချက်များ: Windows 10/11၊ 4 GB ရှိတဲ့ NVIDIA GPU၊ CUDA 12.8 ကို ထောက်ပံ့တဲ့ driver (driver 581.29 နဲ့ တိုင်းထားတယ်၊ ဟောင်းတဲ့ driver တွေကို မစမ်းရသေးဘူး၊ CUDA runtime ကိုယ်တိုင်ကို သင့်အတွက် download လုပ်ပေးပါတယ်)၊ Python 3.10 သို့မဟုတ် အထက်၊
git၊ disk လွတ် ခန့်မှန်းခြေ 14 GB (cuDNN ပါရင် download က ခန့်မှန်းခြေ 12.2 GB၊ disk လွတ်ကိန်းက ခန့်မှန်းချက်ပါ) နဲ့ RAM 16 GB (တိုင်းထားတဲ့ပမာဏ၊ ဒါထက်နည်းရင် မစမ်းရသေးပါ)။

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- `setup.py` က အရင်ဆုံး "Preflight" block ကို ထုတ်ပြပါတယ် (သင့် GPU၊ RAM နဲ့ disk လွတ်နေတဲ့နေရာကို ကျွန်တော်တို့ တိုင်းထားတဲ့တန်ဖိုးဘေးမှာ ပြတာဖြစ်ပြီး အသိပေးရုံပဲ၊ ဘာကိုမှ မတားပါဘူး)။ ပြီးရင် [`models.lock.json`](models.lock.json) ထဲက ပင်ထားတဲ့ လိပ်စာတွေကနေ download လုပ်ပြီး ဖိုင်တိုင်းကို sha256 နဲ့ စစ်ပါတယ်။ `MODEL_OK <name>`၊ `ENGINE_OK`၊ `CUDART_OK` ပြီးရင် `CUDNN_OK` ဒါမှမဟုတ် `CUDNN_SKIPPED` ကို ထုတ်ပြပြီး နောက်ဆုံးမှာ `SETUP_OK` ကို ထုတ်ပြပါတယ်။
  `--models-dir` နဲ့ `--bin-dir` မပေးရင် repo root ထဲက `models/` နဲ့ `bin/` ကို သုံးပါတယ်။ model တွေကို SSD ပေါ်မှာ ထားပါ (SSD နဲ့ပဲ တိုင်းထားပါတယ်)။
  Ctrl+C နဲ့ ဘယ်အချိန်မဆို ရပ်လို့ရပါတယ်၊ command အတူတူကို ထပ်ပြေးပါ။ download က `.part` ဖိုင်တွေကနေ ဆက်သွားပါတယ်။
- **cuDNN ကို မူလအတိုင်း တပ်ဆင်ပေးပြီး ဒီ repository ရဲ့ အစိတ်အပိုင်း မဟုတ်ပါဘူး။** ဒါက NVIDIA ကိုယ်ပိုင် လိုင်စင်အောက်က NVIDIA software ဖြစ်ပြီး ([လိုင်စင်စာသား](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)) NVIDIA GPU ပါတဲ့ စနစ်တွေအတွက်ပါ။ NVIDIA ရဲ့ server ကနေ ငွေပေးချေဖို့ မတောင်းဘဲ၊ account သို့မဟုတ် sign-in မလိုဘဲ download လုပ်လို့ရပြီး လိုင်စင်ထဲမှာ စီးပွားရေးအတွက်ဖြစ်စေ ကိုယ်ပိုင်အတွက်ဖြစ်စေ အသုံးပြုမှုကို ကန့်သတ်တဲ့ ပုဒ်မ ကျွန်တော်တို့ မတွေ့ခဲ့ပါဘူး။ `setup.py` က လိုင်စင်လိပ်စာကို ပြပြီး ဖိုင်ကို download လုပ်ကာ DLL ရှစ်ခုကိုသာ `sd-cli.exe` ဘေးကို ကူးထည့်ပါတယ်။ NVIDIA ရဲ့ လိုင်စင်က သူ့စည်းကမ်းတွေကို မလက်ခံသူတွေ download မလုပ်ရ၊ မတပ်ဆင်ရ၊ မသုံးရဘူးလို့ ဖော်ပြထားပါတယ်။ အဲဒီလိုဆိုရင် `python scripts/setup.py --no-cudnn` ကို run ပါ။ cuDNN မရှိရင်လည်း အားလုံး ပိုနှေးတဲ့ v0.1.0 VAE လမ်းကြောင်း (`--vae legacy`) နဲ့ အလုပ်လုပ်ပြီး `generate.py` က အဲဒါကို ပြောပြပါတယ်။
- `generate.py` က `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`၊ `run.json` (အချိန်၊ အဆင့်တွေ၊ ဘယ် VAE လမ်းကြောင်း ပြေးခဲ့လဲ၊ GPU မှတ်ဉာဏ် အမြင့်ဆုံး၊ command အတိအကျ) နဲ့ `log.txt` ကို ရေးပြီး `IMAGE_OK <path>` ကို ထုတ်ပြပါတယ်။

## အသုံးပြုပုံ

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| Option | အဓိပ္ပာယ် |
|---|---|
| `--prompt "<text>"` သို့မဟုတ် `--prompt-file <txt>` | prompt (နှစ်ခုထဲက တစ်ခု လိုအပ်သည်) |
| `--width`, `--height` | 16 ရဲ့ ဆတိုးကိန်းများ၊ 256 ကနေ 2048 အထိ၊ default 768x1344၊ စမ်းထားတာ: 768x1344, 1344x768, 1024x1024 |
| `--seed` | default 42 |
| `--out`, `--name` | output folder ရဲ့ root (default `outputs/`) နဲ့ run folder အတွက် နာမည်တိုတစ်ခု |
| `--models-dir`, `--bin-dir` | `setup.py` က model တွေနဲ့ engine ကို ထားတဲ့နေရာ |
| `--vae auto` (default) | cuDNN float32၊ အပိုင်းတစ်ခုတည်းနဲ့ အရင်စမ်း၊ ပြီးရင် tile ကြီးနှစ်ခု၊ ပြီးရင် default tile သေးသေး |
| `--vae tiled` | cuDNN float32၊ tile ကြီးနှစ်ခု အမြဲ |
| `--vae legacy` | v0.1.0 လမ်းကြောင်း: cuDNN မပါ၊ tile သေးသေးတွေ။ cuDNN DLL တွေ မရှိရင် အလိုအလျောက် (သတိပေးချက်နဲ့အတူ) သုံးပါတယ် |

Steps (8)၊ cfg (1.0)၊ sampler နဲ့ scheduler တို့ကို ရည်ရွယ်ချက်ရှိရှိ သတ်မှတ်ထားပါတယ်။ [ဘာကို အသုံးပြုသလဲ](#what-it-runs) ကို ကြည့်ပါ။

## ကိုယ်တိုင် စစ်ကြည့်ပါ

- `generate.py` က နောက်ဆုံးလိုင်းတွေထဲက တစ်ခုအဖြစ် `PIXEL_SHA256 <hex>` ကို ထုတ်ပြပါတယ်။ ဒါက decode လုပ်ပြီးသား pixel တွေရဲ့ hash ပါ။ command တူတူကို နှစ်ကြိမ်ပြေးပြီး ပုံနှစ်ပုံကို နှိုင်းယှဉ်ပါ။ `python scripts/compare.py <run A>/image.png <run B>/image.png` က `SAME_PIXELS` ကို ထုတ်ပြသင့်ပါတယ်။
- ကျွန်တော်တို့စက်မှာ နမူနာငါးခုရဲ့ `PIXEL_SHA256` ကို [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) ထဲမှာ ထည့်ထားပါတယ်။ PNG ရဲ့ ဖိုင် hash က pixel တူနေရင်တောင် မတူနိုင်ပါဘူး၊ PNG က ဖန်တီးမှု parameter တွေကို စာသားအဖြစ် သယ်ထားလို့ပါ။ ဖိုင်တွေကို မဟုတ်ဘဲ pixel တွေကို နှိုင်းယှဉ်ပါ။
- ရိုးရိုးသားသား ကန့်သတ်ချက်: တခြားကတ် ဒါမှမဟုတ် တခြား driver က pixel တူတူ ပေးမပေးကို ကျွန်တော်တို့ မတိုင်းထားပါဘူး။

## 4 GB ထဲမှာ ဘာကြောင့် ဆန့်သလဲ

- **model ဖန်တီးသူတွေ ဘာပြောသလဲ။** Z-Image-Turbo model card က model သည် "fits comfortably within 16G VRAM consumer devices" (VRAM 16 GB ရှိတဲ့ သုံးစွဲသူအဆင့် ကိရိယာတွေမှာ အဆင်ပြေပြေ ဆန့်သည်) လို့ ပြောထားပါတယ် ([model card](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo))။ ဒါက 16 GB ကတ်တွေအကြောင်း ပြောချက်ပါ။ တရားဝင် README ကလည်း stable-diffusion.cpp ကို ပြင်ပအဖွဲ့တစ်ခုရဲ့ ရွေးချယ်စရာအဖြစ် စာရင်းပြုထားပြီး "as little as 4GB of VRAM" (VRAM 4 GB လောက်သာ လိုသည်) လို့ ကိုးကားထားပါတယ် ([README](https://github.com/Tongyi-MAI/Z-Image))။ အဲဒါက stable-diffusion.cpp project ရဲ့ ပြောချက်ဖြစ်ပြီး Z-Image အဖွဲ့ရဲ့ လိုအပ်ချက် မဟုတ်ပါဘူး။
- **ကျွန်တော်တို့ ဘာတိုင်းခဲ့သလဲ။** Z-Image-Turbo Q8_0 (6.6 GB ဖိုင်) နဲ့ Qwen3-4B Q8_0 text encoder၊ 768x1344: nvidia-smi က 2 s တစ်ခါ နမူနာယူတဲ့ GPU အမြင့်ဆုံးတန်ဖိုး (တိုတောင်းတဲ့ တက်လာမှုကို လွတ်သွားနိုင်တယ်) က 4096 MiB ကတ်ပေါ်မှာ 2949 ကနေ 2957 MiB (v0.1.0 engine) နဲ့ 3057–3059 MiB (v0.2.0 engine) ဖြစ်ခဲ့ပါတယ်။ weight တွေ (10 509 MiB၊ engine log က MB လို့ ရိုက်ထုတ်တယ်) က system RAM ထဲမှာ ကျန်ပါတယ်။ engine က network ကို GPU ဆီ segment တစ်ခုချင်း (network ရဲ့ အပိုင်းတစ်ပိုင်း) ကူးပေးပါတယ်: log လိုင်း `z_image using 36 segments` မှာလို segment 36 ခု။
- **ဘာတွေ ကုန်ကျသလဲ။** အချိန်နဲ့ system မှတ်ဉာဏ်: ပုံတစ်ပုံကို 193–228 s၊ engine process က RAM 16 GB စက်ပေါ်မှာ RAM ခန့်မှန်းခြေ 10 667–10 915 MiB ကို ကိုင်ထားပါတယ် (memory-map လုပ်ထားတဲ့ model page တွေ အပါအဝင်)၊ ဒါကြောင့် ပြေးနေစဉ် RAM လွတ်က MiB ရာဂဏန်းလောက်ပဲ ကျန်ပါတော့တယ်။
- **တခြားသူတွေရဲ့ တပ်ဆင်မှုများ။** တခြားသူတွေက Z-Image ကို 4 GB ကတ်တွေမှာ quantization နိမ့်နိမ့် ဒါမှမဟုတ် အရွယ်အစား သေးသေးနဲ့ ပြေးတယ်လို့ ပြောကြပါတယ် (ဥပမာ 4 GB ကတ်တွေအတွက် stable-diffusion.cpp wiki စာမျက်နှာက 1024x512 မှာ Q3_K ဒါမှမဟုတ် Q4_0 ကို အကြံပြုပါတယ်)။ ကျွန်တော်တို့ ရှာကြည့်ခဲ့တဲ့နေရာတွေမှာ (စာရင်းနဲ့ ရက်စွဲက [`docs/RELATED.md`](docs/RELATED.md) မှာ) လေးခုလုံးကို ပေါင်းထားတဲ့ ထုတ်ပြန်ပြီးသား တပ်ဆင်မှု မတွေ့ခဲ့ပါဘူး: 4 GB ကတ်၊ Q8_0၊ 768x1344 ဒါမှမဟုတ် ပိုကြီးတာ၊ တိုင်းထားတဲ့ အချိန်နဲ့ GPU မှတ်ဉာဏ်။ ဒါက ကျွန်တော်တို့ ရှာကြည့်ခဲ့တဲ့နေရာအကြောင်း ပြောချက်ပဲဖြစ်ပြီး နေရာတိုင်းအကြောင်း မဟုတ်ပါဘူး။
- **ဘယ်သူက ဘာလုပ်သလဲ။** 4 GB ထဲ ဆန့်အောင်လုပ်တာက stable-diffusion.cpp ကိုယ်တိုင်ကနေ လာပါတယ်: `--offload-to-cpu`၊ `--mmap`၊ အပိုင်းလေးတွေခွဲပြီး အလုပ်လုပ်ခြင်းနဲ့ flash attention (ပိတ်ထားရင် တစ်ကြိမ်ပြေးမှုက 4205 MB လိုပြီး မဆန့်ခဲ့ပါဘူး)။ ကျွန်တော်တို့ရဲ့ patch တွေက မြန်နှုန်းနဲ့ ပိုကောင်းတဲ့ VAE အဆင့်အတွက်ဖြစ်ပြီး ဆန့်ဖို့အတွက် မဟုတ်ပါဘူး။ patch မထည့်ရသေးတဲ့ upstream engine ကို ဒီကတ်ပေါ်မှာ မပြေးခဲ့လို့ ဆန့်မဆန့် ကျွန်တော်တို့ မပြောနိုင်ပါဘူး။

## ဘယ်လိုအလုပ်လုပ်သလဲ

stable-diffusion.cpp `master-1088-32d516c` အပေါ်မှာ အပြောင်းအလဲ သုံးခု (အားလုံးက switch တွေပါ၊ [`patches/README.md`](patches/README.md) ထဲက ဇယားက တစ်ခုချင်းကို သူ့ environment variable နဲ့အတူ စာရင်းပြထားပါတယ်):

1. **refiner က step တစ်ခုကို တစ်ကြိမ်ပဲ ပြေးပါတယ်။** group name တစ်ခုကို နှစ်ကြိမ် သုံးထားလို့ refiner block လေးခုကို ဒုတိယအကြိမ် တွက်နေခဲ့ပါတယ်။ ပြင်လိုက်တော့ step 2 ကနေ 8 အထိ တစ်ခုချင်း ခန့်မှန်းခြေ 1.3 s မြန်လာပြီး (22.0 ကနေ 20.7 s) ပုံက pixel တစ်ခုချင်း တူပါတယ် (ပုံ 3 ပုံ စစ်ထားတယ်)။
2. **VAE ကို cuDNN နဲ့၊ float32 မှာ။** နောက်ဆုံးအဆင့် (latent ကို pixel အဖြစ် ပြောင်းတာ) က ယခု NVIDIA ရဲ့ cuDNN float32 convolution ကို သုံးပါတယ်။ ကျွန်တော်တို့ကတ်မှာ VAE ကို 23 ကနေ 27 s ကနေ 10 ကနေ 15 s အထိ လျှော့ပေးပြီး ကိုးကားချက်နဲ့ PSNR ကို 38 ကနေ 43 dB ကနေ 45 ကနေ 49 dB အထိ တင်ပေးခဲ့ပါတယ် (tile ကြီးတွေနဲ့)။
3. **အပိုင်းတစ်ခုတည်းနဲ့ အရင်စမ်းပါတယ်။** engine က မှတ်ဉာဏ်စစ်ဆေးမှုက ဆန့်တယ်လို့ ပြောရင် (margin 256 MiB) ပုံတစ်ခုလုံးကို အပိုင်းတစ်ခုတည်းနဲ့ decode လုပ်ကြည့်ပြီး မရရင် tile ကြီးနှစ်ခုကို ပြန်သွားကာ ပြီးရင် tile သေးသေးတွေကို သွားပါတယ်။ အပိုင်းတစ်ခုတည်းမှာ VAE က ခန့်မှန်းခြေ 8–16 s ကြာပြီး ကိုးကားချက်နဲ့ PSNR က 71 ကနေ 73 dB ရခဲ့ပါတယ်။ အတင်းအကျပ် ပြန်ကျသွားတဲ့အခါ ပုံက tile နဲ့လုပ်ထားတာနဲ့ pixel တူပါတယ် (`PIXEL_SHA256` နဲ့ စစ်ထားတယ်)။ ဘာဖြစ်ခဲ့လဲဆိုတာကို `run.json` ထဲ ရေးထားပါတယ် (`stages.vae_path`: `full`, `tile`, `floor` ဒါမှမဟုတ် `retry`)။

ထပ်ပြောရရင်: `--eager-load` (model page တွေကို ကြိုဖတ်တယ်၊ တူညီတဲ့ပုံမှာ 241.2 s ကနေ 220.3 s၊ development build၊ တစ်ခုချင်း တစ်ကြိမ်ပြေးမှု) က သတ်မှတ်ထားတဲ့ command ရဲ့ အစိတ်အပိုင်းပါ။

<a id="what-it-runs"></a>
## ဘာကို အသုံးပြုသလဲ

| အစိတ်အပိုင်း | ဖိုင် | ရင်းမြစ် |
|---|---|---|
| Diffusion model | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), base [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Text encoder | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), FLUX.1 အမျိုးအစား autoencoder |
| Engine | `sd-cli.exe`, stable-diffusion.cpp `32d516c` နဲ့ [`patches/`](patches) ထဲက patch တွေ | ဒီ repository ရဲ့ v0.2.0 release (`sinirsiz-foto-engine-v0.2.0-win-x64-cuda12.8-sm61.zip`) |
| CUDA runtime | `cudart`, `cublas`, `cublasLt` (12.8)၊ မပြင်ထားပါ | wan22-pascal-4gb v0.1.0 release က zip |
| cuDNN (မူလအတိုင်း တပ်ဆင်ပေးသည်; `--no-cudnn` က ကျော်သည်) | DLL 8 ခု၊ version 9.10.2.21 (CUDA 11 build) | NVIDIA ရဲ့ ကိုယ်ပိုင် server၊ NVIDIA ရဲ့ လိုင်စင်အောက်မှာ၊ ဒီမှာ မသိမ်းထားပါ |

သတ်မှတ်ထားတဲ့ setting များ: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`။
steps ကို မလျှော့ပါဘူး၊ negative prompt မထည့်ပါဘူး၊ caching မဖွင့်ပါဘူး: model ကို 8 steps အတွက် distill လုပ်ထားပြီး negative prompt မသုံးပါဘူး ([prompts](docs/PROMPTS.md) ကို ကြည့်ပါ)။

## ကန့်သတ်ချက်များ (အားထားမယ့်အရင် ဖတ်ပါ)

- **Windows သာ။** အသင့်ပြင်ထားတဲ့ engine နဲ့ ဒီ script တွေက Windows အတွက်ပဲ ဖြစ်ပါတယ်။
- **ကတ်တစ်ခု၊ စက်တစ်လုံး။** GTX 1050 Ti 4 GB လက်ပ်တော့တစ်လုံးပေါ်မှာပဲ တိုင်းထားတယ် (i7-7700HQ၊ RAM 16 GB၊ Windows 10၊ driver 581.29၊ model တွေ SSD ပေါ်မှာ)။ တခြား GPU နဲ့ driver တွေ၊ RAM 16 GB ထက်နည်းတဲ့ စက်တွေ၊ Linux နဲ့ macOS: **မစမ်းရသေးပါ**။
- အခြားကတ်များနှင့် စနစ်များ (မည်သည့်လမ်းကြောင်း ရှိသည်၊ ကျွန်ုပ်တို့ ကိုယ်တိုင် မစမ်းခဲ့သော Linux ပေါ်ရှိ AMD ကတ်တစ်ခု၏ အသိုင်းအဝိုင်း စမ်းသပ်ချက်): [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md)။
- **engine ကို Pascal (sm_61) အတွက်ပဲ build လုပ်ထားပါတယ်။** တခြား architecture တွေအတွက် ကိုယ်ပိုင် build လိုပါတယ် ([`docs/BUILD.md`](docs/BUILD.md))၊ တစ်ခုမှ မစမ်းရသေးပါ။
- **cuDNN:** cuDNN 9.10.2.21 ရဲ့ CUDA 11 build နဲ့ တိုင်းခဲ့ပါတယ်။ CUDA 12 build က ဖိုင်တွေ မတူဘဲ မတိုင်းရသေးပါ။
- **မှတ်ဉာဏ် ကျပ်ပါတယ်။** RAM လွတ်က MiB ရာဂဏန်းလောက်ပဲ ကျန်ပါတော့တယ်၊ တခြားပရိုဂရမ်တွေကို ပိတ်ပါ၊ တစ်ကြိမ်ကို ပုံတစ်ပုံပဲ ပြေးပါ။ engine ရဲ့ မှတ်ဉာဏ်စစ်ဆေးမှု ကျော်ပြီးနောက် GPU မှတ်ဉာဏ် ကုန်သွားတာ မတွေ့ခဲ့ပါဘူး၊ အဲဒီအခါ ဘာဖြစ်မလဲဆိုတာလည်း မစမ်းခဲ့ပါဘူး။
- **အရွယ်အစားများ:** 768x1344၊ 1344x768 နဲ့ 1024x1024 ကိုပဲ စမ်းထားပါတယ်။ ပိုကြီးတဲ့ အရွယ်အစားတွေက သတိပေးချက် ထုတ်ပြပြီး မှတ်ဉာဏ် ကုန်သွားနိုင်ပါတယ်။
- prompt နဲ့ ကိုက်ညီမှုက တစ်စိတ်တစ်ပိုင်းပဲ ဖြစ်ပါတယ်: ပုံတစ်ပုံက prompt ကို အသေးစိတ်အားလုံးမှာ အမြဲမလိုက်ပါဘူး။ ပုံထဲက စာသားနဲ့ လက်တွေ့ကမ္ဘာက အဆောက်အအုံတွေကို မအကဲဖြတ်ရသေးပါ။
- PSNR ကိုးကားချက်က ကျွန်တော်တို့ engine ကိုယ်တိုင်ရဲ့ CPU decode ဖြစ်ပြီး လွတ်လပ်တဲ့ implementation မဟုတ်ပါဘူး။
- [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) ထဲက ကိန်းတွေက တခြားပြောမထားရင် တစ်ခုချင်း တစ်ကြိမ်ပြေးမှုက လာတာပါ။

## လိုင်စင်နဲ့ အသိအမှတ်ပြုခြင်း

- ဒီ repository ရဲ့ script တွေနဲ့ စာရွက်စာတမ်းတွေ: [Apache-2.0](LICENSE) နဲ့ [`NOTICE`](NOTICE) ဖိုင်တစ်ခု။ [`patches/`](patches) ထဲက engine patch တွေက ပြင်ထားတဲ့ကုဒ်လိုပဲ MIT ဖြစ်ပါတယ်။
- stable-diffusion.cpp နဲ့ ggml က MIT ဖြစ်ပါတယ်။ engine ထဲကို compile လုပ်ထည့်ထားတဲ့ ပြင်ပအဖွဲ့ကုဒ်တွေရဲ့ notice တွေက [`licenses/`](licenses) နဲ့ [`THIRD_PARTY.md`](THIRD_PARTY.md) ထဲမှာ ရှိပါတယ်။
- model ဖိုင်တွေကို ဒီမှာ မသိမ်းထားပါဘူး။ အပေါ်က ရင်းမြစ်တွေကနေ သူတို့ကိုယ်ပိုင် လိုင်စင်အောက်မှာ download လုပ်ပါတယ် (Hugging Face က အားလုံးအတွက် Apache-2.0 လို့ ပြထားတယ်၊ 2026-11-13 မှာ ဖတ်ခဲ့တယ်)။ model card က ဖန်တီးထားတဲ့ပုံတွေကို ဘယ်သူပိုင်လဲဆိုတာ ဘာမှ မပြောထားပါဘူး၊ ကျွန်တော်တို့လည်း အဲဒီအကြောင်း ဘာမှ မဆိုပါဘူး။
- **cuDNN နဲ့ CUDA runtime တို့က NVIDIA ပိုင်ပါတယ်**၊ ဒီ repository ရဲ့ လိုင်စင်အောက်မှာ မပါပါဘူး။ cuDNN ကို NVIDIA ရဲ့ server ကနေ NVIDIA ရဲ့ လိုင်စင်အောက်မှာ download လုပ်ပါတယ် (`--no-cudnn` က ကျော်ပါတယ်)။ CUDA runtime DLL တွေက မပြင်ထားတဲ့ သီးခြား zip တစ်ခုထဲမှာ ရှိပါတယ် (CUDA Toolkit EULA, Attachment A)။ အသေးစိတ်နဲ့ ကျွန်တော်တို့ မစစ်နိုင်ခဲ့တာတွေ: [`THIRD_PARTY.md`](THIRD_PARTY.md)။
- **အသိအမှတ်ပြုခြင်း။** `NOTICE` ဖိုင်ကို မိတ္တူတွေနဲ့ ဆင့်ပွားလုပ်ငန်းတွေနဲ့အတူ ထိန်းထားရတာက စည်းကမ်းချက် (condition) ဖြစ်ပါတယ် (Apache-2.0၊ ပုဒ်မ 4)။ ဒါ့အပြင် "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey" လိုမျိုး စာကြောင်းတစ်ကြောင်း ထည့်ပေးရင် ကျေးဇူးတင်ပါတယ်၊ ဒါပေမယ့် မဖြစ်မနေ မလိုပါဘူး။
- [`ETHICS.md`](ETHICS.md) ကို ဖတ်ပေးပါ: ပုံတိုင်းက ဖန်တီးထားတာဖြစ်ပြီး သင်ထုတ်ပြန်တာအတွက် သင့်တာဝန်ပါ။

## ပါဝင်ကူညီခြင်း

သင်လုပ်နိုင်တဲ့ အသုံးဝင်ဆုံးအရာက **သင့်ကတ်ကို စမ်းကြည့်ပြီး** ဘာဖြစ်ခဲ့လဲ ပြောပြတာပါ: GPU နာမည်၊ driver၊ RAM၊ `run.json` နဲ့ log ရဲ့ နောက်ဆုံးလိုင်းတွေ ("Hardware test report" issue form)။ စာရွက်စာတမ်းနဲ့ script တွေကို ပြင်ဆင်ပေးတာကိုလည်း ကြိုဆိုပါတယ်၊ [`CONTRIBUTING.md`](CONTRIBUTING.md) ကို ကြည့်ပါ။ လုံခြုံရေး အစီရင်ခံစာတွေကို [`SECURITY.md`](SECURITY.md) ထဲက ပုဂ္ဂိုလ်ရေးလမ်းကြောင်းနဲ့ ပို့ပါ။

[AI agent များအတွက် တပ်ဆင်လမ်းညွှန်](AGENTS.md) · [တိုင်းတာမှုများ](docs/MEASUREMENTS.md) · [ပြဿနာဖြေရှင်းခြင်း](docs/TROUBLESHOOTING.md) · [Engine build လုပ်ခြင်း](docs/BUILD.md) · [Patch များ](patches/README.md) · [Prompt များ](docs/PROMPTS.md) · [ပြင်ပအဖွဲ့](THIRD_PARTY.md) · [ပြောင်းလဲမှုမှတ်တမ်း](CHANGELOG.md)

ဒီစာမျက်နှာကို AI ရဲ့ အကူအညီနဲ့ ဒေသအလိုက် ပြင်ဆင်ထားတာဖြစ်ပြီး ပြင်ဆင်ချက်တွေကို အပြည့်အဝ ကြိုဆိုပါတယ်: [`CONTRIBUTING.md`](CONTRIBUTING.md) ကို ကြည့်ပါ။
