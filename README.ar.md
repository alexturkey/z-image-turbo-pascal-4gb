[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · **العربية** · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**توليد الصور من النص بنموذج Z-Image-Turbo (Q8_0 GGUF) بدقة 768x1344 على بطاقة GTX 1050 Ti بذاكرة 4 GB (Pascal, sm_61)، عبر stable-diffusion.cpp وعلى Windows.** جرى القياس على حاسوب محمول بذاكرة RAM سعتها 16 GB، وتستهلك العملية فيه نحو 11 GB من الذاكرة. البذرة (seed) نفسها تعطي البكسلات نفسها، بكسلًا ببكسل. القياسات وتعديلات المحرّك منشورة، والتنزيلات مثبّتة بقيمة sha256، ويستطيع وكيل برمجة بالذكاء الاصطناعي تنفيذ التثبيت خطوة بخطوة.

*غير رسمي. لا صلة له بـ Tongyi-MAI (Z-Image) ولا بـ leejet (stable-diffusion.cpp) ولا بـ NVIDIA.*

> **هل تستخدم وكيل برمجة بالذكاء الاصطناعي (Codex, Claude Code, Gemini, Cursor)؟** أعطه هذه الجملة الواحدة: «اقرأ `AGENTS_HIZLI.md` حتى النهاية، وشغّل `python scripts/tani.py` أولاً، وسجّل تقدمك في `DURUM.md`، واسألني قبل أن تحذف أو تنقل أي شيء، أو تغيّر Python النظام أو PATH، أو تخفض أي إعداد جودة.» سيشخّص الوكيل هذا الجهاز ويكتب قائمة تحقق ويسألك عند كل قرار.

## ابدأ من هنا

توجد حزمة جاهزة، فجرّبها أولًا. إن كان عتادك مختلفًا أو تعثّرت إحدى الخطوات فبقية المشروع مفتوحة: التعديلات (patches) ووصفة البناء والقياسات كلها في هذا المستودع، ويمكنك البناء لبطاقتك أو تكييفها.

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

تنزّل الخطوة 2 نحو 12.2 GB، واستغرقت 29 دقيقة في مرة واحدة على اتصالنا. تطبع أولًا كتلة "Preflight" (بطاقتك وذاكرة RAM والمساحة الحرة على القرص إلى جانب ما قسناه نحن؛ للإعلام فقط).
قِيست بطاقة واحدة فقط: GTX 1050 Ti بذاكرة 4 GB في حاسوب محمول (Pascal، قدرة الحوسبة 6.1). أما البطاقات الأخرى فلم تُختبر.
إن كنت تستخدم وكيل برمجة بالذكاء الاصطناعي (Claude Code وCodex وCursor وما شابهها) فوجّهه إلى الملف [`AGENTS.md`](AGENTS.md).

## نظرة سريعة

مقارنةً ببنية v0.1.0: تستغرق الصورة 188–193 s بدلًا من 261.6 s، ومرحلة VAE 12.5–21.7 s بدلًا من 29.8 إلى 36.3 s، والبذرة نفسها تعطي البكسلات نفسها، وخلف كل رقم في هذا الملف أمر وملف يمكن الرجوع إليهما.

768x1344، بذرة 42، 8 خطوات، الجهاز نفسه. أرقام v0.1.0 من ملف README الخاص بـ v0.1.0 (اختبار الجذر النظيف وخمس تشغيلات)، وأرقام v0.3.0 من اختبار الجذر النظيف لهذا الإصدار.

| | v0.1.0 (لم يُنشر؛ بنية قديمة) | v0.3.0 |
|---|---|---|
| زمن الصورة الواحدة (تشغيلة واحدة لـ `generate.py`) | 261.6 s | 188–193 s |
| فك ترميز VAE (المرحلة الأخيرة) | 29.8 إلى 36.3 s | 12.5–21.7 s |
| القرب من فك ترميز مرجعي (PSNR، الأعلى أقرب) | 38 إلى 43 dB | 71 إلى 73 dB |
| ذروة ذاكرة GPU (nvidia-smi) | 2949 إلى 2957 MiB | 3057–3059 MiB |
| ذاكرة العملية، الذروة | 10.5 إلى 10.9 GB (كما سُجّلت حينها) | 10 489–11 203 MiB |
| أدنى ذاكرة RAM حرة لوحظت | 331 إلى 576 MiB | 303–532 MiB |

كيف تقرأ هذا: المرجع هو الـ latent نفسه بعد فك ترميزه على المعالج (CPU) قطعةً واحدة بدقة float32. يقارن PSNR فك الترميز على GPU عندنا بهذا المرجع (3 صور). هو يبيّن مدى قرب مرحلة VAE من المرجع، ولا يبيّن مدى جودة الصورة. صور v0.2.0 ليست مطابقة بايتًا ببايت لصور v0.1.0 مع الموجّه (prompt) والبذرة نفسيهما، لأن مسار VAE تغيّر عمدًا. الطريقة والأجزاء التي لم تُقَس: [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md).

## أمثلة

**صور مولّدة بالذكاء الاصطناعي بهذا المستودع** (Z-Image-Turbo Q8_0، بذرة 42، 8 خطوات). هذه ليست صورًا فوتوغرافية حقيقية؛ وقد تكون المعالم والتفاصيل
غير دقيقة، وقد لا تتبع الصورة موجّهها في كل تفصيل. الموجّهات الكاملة في [`prompts/`](prompts) وفي [`docs/PROMPTS.md`](docs/PROMPTS.md).

| | | |
|---|---|---|
| ![برج إيفل عند الساعة الذهبية](docs/examples/eiffel.jpg) | ![كوب شاي تركي](docs/examples/turkish_tea.jpg) | ![صياد مسن](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![قرية على سفح تل](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![إسطنبول من الجو](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. ليست صورة حقيقية؛ وقد تكون المعالم غير دقيقة.

## التثبيت السريع

المتطلبات: Windows 10/11، وبطاقة NVIDIA بذاكرة 4 GB، وتعريف يدعم CUDA 12.8 (قِيس مع التعريف 581.29؛ أما التعريفات الأقدم فلم تُختبر؛ وبيئة CUDA نفسها تُنزَّل لك)، وPython 3.10 أو أحدث،
وgit، ونحو 14 GB مساحة حرة على القرص (التنزيلات نحو 12.2 GB مع cuDNN؛ ورقم المساحة الحرة تقدير)، وذاكرة RAM بسعة 16 GB (هذا ما قِيس؛ أما الأقل فلم يُختبر).

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- يطبع `setup.py` أولًا كتلة "Preflight" (بطاقتك وذاكرة RAM والمساحة الحرة على القرص إلى جانب ما قسناه نحن؛ للإعلام فقط ولا يمنع شيئًا). ثم ينزّل من العناوين المثبّتة في [`models.lock.json`](models.lock.json) ويتحقق من كل ملف بـ sha256. ويطبع `MODEL_OK <name>` و`ENGINE_OK` و`CUDART_OK`، ثم `CUDNN_OK` أو `CUDNN_SKIPPED`، وأخيرًا `SETUP_OK`.
  إن لم تمرّر `--models-dir` و`--bin-dir` فسيستخدم المجلدين `models/` و`bin/` في جذر المستودع. ضع النماذج على SSD (لم يُقَس إلا مع SSD).
  يمكنك إيقافه في أي وقت بـ Ctrl+C ثم تشغيل الأمر نفسه من جديد: تستأنف التنزيلات من ملفات `.part`.
- **يُثبَّت cuDNN افتراضيًا وليس جزءًا من هذا المستودع.** هو برنامج من NVIDIA بترخيص NVIDIA نفسها ([نص الترخيص](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html))، للأجهزة التي فيها بطاقات NVIDIA. يُنزَّل من خادم NVIDIA دون طلب أي دفع ودون حساب أو تسجيل دخول، ولم نجد في الترخيص أي بند يقيّد الاستخدام التجاري أو الشخصي. يعرض `setup.py` عنوان الترخيص، وينزّل الملف، ولا ينسخ سوى ثمانية ملفات DLL إلى جوار `sd-cli.exe`. ويقول ترخيص NVIDIA إن من لا يقبل شروطه فلا يجوز له تنزيله ولا تثبيته ولا استخدامه؛ وفي هذه الحالة شغّل `python scripts/setup.py --no-cudnn`. وبدون cuDNN يعمل كل شيء بمسار VAE الأبطأ من v0.1.0 (`--vae legacy`)، ويذكر `generate.py` ذلك.
- يكتب `generate.py` الملفات `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png` و`run.json` (الزمن والمراحل ومسار VAE الذي عمل وذروة ذاكرة GPU والأمر الكامل) و`log.txt`، ويطبع `IMAGE_OK <path>`.

## الاستخدام

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| الخيار | المعنى |
|---|---|
| `--prompt "<text>"` أو `--prompt-file <txt>` | الموجّه (prompt)، ولا بد من أحد الخيارين |
| `--width`, `--height` | من مضاعفات 16، بين 256 و2048؛ الافتراضي 768x1344؛ ما اختُبر: 768x1344 و1344x768 و1024x1024 |
| `--seed` | الافتراضي 42 |
| `--out`, `--name` | جذر مجلد المخرجات (الافتراضي `outputs/`) واسم قصير لمجلد التشغيلة |
| `--models-dir`, `--bin-dir` | المكانان اللذان وضع فيهما `setup.py` النماذج والمحرّك |
| `--vae auto` (الافتراضي) | cuDNN بدقة float32؛ يجرّب قطعة واحدة أولًا، ثم بلاطتين كبيرتين (tile)، ثم البلاطة الصغيرة الافتراضية |
| `--vae tiled` | cuDNN بدقة float32، وبلاطتان كبيرتان دائمًا |
| `--vae legacy` | مسار v0.1.0: بلا cuDNN وببلاطات صغيرة. يُستخدم تلقائيًا (مع تحذير) عند غياب ملفات DLL الخاصة بـ cuDNN |

الخطوات (8) وcfg (1.0) وأداة أخذ العينات (sampler) والجدولة (scheduler) ثابتة عمدًا؛ انظر [ما الذي يشغّله](#what-it-runs).

## تحقّق بنفسك

- يطبع `generate.py` السطر `PIXEL_SHA256 <hex>` ضمن آخر أسطره: بصمة للبكسلات بعد فك الترميز. شغّل الأمر نفسه مرتين وقارن الصورتين: ينبغي أن يطبع `python scripts/compare.py <run A>/image.png <run B>/image.png` العبارة `SAME_PIXELS`.
- قيمة `PIXEL_SHA256` للأمثلة الخمسة على جهازنا موجودة في [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md). قد تختلف بصمة ملف PNG حتى مع تطابق البكسلات، لأن PNG يحمل معاملات التوليد نصًّا؛ فقارن البكسلات لا الملفات.
- حدّ صريح: لم نقس هل تعطي بطاقة أخرى أو تعريف آخر البكسلات نفسها.

## لماذا تتسع 4 GB

- **ما يقوله مؤلفو النموذج.** تذكر بطاقة نموذج Z-Image-Turbo أن النموذج "fits comfortably within 16G VRAM consumer devices" (يتسع بارتياح في أجهزة المستهلكين ذات ذاكرة 16 GB) ([بطاقة النموذج](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)). وهذا كلام عن بطاقات 16 GB. كما يذكر ملف README الرسمي stable-diffusion.cpp خيارًا من طرف ثالث وينقل عنه "as little as 4GB of VRAM" (بقدر 4 GB فقط من VRAM) ([README](https://github.com/Tongyi-MAI/Z-Image)). وهذا ادّعاء مشروع stable-diffusion.cpp، وليس شرطًا من فريق Z-Image.
- **ما قسناه.** Z-Image-Turbo Q8_0 (ملف حجمه 6.6 GB) مع مرمّز النص Qwen3-4B Q8_0، بدقة 768x1344: كانت ذروة GPU، التي يأخذ nvidia-smi عيّنة منها كل 2 s (وقد تفوته قفزة قصيرة)، بين 2949 و2957 MiB (محرّك v0.1.0) و3057–3059 MiB (محرّك v0.2.0) على بطاقة 4096 MiB. تبقى الأوزان (10 509 MiB؛ ويطبعها سجل المحرّك بوحدة MB) في ذاكرة النظام RAM؛ وينسخ المحرّك الشبكة إلى GPU مقطعًا بعد مقطع (المقطع شريحة من الشبكة): 36 مقطعًا، كما في سطر السجل `z_image using 36 segments`.
- **كلفة ذلك.** الوقت وذاكرة النظام: 188–193 s للصورة الواحدة، وتحتفظ عملية المحرّك بنحو 10 489–11 203 MiB من RAM (بما فيها صفحات النموذج المربوطة بالذاكرة) على جهاز بذاكرة 16 GB، فتنخفض الذاكرة الحرة إلى بضع مئات من MiB أثناء التشغيل.
- **إعدادات الآخرين.** يذكر آخرون تشغيل Z-Image على بطاقات 4 GB بتكميم (quantization) أدنى أو بأحجام أصغر (مثلًا توصي صفحة wiki الخاصة ببطاقات 4 GB في stable-diffusion.cpp بـ Q3_K أو Q4_0 عند 1024x512). وفي الأماكن التي بحثنا فيها (القائمة والتاريخ في [`docs/RELATED.md`](docs/RELATED.md)) لم نجد إعدادًا منشورًا يجمع الأربعة معًا: بطاقة 4 GB، وQ8_0، ودقة 768x1344 أو أكبر، وزمنًا وذاكرة GPU مقيسين. وهذا كلام عن الأماكن التي بحثنا فيها، لا عن كل مكان.
- **من يفعل ماذا.** الاتساع في 4 GB مصدره stable-diffusion.cpp نفسه: `--offload-to-cpu` و`--mmap` والعمل على شرائح وflash attention (وعند إيقافها احتاجت تشغيلة إلى 4205 MB ولم تتسع). تعديلاتنا للسرعة ولمرحلة VAE أفضل، لا للاتساع. لم نشغّل المحرّك الأصلي غير المعدَّل على هذه البطاقة، فلا نستطيع القول هل يتسع.

## كيف يعمل

ثلاثة تغييرات فوق stable-diffusion.cpp `master-1088-32d516c` (وكلها مفاتيح تشغيل؛ والجدول في [`patches/README.md`](patches/README.md) يسرد كل واحد منها مع متغير البيئة الخاص به):

1. **يعمل المحسِّن (refiner) مرة واحدة في كل خطوة.** كان اسم مجموعة يُستخدم مرتين، فكانت أربع كتل من المحسِّن تُحسب مرة ثانية. بعد إصلاحه صارت الخطوات من 2 إلى 8 أسرع بنحو 1.3 s لكل واحدة (من 22.0 إلى 20.7 s) مع صورة مطابقة بكسلًا ببكسل (فُحصت 3 صور).
2. **VAE عبر cuDNN بدقة float32.** تستخدم المرحلة الأخيرة (تحويل الـ latent إلى بكسلات) الآن التفاف float32 من cuDNN التابع لـ NVIDIA. على بطاقتنا خفّض هذا زمن VAE من 23 إلى 27 s إلى 10 إلى 15 s، ورفع PSNR مقابل المرجع من 38 إلى 43 dB إلى 45 إلى 49 dB (مع بلاطات كبيرة).
3. **قطعة واحدة أولًا.** يحاول المحرّك الآن فك ترميز الصورة كلها قطعةً واحدة متى قال فحص الذاكرة إنها تتسع (هامش 256 MiB)، ثم يتراجع إلى بلاطتين كبيرتين، ثم إلى بلاطات صغيرة. في حالة القطعة الواحدة استغرق VAE نحو 8–16 s وبلغ PSNR مقابل المرجع من 71 إلى 73 dB. وإذا حدث تراجع قسري فللصورة البكسلات نفسها التي في النسخة ذات البلاطات (فُحص بـ `PIXEL_SHA256`). وما حدث يُكتب في `run.json` (`stages.vae_path`: `full` أو `tile` أو `floor` أو `retry`).

وأيضًا: `--eager-load` (يقرأ صفحات النموذج مقدمًا؛ من 241.2 s إلى 220.3 s للصورة نفسها، نسخة تطوير، تشغيلة واحدة لكل رقم) جزء من الأمر الثابت.

<a id="what-it-runs"></a>
## ما الذي يشغّله

| الجزء | الملف | المصدر |
|---|---|---|
| نموذج الانتشار | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF)، والأساس [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| مرمّز النص | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo)، مرمّز تلقائي من نوع FLUX.1 |
| المحرّك | `sd-cli.exe`، stable-diffusion.cpp `32d516c` مع التعديلات الموجودة في [`patches/`](patches) | إصدار v0.3.0 من هذا المستودع (`sinirsiz-foto-engine-v0.3.0-win-x64-cuda12.8-sm61.zip`) |
| بيئة CUDA | `cudart` و`cublas` و`cublasLt` (12.8)، دون تعديل | ملف zip من إصدار v0.1.0 لمشروع wan22-pascal-4gb |
| cuDNN (يُثبَّت افتراضيًا؛ `--no-cudnn` يتخطاه) | 8 ملفات DLL، الإصدار 9.10.2.21 (بناء CUDA 11) | خادم NVIDIA نفسها، بموجب ترخيص NVIDIA؛ لا يُحفظ هنا |

الإعدادات الثابتة: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`.
لا نخفّض الخطوات، ولا نضيف موجّهًا سلبيًا، ولا نفعّل التخزين المؤقت: فالنموذج مقطَّر لثماني خطوات ولا يستخدم موجّهات سلبية (انظر [الموجّهات](docs/PROMPTS.md)).

## الحدود (اقرأها قبل أن تعتمد عليه)

- **Windows فقط.** المحرّك الجاهز وهذه السكربتات تعمل على Windows فقط.
- **بطاقة واحدة وجهاز واحد.** القياس جرى على حاسوب محمول واحد ببطاقة GTX 1050 Ti بذاكرة 4 GB (i7-7700HQ، وRAM بسعة 16 GB، وWindows 10، والتعريف 581.29، والنماذج على SSD). وغير ذلك، أي بطاقات GPU وتعريفات أخرى، وأجهزة بذاكرة RAM أقل من 16 GB، وLinux وmacOS: **لم يُختبر**.
- البطاقات والأنظمة الأخرى (أي طريق متاح، واختبار من المجتمع على بطاقة AMD تحت Linux لم نُجرِه بأنفسنا): [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md).
- **المحرّك مبني لمعمارية Pascal (sm_61) فقط.** المعماريات الأخرى تحتاج إلى بناء من عندك ([`docs/BUILD.md`](docs/BUILD.md))؛ ولم نجرّب أيًّا منها.
- **cuDNN:** قسنا ببناء CUDA 11 من cuDNN 9.10.2.21. أما بناء CUDA 12 فملفاته مختلفة ولم يُقَس.
- **الذاكرة ضيقة.** تنخفض ذاكرة RAM الحرة إلى بضع مئات من MiB؛ أغلق البرامج الأخرى وولّد صورة واحدة في كل مرة. لم نرَ ذاكرة GPU تنفد بعد اجتياز فحص الذاكرة في المحرّك، ولم نختبر ما يحدث عندها.
- **الأحجام:** اختُبرت 768x1344 و1344x768 و1024x1024 فقط. الأحجام الأكبر تطبع تحذيرًا وقد تنفد معها الذاكرة.
- الالتزام بالموجّه جزئي: قد لا تتبع الصورة موجّهها في كل تفصيل. أما النص داخل الصور والمعالم الحقيقية فلم يجرِ تقييمهما.
- مرجع PSNR هو فك الترميز على CPU بمحرّكنا نحن، وليس تنفيذًا مستقلًّا.
- الأرقام في [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) من تشغيلة واحدة لكل رقم ما لم يُذكر خلاف ذلك.

## الترخيص والإسناد

- سكربتات هذا المستودع ووثائقه: [Apache-2.0](LICENSE) مع ملف [`NOTICE`](NOTICE). وتعديلات المحرّك في [`patches/`](patches) بترخيص MIT، مثل الشيفرة التي تعدّلها.
- stable-diffusion.cpp وggml بترخيص MIT. وإشعارات الشيفرة الخارجية المضمَّنة في المحرّك موجودة في [`licenses/`](licenses) وفي [`THIRD_PARTY.md`](THIRD_PARTY.md).
- ملفات النماذج لا تُحفظ هنا؛ تُنزَّل من المصادر أعلاه بتراخيصها الخاصة (تذكر Hugging Face الترخيص Apache-2.0 لها جميعًا، وقُرئ بتاريخ 2026-11-13). لا تقول بطاقة النموذج شيئًا عن مالك الصور المولّدة، ونحن لا ندّعي شيئًا في ذلك.
- **cuDNN وبيئة CUDA ملك لـ NVIDIA** وليستا تحت ترخيص هذا المستودع. يُنزَّل cuDNN من خادم NVIDIA بموجب ترخيص NVIDIA (`--no-cudnn` يتخطاه)؛ أما ملفات DLL الخاصة ببيئة CUDA فهي في ملف zip منفصل دون تعديل (CUDA Toolkit EULA، الملحق A). التفاصيل وما لم نستطع التحقق منه: [`THIRD_PARTY.md`](THIRD_PARTY.md).
- **الإسناد.** إبقاء ملف `NOTICE` مع النسخ والأعمال المشتقة هو الشرط (Apache-2.0، البند 4). وما عدا ذلك، فسطر مثل "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey" موضع تقدير، وليس مطلوبًا.
- نرجو أن تقرأ [`ETHICS.md`](ETHICS.md): كل صورة مصطنعة، وأنت المسؤول عمّا تنشره.

## المساهمة

أنفع ما يمكنك فعله هو **اختبار بطاقتك** وإخبارنا بما حدث: اسم البطاقة والتعريف وذاكرة RAM وملف `run.json` وآخر أسطر السجل (نموذج البلاغ "Hardware test report"). والتصحيحات في الوثائق وفي السكربتات مرحَّب بها أيضًا؛ انظر [`CONTRIBUTING.md`](CONTRIBUTING.md). وتُرسل البلاغات الأمنية عبر المسار الخاص المشروح في [`SECURITY.md`](SECURITY.md).

[دليل التثبيت لوكلاء الذكاء الاصطناعي](AGENTS.md) · [القياسات](docs/MEASUREMENTS.md) · [حل المشكلات](docs/TROUBLESHOOTING.md) · [بناء المحرّك](docs/BUILD.md) · [التعديلات](patches/README.md) · [الموجّهات](docs/PROMPTS.md) · [أطراف ثالثة](THIRD_PARTY.md) · [سجل التغييرات](CHANGELOG.md)

جرى توطين هذه الصفحة بالعربية بمساعدة الذكاء الاصطناعي، والتصحيحات مرحَّب بها جدًا (انظر [`CONTRIBUTING.md`](CONTRIBUTING.md)).
