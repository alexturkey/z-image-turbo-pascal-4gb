# Privacy / Gizlilik

## English (authoritative)

**Short version: z-image-turbo-pascal-4gb has no telemetry. Its scripts use the network only for the downloads listed below, and only from the hosts listed below.** Nothing about you, your machine or your data is uploaded.

### What the scripts fetch
| Host | What | Which script, when |
|---|---|---|
| `huggingface.co` | the three model files at pinned commits | `scripts/setup.py`, install |
| `github.com` | the engine zip and the CUDA runtime zip (pinned release tags) | `scripts/setup.py`, install |
| `developer.download.nvidia.com` | the NVIDIA cuDNN archive (skipped with `--no-cudnn`) | `scripts/setup.py`, install |
| `docs.nvidia.com` | printed as the license address only; the script does not open it | `scripts/setup.py`, install |

A download from these hosts may be redirected by the host to its own file-delivery (CDN) address; that follows the redirect of the pinned address and is not listed separately [read from the code, urllib follows redirects].

Every download is checked against a pinned sha256 where one exists and stops on a mismatch. Like any download, the host sees your IP address and the ordinary request headers. We send nothing else: no account, no usernames, no system information, no usage data.

### What it does not do
No telemetry or analytics, no crash reports, no update check, no accounts or cookies, no network ports opened. Image generation runs fully on your machine: your prompts and pictures never leave it.

### What stays on your computer
The folders you choose (`models/`, `bin/` by default, or the `--models-dir` and `--bin-dir` ones) and the `outputs/` folders with your prompts' pictures, `run.json` and `log.txt` (the exact command is in them). Logs can contain your folder path: remove it before you post a log in an issue.

### Outside our scripts
- GitHub processes what you post here (issues, pull requests, stars) under the GitHub Privacy Statement; it is public.
- The model files and NVIDIA cuDNN are under their own licenses, not under this policy (`THIRD_PARTY.md`).

### Check it yourself (a few seconds, nothing is downloaded)
Every network call in the code: `grep -rnE "https?://|urllib|socket" scripts models.lock.json`. Expected today: the hosts above and nothing else. If you find a call that is not listed here, please report it as in `SECURITY.md`. When a release adds a host, this file is updated in the same change.

## Türkçe

**Kısaca: z-image-turbo-pascal-4gb'da telemetri yok. Betikler ağı yalnız aşağıdaki indirmeler için, yalnız aşağıdaki adreslerden kullanır.** Sizin, makinenizin ya da verinizin hiçbir bilgisi yüklenmez.

### Betiklerin indirdikleri
| Adres | Ne | Hangi betik, ne zaman |
|---|---|---|
| `huggingface.co` | sabit commit'lerdeki üç model dosyası | `scripts/setup.py`, kurulum |
| `github.com` | motor zip'i ve CUDA çalışma zamanı zip'i (sabit sürüm etiketleri) | `scripts/setup.py`, kurulum |
| `developer.download.nvidia.com` | NVIDIA cuDNN arşivi (`--no-cudnn` ile atlanır) | `scripts/setup.py`, kurulum |
| `docs.nvidia.com` | yalnız lisans adresi olarak yazdırılır; betik açmaz | `scripts/setup.py`, kurulum |

Bu adreslerden bir indirme, adresin kendi dosya dağıtım (CDN) adresine yönlendirilebilir; bu, sabit adresin yönlendirmesini izler ve ayrıca listelenmez [koddan okudum, urllib yönlendirmeyi izler].

Sabitlenmiş sha256 olan her indirme ona karşı denetlenir, uyuşmazsa durur. Her indirmede olduğu gibi karşı taraf IP adresinizi ve olağan istek başlıklarını görür. Başka hiçbir şey göndermeyiz: hesap, kullanıcı adı, sistem bilgisi, kullanım verisi yok.

### Yapmadıkları
Telemetri/analitik yok, çökme raporu yok, güncelleme denetimi yok, hesap ya da çerez yok, ağ portu açmaz. Resim üretimi tamamen makinenizde çalışır: istemleriniz ve resimleriniz makineden çıkmaz.

### Bilgisayarınızda kalanlar
Seçtiğiniz klasörler (varsayılan `models/`, `bin/` ya da `--models-dir` ve `--bin-dir` ile verdikleriniz) ve resimlerin, `run.json` ile `log.txt` dosyalarının olduğu `outputs/` klasörleri (tam komut içlerinde yazar). Günlüklerde klasör yolunuz olabilir: issue'ya günlük koymadan önce silin.

### Betiklerimizin dışında
- Burada paylaştığınız (issue, PR, yıldız) GitHub tarafından GitHub Gizlilik Bildirimi'ne göre işlenir ve herkese açıktır.
- Model dosyaları ve NVIDIA cuDNN kendi lisanslarındadır, bu metnin kapsamı dışındadır (`THIRD_PARTY.md`).

### Kendiniz denetleyin (birkaç saniye, hiçbir şey indirilmez)
Koddaki bütün ağ çağrıları: `grep -rnE "https?://|urllib|socket" scripts models.lock.json`. Bugün beklenen: yalnız yukarıdaki adresler. Listede olmayan bir çağrı bulursanız `SECURITY.md`'deki gibi bildirin. Bir sürüm yeni adres eklerse bu dosya aynı değişiklikte güncellenir.
