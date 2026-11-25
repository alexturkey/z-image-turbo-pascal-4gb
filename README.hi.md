[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · **हिन्दी** · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**Windows पर, stable-diffusion.cpp के साथ, 4 GB की GTX 1050 Ti (Pascal, sm_61) पर 768x1344 साइज़ का Z-Image-Turbo (Q8_0 GGUF) text-to-image (टेक्स्ट से इमेज बनाना)।** इसे 16 GB RAM वाले एक लैपटॉप पर मापा गया, जहाँ प्रोसेस लगभग 11 GB RAM इस्तेमाल करता है। एक ही seed एक जैसे पिक्सल देता है, पिक्सल दर पिक्सल; मापें और इंजन के पैच सार्वजनिक हैं, डाउनलोड sha256 से पिन किए गए हैं, और कोई AI कोडिंग एजेंट इसे कदम-दर-कदम इंस्टॉल कर सकता है।

*अनौपचारिक (unofficial)। Tongyi-MAI (Z-Image), leejet (stable-diffusion.cpp) या NVIDIA से कोई संबंध नहीं है।*

## यहाँ से शुरू करें

एक तैयार पैकेज मौजूद है, इसलिए पहले उसे आज़माएँ। अगर आपका हार्डवेयर अलग है या कोई कदम अटक जाए, तो बाकी सब खुला है: पैच, बिल्ड की विधि और मापें इसी रिपॉज़िटरी में हैं, इसलिए आप अपने कार्ड के लिए बिल्ड कर सकते हैं या इन्हें अपने हिसाब से ढाल सकते हैं।

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

दूसरा कदम लगभग 12.2 GB डाउनलोड करता है और हमारे कनेक्शन पर एक बार में 29 मिनट लगे; यह पहले एक "Preflight" ब्लॉक दिखाता है (आपका GPU, RAM और खाली डिस्क, हमारी मापी हुई वैल्यू के बगल में; यह सिर्फ़ जानकारी देता है)।
सिर्फ़ GTX 1050 Ti 4 GB लैपटॉप कार्ड (Pascal, compute capability 6.1) को मापा गया। दूसरे कार्ड आज़माए नहीं गए।
अगर आप कोई AI कोडिंग एजेंट इस्तेमाल करते हैं (Claude Code, Codex, Cursor और इसी तरह के), तो उसे [`AGENTS.md`](AGENTS.md) पर भेजें।

## एक नज़र में

v0.1.0 वाले ढाँचे की तुलना में: एक तस्वीर में 261.6 s की जगह 188–193 s लगते हैं, VAE चरण में 29.8 से 36.3 s की जगह 12.5–21.7 s लगते हैं, वही seed वही पिक्सल देता है, और इस README की हर संख्या के पीछे एक कमांड और एक फ़ाइल है।

768x1344, seed 42, 8 steps, वही मशीन। v0.1.0 की संख्याएँ v0.1.0 के README से हैं (clean-root टेस्ट और पाँच रन); v0.3.0 की संख्याएँ इस रिलीज़ के clean-root टेस्ट से हैं।

| | v0.1.0 (कभी प्रकाशित नहीं हुआ; पुराना ढाँचा) | v0.3.0 |
|---|---|---|
| एक तस्वीर का समय (एक `generate.py` रन) | 261.6 s | 188–193 s |
| VAE डिकोड (आख़िरी चरण) | 29.8 से 36.3 s | 12.5–21.7 s |
| रेफ़रेंस डिकोड से नज़दीकी (PSNR, ज़्यादा यानी बेहतर) | 38 से 43 dB | 71 से 73 dB |
| GPU मेमोरी का शिखर (nvidia-smi) | 2949 से 2957 MiB | 3057–3059 MiB |
| प्रोसेस मेमोरी, शिखर | 10.5 से 10.9 GB (जैसा तब दर्ज हुआ) | 10 489–11 203 MiB |
| सबसे कम खाली RAM | 331 से 576 MiB | 303–532 MiB |

इसे कैसे पढ़ें: रेफ़रेंस वही latent है जिसे CPU पर एक ही float32 टुकड़े में डिकोड किया गया; PSNR हमारे GPU डिकोड की उससे तुलना करता है (3 तस्वीरें)। यह बताता है कि VAE चरण उस रेफ़रेंस के कितने क़रीब है। यह नहीं बताता कि कोई तस्वीर कितनी अच्छी दिखती है। v0.2.0 की तस्वीरें, एक ही prompt और seed के लिए, v0.1.0 से बाइट-दर-बाइट एक जैसी नहीं हैं, क्योंकि VAE का रास्ता जानबूझकर बदला गया। तरीक़ा और जो नहीं मापा गया: [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md)।

## उदाहरण

**इस रिपॉज़िटरी से AI द्वारा बनाई गई तस्वीरें** (Z-Image-Turbo Q8_0, seed 42, 8 steps)। ये असली फ़ोटो नहीं हैं; इमारतें और ब्योरे
ग़लत हो सकते हैं, और कोई तस्वीर हर ब्योरे में अपने prompt का पालन नहीं भी कर सकती। पूरे prompt [`prompts/`](prompts) और [`docs/PROMPTS.md`](docs/PROMPTS.md) में हैं।

| | | |
|---|---|---|
| ![सुनहरे पहर में एफ़िल टावर](docs/examples/eiffel.jpg) | ![तुर्की चाय का गिलास](docs/examples/turkish_tea.jpg) | ![बुज़ुर्ग मछुआरा](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![पहाड़ी ढलान पर गाँव](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![आसमान से इस्तांबुल](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768। असली फ़ोटो नहीं; इमारतें ग़लत हो सकती हैं।

## क्विक स्टार्ट

ज़रूरतें: Windows 10/11, 4 GB वाला NVIDIA GPU, CUDA 12.8 को सपोर्ट करने वाला ड्राइवर (ड्राइवर 581.29 पर मापा गया; पुराने ड्राइवर आज़माए नहीं गए; CUDA runtime अपने आप डाउनलोड हो जाता है), Python 3.10 या नया,
git, लगभग 14 GB खाली डिस्क (डाउनलोड cuDNN के साथ लगभग 12.2 GB; खाली डिस्क का आँकड़ा एक अनुमान है) और 16 GB RAM (जो मापा गया; इससे कम आज़माया नहीं गया)।

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- `setup.py` पहले एक "Preflight" ब्लॉक दिखाता है (आपका GPU, RAM और खाली डिस्क, हमारी मापी हुई वैल्यू के बगल में; यह सिर्फ़ जानकारी देता है और कभी कुछ रोकता नहीं)। फिर यह [`models.lock.json`](models.lock.json) में दिए पिन किए हुए पतों से डाउनलोड करता है और हर फ़ाइल को sha256 से जाँचता है। यह `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK`, फिर `CUDNN_OK` या `CUDNN_SKIPPED`, और आख़िर में `SETUP_OK` दिखाता है।
  `--models-dir` और `--bin-dir` न देने पर यह रिपॉज़िटरी के root में `models/` और `bin/` इस्तेमाल करता है; मॉडल SSD पर रखें (सिर्फ़ SSD पर मापा गया)।
  इसे कभी भी Ctrl+C से रोकें और वही कमांड दोबारा चलाएँ: डाउनलोड `.part` फ़ाइलों से आगे बढ़ते हैं।
- **cuDNN डिफ़ॉल्ट रूप से इंस्टॉल होता है और इस रिपॉज़िटरी का हिस्सा नहीं है।** यह NVIDIA का सॉफ़्टवेयर है, जो NVIDIA के अपने लाइसेंस ([लाइसेंस का पाठ](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)) के तहत आता है और NVIDIA GPU वाले सिस्टम के लिए है। यह NVIDIA के सर्वर से बिना किसी भुगतान की माँग और बिना साइन-इन के डाउनलोड होता है, और हमें लाइसेंस में ऐसी कोई धारा नहीं मिली जो व्यावसायिक या निजी इस्तेमाल को सीमित करती हो। `setup.py` लाइसेंस का पता दिखाता है, फ़ाइल डाउनलोड करता है और सिर्फ़ आठ DLL `sd-cli.exe` के बगल में कॉपी करता है। NVIDIA के लाइसेंस में लिखा है कि जो इसकी शर्तें स्वीकार नहीं करता, उसके लिए इसे डाउनलोड, इंस्टॉल या इस्तेमाल करना मना है; ऐसे में `python scripts/setup.py --no-cudnn` चलाएँ। cuDNN के बिना भी सब कुछ धीमे v0.1.0 वाले VAE रास्ते (`--vae legacy`) से चलता है, और `generate.py` यह बता देता है।
- `generate.py` `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, `run.json` (समय, चरण, कौन-सा VAE रास्ता चला, GPU मेमोरी का शिखर, पूरी कमांड) और `log.txt` लिखता है, और `IMAGE_OK <path>` दिखाता है।

## इस्तेमाल

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| विकल्प | मतलब |
|---|---|
| `--prompt "<text>"` या `--prompt-file <txt>` | prompt (दोनों में से एक ज़रूरी है) |
| `--width`, `--height` | 16 के गुणज, 256 से 2048; डिफ़ॉल्ट 768x1344; आज़माए गए: 768x1344, 1344x768, 1024x1024 |
| `--seed` | डिफ़ॉल्ट 42 |
| `--out`, `--name` | आउटपुट फ़ोल्डर का root (डिफ़ॉल्ट `outputs/`) और रन फ़ोल्डर के लिए एक छोटा नाम |
| `--models-dir`, `--bin-dir` | जहाँ `setup.py` ने मॉडल और इंजन रखे |
| `--vae auto` (डिफ़ॉल्ट) | cuDNN float32; पहले एक टुकड़ा, फिर दो बड़ी tile, फिर छोटी डिफ़ॉल्ट tile |
| `--vae tiled` | cuDNN float32, हमेशा दो बड़ी tile |
| `--vae legacy` | v0.1.0 वाला रास्ता: cuDNN नहीं, छोटी tile। cuDNN की DLL न मिलने पर अपने आप (चेतावनी के साथ) इस्तेमाल होता है |

Steps (8), cfg (1.0), sampler और scheduler जानबूझकर तय रखे गए हैं; देखें [यह क्या चलाता है](#what-it-runs)।

## ख़ुद जाँचें

- `generate.py` अपनी आख़िरी पंक्तियों में से एक के रूप में `PIXEL_SHA256 <hex>` दिखाता है: डिकोड किए गए पिक्सलों का हैश। वही कमांड दो बार चलाएँ और दोनों तस्वीरों की तुलना करें: `python scripts/compare.py <run A>/image.png <run B>/image.png` को `SAME_PIXELS` दिखाना चाहिए।
- हमारी मशीन पर पाँचों उदाहरणों का `PIXEL_SHA256` [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) में है। किसी PNG का फ़ाइल-हैश अलग हो सकता है, भले ही पिक्सल एक जैसे हों, क्योंकि PNG में जनरेशन के पैरामीटर टेक्स्ट के रूप में रहते हैं; फ़ाइलों की नहीं, पिक्सलों की तुलना करें।
- ईमानदार सीमा: हमने यह नहीं मापा कि कोई दूसरा कार्ड या ड्राइवर वही पिक्सल देता है या नहीं।

## यह 4 GB में कैसे समाता है

- **मॉडल के लेखक क्या कहते हैं।** Z-Image-Turbo का model card कहता है कि मॉडल "fits comfortably within 16G VRAM consumer devices" (यानी 16 GB वाले कंज़्यूमर कार्ड पर आराम से आ जाता है) ([model card](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo))। यह 16 GB वाले कार्ड के बारे में एक कथन है। आधिकारिक README भी stable-diffusion.cpp को तीसरे पक्ष के विकल्प के रूप में सूचीबद्ध करता है और उसके लिए "as little as 4GB of VRAM" (यानी कम से कम 4 GB VRAM में) उद्धृत करता है ([README](https://github.com/Tongyi-MAI/Z-Image)); यह stable-diffusion.cpp प्रोजेक्ट का दावा है, Z-Image टीम की कोई शर्त नहीं।
- **हमने क्या मापा।** Z-Image-Turbo Q8_0 (6.6 GB की फ़ाइल) और Qwen3-4B Q8_0 टेक्स्ट एनकोडर, 768x1344: nvidia-smi द्वारा हर 2 s पर लिया गया GPU शिखर (कोई छोटा उछाल छूट सकता है) 4096 MiB वाले कार्ड पर 2949 से 2957 MiB (v0.1.0 इंजन) और 3057–3059 MiB (v0.2.0 इंजन) रहा। वेट (10 509 MiB; इंजन का लॉग इसे MB लिखता है) सिस्टम RAM में रहते हैं; इंजन नेटवर्क को GPU पर एक बार में एक segment (नेटवर्क का एक टुकड़ा) कॉपी करता है: 36 segment, जैसा लॉग की पंक्ति `z_image using 36 segments` में है।
- **इसकी क़ीमत क्या है।** समय और सिस्टम मेमोरी: हर तस्वीर पर 188–193 s, और इंजन प्रोसेस 16 GB की मशीन पर लगभग 10 489–11 203 MiB RAM थामे रखता है (memory-mapped मॉडल पेज समेत), इसलिए चलते समय खाली RAM कुछ सौ MiB तक गिर जाती है।
- **दूसरों के सेटअप।** दूसरे लोग 4 GB कार्ड पर Z-Image कम quantization या छोटे साइज़ के साथ चलाने की रिपोर्ट करते हैं (उदाहरण के लिए 4 GB कार्ड वाला stable-diffusion.cpp का विकी पेज 1024x512 पर Q3_K या Q4_0 सुझाता है)। जहाँ हमने देखा (सूची और तारीख़ [`docs/RELATED.md`](docs/RELATED.md) में) वहाँ हमें ऐसा कोई प्रकाशित सेटअप नहीं मिला जो चारों को एक साथ जोड़ता हो: 4 GB का कार्ड, Q8_0, 768x1344 या उससे बड़ा साइज़, और मापा हुआ समय व GPU मेमोरी। यह उन जगहों के बारे में कथन है जहाँ हमने देखा, हर जगह के बारे में नहीं।
- **कौन क्या करता है।** 4 GB में समाना स्वयं stable-diffusion.cpp से आता है: `--offload-to-cpu`, `--mmap`, टुकड़ों में काम करना, और flash attention (इसे बंद करने पर एक रन को 4205 MB चाहिए थे और वह नहीं समाया)। हमारे पैच गति और बेहतर VAE चरण के लिए हैं, समाने के लिए नहीं। हमने बिना पैच वाले upstream इंजन को इस कार्ड पर नहीं चलाया, इसलिए नहीं कह सकते कि वह समाता है या नहीं।

## यह कैसे काम करता है

stable-diffusion.cpp `master-1088-32d516c` के ऊपर तीन बदलाव (सब स्विच हैं; [`patches/README.md`](patches/README.md) की तालिका हर एक को उसके environment variable के साथ सूचीबद्ध करती है):

1. **Refiner हर step में एक बार चलता है।** एक ग्रुप का नाम दो बार इस्तेमाल हो रहा था, इसलिए चार refiner ब्लॉक दूसरी बार गिने जा रहे थे। इसे ठीक करने से step 2 से 8 हर एक में लगभग 1.3 s तेज़ हुए (22.0 से 20.7 s), और तस्वीर पिक्सल के स्तर पर वही रही (3 तस्वीरें जाँची गईं)।
2. **VAE, cuDNN से, float32 में।** आख़िरी चरण (latent को पिक्सल में बदलना) अब NVIDIA का cuDNN float32 convolution इस्तेमाल करता है। हमारे कार्ड पर इसने VAE को 23 से 27 s से घटाकर 10 से 15 s कर दिया और रेफ़रेंस के मुक़ाबले PSNR 38 से 43 dB से बढ़ाकर 45 से 49 dB कर दिया (बड़ी tile के साथ)।
3. **पहले एक टुकड़ा।** अब इंजन पूरी तस्वीर को एक ही टुकड़े में डिकोड करने की कोशिश करता है जब मेमोरी की जाँच कहे कि वह समाएगा (margin 256 MiB), नहीं तो दो बड़ी tile पर, और फिर छोटी tile पर लौटता है। एक टुकड़े में VAE में लगभग 8–16 s लगे और रेफ़रेंस के मुक़ाबले PSNR 71 से 73 dB रहा। अगर मजबूरी में पीछे हटना पड़े, तो तस्वीर के पिक्सल tile वाली तस्वीर जैसे ही रहते हैं (`PIXEL_SHA256` से जाँचा गया)। क्या हुआ, यह `run.json` में लिखा जाता है (`stages.vae_path`: `full`, `tile`, `floor` या `retry`)।

इसके अलावा: `--eager-load` (मॉडल पेज पहले ही पढ़ लेता है; उसी तस्वीर पर 241.2 s से 220.3 s, development build, हर एक का एक रन) तय कमांड का हिस्सा है।

<a id="what-it-runs"></a>
## यह क्या चलाता है

| हिस्सा | फ़ाइल | स्रोत |
|---|---|---|
| Diffusion मॉडल | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), आधार [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| टेक्स्ट एनकोडर | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), FLUX.1 प्रकार का autoencoder |
| इंजन | `sd-cli.exe`, stable-diffusion.cpp `32d516c`, [`patches/`](patches) के पैच के साथ | इस रिपॉज़िटरी की v0.3.0 रिलीज़ (`sinirsiz-foto-engine-v0.3.0-win-x64-cuda12.8-sm61.zip`) |
| CUDA runtime | `cudart`, `cublas`, `cublasLt` (12.8), बिना बदले | wan22-pascal-4gb की v0.1.0 रिलीज़ की zip |
| cuDNN (डिफ़ॉल्ट रूप से इंस्टॉल; `--no-cudnn` इसे छोड़ देता है) | 8 DLL, संस्करण 9.10.2.21 (CUDA 11 बिल्ड) | NVIDIA का अपना सर्वर, NVIDIA के लाइसेंस के तहत; यहाँ नहीं रखा जाता |

तय सेटिंग: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`।
हम steps कम नहीं करते, negative prompt नहीं जोड़ते और caching चालू नहीं करते: मॉडल 8 steps के लिए distilled है और negative prompt इस्तेमाल नहीं करता (देखें [prompts](docs/PROMPTS.md))।

## सीमाएँ (भरोसा करने से पहले पढ़ें)

- **सिर्फ़ Windows।** तैयार इंजन और ये स्क्रिप्ट सिर्फ़ Windows के लिए हैं।
- **एक कार्ड, एक मशीन।** सिर्फ़ एक GTX 1050 Ti 4 GB लैपटॉप पर मापा गया (i7-7700HQ, 16 GB RAM, Windows 10, ड्राइवर 581.29, मॉडल SSD पर)। दूसरे GPU और ड्राइवर, 16 GB से कम RAM वाली मशीनें, Linux और macOS: **आज़माए नहीं गए**।
- दूसरे कार्ड और सिस्टम (कौन-सा रास्ता मौजूद है, और Linux पर एक AMD कार्ड का सामुदायिक परीक्षण जिसे हमने खुद नहीं चलाया): [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md)।
- **इंजन सिर्फ़ Pascal (sm_61) के लिए बनाया गया है।** दूसरे आर्किटेक्चर के लिए आपको अपना बिल्ड चाहिए ([`docs/BUILD.md`](docs/BUILD.md)); हमने ऐसा कोई बिल्ड आज़माया नहीं।
- **cuDNN:** हमने cuDNN 9.10.2.21 के CUDA 11 बिल्ड के साथ मापा। CUDA 12 बिल्ड की फ़ाइलें अलग हैं और उसे मापा नहीं गया।
- **मेमोरी तंग है।** खाली RAM कुछ सौ MiB तक गिर जाती है; दूसरे प्रोग्राम बंद करें, एक बार में एक तस्वीर बनाएँ। इंजन की मेमोरी जाँच पास होने के बाद हमने GPU मेमोरी ख़त्म होते नहीं देखी, और तब क्या होता है, यह हमने आज़माया नहीं।
- **साइज़:** सिर्फ़ 768x1344, 1344x768 और 1024x1024 आज़माए गए। इनसे बड़े साइज़ चेतावनी दिखाते हैं और मेमोरी से बाहर जा सकते हैं।
- Prompt का पालन आंशिक है: कोई तस्वीर हर ब्योरे में अपने prompt का पालन नहीं भी कर सकती। तस्वीरों के अंदर का टेक्स्ट और असली दुनिया की इमारतों का मूल्यांकन नहीं किया गया।
- PSNR का रेफ़रेंस हमारे अपने इंजन का CPU डिकोड है, कोई स्वतंत्र इम्प्लीमेंटेशन नहीं।
- [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) की संख्याएँ, जब तक कुछ और न लिखा हो, एक-एक रन से आई हैं।

## लाइसेंस और श्रेय

- इस रिपॉज़िटरी की स्क्रिप्ट और दस्तावेज़: [Apache-2.0](LICENSE), साथ में एक [`NOTICE`](NOTICE) फ़ाइल। [`patches/`](patches) के इंजन पैच MIT हैं, उस कोड की तरह जिसे वे बदलते हैं।
- stable-diffusion.cpp और ggml MIT हैं। इंजन में कंपाइल किए गए तीसरे पक्ष के कोड की सूचनाएँ [`licenses/`](licenses) और [`THIRD_PARTY.md`](THIRD_PARTY.md) में हैं।
- मॉडल फ़ाइलें यहाँ नहीं रखी जातीं; वे ऊपर दिए स्रोतों से, अपने-अपने लाइसेंस के तहत डाउनलोड होती हैं (Hugging Face सबके लिए Apache-2.0 दिखाता है, 2026-11-13 को पढ़ा गया)। Model card यह नहीं बताता कि बनाई गई तस्वीरों का मालिक कौन है, और हम इस बारे में कोई दावा नहीं करते।
- **cuDNN और CUDA runtime NVIDIA की संपत्ति हैं** और इस रिपॉज़िटरी के लाइसेंस के अंतर्गत नहीं हैं। cuDNN NVIDIA के सर्वर से NVIDIA के लाइसेंस के तहत डाउनलोड होता है (`--no-cudnn` इसे छोड़ देता है); CUDA runtime की DLL एक अलग, बिना बदली zip में हैं (CUDA Toolkit EULA, Attachment A)। ब्योरे और जो हम सत्यापित नहीं कर सके: [`THIRD_PARTY.md`](THIRD_PARTY.md)।
- **श्रेय।** कॉपियों और व्युत्पन्न कामों के साथ `NOTICE` फ़ाइल को बनाए रखना शर्त है (Apache-2.0, section 4)। इसके अलावा, "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey" जैसी एक पंक्ति का स्वागत है, पर वह ज़रूरी नहीं है।
- कृपया [`ETHICS.md`](ETHICS.md) पढ़ें: हर तस्वीर कृत्रिम (synthetic) है, और आप जो प्रकाशित करते हैं उसकी ज़िम्मेदारी आपकी है।

## योगदान

सबसे उपयोगी काम है **अपने कार्ड को टेस्ट करना** और हमें बताना कि क्या हुआ: GPU का नाम, ड्राइवर, RAM, `run.json` और लॉग की आख़िरी पंक्तियाँ ("Hardware test report" issue फ़ॉर्म)। दस्तावेज़ों और स्क्रिप्ट में सुधारों का भी स्वागत है; देखें [`CONTRIBUTING.md`](CONTRIBUTING.md)। सुरक्षा संबंधी रिपोर्ट [`SECURITY.md`](SECURITY.md) में बताए निजी रास्ते से भेजी जाती हैं।

[AI एजेंटों के लिए इंस्टॉल गाइड](AGENTS.md) · [मापें](docs/MEASUREMENTS.md) · [समस्या-निवारण](docs/TROUBLESHOOTING.md) · [इंजन बिल्ड करना](docs/BUILD.md) · [पैच](patches/README.md) · [Prompts](docs/PROMPTS.md) · [तीसरे पक्ष](THIRD_PARTY.md) · [चेंजलॉग](CHANGELOG.md)

यह पन्ना AI की मदद से हिन्दी में ढाला गया है; सुधार बहुत स्वागत योग्य हैं, देखें [`CONTRIBUTING.md`](CONTRIBUTING.md)।
