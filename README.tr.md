**Türkçe** · [English](README.md)

# sinirsiz-foto

**4 GB'lık GTX 1050 Ti'da (Windows) Z-Image-Turbo ile yazıdan resim.** Küçük ve tekrarlanabilir bir kurulum: sha256 ile
doğrulanan sabit model dosyaları, Pascal yamalı hazır motor, iki Python betiği (yalnız standart kütüphane) ve ayarların
arkasındaki ölçümler. Bu kartta 768x1344'lük bir resim yaklaşık dört dakika sürer.

- **Kimin için:** eski, 4 GB'lık NVIDIA kart (Pascal, hesaplama kapasitesi 6.1) sahipleri. Yalnız GTX 1050 Ti 4 GB dizüstü kartı ölçüldü; diğer kartlar denenmedi.
  Kodlama ajanları için de: [`AGENTS.md`](AGENTS.md) adım adım izlenebilir kurulumdur (İngilizce).
- **Ne alırsın:** Z-Image-Turbo (Q8_0), Qwen3-4B-Instruct-2507 (Q8_0) metin kodlayıcı, 8 adım, negatif istem yok, varsayılan dikey 768x1344.
- **Bedeli:** zaman ve RAM. Resim başına yaklaşık 250-259 sn; 16 GB'lık makinede boş RAM en düşük 331-576 MiB'e iniyor ([ölçümler](docs/MEASUREMENTS.md)). Çalışırken başka program açma.

[Yapay zeka ajanları için kurulum](AGENTS.md) · [Ölçümler](docs/MEASUREMENTS.md) · [İstemler](docs/PROMPTS.md) · [Sorun giderme](docs/TROUBLESHOOTING.md) · [Üçüncü taraf](THIRD_PARTY.md) · [Değişiklikler](CHANGELOG.md)

Not: ayrıntılı belgeler İngilizcedir; bu sayfa özetidir.

## Örnekler

**Bu depoyla yapay zekâ üretimi** (Z-Image-Turbo Q8_0, tohum 42, 8 adım). Gerçek fotoğraf değildir; yapılar ve ayrıntılar
yanlış olabilir. İstemlerin tamamı [`prompts/`](prompts) klasöründe.

| | | |
|---|---|---|
| ![Altın saatte Eyfel Kulesi](docs/examples/eiffel.jpg) | ![Türk çay bardağı](docs/examples/turkish_tea.jpg) | ![Yaşlı balıkçı](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![Yamaç köyü](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344. Yuvarlak kapılar tepeye oyulmuş değil, ayrı kulübeler çıktı: istem uyumu kısmi. | | |

![Havadan İstanbul](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. Gerçek fotoğraf değil; yapılar yanlış olabilir.

## Hızlı başlangıç

Gerekenler: Windows 10/11, 4 GB'lık NVIDIA kart, güncel sürücü (CUDA 12.8 çalışma zamanı sizin için indirilir),
Python 3.10 veya üstü, yaklaşık 13 GB boş disk (indirmeler yaklaşık 11,8 GB) ve 16 GB RAM (ölçülen buydu; daha azı denenmedi).

```powershell
git clone https://github.com/alexturkey/sinirsiz-foto.git
cd sinirsiz-foto
python scripts/setup.py --models-dir D:\models --bin-dir D:\bin
python scripts/generate.py --prompt-file prompts/eiffel.txt --models-dir D:\models --bin-dir D:\bin
```

- `setup.py`, [`models.lock.json`](models.lock.json) içindeki sabit adreslerden indirir ve her dosyayı sha256 ile doğrular.
  Çıktı: `MODEL_OK <ad>`, `ENGINE_OK`, `CUDART_OK`, son satır `SETUP_OK`. `--models-dir` ve `--bin-dir` verilmezse depo kökündeki `models/` ve `bin/` kullanılır; modelleri SSD'ye koy (yalnız SSD'de ölçüldü).
- `generate.py`, `outputs/<YYYYmmdd_HHMMSS>_<ad>/image.png` ve `run.json` yazar (süre, aşamalar, nvidia-smi'den VRAM tepesi, tam komut) ve `IMAGE_OK <yol>` basar.
- Seçenekler: `--prompt "<metin>"` ya da `--prompt-file <txt>`, `--width 768 --height 1344 --seed 42 --out outputs/`. Yatay için `--width 1344 --height 768`.

İndirme boyutu yaklaşık 11,8 GB (modeller 11.193.150.692 bayt, motor zip 37.182.063 bayt, CUDA zip 567.007.257 bayt; `models.lock.json` boyutlarından).

## Neyi çalıştırır

| Parça | Dosya | Kaynak |
|---|---|---|
| Çizim modeli | `z_image_turbo-Q8_0.gguf` (6.577.440.704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), asıl [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Metin kodlayıcı | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4.280.405.600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335.304.388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), FLUX.1 türü otokodlayıcı |
| Motor | `sd-cli.exe`, stable-diffusion.cpp `master-1088-32d516c` + dört Pascal yaması | [wan22-pascal-4gb v0.1.0 sürümü](https://github.com/alexturkey/wan22-pascal-4gb/releases/tag/v0.1.0) zip'i |
| CUDA çalışma zamanı | `cudart`, `cublas`, `cublasLt` (12.8), değiştirilmemiş | aynı sürüm, ayrı zip |

Sabit ayarlar (ölçüldü): `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --flash-attn on`.
Adım düşürmüyoruz, negatif istem eklemiyoruz, önbellek açmıyoruz: model 8 adım için damıtılmış ve negatif istem kullanmıyor ([istemler](docs/PROMPTS.md)).

## Ölçüm (özet)

Tek makine: GTX 1050 Ti 4 GB dizüstü, i7-7700HQ, 16 GB RAM, Windows 10, sürücü 581.29, modeller SSD'de. 768x1344, tohum 42.

| Resim | Toplam | Metin kodlama | Örnekleme | VAE çözme | VRAM tepe | Boş RAM en düşük |
|---|---|---|---|---|---|---|
| eiffel | 250,4 sn | 13,0 sn | 199,5 sn | 29,8 sn | 2949 MiB | 363 MiB |
| village | 256,2 sn | 12,9 sn | 200,6 sn | 36,3 sn | 2949 MiB | 429 MiB |
| turkish_tea | 257,5 sn | 13,3 sn | 201,3 sn | 34,5 sn | kaydedilmedi | 331 MiB |
| fisherman | 258,5 sn | 13,9 sn | 204,0 sn | 34,2 sn | kaydedilmedi | 538 MiB |
| istanbul_aerial (1344x768) | 250,7 sn | 13,5 sn | 199,5 sn | 32,6 sn | 2951 MiB | 576 MiB |

Bu beş çalıştırmada siyah ya da NaN resim çıkmadı. 768x1344'te VAE tek parça VRAM'e sığmıyor; motor kendiliğinden 384x672
karolarla yeniden deniyor (log satırı: `VAE decode ran out of memory; retrying with spatial tiling`). Motor süreci yaklaşık
10,5-10,9 GB yer kaplıyor (bellek eşlemeli model sayfaları dahil), bu yüzden boş RAM çok düşüyor.
Bu çalıştırmalar aynı dört yamanın geliştirme derlemesiyle yapıldı. Yayımlanan sürüm zip'leriyle temiz kök testi (deponun temiz kopyası, önce `setup.py` sonra `prompts/turkish_tea.txt` ile `generate.py`, 768x1344): kurulum 165 sn'de bitti, tüm `*_OK` satırları ve `SETUP_OK` göründü (iki büyük model önceden kopyalanıp sha256 ile doğrulandı; `ae.safetensors` ve iki zip gerçekten indirildi); üretim 261,6 sn sürdü (metin 13,0, örnekleme 198,7, VAE 33,7 sn), VRAM tepe 2957 MiB, boş RAM en düşük 488 MiB; çıkan resim geliştirme motorunun resmiyle bayt bayt aynı.

## Sınırlar (güvenmeden önce oku)

- Tek GTX 1050 Ti 4 GB dizüstü, Windows 10'da ölçüldü. Diğer kartlar, sürücüler, 8 GB RAM'li makineler, Linux ve macOS: **denenmedi**.
- Çalışırken boş RAM birkaç yüz MiB'e iniyor. Tarayıcı ya da başka ağır program açma.
- İstem uyumu kısmi (köy örneğine bak). Resim içindeki yazı ve gerçek yapıların doğruluğu değerlendirilmedi.
- Aynı anda tek iş. Hız hedef değildi; ayarlar test edilmiş noktadır, ayarlanmış en iyi değer değil.

## Lisans

- **Bu deponun betikleri ve belgeleri:** MIT, Telif (c) 2026 alexturkey ([`LICENSE`](LICENSE)).
- **stable-diffusion.cpp** ve **ggml** (motor): MIT. Motora derlenen üçüncü taraf kodların bildirimleri [`licenses/`](licenses) ve [`THIRD_PARTY.md`](THIRD_PARTY.md) içinde.
- **Model dosyaları** bu depoda yok; yukarıdaki kaynaklardan indirilir. Hugging Face, Z-Image-Turbo, GGUF dönüşümü, Qwen3-4B-Instruct-2507, onun GGUF dönüşümü ve Comfy-Org paketi için `license: apache-2.0` gösteriyor (Hugging Face API'den 2026-11-13'te okundu).
  Apache-2.0 model dosyalarının lisansıdır; **Z-Image-Turbo model kartı üretilen resimlerin sahipliği hakkında bir şey söylemiyor** ve biz de bu konuda iddia etmiyoruz. Yapay zekâ çıktısının kime ait olduğu ülkenize göre değişir; kendiniz kontrol edin.
- VAE, Comfy-Org deposundan alınan FLUX.1 türü bir otokodlayıcıdır (Apache-2.0 etiketli). FLUX.1-schnell ve FLUX.1-dev depolarındaki dosyayla bayt bayt aynı olup olmadığı doğrulanamadı (depolar kapılı ve dosya özetleri okunamadı).
- **NVIDIA CUDA çalışma zamanı DLL'leri** NVIDIA'nındır, MIT kapsamında değildir. Ayrı, değiştirilmemiş zip'te, CUDA Toolkit EULA Ek A altında. Visual C++ çalışma zamanı ve ffmpeg dahil değil.
- Örnek resimler bu depoyla yapay zekâ üretimidir.
