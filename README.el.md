[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · **Ελληνικά** · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**Z-Image-Turbo (Q8_0 GGUF) text-to-image (παραγωγή εικόνας από κείμενο) στα 768x1344 σε κάρτα GTX 1050 Ti 4 GB (Pascal, sm_61), με stable-diffusion.cpp, σε Windows.** Μετρήθηκε σε laptop με 16 GB RAM, όπου η διεργασία χρησιμοποιεί περίπου 11 GB RAM. Το ίδιο seed δίνει τα ίδια pixel, pixel προς pixel· οι μετρήσεις και τα patches της μηχανής είναι δημοσιευμένα, οι λήψεις είναι καρφιτσωμένες με sha256 και ένας AI βοηθός προγραμματισμού μπορεί να κάνει την εγκατάσταση βήμα βήμα.

*Ανεπίσημο. Δεν συνδέεται με την Tongyi-MAI (Z-Image), τον leejet (stable-diffusion.cpp) ή την NVIDIA.*

> **Χρησιμοποιείτε πράκτορα προγραμματισμού με τεχνητή νοημοσύνη (Codex, Claude Code, Gemini, Cursor);** Δώστε του αυτή τη μία πρόταση: «Διάβασε το `AGENTS_HIZLI.md` ως το τέλος, τρέξε πρώτα το `python scripts/tani.py`, κράτα την πρόοδό σου στο `DURUM.md` και ρώτα με πριν διαγράψεις ή μετακινήσεις οτιδήποτε, αλλάξεις το Python του συστήματος ή το PATH ή μειώσεις μια ρύθμιση ποιότητας.» Ο πράκτορας θα διαγνώσει αυτόν τον υπολογιστή, θα γράψει μια λίστα ελέγχου και θα σας ρωτά σε κάθε απόφαση.

## Ξεκίνα εδώ

Υπάρχει έτοιμο πακέτο, γι' αυτό δοκίμασέ το πρώτα. Αν το hardware σου είναι διαφορετικό ή κάποιο βήμα αποτύχει, όλα τα υπόλοιπα είναι ανοιχτά: τα patches, η συνταγή του build και οι μετρήσεις βρίσκονται σε αυτό το αποθετήριο, ώστε να κάνεις build για τη δική σου κάρτα ή να τα προσαρμόσεις.

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

Το βήμα 2 κατεβάζει περίπου 12.2 GB και κράτησε 29 λεπτά μία φορά, στη δική μας σύνδεση· πρώτα τυπώνει ένα μπλοκ «Preflight» (η GPU, η RAM και ο ελεύθερος δίσκος σου δίπλα σε όσα μετρήσαμε· απλώς ενημερώνει).
Μετρήθηκε μόνο η κάρτα laptop GTX 1050 Ti 4 GB (Pascal, compute capability 6.1). Άλλες κάρτες δεν δοκιμάστηκαν.
Αν χρησιμοποιείς AI βοηθό προγραμματισμού (Claude Code, Codex, Cursor και παρόμοιους), δώσ' του το [`AGENTS.md`](AGENTS.md).

## Με μια ματιά

Σε σύγκριση με τη διάταξη του v0.1.0: μια εικόνα παίρνει 188–193 s αντί για 261.6 s, το στάδιο VAE παίρνει 12.5–21.7 s αντί για 29.8 έως 36.3 s, το ίδιο seed δίνει τα ίδια pixel, και πίσω από κάθε αριθμό αυτού του README υπάρχει μια εντολή και ένα αρχείο.

768x1344, seed 42, 8 βήματα, ίδιο μηχάνημα. Οι αριθμοί του v0.1.0 προέρχονται από το README του v0.1.0 (δοκιμή σε καθαρή ρίζα και πέντε εκτελέσεις)· οι αριθμοί του v0.3.0 προέρχονται από τη δοκιμή σε καθαρή ρίζα αυτής της έκδοσης.

| | v0.1.0 (δεν δημοσιεύτηκε ποτέ· παλιά διάταξη) | v0.3.0 |
|---|---|---|
| Χρόνος για μία εικόνα (μία εκτέλεση του `generate.py`) | 261.6 s | 188–193 s |
| Αποκωδικοποίηση VAE (τελευταίο στάδιο) | 29.8 έως 36.3 s | 12.5–21.7 s |
| Εγγύτητα σε μια αποκωδικοποίηση αναφοράς (PSNR, όσο υψηλότερο τόσο καλύτερα) | 38 έως 43 dB | 71 έως 73 dB |
| Μέγιστη μνήμη GPU (nvidia-smi) | 2949 έως 2957 MiB | 3057–3059 MiB |
| Μνήμη διεργασίας, μέγιστη | 10.5 έως 10.9 GB (όπως καταγράφηκε τότε) | 10 489–11 203 MiB |
| Χαμηλότερη ελεύθερη RAM που παρατηρήθηκε | 331 έως 576 MiB | 303–532 MiB |

Πώς διαβάζεται: η αναφορά είναι το ίδιο latent αποκωδικοποιημένο στη CPU ως ένα κομμάτι float32· το PSNR συγκρίνει την αποκωδικοποίηση της GPU μας με αυτήν (3 εικόνες). Δείχνει πόσο κοντά είναι το στάδιο VAE σε αυτή την αναφορά. Δεν δείχνει πόσο καλή φαίνεται μια εικόνα. Οι εικόνες του v0.2.0 δεν είναι byte προς byte ίδιες με του v0.1.0 για το ίδιο prompt και seed, επειδή η διαδρομή του VAE άλλαξε επίτηδες. Μέθοδος και ό,τι δεν μετρήθηκε: [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md).

## Παραδείγματα

**Παραγμένες με AI από αυτό το αποθετήριο** (Z-Image-Turbo Q8_0, seed 42, 8 βήματα). Δεν είναι πραγματικές φωτογραφίες· τα αξιοθέατα και οι λεπτομέρειες
μπορεί να μην είναι ακριβή, και μια εικόνα δεν ακολουθεί πάντα το prompt της σε κάθε λεπτομέρεια. Τα ακριβή prompts βρίσκονται στο [`prompts/`](prompts) και στο [`docs/PROMPTS.md`](docs/PROMPTS.md).

| | | |
|---|---|---|
| ![Πύργος του Άιφελ τη χρυσή ώρα](docs/examples/eiffel.jpg) | ![Ποτήρι τουρκικού τσαγιού](docs/examples/turkish_tea.jpg) | ![Ηλικιωμένος ψαράς](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![Χωριό σε πλαγιά λόφου](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![Η Ιστανμπούλ από ψηλά](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. Δεν είναι πραγματική φωτογραφία· τα αξιοθέατα μπορεί να μην είναι ακριβή.

## Γρήγορη εκκίνηση

Απαιτήσεις: Windows 10/11, κάρτα γραφικών NVIDIA με 4 GB, driver που υποστηρίζει CUDA 12.8 (μετρήθηκε ο driver 581.29· παλαιότεροι driver δεν δοκιμάστηκαν· το ίδιο το CUDA runtime κατεβαίνει για εσένα), Python 3.10 ή νεότερη,
git, περίπου 14 GB ελεύθερος δίσκος (οι λήψεις είναι περίπου 12.2 GB με το cuDNN· το νούμερο του ελεύθερου δίσκου είναι εκτίμηση) και 16 GB RAM (όσα μετρήθηκαν· λιγότερα δεν δοκιμάστηκαν).

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- Το `setup.py` τυπώνει πρώτα ένα μπλοκ «Preflight» (η GPU, η RAM και ο ελεύθερος δίσκος σου δίπλα σε όσα μετρήσαμε· απλώς ενημερώνει και ποτέ δεν μπλοκάρει). Ύστερα κατεβάζει από τις καρφιτσωμένες διευθύνσεις στο [`models.lock.json`](models.lock.json) και ελέγχει κάθε αρχείο με sha256. Τυπώνει `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK`, μετά `CUDNN_OK` ή `CUDNN_SKIPPED` και τέλος `SETUP_OK`.
  Χωρίς `--models-dir` και `--bin-dir` χρησιμοποιεί τους φακέλους `models/` και `bin/` στη ρίζα του αποθετηρίου· βάλε τα μοντέλα σε SSD (μετρήθηκε μόνο SSD).
  Μπορείς να το σταματήσεις οποιαδήποτε στιγμή με Ctrl+C και να ξανατρέξεις την ίδια εντολή: οι λήψεις συνεχίζονται από τα αρχεία `.part`.
- **Το cuDNN εγκαθίσταται από προεπιλογή και δεν ανήκει σε αυτό το αποθετήριο.** Είναι λογισμικό της NVIDIA με τη δική της άδεια χρήσης ([κείμενο της άδειας](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)), για συστήματα με κάρτες γραφικών NVIDIA. Κατεβαίνει από τον server της NVIDIA χωρίς να ζητηθεί πληρωμή και χωρίς σύνδεση σε λογαριασμό, και δεν βρήκαμε στην άδεια όρο που να περιορίζει την εμπορική ή την προσωπική χρήση. Το `setup.py` δείχνει τη διεύθυνση της άδειας, κατεβάζει το αρχείο και αντιγράφει μόνο οκτώ DLL δίπλα στο `sd-cli.exe`. Η άδεια της NVIDIA λέει ότι όποιος δεν αποδέχεται τους όρους της δεν πρέπει να το κατεβάσει, να το εγκαταστήσει ή να το χρησιμοποιήσει· σε αυτή την περίπτωση τρέξε `python scripts/setup.py --no-cudnn`. Χωρίς το cuDNN όλα δουλεύουν με την πιο αργή διαδρομή VAE του v0.1.0 (`--vae legacy`), και το `generate.py` το αναφέρει.
- Το `generate.py` γράφει `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, `run.json` (χρόνος, στάδια, ποια διαδρομή VAE έτρεξε, μέγιστη μνήμη GPU, η ακριβής εντολή) και `log.txt`, και τυπώνει `IMAGE_OK <path>`.

## Χρήση

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| Επιλογή | Σημασία |
|---|---|
| `--prompt "<text>"` ή `--prompt-file <txt>` | το prompt (απαιτείται ένα από τα δύο) |
| `--width`, `--height` | πολλαπλάσια του 16, από 256 έως 2048· προεπιλογή 768x1344· δοκιμασμένα: 768x1344, 1344x768, 1024x1024 |
| `--seed` | προεπιλογή 42 |
| `--out`, `--name` | ρίζα του φακέλου εξόδου (προεπιλογή `outputs/`) και ένα σύντομο όνομα για τον φάκελο της εκτέλεσης |
| `--models-dir`, `--bin-dir` | πού έβαλε το `setup.py` τα μοντέλα και τη μηχανή |
| `--vae auto` (προεπιλογή) | cuDNN float32· δοκιμάζει πρώτα ένα κομμάτι, μετά δύο μεγάλα tiles, μετά το μικρό προεπιλεγμένο tile |
| `--vae tiled` | cuDNN float32, πάντα δύο μεγάλα tiles |
| `--vae legacy` | η διαδρομή του v0.1.0: χωρίς cuDNN, μικρά tiles. Χρησιμοποιείται αυτόματα (με προειδοποίηση) όταν λείπουν τα DLL του cuDNN |

Τα βήματα (8), το cfg (1.0), ο sampler και ο scheduler είναι σταθερά επίτηδες· δες το [Τι τρέχει](#what-it-runs).

## Επαλήθευση

- Το `generate.py` τυπώνει `PIXEL_SHA256 <hex>` σε μία από τις τελευταίες γραμμές του: ένα hash των αποκωδικοποιημένων pixel. Τρέξε την ίδια εντολή δύο φορές και σύγκρινε τις δύο εικόνες: το `python scripts/compare.py <run A>/image.png <run B>/image.png` πρέπει να τυπώσει `SAME_PIXELS`.
- Το `PIXEL_SHA256` των πέντε παραδειγμάτων στο μηχάνημά μας βρίσκεται στο [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md). Το hash του αρχείου ενός PNG μπορεί να διαφέρει ακόμη κι όταν τα pixel είναι ίδια, επειδή το PNG κρατά τις παραμέτρους παραγωγής ως κείμενο· σύγκρινε pixel, όχι αρχεία.
- Ειλικρινές όριο: δεν μετρήσαμε αν μια άλλη κάρτα ή ένας άλλος driver δίνει τα ίδια pixel.

## Γιατί χωράει σε 4 GB

- **Τι λένε οι δημιουργοί του μοντέλου.** Η κάρτα μοντέλου (model card) του Z-Image-Turbo λέει ότι το μοντέλο "fits comfortably within 16G VRAM consumer devices" ([model card](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)), δηλαδή «χωράει άνετα σε καταναλωτικές συσκευές με 16 GB VRAM». Αυτό είναι δήλωση για κάρτες 16 GB. Το επίσημο README αναφέρει επίσης το stable-diffusion.cpp ως επιλογή τρίτου και το παραθέτει για "as little as 4GB of VRAM" ([README](https://github.com/Tongyi-MAI/Z-Image)), δηλαδή «μόλις 4 GB VRAM»· αυτό είναι ισχυρισμός του έργου stable-diffusion.cpp, όχι απαίτηση της ομάδας του Z-Image.
- **Τι μετρήσαμε.** Z-Image-Turbo Q8_0 (αρχείο 6.6 GB) με text encoder Qwen3-4B Q8_0, στα 768x1344: η κορυφή της GPU, με δειγματοληψία από το nvidia-smi κάθε 2 s (μια σύντομη αιχμή μπορεί να χαθεί), ήταν 2949 έως 2957 MiB (μηχανή v0.1.0) και 3057–3059 MiB (μηχανή v0.2.0) σε κάρτα των 4096 MiB. Τα βάρη (10 509 MiB· το log της μηχανής τα τυπώνει ως MB) μένουν στη RAM του συστήματος· η μηχανή αντιγράφει το δίκτυο στη GPU ένα τμήμα (segment, μια φέτα του δικτύου) τη φορά: 36 τμήματα, όπως στη γραμμή του log `z_image using 36 segments`.
- **Τι κοστίζει.** Χρόνο και μνήμη συστήματος: 188–193 s ανά εικόνα, και η διεργασία της μηχανής κρατά περίπου 10 489–11 203 MiB RAM (μαζί με τις σελίδες μοντέλου που έχουν γίνει memory-map) σε μηχάνημα 16 GB, οπότε η ελεύθερη RAM πέφτει σε λίγες εκατοντάδες MiB όσο τρέχει.
- **Οι ρυθμίσεις άλλων.** Άλλοι αναφέρουν Z-Image σε κάρτες 4 GB με χαμηλότερο κβαντισμό ή μικρότερα μεγέθη (για παράδειγμα η σελίδα wiki του stable-diffusion.cpp για κάρτες 4 GB προτείνει Q3_K ή Q4_0 στα 1024x512). Όπου ψάξαμε (λίστα και ημερομηνία στο [`docs/RELATED.md`](docs/RELATED.md)) δεν βρήκαμε δημοσιευμένη ρύθμιση που να συνδυάζει και τα τέσσερα: κάρτα 4 GB, Q8_0, 768x1344 ή μεγαλύτερο, και μετρημένο χρόνο και μνήμη GPU. Αυτό είναι δήλωση για το πού ψάξαμε, όχι για παντού.
- **Ποιος κάνει τι.** Το να χωρέσει σε 4 GB οφείλεται στο ίδιο το stable-diffusion.cpp: `--offload-to-cpu`, `--mmap`, η δουλειά σε φέτες και το flash attention (με αυτό κλειστό, μια εκτέλεση χρειάστηκε 4205 MB και δεν χωρούσε). Τα patches μας είναι για ταχύτητα και για καλύτερο στάδιο VAE, όχι για να χωρέσει. Δεν τρέξαμε τη μηχανή upstream χωρίς patches σε αυτή την κάρτα, άρα δεν μπορούμε να πούμε αν χωράει.

## Πώς λειτουργεί

Τρεις αλλαγές πάνω στο stable-diffusion.cpp `master-1088-32d516c` (όλες είναι διακόπτες· ο πίνακας στο [`patches/README.md`](patches/README.md) τις αναφέρει μία μία με τη μεταβλητή περιβάλλοντος της καθεμιάς):

1. **Ο refiner τρέχει μία φορά ανά βήμα.** Ένα όνομα ομάδας χρησιμοποιήθηκε δύο φορές, οπότε τέσσερα μπλοκ του refiner υπολογίζονταν για δεύτερη φορά. Η διόρθωση κάνει τα βήματα 2 έως 8 περίπου 1.3 s ταχύτερα το καθένα (22.0 έως 20.7 s) με εικόνα πανομοιότυπη ως προς τα pixel (ελέγχθηκαν 3 εικόνες).
2. **VAE μέσω cuDNN, σε float32.** Το τελευταίο στάδιο (η μετατροπή του latent σε pixel) χρησιμοποιεί πλέον τη συνέλιξη float32 του cuDNN της NVIDIA. Στην κάρτα μας έφερε το VAE από 23 έως 27 s σε 10 έως 15 s και ανέβασε το PSNR ως προς την αναφορά από 38 έως 43 dB σε 45 έως 49 dB (μεγάλα tiles).
3. **Πρώτα ένα κομμάτι.** Η μηχανή δοκιμάζει πλέον να αποκωδικοποιήσει ολόκληρη την εικόνα ως ένα κομμάτι όταν ο έλεγχος μνήμης λέει ότι χωράει (περιθώριο 256 MiB), πέφτει σε δύο μεγάλα tiles και ύστερα σε μικρά tiles. Ως ένα κομμάτι το VAE κράτησε περίπου 8–16 s και το PSNR ως προς την αναφορά ήταν 71 έως 73 dB. Αν γίνει αναγκαστική υποχώρηση, η εικόνα έχει τα ίδια pixel με την εικόνα που βγαίνει με tiles (ελέγχθηκε με `PIXEL_SHA256`). Τι συνέβη γράφεται στο `run.json` (`stages.vae_path`: `full`, `tile`, `floor` ή `retry`).

Επίσης: το `--eager-load` (διαβάζει τις σελίδες του μοντέλου εκ των προτέρων· 241.2 s σε 220.3 s στην ίδια εικόνα, build ανάπτυξης, μία εκτέλεση το καθένα) είναι μέρος της σταθερής εντολής.

<a id="what-it-runs"></a>
## Τι τρέχει

| Μέρος | Αρχείο | Πηγή |
|---|---|---|
| Μοντέλο διάχυσης (diffusion) | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), βάση [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Text encoder | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), autoencoder τύπου FLUX.1 |
| Μηχανή | `sd-cli.exe`, stable-diffusion.cpp `32d516c` με τα patches στο [`patches/`](patches) | η έκδοση v0.3.0 αυτού του αποθετηρίου (`sinirsiz-foto-engine-v0.3.0-win-x64-cuda12.8-sm61.zip`) |
| CUDA runtime | `cudart`, `cublas`, `cublasLt` (12.8), αμετάβλητα | zip από την έκδοση v0.1.0 του wan22-pascal-4gb |
| cuDNN (εγκαθίσταται από προεπιλογή· το `--no-cudnn` το παραλείπει) | 8 DLL, έκδοση 9.10.2.21 (build για CUDA 11) | ο ίδιος ο server της NVIDIA, με την άδεια της NVIDIA· δεν αποθηκεύεται εδώ |

Σταθερές ρυθμίσεις: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`.
Δεν μειώνουμε τα βήματα, δεν προσθέτουμε negative prompt και δεν ενεργοποιούμε caching: το μοντέλο είναι distilled για 8 βήματα και δεν χρησιμοποιεί negative prompts (δες τα [prompts](docs/PROMPTS.md)).

## Όρια (διάβασέ τα πριν βασιστείς)

- **Μόνο Windows.** Η προμεταγλωττισμένη μηχανή και αυτά τα scripts είναι μόνο για Windows.
- **Μία κάρτα, ένα μηχάνημα.** Μετρήθηκε μόνο σε laptop με GTX 1050 Ti 4 GB (i7-7700HQ, 16 GB RAM, Windows 10, driver 581.29, μοντέλα σε SSD). Άλλες GPU και driver, μηχανήματα με λιγότερα από 16 GB RAM, Linux και macOS: **δεν δοκιμάστηκαν**.
- Άλλες κάρτες και συστήματα (ποιος δρόμος υπάρχει, και μια δοκιμή της κοινότητας σε κάρτα AMD σε Linux που δεν εκτελέσαμε εμείς): [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md).
- **Η μηχανή είναι χτισμένη μόνο για Pascal (sm_61).** Οι άλλες αρχιτεκτονικές χρειάζονται δικό σου build ([`docs/BUILD.md`](docs/BUILD.md))· δεν δοκιμάσαμε κάποιο.
- **cuDNN:** μετρήσαμε με το build για CUDA 11 του cuDNN 9.10.2.21. Το build για CUDA 12 έχει διαφορετικά αρχεία και δεν μετρήθηκε.
- **Η μνήμη είναι στο όριο.** Η ελεύθερη RAM πέφτει σε λίγες εκατοντάδες MiB· κλείσε τα άλλα προγράμματα και τρέχε μία εικόνα τη φορά. Δεν έχουμε δει τη μνήμη GPU να τελειώνει αφού πέρασε ο έλεγχος μνήμης της μηχανής, και δεν δοκιμάσαμε τι συμβαίνει τότε.
- **Μεγέθη:** δοκιμάστηκαν μόνο τα 768x1344, 1344x768 και 1024x1024. Τα μεγαλύτερα μεγέθη τυπώνουν προειδοποίηση και μπορεί να εξαντλήσουν τη μνήμη.
- Η πιστότητα ως προς το prompt είναι μερική: μια εικόνα δεν ακολουθεί πάντα το prompt της σε κάθε λεπτομέρεια. Το κείμενο μέσα σε εικόνες και τα πραγματικά αξιοθέατα δεν αξιολογήθηκαν.
- Η αναφορά του PSNR είναι η αποκωδικοποίηση στη CPU από τη δική μας μηχανή, όχι μια ανεξάρτητη υλοποίηση.
- Οι αριθμοί στο [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) προέρχονται από μία εκτέλεση ο καθένας, εκτός αν αναφέρεται διαφορετικά.

## Άδεια χρήσης και πίστωση

- Τα scripts και τα έγγραφα αυτού του αποθετηρίου: [Apache-2.0](LICENSE) με αρχείο [`NOTICE`](NOTICE). Τα patches της μηχανής στο [`patches/`](patches) είναι MIT, όπως ο κώδικας που τροποποιούν.
- Το stable-diffusion.cpp και το ggml είναι MIT. Οι σημειώσεις για τον κώδικα τρίτων που έχει μεταγλωττιστεί μέσα στη μηχανή βρίσκονται στο [`licenses/`](licenses) και στο [`THIRD_PARTY.md`](THIRD_PARTY.md).
- Τα αρχεία μοντέλων δεν αποθηκεύονται εδώ· κατεβαίνουν από τις παραπάνω πηγές με τις δικές τους άδειες (το Hugging Face δείχνει Apache-2.0 για όλα, διαβάστηκε στις 2026-11-13). Η κάρτα μοντέλου δεν λέει τίποτα για το ποιος κατέχει τις παραγόμενες εικόνες, και εμείς δεν διατυπώνουμε κανέναν ισχυρισμό σχετικά.
- **Το cuDNN και το CUDA runtime ανήκουν στη NVIDIA** και δεν καλύπτονται από την άδεια αυτού του αποθετηρίου. Το cuDNN κατεβαίνει από τον server της NVIDIA με την άδεια της NVIDIA (το `--no-cudnn` το παραλείπει)· τα DLL του CUDA runtime βρίσκονται σε ξεχωριστό αμετάβλητο zip (CUDA Toolkit EULA, Attachment A). Λεπτομέρειες και όσα δεν μπορέσαμε να επαληθεύσουμε: [`THIRD_PARTY.md`](THIRD_PARTY.md).
- **Πίστωση.** Η διατήρηση του αρχείου `NOTICE` μαζί με τα αντίγραφα και τα παράγωγα έργα είναι προϋπόθεση (Apache-2.0, ενότητα 4). Πέρα από αυτό, μια γραμμή όπως "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey" είναι ευπρόσδεκτη, αλλά δεν απαιτείται.
- Διάβασε το [`ETHICS.md`](ETHICS.md): κάθε εικόνα είναι συνθετική, και εσύ ευθύνεσαι για ό,τι δημοσιεύεις.

## Συνεισφορά

Το πιο χρήσιμο που μπορείς να κάνεις είναι να **δοκιμάσεις την κάρτα σου** και να μας πεις τι έγινε: όνομα GPU, driver, RAM, το `run.json` και τις τελευταίες γραμμές του log (η φόρμα issue "Hardware test report"). Διορθώσεις στα έγγραφα και στα scripts είναι επίσης ευπρόσδεκτες· δες το [`CONTRIBUTING.md`](CONTRIBUTING.md). Οι αναφορές ασφαλείας γίνονται μέσω της ιδιωτικής διαδρομής στο [`SECURITY.md`](SECURITY.md).

[Οδηγός εγκατάστασης για AI agents](AGENTS.md) · [Μετρήσεις](docs/MEASUREMENTS.md) · [Αντιμετώπιση προβλημάτων](docs/TROUBLESHOOTING.md) · [Χτίσιμο της μηχανής](docs/BUILD.md) · [Patches](patches/README.md) · [Prompts](docs/PROMPTS.md) · [Τρίτοι](THIRD_PARTY.md) · [Αλλαγές](CHANGELOG.md)

Αυτή η σελίδα μεταφράστηκε και προσαρμόστηκε στα ελληνικά με τη βοήθεια AI· διορθώσεις είναι ευπρόσδεκτες, δες το [CONTRIBUTING.md](CONTRIBUTING.md).
