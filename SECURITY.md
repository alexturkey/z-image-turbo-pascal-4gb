# Security / Güvenlik

**EN**

If you find a security vulnerability, please do not open a public issue. Use GitHub's private reporting:
**Security → Report a vulnerability** on the repository page (or
https://github.com/alexturkey/z-image-turbo-pascal-4gb/security/advisories/new). Reports reach only the maintainer.

Please include the version (`git log -1` or the Release tag), how to trigger it and the impact. We try to look at
reports as soon as we can. Please hold details until a fix is published; the fix notes will credit you if you wish.

Scope: the Python code under `scripts/`, the lock file `models.lock.json`, the patches in `patches/` and the prebuilt
engine zip on Releases. Out of scope: the model files, stable-diffusion.cpp and ggml themselves, NVIDIA CUDA and cuDNN
(report those upstream).

How the download chain is built (intentional design, so you can check it):
- `scripts/setup.py` downloads only what `models.lock.json` lists: pinned Hugging Face commits, pinned release tags and
  one versioned NVIDIA archive. Never `main` or `latest`.
- Every file is checked against the size and sha256 in the lock file. On a mismatch the file is not used.
- Zip archives are unpacked with a path check (no entry may leave the target folder). From the NVIDIA cuDNN archive
  only the listed DLLs and the license file are copied, each checked by size and CRC32.
- cuDNN is downloaded from NVIDIA's own server by default, under NVIDIA's license. Setup prints a line with the license
  address before the download and `--no-cudnn` skips it; a local record (license text and that it was the disclosed default, `mode: default_download_disclosed`)
  is written to `cudnn_license_record.json`.
- The scripts use the Python standard library only. No `pip install`, no administrator rights, no change to `PATH` or
  any system setting. `generate.py` puts the engine folder first on the `PATH` of the engine process only.
- The scripts open no network port and send no prompt, image or usage data. The engine zip also contains
  `sd-server.exe`; the scripts in this repository do not start it. If you start it yourself, keep it on `127.0.0.1`.

**TR**

Bir güvenlik açığı bulduysanız lütfen herkese açık bir issue açmayın. GitHub'ın özel bildirim yolunu kullanın:
repo sayfasında **Security → Report a vulnerability** (ya da doğrudan
https://github.com/alexturkey/z-image-turbo-pascal-4gb/security/advisories/new). Bildirim yalnız bakımcıya gider.

Yazarken: hangi sürüm (`git log -1` ya da Release etiketi), nasıl tetiklendiği, etkisi. Bildirimlere en kısa sürede
bakmaya çalışırız. Düzeltme yayınlanana kadar ayrıntıyı paylaşmamanızı rica ederiz; düzeltme notunda isterseniz
adınızla teşekkür edilir.

Kapsam: `scripts/` altındaki Python kodu, `models.lock.json` kilit dosyası, `patches/` altındaki yamalar ve
Releases'taki hazır motor zip'i. Kapsam dışı: model dosyaları, stable-diffusion.cpp ve ggml'in kendisi, NVIDIA CUDA ve
cuDNN (kendi projelerine bildirin).

İndirme zinciri nasıl kurulu (bilerek böyle; denetleyebilmeniz için):
- `scripts/setup.py` yalnız `models.lock.json` içinde yazılı olanı indirir: sabit Hugging Face commit'leri, sabit
  sürüm etiketleri ve tek bir sürümlü NVIDIA arşivi. `main` ya da `latest` asla.
- Her dosya kilitteki boyut ve sha256 ile denetlenir. Tutmazsa dosya kullanılmaz.
- Zip arşivleri yol denetimiyle açılır (hiçbir girdi hedef klasörün dışına çıkamaz). NVIDIA cuDNN arşivinden yalnız
  listelenen DLL'ler ve lisans dosyası kopyalanır; her biri boyut ve CRC32 ile denetlenir.
- cuDNN varsayılan olarak NVIDIA'nın kendi sunucusundan, NVIDIA'nın lisansı altında iner. Kurulum indirmeden önce
  lisans adresini bir satırla yazar, `--no-cudnn` atlar; yerelde bir kayıt (lisans metni ve bunun varsayılan olduğu)
  `cudnn_license_record.json` dosyasına yazılır.
- Betikler yalnız Python standart kitaplığını kullanır. `pip install` yok, yönetici hakkı yok, `PATH` ya da başka
  bir sistem ayarı değişmez. `generate.py` motor klasörünü yalnız motor sürecinin `PATH`'inin başına koyar.
- Betikler ağ kapısı açmaz; istem, resim ya da kullanım verisi göndermez. Motor zip'inde `sd-server.exe` de vardır;
  bu repodaki betikler onu başlatmaz. Kendiniz başlatırsanız `127.0.0.1`'de tutun.
