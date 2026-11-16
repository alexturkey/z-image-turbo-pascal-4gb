# Katkı / Contributing

**EN**

Welcome. This repository started as one person's measurements on one 4 GB laptop GPU; every report and fix makes it sturdier.
We measured **one card** (GTX 1050 Ti 4 GB, 16 GB RAM, Windows 10), so the most useful contribution is the simplest one.

**Test your card, write a report.** No coding needed: run `python scripts/setup.py` and `python scripts/generate.py --prompt-file prompts/eiffel.txt`, then fill in the
[Hardware test report](https://github.com/alexturkey/z-image-turbo-pascal-4gb/issues/new?template=hardware-test.yml) form: GPU, driver, RAM, and the numbers from `run.json` next to the picture (`outputs/<time>_<name>/run.json`).
Not on Windows with NVIDIA? Read [`docs/OTHER_GPUS.md`](docs/OTHER_GPUS.md) first: it says which path exists for your card; the same form takes your result.
Write even if it failed; an error is a finding too. Cards we have no data for are the most interesting: other 4 GB cards, 6 GB and 8 GB cards, machines with less than 16 GB RAM, other Windows or driver versions.

**Other ways to help**
- Install problems: the [install problem form](https://github.com/alexturkey/z-image-turbo-pascal-4gb/issues/new?template=install-problem.yml). Bugs and ideas have their own forms.
- A wrong or unclear sentence in a document, or in a translated README: open an issue or a pull request. The translations are AI-assisted; a native speaker's correction is very welcome (notes per language are in `docs/translation_notes/`).
- A related setup we missed: tell us, we add it to `docs/RELATED.md` with a link.

**Sending code.** Fork the repository, open a short branch, send a small pull request about one thing. Fill in the pull request template: what changed, how it was tested (command, GPU, Windows version, seconds, pixel hash), whether there are binary files, network calls or new numbers.
Rules:
- The tests pass: `python -B -m unittest discover -s tests`.
- **Image quality is not lowered.** The settings in `scripts/generate.py` (8 steps, cfg 1.0, Q8_0) are the tested point. A change that touches the pixels is accepted when the pixels are identical (`python scripts/compare.py A.png B.png` prints `SAME_PIXELS`) or when it is closer to the reference decode, with the before/after numbers (see "Quality" in `docs/MEASUREMENTS.md`).
- Every new number names its command, hardware, date and number of runs. Do not write a number you did not measure; write "not tested". Exception: a published community result may be quoted in `docs/OTHER_GPUS.md`, labelled "community test", with its author, link, hardware, date and number of runs; never in `docs/MEASUREMENTS.md`.
- No binary files in pull requests (exe, dll, zip, model files). The maintainer publishes engine packages on Releases.
- No image of a real person, and no personal paths or names in files; run `python scripts/privacy_scan.py .` before you send.
- Python 3.10, standard library only: the scripts have no dependencies.

**Questions and results:** [Discussions](https://github.com/alexturkey/z-image-turbo-pascal-4gb/discussions).
**Security vulnerabilities:** do not open a public issue; use the private route in [`SECURITY.md`](SECURITY.md).
By taking part you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md). Contributions are under the repository's Apache-2.0 license; contributions to `patches/` are under MIT.

**TR**

Hoş geldin. Bu depo, tek bir 4 GB dizüstü ekran kartında yapılan ölçümlerle başladı; her rapor ve düzeltme onu biraz daha sağlam yapar.
Yalnız **tek bir kartı** ölçtük (GTX 1050 Ti 4 GB, 16 GB RAM, Windows 10); bu yüzden en işe yarar katkı en basit olanı.

**Kartını test et, rapor yaz.** Kod bilmen gerekmez: `python scripts/setup.py` ve `python scripts/generate.py --prompt-file prompts/eiffel.txt` komutlarını çalıştır, sonra
[Donanım test raporu](https://github.com/alexturkey/z-image-turbo-pascal-4gb/issues/new?template=hardware-test.yml) formunu doldur: ekran kartı, sürücü, RAM ve resmin yanındaki `run.json` içindeki sayılar (`outputs/<zaman>_<ad>/run.json`).
Windows ve NVIDIA dışındaysan önce [`docs/OTHER_GPUS.md`](docs/OTHER_GPUS.md) belgesini oku: kartın için hangi yol olduğunu söyler; sonucunu aynı form alır.
Çalışmadıysa da yaz; hata da bulgudur. Verimiz olmayan kartlar en ilginç olanlar: öteki 4 GB kartlar, 6 GB ve 8 GB kartlar, 16 GB'tan az RAM'li makineler, başka Windows ya da sürücü sürümleri.

**Başka yardım yolları**
- Kurulum sorunu: [kurulum sorunu formu](https://github.com/alexturkey/z-image-turbo-pascal-4gb/issues/new?template=install-problem.yml). Hata ve öneri için ayrı formlar var.
- Bir belgede ya da çevrilmiş bir README'de yanlış ya da belirsiz cümle: issue ya da PR aç. Çeviriler yapay zekâ destekli; anadili konuşanın düzeltmesi çok değerli (dil notları `docs/translation_notes/` içinde).
- Kaçırdığımız benzer bir kurulum: haber ver, bağlantısıyla `docs/RELATED.md`'ye ekleriz.

**Kod göndermek.** Depoyu çatalla (fork), kısa bir dal aç, tek konuya odaklı küçük bir PR gönder. PR şablonunu doldur: ne değişti, nasıl test edildi (komut, ekran kartı, Windows sürümü, süre, piksel özeti), ikili dosya, ağ çağrısı ya da yeni sayı var mı.
Kurallar:
- Testler geçer: `python -B -m unittest discover -s tests`.
- **Görüntü kalitesi düşürülmez.** `scripts/generate.py` içindeki ayarlar (8 adım, cfg 1.0, Q8_0) denenmiş noktadır. Pikselleri değiştiren bir değişiklik, pikseller aynıysa (`python scripts/compare.py A.png B.png` çıktısı `SAME_PIXELS`) ya da referans çözüme daha yakınsa, önce/sonra sayılarıyla kabul edilir (`docs/MEASUREMENTS.md` içindeki "Quality" bölümüne bak).
- Her yeni sayının komutu, donanımı, tarihi ve koşu sayısı yazılır. Ölçmediğin sayıyı yazma; "not tested" yaz. İstisna: yayımlanmış bir topluluk sonucu `docs/OTHER_GPUS.md` içinde "community test" etiketiyle, yazarı, bağlantısı, donanımı, tarihi ve koşu sayısıyla alıntılanabilir; `docs/MEASUREMENTS.md` içine asla.
- PR'a ikili dosya (exe, dll, zip, model dosyası) girmez. Motor paketlerini bakımcı Releases'e koyar.
- Gerçek bir kişinin görüntüsü ve dosyalarda kişisel yol ya da ad olmaz; göndermeden önce `python scripts/privacy_scan.py .` çalıştır.
- Python 3.10, yalnız standart kitaplık: betiklerin bağımlılığı yok.

**Soru ve sonuç:** [Discussions](https://github.com/alexturkey/z-image-turbo-pascal-4gb/discussions). **Güvenlik açığı:** herkese açık issue açma; [`SECURITY.md`](SECURITY.md)'deki özel bildirim yolunu kullan.
Katılarak [Davranış Kuralları](CODE_OF_CONDUCT.md)'na uymayı kabul edersin. Katkılar deponun Apache-2.0 lisansı altındadır; `patches/` altındaki katkılar MIT'tir.
