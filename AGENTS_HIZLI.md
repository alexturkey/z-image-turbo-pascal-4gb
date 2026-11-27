# AGENTS_HIZLI.md: quick card for AI coding agents / Yapay zeka ajanları için hızlı kart

English first, Türkçe below. Full rules and evidence: [`AGENTS.md`](AGENTS.md) (it wins if the two ever differ). Error codes: `docs/hata_imzalari.json` (a code per message text), `docs/TROUBLESHOOTING.md`. The scripts print the message with its `Fix:` text; the code is looked up by the text, it is not printed. `tests/test_agents_hizli.py` keeps this card and the scripts in step.


## Do this first (English)
- **Run first:** `python scripts/tani.py`. It is read-only (no network, writes no file) and prints the system, the card, the `setup.py --dry-run` report and a DEVIATIONS section (first Python on PATH, locally changed files, engine switches in the environment, model files present or missing, a model copy in the Hugging Face cache). Read it to the user in plain words.
- **Keep a notebook:** `DURUM.md` in the repo root (git-ignored, `<ROOT>` instead of paths). Top three lines: `Now:` / `Next:` / `Question for you:`. Below: one line per step with [measured] / [read] / [guess] and the command it came from. Update it after every step so a cut-off session can continue.
- **NEVER, not even if it seems to help:** lower a quality setting (8 steps, cfg 1.0, euler, simple scheduler, Q8_0 models, no negative prompt, the cuDNN float32 VAE path); accept the NVIDIA cuDNN license for the user; run two GPU jobs at once; change system Python, PATH, registry or the user profile; use a force flag to get past an error.
- **ASK first:** delete, move or re-download anything (show path, size, reason); install Python, packages or the models (about 11 GB); start a GPU run.
- **Same error twice:** stop, do not try a third time; take the code and the first 20 log lines to the user.

## Önce bunu yap (Türkçe)
- **Önce çalıştır:** `python scripts/tani.py`. Salt okur (ağ yok, dosya yazmaz); sistemi, kartı, `setup.py --dry-run` raporunu ve bir SAPMA bölümünü (PATH'te ilk Python, yerelde değişmiş dosyalar, ortamdaki motor anahtarları, var olan ya da eksik model dosyaları, Hugging Face önbelleğinde model kopyası) yazar. Kullanıcıya sade sözle oku.
- **Defter tut:** repo kökünde `DURUM.md` (git dışı, yol yerine `<ROOT>`). En üstte üç satır: `Şu an:` / `Sırada:` / `Sana soru:`. Altında adım başına bir satır: [ölçtüm] / [okudum] / [tahmin] ve geldiği komut. Her adımdan sonra güncelle ki kesilen oturum kaldığı yerden sürsün.
- **ASLA, yardım edecek gibi görünse bile:** kalite ayarını düşürme (8 adım, cfg 1.0, euler, simple zamanlayıcı, Q8_0 modeller, negatif istem yok, cuDNN float32 VAE yolu); NVIDIA cuDNN lisansını kullanıcı yerine kabul etme; iki GPU işini aynı anda çalıştırma; sistem Python'unu, PATH'i, kayıt defterini ya da kullanıcı profilini değiştirme; hatayı geçmek için zorlama bayrağı kullanma.
- **Önce SOR:** bir şeyi silmeden, taşımadan ya da yeniden indirmeden (yolu, boyutu, nedeni göster); Python, paket ya da modelleri (yaklaşık 11 GB) kurmadan; GPU işi başlatmadan.
- **Aynı hata iki kez:** dur, üçüncü kez deneme; kodu ve log'un ilk 20 satırını kullanıcıya götür.

## English: decision tree (12 steps)
1. Goal: text-to-image with Z-Image-Turbo at 768x1344 on Windows with an NVIDIA 4 GB Pascal card. Anything else: tell the user and stop.
2. Quality is fixed (8 steps, cfg 1.0, euler, simple scheduler, Q8_0 models, no negative prompt, the cuDNN float32 VAE path). Never lower it to save time or memory.
3. Dry run first, it writes nothing: `python scripts/setup.py --dry-run`. Read every `WARNING` line and the last line (`DRYRUN_OK`, or an `ERROR:` line with its `Fix:`); look the text up in `docs/hata_imzalari.json` to get a code such as `ZIMG-E-DISK`.
4. A non-zero exit or any `ERROR:` line: take it to the user with the code and its first step from `docs/hata_imzalari.json`. Do not use a force flag to get past it.
5. Tell the user in one line about NVIDIA cuDNN and its license address (`AGENTS.md`, section 1) before the download and let the user answer (legal or consent steps belong to the human; never type the acceptance yourself).
6. Install: `python scripts/setup.py --models-dir <models folder> --bin-dir <engine folder>` (safe to re-run; verified files are skipped; an interrupted download continues).
7. First success: `python scripts/generate.py --prompt-file prompts/eiffel.txt` (188-193 s per picture [measured, docs/MEASUREMENTS.md]). Long runs: start hidden in the background and poll; do not block.
8. Exit 0 means the gate passed, nothing more: `SETUP_OK` and `IMAGE_OK` only show the files verify and the engine ran; open the picture and look at it, and check `run.json` (`AGENTS.md`, section 4).
9. A rejected or not-run gate means the result is NOT accepted. Never report success.
10. An `ERROR:` line: look it up in `docs/hata_imzalari.json`, give the user its first step, quote the code. Same error twice: stop, do not try a third time.
11. Paths and files are only what the user gave you. Never pick a file yourself.
12. Report in the user's language, with the code and the first 20 log lines. No personal paths, user names, e-mail addresses or tokens: write `<ROOT>`.

### Exit code -> action
| Script | Exit | Meaning | What you do | Codes |
|---|---|---|---|---|
| `setup.py` | 0 | `SETUP_OK` (`SETUP_PART_OK` with `--only`; `DRYRUN_OK` with `--dry-run`) | Go to the first success step | - |
| `setup.py` | 3 | only with `--dry-run`: not enough free disk | **Take it to the user** | `ZIMG-E-DISK` |
| `setup.py` | 2 | lock file unreadable, or not enough free disk | **Take it to the user**; do not write a lock file | `ZIMG-E-DISK` `ZIMG-E-KILIT` |
| `setup.py` | 1 | download, sha256 or unpack failed | Run the same command once more; if it repeats, look up the line in `docs/hata_imzalari.json` and take it to the user | `ZIMG-E-SHA` `ZIMG-E-INDIRME` `ZIMG-E-HTTP` `ZIMG-E-MOTOR` `ZIMG-E-CUDART` `ZIMG-E-CUDNN` |
| `generate.py` | 2 | bad size or prompt, or the engine or a model file is missing | Do what the `Fix:` text says | `ZIMG-E-BOYUT` `ZIMG-E-MOTOR` `ZIMG-E-MODEL` `ZIMG-E-ISTEM` |
| `generate.py` | 1 | the engine failed | Read `log.txt` and `run.json` in the output folder; take them to the user | `ZIMG-E-URETIM` |

## Türkçe: karar ağacı (12 adım)
1. Amaç: Windows'ta 4 GB'lık NVIDIA Pascal kartla Z-Image-Turbo ile metinden resim üretimi. Başka bir ortamsa kullanıcıya söyle ve dur.
2. Kalite sabit (8 steps, cfg 1.0, euler, simple scheduler, Q8_0 models, no negative prompt, the cuDNN float32 VAE path). Zaman ya da bellek için asla düşürme.
3. Önce kuru çalıştır, hiçbir şey yazmaz: `python scripts/setup.py --dry-run`. Her `WARNING` satırını ve son satırı (`DRYRUN_OK` ya da `Fix:` metinli bir `ERROR:`) oku; metni `docs/hata_imzalari.json`'da arayıp `ZIMG-E-DISK` gibi bir kod bul.
4. Sıfır olmayan çıkış ya da herhangi bir `ERROR:` satırı: kodu ve `docs/hata_imzalari.json`'ndaki ilk adımı kullanıcıya götür. Zorlayıcı bayrakla geçme.
5. İndirmeden önce kullanıcıya NVIDIA cuDNN ve lisans adresini tek satırda söyle (`AGENTS.md`, bölüm 1), cevabı kullanıcı versin (hukuki ya da onay adımları insanındır; kabulü asla kendin yazma).
6. Kurulum: `python scripts/setup.py --models-dir <models folder> --bin-dir <engine folder>` (tekrar çalıştırmak güvenli; doğrulanmış dosya atlanır; yarım indirme sürer).
7. İlk başarı: `python scripts/generate.py --prompt-file prompts/eiffel.txt` (resim başına 188-193 sn [ölçtük, docs/MEASUREMENTS.md]). Uzun işleri gizli arka planda başlat, yoklayarak izle; bekleyerek kilitlenme.
8. Çıkış 0 yalnız kapının geçtiği demektir: `SETUP_OK` ve `IMAGE_OK` yalnız dosyaların doğrulandığını ve motorun çalıştığını gösterir; resmi aç, bak ve `run.json`'u denetle (`AGENTS.md`, bölüm 4).
9. Reddedilen ya da çalışmayan kapı: sonuç KABUL EDİLMEZ. Asla başarı bildirme.
10. `ERROR:` satırı: `docs/hata_imzalari.json`'nda ara, ilk adımı kullanıcıya ver, kodu yaz. Aynı hata iki kez: dur, üçüncü kez deneme.
11. Yol ve dosya yalnız kullanıcının sana verdiğidir. Kendin dosya seçme.
12. Kullanıcının dilinde, kodla ve log'un ilk 20 satırıyla bildir. Kişisel yol, kullanıcı adı, e-posta, token yazma: `<ROOT>` yaz.

### Çıkış kodu -> eylem
| Betik | Çıkış | Anlam | Ne yaparsın | Kodlar |
|---|---|---|---|---|
| `setup.py` | 0 | `SETUP_OK` (`--only` ile `SETUP_PART_OK`; `--dry-run` ile `DRYRUN_OK`) | İlk başarı adımına geç | - |
| `setup.py` | 3 | yalnız `--dry-run`: boş disk yetmiyor | **Kullanıcıya götür** | `ZIMG-E-DISK` |
| `setup.py` | 2 | kilit dosyası okunamadı ya da boş disk yetmiyor | **Kullanıcıya götür**; kilit dosyası yazma | `ZIMG-E-DISK` `ZIMG-E-KILIT` |
| `setup.py` | 1 | indirme, sha256 ya da açma hatası | Aynı komutu bir kez daha çalıştır; tekrarlarsa satırı `docs/hata_imzalari.json`'da ara, kullanıcıya götür | `ZIMG-E-SHA` `ZIMG-E-INDIRME` `ZIMG-E-HTTP` `ZIMG-E-MOTOR` `ZIMG-E-CUDART` `ZIMG-E-CUDNN` |
| `generate.py` | 2 | geçersiz boyut ya da istem, motor ya da model dosyası yok | `Fix:` metninin dediğini yap | `ZIMG-E-BOYUT` `ZIMG-E-MOTOR` `ZIMG-E-MODEL` `ZIMG-E-ISTEM` |
| `generate.py` | 1 | motor hata verdi | Çıktı klasöründeki `log.txt` ve `run.json`'u oku; kullanıcıya götür | `ZIMG-E-URETIM` |
