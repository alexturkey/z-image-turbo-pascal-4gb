[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · **עברית** · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**יצירת תמונות מטקסט עם Z-Image-Turbo (Q8_0 GGUF) ברזולוציה 768x1344 על GTX 1050 Ti עם 4 GB (Pascal, sm_61), באמצעות stable-diffusion.cpp, על Windows.** נמדד על מחשב נייד עם 16 GB של RAM, שבו התהליך משתמש בכ-11 GB של זיכרון. אותו seed נותן את אותם פיקסלים, פיקסל אחר פיקסל. המדידות והטלאים (patches) למנוע פורסמו, ההורדות נעוצות עם sha256, וסוכן קוד מבוסס בינה מלאכותית יכול לבצע את ההתקנה צעד אחר צעד.

*לא רשמי. אין קשר ל-Tongyi-MAI (Z-Image), ל-leejet (stable-diffusion.cpp) או ל-NVIDIA.*

> **משתמשים בסוכן תכנות מבוסס בינה מלאכותית (Codex, Claude Code, Gemini, Cursor)?** תנו לו את המשפט האחד הזה: ״קרא את `AGENTS_HIZLI.md` עד הסוף, הרץ קודם את `python scripts/tani.py`, שמור את ההתקדמות שלך ב-`DURUM.md`, ושאל אותי לפני שאתה מוחק או מעביר משהו, משנה את Python של המערכת או את PATH, או מוריד הגדרת איכות.״ הסוכן יאבחן את המחשב הזה, יכתוב רשימת בדיקה וישאל אתכם בכל החלטה.

## מתחילים כאן

יש חבילה מוכנה, אז כדאי לנסות אותה קודם. אם החומרה שלכם שונה או שצעד נכשל, כל השאר פתוח: הטלאים, מתכון הבנייה והמדידות נמצאים במאגר הזה, וכך אפשר לבנות לכרטיס שלכם או להתאים אותם.

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

צעד 2 מוריד כ-12.2 GB ולקח 29 דקות בפעם אחת, בחיבור שלנו. הוא מדפיס קודם בלוק "Preflight" (כרטיס המסך, ה-RAM והדיסק הפנוי שלכם לצד מה שמדדנו; הוא רק מידע).
נמדד רק כרטיס אחד: GTX 1050 Ti עם 4 GB במחשב נייד (Pascal, יכולת חישוב 6.1). כרטיסים אחרים לא נבדקו.
אם אתם משתמשים בסוכן קוד מבוסס בינה מלאכותית (Claude Code, Codex, Cursor ודומיהם), הפנו אותו אל [`AGENTS.md`](AGENTS.md).

## במבט אחד

לעומת המבנה של v0.1.0: תמונה אחת לוקחת 188–193 s במקום 261.6 s, שלב ה-VAE לוקח 12.5–21.7 s במקום 29.8 עד 36.3 s, אותו seed נותן את אותם פיקסלים, ומאחורי כל מספר ב-README הזה יש פקודה וקובץ.

768x1344, seed 42, 8 צעדים, אותו מחשב. המספרים של v0.1.0 לקוחים מה-README של v0.1.0 (בדיקת שורש נקי וחמש הרצות); המספרים של v0.3.0 מבדיקת השורש הנקי של הגרסה הזאת.

| | v0.1.0 (לא פורסמה; מבנה ישן) | v0.3.0 |
|---|---|---|
| זמן לתמונה אחת (הרצה אחת של `generate.py`) | 261.6 s | 188–193 s |
| פענוח VAE (השלב האחרון) | 29.8 עד 36.3 s | 12.5–21.7 s |
| קרבה לפענוח ייחוס (PSNR, גבוה יותר קרוב יותר) | 38 עד 43 dB | 71 עד 73 dB |
| שיא זיכרון GPU (nvidia-smi) | 2949 עד 2957 MiB | 3057–3059 MiB |
| זיכרון התהליך, שיא | 10.5 עד 10.9 GB (כפי שנרשם אז) | 10 489–11 203 MiB |
| הזיכרון הפנוי הנמוך ביותר שנראה | 331 עד 576 MiB | 303–532 MiB |

איך לקרוא: הייחוס הוא אותו latent שפוענח על ה-CPU כחתיכה אחת ב-float32; PSNR משווה את הפענוח שלנו על ה-GPU אליו (3 תמונות). הוא אומר עד כמה שלב ה-VAE קרוב לייחוס הזה. הוא לא אומר עד כמה התמונה יפה. התמונות של v0.2.0 אינן זהות בבייטים לאלה של v0.1.0 עבור אותו פרומפט ואותו seed, כי מסלול ה-VAE שונה בכוונה. השיטה והחלקים שלא נמדדו: [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md).

## דוגמאות

**נוצרו בבינה מלאכותית עם המאגר הזה** (Z-Image-Turbo Q8_0, seed 42, 8 צעדים). אלה לא צילומים אמיתיים; ייתכן שאתרי ציון ופרטים
אינם מדויקים, ותמונה לא תמיד עוקבת אחרי הפרומפט שלה בכל פרט. הפרומפטים המלאים ב-[`prompts/`](prompts) וב-[`docs/PROMPTS.md`](docs/PROMPTS.md).

| | | |
|---|---|---|
| ![מגדל אייפל בשעת הזהב](docs/examples/eiffel.jpg) | ![כוס תה טורקית](docs/examples/turkish_tea.jpg) | ![דייג מבוגר](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![כפר על מדרון](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![איסטנבול מהאוויר](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. לא צילום אמיתי; ייתכן שאתרי ציון אינם מדויקים.

## התחלה מהירה

דרישות: Windows 10/11, כרטיס NVIDIA עם 4 GB, דרייבר שתומך ב-CUDA 12.8 (נמדד עם דרייבר 581.29; דרייברים ישנים יותר לא נבדקו; סביבת הריצה של CUDA עצמה מורדת בשבילכם), Python 3.10 ומעלה,
git, כ-14 GB של דיסק פנוי (ההורדות הן כ-12.2 GB עם cuDNN; הנתון על הדיסק הפנוי הוא הערכה), ו-16 GB של RAM (זה מה שנמדד; פחות מזה לא נבדק).

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- `setup.py` מדפיס קודם בלוק "Preflight" (כרטיס המסך, ה-RAM והדיסק הפנוי שלכם לצד מה שמדדנו; הוא רק מידע ואף פעם לא חוסם). אחר כך הוא מוריד מהכתובות הנעוצות ב-[`models.lock.json`](models.lock.json) ובודק כל קובץ עם sha256. הוא מדפיס `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK`, אחר כך `CUDNN_OK` או `CUDNN_SKIPPED`, ולבסוף `SETUP_OK`.
  בלי `--models-dir` ו-`--bin-dir` הוא משתמש ב-`models/` וב-`bin/` בשורש המאגר; כדאי לשים את המודלים על SSD (רק SSD נמדד).
  אפשר לעצור אותו בכל רגע עם Ctrl+C ולהריץ שוב את אותה פקודה: ההורדות ממשיכות מקבצי `.part`.
- **cuDNN מותקן כברירת מחדל ואינו חלק מהמאגר הזה.** זו תוכנה של NVIDIA, ברישיון של NVIDIA עצמה ([נוסח הרישיון](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)), למחשבים עם כרטיסי NVIDIA. הוא מורד מהשרת של NVIDIA בלי שמבקשים תשלום ובלי חשבון או התחברות, ולא מצאנו ברישיון שום סעיף שמגביל שימוש מסחרי או אישי. `setup.py` מציג את כתובת הרישיון, מוריד את הקובץ ומעתיק רק שמונה קובצי DLL לצד `sd-cli.exe`. הרישיון של NVIDIA אומר שמי שאינו מקבל את תנאיו אסור לו להוריד אותו, להתקין אותו או להשתמש בו; במקרה כזה הריצו `python scripts/setup.py --no-cudnn`. בלי cuDNN הכול עובד עם מסלול ה-VAE האיטי יותר של v0.1.0 (`--vae legacy`), ו-`generate.py` אומר זאת.
- `generate.py` כותב את `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, את `run.json` (זמן, שלבים, איזה מסלול VAE רץ, שיא זיכרון GPU, הפקודה המלאה) ואת `log.txt`, ומדפיס `IMAGE_OK <path>`.

## שימוש

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| אפשרות | משמעות |
|---|---|
| `--prompt "<text>"` או `--prompt-file <txt>` | הפרומפט (אחד משני אלה חובה) |
| `--width`, `--height` | כפולות של 16, בין 256 ל-2048; ברירת מחדל 768x1344; נבדקו: 768x1344, 1344x768, 1024x1024 |
| `--seed` | ברירת מחדל 42 |
| `--out`, `--name` | שורש תיקיית הפלט (ברירת מחדל `outputs/`) ושם קצר לתיקיית ההרצה |
| `--models-dir`, `--bin-dir` | המקומות ש-`setup.py` שם בהם את המודלים ואת המנוע |
| `--vae auto` (ברירת מחדל) | cuDNN ב-float32; קודם חתיכה אחת, אחר כך שני אריחים (tiles) גדולים, ואז האריח הקטן של ברירת המחדל |
| `--vae tiled` | cuDNN ב-float32, תמיד שני אריחים גדולים |
| `--vae legacy` | המסלול של v0.1.0: בלי cuDNN, אריחים קטנים. נבחר אוטומטית (עם אזהרה) כשקובצי ה-DLL של cuDNN חסרים |

הצעדים (8), cfg (1.0), ה-sampler וה-scheduler קבועים בכוונה; ראו [מה זה מריץ](#what-it-runs).

## בדקו בעצמכם

- `generate.py` מדפיס `PIXEL_SHA256 <hex>` באחת משורותיו האחרונות: גיבוב של הפיקסלים המפוענחים. הריצו את אותה פקודה פעמיים והשוו את שתי התמונות: `python scripts/compare.py <run A>/image.png <run B>/image.png` אמור להדפיס `SAME_PIXELS`.
- ה-`PIXEL_SHA256` של חמש הדוגמאות במחשב שלנו נמצא ב-[`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md). הגיבוב של קובץ PNG יכול להיות שונה גם כשהפיקסלים זהים, כי ה-PNG נושא את פרמטרי היצירה כטקסט; משווים פיקסלים, לא קבצים.
- הגבלה כנה: לא מדדנו אם כרטיס או דרייבר אחר נותנים את אותם פיקסלים.

## למה זה נכנס ב-4 GB

- **מה כותבי המודל אומרים.** כרטיס המודל של Z-Image-Turbo אומר שהמודל "fits comfortably within 16G VRAM consumer devices" (נכנס בנוחות במכשירי צרכן עם 16 GB של VRAM) ([כרטיס המודל](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)). זו אמירה על כרטיסים של 16 GB. ה-README הרשמי גם מציין את stable-diffusion.cpp כאפשרות של צד שלישי ומצטט אותו עם "as little as 4GB of VRAM" (עד 4 GB בלבד של VRAM) ([README](https://github.com/Tongyi-MAI/Z-Image)); זו טענה של הפרויקט stable-diffusion.cpp, לא דרישה של צוות Z-Image.
- **מה מדדנו.** Z-Image-Turbo Q8_0 (קובץ של 6.6 GB) עם מקודד הטקסט Qwen3-4B Q8_0, ברזולוציה 768x1344: שיא ה-GPU, שנדגם על ידי nvidia-smi כל 2 s (קפיצה קצרה עלולה לחמוק), היה 2949 עד 2957 MiB (מנוע v0.1.0) ו-3057–3059 MiB (מנוע v0.2.0) על כרטיס של 4096 MiB. המשקלים (10 509 MiB; יומן המנוע מדפיס זאת כ-MB) נשארים ב-RAM של המערכת; המנוע מעתיק את הרשת ל-GPU קטע אחד בכל פעם (קטע הוא פרוסה של הרשת): 36 קטעים, כמו בשורת היומן `z_image using 36 segments`.
- **מה המחיר.** זמן וזיכרון מערכת: 188–193 s לתמונה, ותהליך המנוע מחזיק כ-10 489–11 203 MiB של RAM (כולל דפי מודל ממופים לזיכרון) על מחשב של 16 GB, ולכן הזיכרון הפנוי יורד לכמה מאות MiB בזמן הריצה.
- **ההתקנות של אחרים.** אחרים מדווחים על Z-Image בכרטיסים של 4 GB עם קוונטיזציה נמוכה יותר או בגדלים קטנים יותר (למשל דף ה-wiki של stable-diffusion.cpp לכרטיסי 4 GB ממליץ על Q3_K או Q4_0 ב-1024x512). במקומות שבהם חיפשנו (הרשימה והתאריך ב-[`docs/RELATED.md`](docs/RELATED.md)) לא מצאנו התקנה מפורסמת שמשלבת את כל הארבעה: כרטיס של 4 GB, Q8_0, 768x1344 או גדול יותר, וזמן וזיכרון GPU שנמדדו. זו אמירה על המקומות שבהם חיפשנו, לא על כל מקום.
- **מי עושה מה.** ההתאמה ל-4 GB מגיעה מ-stable-diffusion.cpp עצמו: `--offload-to-cpu`, `--mmap`, עבודה בפרוסות, ו-flash attention (כשהוא כבוי, הרצה דרשה 4205 MB ולא נכנסה). הטלאים שלנו הם למהירות ולשלב VAE טוב יותר, לא בשביל להיכנס. לא הרצנו את המנוע המקורי בלי טלאים על הכרטיס הזה, ולכן איננו יכולים לומר אם הוא נכנס.

## איך זה עובד

שלושה שינויים מעל stable-diffusion.cpp `master-1088-32d516c` (כולם מתגים; הטבלה ב-[`patches/README.md`](patches/README.md) מפרטת כל אחד עם משתנה הסביבה שלו):

1. **ה-refiner רץ פעם אחת בכל צעד.** שם של קבוצה שימש פעמיים, ולכן ארבעה בלוקים של ה-refiner חושבו פעם שנייה. אחרי התיקון הצעדים 2 עד 8 מהירים בכ-1.3 s כל אחד (מ-22.0 ל-20.7 s) עם תמונה זהה פיקסל אחר פיקסל (נבדקו 3 תמונות).
2. **VAE דרך cuDNN, ב-float32.** השלב האחרון (הפיכת ה-latent לפיקסלים) משתמש עכשיו בקונבולוציית float32 של cuDNN מבית NVIDIA. בכרטיס שלנו זה הוריד את ה-VAE מ-23 עד 27 s ל-10 עד 15 s והעלה את ה-PSNR מול הייחוס מ-38 עד 43 dB ל-45 עד 49 dB (עם אריחים גדולים).
3. **קודם חתיכה אחת.** המנוע מנסה עכשיו לפענח את התמונה כולה כחתיכה אחת כשבדיקת הזיכרון אומרת שזה נכנס (שולי ביטחון של 256 MiB), נסוג לשני אריחים גדולים, ואחר כך לאריחים קטנים. בחתיכה אחת ה-VAE לקח כ-8–16 s וה-PSNR מול הייחוס היה 71 עד 73 dB. אם קרתה נסיגה כפויה, לתמונה אותם פיקסלים כמו בגרסה עם האריחים (נבדק עם `PIXEL_SHA256`). מה שקרה נכתב ב-`run.json` (`stages.vae_path`: `full`, `tile`, `floor` או `retry`).

בנוסף: `--eager-load` (קורא את דפי המודל מראש; מ-241.2 s ל-220.3 s על אותה תמונה, גרסת פיתוח, הרצה אחת כל אחד) הוא חלק מהפקודה הקבועה.

<a id="what-it-runs"></a>
## מה זה מריץ

| רכיב | קובץ | מקור |
|---|---|---|
| מודל דיפוזיה | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), הבסיס [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| מקודד טקסט | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), מקודד אוטומטי מסוג FLUX.1 |
| מנוע | `sd-cli.exe`, stable-diffusion.cpp `32d516c` עם הטלאים שב-[`patches/`](patches) | גרסה v0.3.0 של המאגר הזה (`sinirsiz-foto-engine-v0.3.0-win-x64-cuda12.8-sm61.zip`) |
| סביבת ריצה של CUDA | `cudart`, `cublas`, `cublasLt` (12.8), ללא שינוי | zip מגרסה v0.1.0 של wan22-pascal-4gb |
| cuDNN (מותקן כברירת מחדל; `--no-cudnn` מדלג עליו) | 8 קובצי DLL, גרסה 9.10.2.21 (גרסת CUDA 11) | השרת של NVIDIA עצמה, לפי הרישיון של NVIDIA; לא נשמר כאן |

הגדרות קבועות: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`.
אנחנו לא מורידים את מספר הצעדים, לא מוסיפים פרומפט שלילי ולא מפעילים מטמון: המודל מזוקק ל-8 צעדים ואינו משתמש בפרומפטים שליליים (ראו [פרומפטים](docs/PROMPTS.md)).

## מגבלות (קראו לפני שסומכים על זה)

- **Windows בלבד.** המנוע המוכן והסקריפטים האלה הם ל-Windows בלבד.
- **כרטיס אחד, מחשב אחד.** נמדד רק על מחשב נייד עם GTX 1050 Ti 4 GB (i7-7700HQ, 16 GB של RAM, Windows 10, דרייבר 581.29, המודלים על SSD). כרטיסי GPU ודרייברים אחרים, מחשבים עם פחות מ-16 GB של RAM, Linux ו-macOS: **לא נבדקו**.
- כרטיסים ומערכות אחרים (איזו דרך קיימת, ובדיקה של הקהילה על כרטיס AMD תחת Linux שלא הרצנו בעצמנו): [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md).
- **המנוע בנוי רק ל-Pascal (sm_61).** ארכיטקטורות אחרות דורשות בנייה עצמית ([`docs/BUILD.md`](docs/BUILD.md)); לא בדקנו אף אחת.
- **cuDNN:** מדדנו עם גרסת CUDA 11 של cuDNN 9.10.2.21. לגרסת CUDA 12 יש קבצים אחרים והיא לא נמדדה.
- **הזיכרון צפוף.** הזיכרון הפנוי יורד לכמה מאות MiB; סגרו תוכנות אחרות והריצו תמונה אחת בכל פעם. לא ראינו זיכרון GPU שנגמר אחרי שבדיקת הזיכרון של המנוע עברה, ולא בדקנו מה קורה אז.
- **גדלים:** נבדקו רק 768x1344, 1344x768 ו-1024x1024. גדלים גדולים יותר מדפיסים אזהרה ועלולים לגמור את הזיכרון.
- ההתאמה לפרומפט חלקית: תמונה לא תמיד עוקבת אחרי הפרומפט שלה בכל פרט. טקסט בתוך תמונות ואתרי ציון אמיתיים מהעולם לא הוערכו.
- ייחוס ה-PSNR הוא פענוח ה-CPU של המנוע שלנו עצמו, לא מימוש עצמאי.
- המספרים ב-[`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) הם מהרצה אחת כל אחד, אלא אם כתוב אחרת.

## רישיון וייחוס

- הסקריפטים והמסמכים של המאגר הזה: [Apache-2.0](LICENSE), עם קובץ [`NOTICE`](NOTICE). הטלאים למנוע שב-[`patches/`](patches) הם MIT, כמו הקוד שהם משנים.
- stable-diffusion.cpp ו-ggml הם MIT. הודעות על קוד של צד שלישי שמהודר לתוך המנוע נמצאות ב-[`licenses/`](licenses) וב-[`THIRD_PARTY.md`](THIRD_PARTY.md).
- קובצי המודלים אינם נשמרים כאן; הם מורדים מהמקורות שלמעלה ברישיונות שלהם (Hugging Face מציגה Apache-2.0 לכולם, נקרא ב-2026-11-13). כרטיס המודל לא אומר דבר על הבעלות בתמונות שנוצרו, ואנחנו לא טוענים דבר בעניין.
- **cuDNN וסביבת הריצה של CUDA הם רכוש של NVIDIA** ואינם תחת הרישיון של המאגר הזה. cuDNN מורד מהשרת של NVIDIA לפי הרישיון של NVIDIA (`--no-cudnn` מדלג עליו); קובצי ה-DLL של סביבת הריצה של CUDA נמצאים ב-zip נפרד וללא שינוי (CUDA Toolkit EULA, נספח A). פרטים ומה שלא הצלחנו לאמת: [`THIRD_PARTY.md`](THIRD_PARTY.md).
- **ייחוס.** שמירת קובץ `NOTICE` עם העתקים ועבודות נגזרות היא התנאי (Apache-2.0, סעיף 4). מעבר לכך, שורה כמו "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey" תתקבל בברכה, אך אינה חובה.
- נא לקרוא את [`ETHICS.md`](ETHICS.md): כל תמונה היא סינתטית, ואתם אחראים למה שאתם מפרסמים.

## תרומה

הדבר השימושי ביותר שאפשר לעשות הוא **לבדוק את הכרטיס שלכם** ולספר לנו מה קרה: שם ה-GPU, הדרייבר, ה-RAM, הקובץ `run.json` והשורות האחרונות של היומן (טופס הדיווח "Hardware test report"). תיקונים במסמכים ובסקריפטים מתקבלים בברכה גם הם; ראו [`CONTRIBUTING.md`](CONTRIBUTING.md). דיווחי אבטחה עוברים בערוץ הפרטי שמתואר ב-[`SECURITY.md`](SECURITY.md).

[מדריך התקנה לסוכני בינה מלאכותית](AGENTS.md) · [מדידות](docs/MEASUREMENTS.md) · [פתרון תקלות](docs/TROUBLESHOOTING.md) · [בניית המנוע](docs/BUILD.md) · [טלאים](patches/README.md) · [פרומפטים](docs/PROMPTS.md) · [צד שלישי](THIRD_PARTY.md) · [יומן שינויים](CHANGELOG.md)

העמוד הזה הותאם לעברית בעזרת בינה מלאכותית, ותיקונים יתקבלו בברכה רבה (ראו [`CONTRIBUTING.md`](CONTRIBUTING.md)).
