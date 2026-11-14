# Responsible use / Sorumlu kullanım

**English**

- Every image this project produces is **synthetic**. When you publish one, label it as AI-generated (in the EU this may
  also be a legal duty, for example for deepfakes: AI Act, Art. 50).
- Do not depict a **real person** in a way that could deceive, defame or harass, and never without their permission
  when the image could be taken for a real photograph of them.
- Prohibited: fraud, forged documents or evidence, disinformation, harassment, sexual content involving minors,
  intimate imagery of real people without consent, and any unlawful use. The licenses of the model files apply as
  well. The Z-Image-Turbo model card listed no extra usage terms when we read it (2026-11-14); read the model cards
  linked in [THIRD_PARTY.md](THIRD_PARTY.md) yourself before you rely on that.
- What the engine does and does not do, stated plainly: it writes the generation parameters (prompt, seed, steps) into
  the PNG text metadata. It does **not** embed an invisible watermark and it has **no** content filter. Do not claim
  otherwise in forks.
- Everything runs on your own computer. The scripts send no prompt, image or usage data anywhere; the only network
  access is the downloads listed in `models.lock.json` during setup.
- The software is provided "as is" (Apache-2.0 §7-8). You are responsible for the content you generate and how you use it.
- To report misuse of this project, use the private reporting route in [SECURITY.md](SECURITY.md).

**Türkçe**

- Bu projenin ürettiği her resim **yapaydır**. Yayımlarken yapay zekâ ürünü olduğunu belirtin (AB'de bu ayrıca yasal
  yükümlülük olabilir, örneğin derin sahte içerikte: Yapay Zekâ Yasası md. 50).
- **Gerçek bir kişiyi** yanıltacak, karalayacak ya da taciz edecek biçimde göstermeyin; resim o kişinin gerçek
  fotoğrafı sanılabilecekse izni olmadan asla.
- Yasaktır: dolandırıcılık, sahte belge ya da delil, dezenformasyon, taciz, çocukları içeren cinsel içerik, gerçek
  kişilerin rızası olmadan mahrem görüntüsü ve her türlü yasa dışı kullanım. Model dosyalarının lisansları da
  geçerlidir. Z-Image-Turbo model kartında okuduğumuz gün (2026-11-14) ek kullanım koşulu yazmıyordu; buna dayanmadan
  önce [THIRD_PARTY.md](THIRD_PARTY.md) içindeki model kartlarını kendiniz okuyun.
- Motorun yaptığı ve yapmadığı, açıkça: üretim parametrelerini (istem, tohum, adım) PNG'nin metin bilgisine yazar.
  Görünmez filigran (watermark) **gömmez** ve içerik süzgeci **yoktur**. Çatallarda (fork) aksini iddia etmeyin.
- Her şey kendi bilgisayarınızda çalışır. Betikler istem, resim ya da kullanım verisi göndermez; tek ağ erişimi kurulum
  sırasında `models.lock.json` içinde yazılı indirmelerdir.
- Yazılım olduğu gibi sunulur (Apache-2.0 §7-8); ürettiğiniz içerikten ve kullanımından siz sorumlusunuz.
- Bu projenin kötüye kullanıldığını görürseniz [SECURITY.md](SECURITY.md)'deki özel bildirim yolunu kullanın.
