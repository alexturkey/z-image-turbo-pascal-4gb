# Türkçe (tr): yerelleştirme notları

Yazan: Sonnet-T, 2026-11-14   Okuyan: bekliyor (Fable)   Durum: ilk taslak; okuma bulguları gelince güncellenecek.
Bu dosya öteki diller için örnektir: aynı başlıklar, kısa, kararlar gerekçesiyle.

## Hitap ve ton
- Hitap: "sen" (samimi, tek kişiye). Türkiye'deki geliştirici README'lerinde ve projenin kendi CONTRIBUTING metninde ("Hoş geldin") böyle. Emir kipi yerine öneri tonu ("önce onu dene", "kapat").
- Üslup: sade, sakin, kaynaklı. Reklam dili yok ("harika", "inanılmaz" kullanılmaz). Sınırlar sonuçlar kadar görünür.

## Terimler (bu README'de hep aynı karşılık)
| English | Burada kullanılan | Not |
|---|---|---|
| text-to-image | metinden görüntü üretimi | "text-to-image" bilinen bir terim ama ilk cümlede açıklayıcı Türkçesi daha iyi |
| GPU memory (VRAM) | GPU belleği, ekran kartı belleği; "VRAM" yalnız alıntıda | Türk geliştiriciler "VRAM" der; alıntı ve model kartı cümlesi İngilizce kaldığı için orada VRAM geçer |
| tile (VAE tile) | karo | |
| seed | tohum | |
| prompt | istem | "prompt" da yaygın; "istem" projenin diğer Türkçe belgelerinde zaten kullanılıyor |
| quantization | nicemleme | |
| refiner | iyileştirici (refiner) | ilk geçişte parantezle |
| latent | latent | çevrilmez, yazılı hâliyle kullanılır |
| pixel for pixel | piksel piksel | |
| measured / not tested | ölçüldü / denenmedi | "test edilmedi" yerine "denenmedi": ölçmediğimizi değil çalıştırmadığımızı söyler |
| setup / install | kurulum | betik adı `setup.py` aynen kalır |
| open (source) | açık | "açık kaynak" yalnız lisans bağlamında |
| unofficial | gayriresmî | |

## Kaçınılanlar
- "Devrim niteliğinde", "kolay", "sihirli" gibi reklam sözleri.
- Kelimesi kelimesine "rahatça sığar" yerine kart cümlesi İngilizce alıntı + açıklamayla verildi.
- "Test edildi" kalıbı yerine "denendi/ölçüldü" ayrımı.

## Biçim
- Sayılar makine denetiminden geçer (`tests/test_readmes.py`): ondalık ayırıcı değiştirilmez. Türkçede normalde ondalık virgül yazılır (6,6), ama denetim EN'deki yazımı (6.6) birebir arar, bu yüzden nokta kalır; okuyan için sorun çıkarmaz çünkü sayılar birimli ve tablo içinde.
- Binlik ayırıcı EN'deki gibi: `10 790`, `6,577,440,704`.
- İç anahtar kelimeler (`[D3]` yer tutucuları dahil), komutlar, dosya adları, bayraklar ve adresler dokunulmadan kalır. Kod bloklarının içi çevrilmez (karar ağacı İngilizce kalır).
- `#what-it-runs` bağlantısı için başlığın üstünde açık bir bağlantı noktası var: `<a id="what-it-runs"></a>`. Başlık Türkçe olduğu için otomatik bağlantı farklı olurdu.
- Dil çubuğunda geçerli dil kalın ve bağlantısız.

## Geri çeviri denetimi
- Okuyucu ilk paragrafı İngilizceye çevirecek: <metin>; farklar: <bekliyor>
- Dört kritik bölüm (ilk paragraf, hızlı kurulum, sınırlar, lisans) için okuma: <bekliyor>

## Açık noktalar / düzeltme isteği
- "Hardware test report" sorun formunun adı İngilizce bırakıldı (form adı olduğu için, çünkü form başlığı iki dilli).
- Sayı yuvaları: `193–228` gibi yuvalar ve yanlarındaki birim (`s`, `MiB`) İngilizcedeki gibi kalır; sayıları bir betik tüm dillerde birlikte doldurur. Saniye için `sn` değil `s` yazılır (yuvayla aynı birim, SI sembolü).


## Round 2
- "Varsayılan olarak" = "varsayılan olarak kurulur"; "without payment or sign-in" = "ödeme istenmeden ve oturum açmadan" (bilerek "ücretsiz" değil); "we found no clause" = "bulamadık"; lisans cümlesi "söyler" + "gerektiğini" ile aktarıldı, üç fiil (indirmemesi, kurmaması, kullanmaması) korundu.
- Okuyucu kontrolü: üç parça ve betikle değişen iki satır (256 MiB, 581.29) okundu; düzeltme gerekmedi, kural 3'teki hiçbir şey ima edilmiyor.
