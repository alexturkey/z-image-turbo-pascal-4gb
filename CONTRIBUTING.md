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

**Sending code: your first pull request in 5 steps.**
1. Fork the repository (Fork button on GitHub), then clone your fork.
2. Open a short branch and change one thing: `git switch -c fix/short-name`.
3. Run the checks (a few seconds, needs Python 3): `python -I -X utf8 scripts/denetim.py --hizli` (the last line says `SONUC: GECTI`, passed, or `SONUC: KIRMIZI`, red); on Windows `scripts\on_kontrol.cmd` does the same. Add `--tam` for the unit tests too.
4. Commit and push to your fork. Use your GitHub no-reply e-mail (see "Your commit e-mail" below).
5. Open the pull request and fill in the short template: what changed, how it was tested (command, GPU, Windows version, seconds, pixel hash), whether there are binary files, network calls or new numbers. Not sure it is ready? Open it as a **draft**; we will say what to fix. Our goal is a first reply within 7 days: a goal of a small volunteer project, not a promise.

Rules:
- The tests pass: `python -B -m unittest discover -s tests`.
- **Image quality is not lowered.** The settings in `scripts/generate.py` (8 steps, cfg 1.0, Q8_0) are the tested point. A change that touches the pixels is accepted when the pixels are identical (`python scripts/compare.py A.png B.png` prints `SAME_PIXELS`) or when it is closer to the reference decode, with the before/after numbers (see "Quality" in `docs/MEASUREMENTS.md`).
- Every new number names its command, hardware, date and number of runs. Do not write a number you did not measure; write "not tested". Exception: a published community result may be quoted in `docs/OTHER_GPUS.md`, labelled "community test", with its author, link, hardware, date and number of runs; never in `docs/MEASUREMENTS.md`.
- No binary files in pull requests (exe, dll, zip, model files). The maintainer publishes engine packages on Releases.
- No image of a real person, and no personal paths or names in files; run `python scripts/privacy_scan.py .` before you send.
- Python 3.10, standard library only: the scripts have no dependencies.

**Evidence labels** (use them in the pull request and in docs): **[measured]** you ran it and kept the log or numbers; **[read]** you read it in a file or document (give the path); **[computed]** derived from measured numbers; **[user-reported]** someone else reported it, not reproduced; **[guess]** not checked. Do not write "works" about something you did not run; a labelled guess is welcome. In this repository the same ideas appear as "measured on ...", "not tested" and "community test".

**One language is enough.** Write in English or Turkish (any language is fine if that is what you have). If your change touches a section, a maintainer writes the other language. For README content edit `README.md` (the English source); translations are updated together by the maintainers. For the license and security text, English is authoritative in every language.

**Your commit e-mail.** Commits keep their e-mail in history for good. To keep your address private use the GitHub no-reply address: GitHub > Settings > Emails > "Keep my email addresses private", then `git config user.email "<ID>+<username>@users.noreply.github.com"` (the ID is shown on that page). Commits with another address are accepted.

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

**Kod göndermek: ilk PR'ın 5 adımda.**
1. Depoyu çatalla (GitHub'da Fork düğmesi), çatalını klonla.
2. Kısa bir dal aç, tek şeyi değiştir: `git switch -c fix/kisa-ad`.
3. Kontrolleri çalıştır (birkaç saniye, Python 3 gerekir): `python -I -X utf8 scripts/denetim.py --hizli` (son satır `SONUC: GECTI` ya da `SONUC: KIRMIZI`); Windows'ta `scripts\on_kontrol.cmd` aynısını yapar. Birim testlerini de çalıştırmak için `--tam` ekle.
4. Çatalına commit ve push yap. GitHub no-reply e-postanı kullan (aşağıda "Commit e-postan").
5. PR aç, kısa şablonu doldur: ne değişti, nasıl test edildi (komut, ekran kartı, Windows sürümü, süre, piksel özeti), ikili dosya, ağ çağrısı ya da yeni sayı var mı. Hazır mı emin değilsen **taslak (draft)** aç; neyi düzelteceğini söyleriz. Hedefimiz ilk yanıtı 7 gün içinde vermek: küçük bir gönüllü projenin hedefi, taahhüdü değil.

Kurallar:
- Testler geçer: `python -B -m unittest discover -s tests`.
- **Görüntü kalitesi düşürülmez.** `scripts/generate.py` içindeki ayarlar (8 adım, cfg 1.0, Q8_0) denenmiş noktadır. Pikselleri değiştiren bir değişiklik, pikseller aynıysa (`python scripts/compare.py A.png B.png` çıktısı `SAME_PIXELS`) ya da referans çözüme daha yakınsa, önce/sonra sayılarıyla kabul edilir (`docs/MEASUREMENTS.md` içindeki "Quality" bölümüne bak).
- Her yeni sayının komutu, donanımı, tarihi ve koşu sayısı yazılır. Ölçmediğin sayıyı yazma; "not tested" yaz. İstisna: yayımlanmış bir topluluk sonucu `docs/OTHER_GPUS.md` içinde "community test" etiketiyle, yazarı, bağlantısı, donanımı, tarihi ve koşu sayısıyla alıntılanabilir; `docs/MEASUREMENTS.md` içine asla.
- PR'a ikili dosya (exe, dll, zip, model dosyası) girmez. Motor paketlerini bakımcı Releases'e koyar.
- Gerçek bir kişinin görüntüsü ve dosyalarda kişisel yol ya da ad olmaz; göndermeden önce `python scripts/privacy_scan.py .` çalıştır.
- Python 3.10, yalnız standart kitaplık: betiklerin bağımlılığı yok.

**Kanıt etiketleri** (PR'da ve belgelerde kullan): **[ölçtüm]** çalıştırdın, günlük ya da sayı elinde; **[okudum]** bir dosya ya da belgede okudun (yolunu yaz); **[hesap]** ölçülen sayılardan türetildi; **[kullanıcı bildirdi]** başkası bildirdi, tekrarlanmadı; **[tahmin]** denenmedi. Çalıştırmadığın şey için "çalışır" yazma; etiketli tahmin makbuldür. Bu depoda aynı fikirler "measured on ...", "not tested" ve "community test" olarak geçer.

**Tek dil yeter.** İngilizce ya da Türkçe yaz (elindeki dil neyse o da olur). Değişiklik bir bölüme dokunuyorsa diğer dili bakımcı yazar. README içeriği için `README.md`'yi (İngilizce kaynak) düzenle; çeviriler bakımcılar tarafından birlikte güncellenir. Lisans ve güvenlik metninde her dilde İngilizce esastır.

**Commit e-postan.** Commit'teki e-posta geçmişte kalıcıdır. Gizli kalması için GitHub no-reply adresini kullan: GitHub > Settings > Emails > "Keep my email addresses private", sonra `git config user.email "<ID>+<kullanici>@users.noreply.github.com"` (ID aynı sayfada yazar). Başka adresli commit de kabul edilir.

**Soru ve sonuç:** [Discussions](https://github.com/alexturkey/z-image-turbo-pascal-4gb/discussions). **Güvenlik açığı:** herkese açık issue açma; [`SECURITY.md`](SECURITY.md)'deki özel bildirim yolunu kullan.
Katılarak [Davranış Kuralları](CODE_OF_CONDUCT.md)'na uymayı kabul edersin. Katkılar deponun Apache-2.0 lisansı altındadır; `patches/` altındaki katkılar MIT'tir.
