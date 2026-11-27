[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · **Suomi** · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**Z-Image-Turbo (Q8_0 GGUF) tekstistä kuvaksi (text-to-image) koossa 768x1344 4 GB:n GTX 1050 Ti -näytönohjaimella (Pascal, sm_61), stable-diffusion.cpp:llä, Windowsissa.** Mitattu kannettavalla, jossa on 16 GB RAM-muistia ja jossa prosessi käyttää noin 11 GB RAM-muistia. Sama siemenluku (seed) antaa samat pikselit, pikseli pikseliltä; mittaukset ja moottorin patchit on julkaistu, lataukset on lukittu sha256-tiivisteillä, ja tekoälyavusteinen koodausagentti voi tehdä asennuksen vaihe vaiheelta.

*Epävirallinen. Ei ole sidoksissa Tongyi-MAI:hin (Z-Image), leejetiin (stable-diffusion.cpp) eikä NVIDIAan.*

> **Käytätkö tekoälykoodausagenttia (Codex, Claude Code, Gemini, Cursor)?** Anna sille tämä yksi lause: ”Lue `AGENTS_HIZLI.md` loppuun asti, aja ensin `python scripts/tani.py`, pidä edistymisesi kirjaa tiedostossa `DURUM.md` ja kysy minulta ennen kuin poistat tai siirrät mitään, muutat järjestelmän Pythonia tai PATHia tai laskat laatuasetusta.” Agentti diagnosoi tämän tietokoneen, kirjoittaa tarkistuslistan ja kysyy sinulta jokaisessa päätöksessä.

## Aloita tästä

Valmis paketti on olemassa, joten kokeile sitä ensin. Jos laitteistosi on erilainen tai jokin vaihe epäonnistuu, kaikki muu on avoinna: patchit, buildausohje ja mittaukset ovat tässä repositoriossa, joten voit tehdä buildin omalle kortillesi tai muokata niitä.

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

Vaihe 2 lataa noin 12.2 GB ja kesti 29 minuuttia yhden kerran, meidän yhteydellämme; se tulostaa ensin "Preflight"-lohkon (oma GPU:si, RAM-muistisi ja vapaa levytilasi meidän mittaustemme vieressä; se vain kertoo).
Mitattiin vain GTX 1050 Ti 4 GB:n kannettavan kortti (Pascal, compute capability 6.1). Muita kortteja ei testattu.
Jos käytät tekoälyavusteista koodausagenttia (Claude Code, Codex, Cursor ja vastaavat), ohjaa se tiedostoon [`AGENTS.md`](AGENTS.md).

## Yhdellä silmäyksellä

Verrattuna v0.1.0-rakenteeseen: yksi kuva vie 188–193 s eikä 261.6 s, VAE-vaihe vie 12.5–21.7 s eikä 29.8–36.3 s, sama siemenluku antaa samat pikselit, ja jokaisen tämän README:n luvun takana on komento ja tiedosto.

768x1344, siemenluku 42, 8 askelta, sama kone. v0.1.0:n luvut ovat v0.1.0:n README:stä (puhtaan juuren testi ja viisi ajoa); v0.3.0:n luvut ovat tämän julkaisun puhtaan juuren testistä.

| | v0.1.0 (ei koskaan julkaistu; vanha rakenne) | v0.3.0 |
|---|---|---|
| Aika yhteen kuvaan (yksi `generate.py`-ajo) | 261.6 s | 188–193 s |
| VAE-dekoodaus (viimeinen vaihe) | 29.8–36.3 s | 12.5–21.7 s |
| Läheisyys vertailudekoodaukseen (PSNR, suurempi on parempi) | 38–43 dB | 71–73 dB |
| GPU-muistin huippu (nvidia-smi) | 2949–2957 MiB | 3057–3059 MiB |
| Prosessin muisti, huippu | 10.5–10.9 GB (sellaisena kuin silloin kirjattiin) | 10 489–11 203 MiB |
| Pienin havaittu vapaa RAM | 331–576 MiB | 303–532 MiB |

Näin luku luetaan: vertailukohta on sama latent, joka on dekoodattu suorittimella yhtenä float32-kappaleena; PSNR vertaa GPU-dekoodaustamme siihen (3 kuvaa). Se kertoo, kuinka lähellä VAE-vaihe on tätä vertailukohtaa. Se ei kerro, miltä kuva näyttää tai kuinka hyvä se on. v0.2.0:n kuvat eivät ole tavu tavulta samat kuin v0.1.0:n samalla kehotteella ja siemenluvulla, koska VAE-polkua muutettiin tarkoituksella. Menetelmä ja mittaamattomat osat: [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md).

## Esimerkkejä

**Tekoälyllä tällä repositoriolla tehty** (Z-Image-Turbo Q8_0, siemenluku 42, 8 askelta). Nämä eivät ole oikeita valokuvia; nähtävyydet ja yksityiskohdat
voivat olla epätarkkoja, eikä kuva aina noudata kehotettaan kaikissa yksityiskohdissa. Tarkat kehotteet ovat hakemistossa [`prompts/`](prompts) ja tiedostossa [`docs/PROMPTS.md`](docs/PROMPTS.md).

| | | |
|---|---|---|
| ![Eiffel-torni kultaisena hetkenä](docs/examples/eiffel.jpg) | ![Turkkilainen teelasi](docs/examples/turkish_tea.jpg) | ![Iäkäs kalastaja](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![Kylä rinteellä](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![Istanbul ilmasta nähtynä](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. Ei oikea valokuva; nähtävyydet voivat olla epätarkkoja.

## Pika-aloitus

Vaatimukset: Windows 10/11, NVIDIA-näytönohjain, jossa on 4 GB, ajuri, joka tukee CUDA 12.8:aa (ajuri 581.29 mitattiin; vanhempia ajureita ei testattu; itse CUDA-runtime ladataan puolestasi), Python 3.10 tai uudempi,
git, noin 14 GB vapaata levytilaa (lataukset ovat noin 12.2 GB cuDNN:n kanssa; vapaan levytilan luku on arvio) ja 16 GB RAM-muistia (mitattu määrä; vähemmän ei ole testattu).

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- `setup.py` tulostaa ensin "Preflight"-lohkon (oma GPU:si, RAM-muistisi ja vapaa levytilasi meidän mittaustemme vieressä; se vain kertoo eikä koskaan estä). Sen jälkeen se lataa tiedostot tiedoston [`models.lock.json`](models.lock.json) lukituista osoitteista ja tarkistaa jokaisen tiedoston sha256:lla. Se tulostaa `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK`, sitten `CUDNN_OK` tai `CUDNN_SKIPPED` ja lopuksi `SETUP_OK`.
  Ilman `--models-dir`- ja `--bin-dir`-valitsimia se käyttää repositorion juuren hakemistoja `models/` ja `bin/`; laita mallit SSD-levylle (vain SSD mitattiin).
  Sen voi keskeyttää milloin tahansa Ctrl+C:llä ja ajaa saman komennon uudelleen: lataukset jatkuvat `.part`-tiedostoista.
- **cuDNN asennetaan oletuksena, eikä se kuulu tähän repositorioon.** Se on NVIDIAn ohjelmisto NVIDIAn omalla lisenssillä ([lisenssin teksti](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)), NVIDIA-näytönohjaimilla varustetuille järjestelmille. Se ladataan NVIDIAn palvelimelta ilman, että maksua pyydetään, ja ilman kirjautumista tilille, emmekä löytäneet lisenssista ehtoa, joka rajoittaisi kaupallista tai henkilökohtaista käyttöä. `setup.py` näyttää lisenssin osoitteen, lataa tiedoston ja kopioi vain kahdeksan DLL-tiedostoa `sd-cli.exe`:n viereen. NVIDIAn lisenssi sanoo, että se, joka ei hyväksy sen ehtoja, ei saa ladata, asentaa tai käyttää sitä; siinä tapauksessa aja `python scripts/setup.py --no-cudnn`. Ilman cuDNN:ää kaikki toimii hitaammalla v0.1.0:n VAE-polulla (`--vae legacy`), ja `generate.py` kertoo siitä.
- `generate.py` kirjoittaa `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, `run.json` (aika, vaiheet, mikä VAE-polku ajettiin, GPU-muistin huippu, tarkka komento) ja `log.txt`, ja tulostaa `IMAGE_OK <path>`.

## Käyttö

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| Valitsin | Merkitys |
|---|---|
| `--prompt "<text>"` tai `--prompt-file <txt>` | kehote (toinen kahdesta vaaditaan) |
| `--width`, `--height` | 16:n monikerrat, 256–2048; oletus 768x1344; testattu: 768x1344, 1344x768, 1024x1024 |
| `--seed` | oletus 42 |
| `--out`, `--name` | tulostushakemiston juuri (oletus `outputs/`) ja lyhyt nimi ajon hakemistolle |
| `--models-dir`, `--bin-dir` | minne `setup.py` laittoi mallit ja moottorin |
| `--vae auto` (oletus) | cuDNN float32; kokeilee ensin yhtä kappaletta, sitten kahta isoa laattaa (tile), sitten pientä oletuslaattaa |
| `--vae tiled` | cuDNN float32, aina kaksi isoa laattaa |
| `--vae legacy` | v0.1.0:n polku: ei cuDNN:ää, pienet laatat. Käytetään automaattisesti (varoituksen kera), kun cuDNN:n DLL-tiedostot puuttuvat |

Askeleet (8), cfg (1.0), sampler ja scheduler on lukittu tarkoituksella; katso [Mitä se ajaa](#what-it-runs).

## Tarkista itse

- `generate.py` tulostaa `PIXEL_SHA256 <hex>` yhtenä viimeisistä riveistään: tiiviste dekoodatuista pikseleistä. Aja sama komento kahdesti ja vertaa kahta kuvaa: `python scripts/compare.py <run A>/image.png <run B>/image.png` pitäisi tulostaa `SAME_PIXELS`.
- Viiden esimerkin `PIXEL_SHA256` meidän koneellamme on tiedostossa [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md). PNG-tiedoston tiedostotiiviste voi poiketa, vaikka pikselit olisivat samat, koska PNG sisältää luontiparametrit tekstinä; vertaa pikseleitä, ei tiedostoja.
- Rehellinen rajoitus: emme mitanneet, antaako toinen kortti tai ajuri samat pikselit.

## Miksi tämä mahtuu 4 GB:iin

- **Mitä mallin tekijät sanovat.** Z-Image-Turbon mallikortti (model card) sanoo, että malli "fits comfortably within 16G VRAM consumer devices" ([model card](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)), eli mahtuu mukavasti kuluttajalaitteisiin, joissa on 16 GB VRAM-muistia. Se on väite 16 GB:n korteista. Virallinen README mainitsee myös stable-diffusion.cpp:n kolmannen osapuolen vaihtoehtona ja siteeraa sitä lauseella "as little as 4GB of VRAM" ([README](https://github.com/Tongyi-MAI/Z-Image)), eli "vain 4 GB VRAM-muistia"; se on stable-diffusion.cpp-projektin väite, ei Z-Image-tiimin vaatimus.
- **Mitä mittasimme.** Z-Image-Turbo Q8_0 (6.6 GB:n tiedosto) ja Qwen3-4B Q8_0 -tekstienkooderi, 768x1344: GPU-muistin huippu, jonka nvidia-smi näytteisti 2 s välein (lyhyt piikki voi jäädä huomaamatta), oli 2949–2957 MiB (v0.1.0-moottori) ja 3057–3059 MiB (v0.2.0-moottori) 4096 MiB:n kortilla. Painot (10 509 MiB; moottorin loki tulostaa sen muodossa MB) pysyvät järjestelmän RAM-muistissa; moottori kopioi verkon GPU:lle yksi segmentti (verkon viipale) kerrallaan: 36 segmenttiä, kuten lokirivillä `z_image using 36 segments`.
- **Mitä se maksaa.** Aikaa ja järjestelmämuistia: 188–193 s kuvaa kohden, ja moottoriprosessi pitää hallussaan noin 10 489–11 203 MiB RAM-muistia (muistikartoitetut mallisivut mukaan lukien) 16 GB:n koneella, joten vapaa RAM putoaa muutamaan sataan MiB:iin ajon aikana.
- **Muiden ratkaisut.** Muut kertovat ajaneensa Z-Imagea 4 GB:n korteilla matalammalla kvantisoinnilla tai pienemmillä koilla (esimerkiksi stable-diffusion.cpp:n wikisivu 4 GB:n korteille suosittelee Q3_K- tai Q4_0-mallia koossa 1024x512). Sieltä, mistä katsoimme (lista ja päivämäärä tiedostossa [`docs/RELATED.md`](docs/RELATED.md)), emme löytäneet julkaistua ratkaisua, joka yhdistäisi kaikki neljä: 4 GB:n kortti, Q8_0, 768x1344 tai suurempi, sekä mitattu aika ja GPU-muisti. Tämä on toteamus siitä, mistä katsoimme, ei kaikesta.
- **Kuka tekee mitä.** Mahtuminen 4 GB:iin tulee itse stable-diffusion.cpp:stä: `--offload-to-cpu`, `--mmap`, työskentely viipaleina ja flash attention (ilman sitä ajo tarvitsi 4205 MB eikä mahtunut). Meidän patchimme ovat nopeutta ja parempaa VAE-vaihetta varten, eivät mahtumista varten. Emme ajaneet muokkaamatonta upstream-moottoria tällä kortilla, joten emme voi sanoa, mahtuuko se.

## Miten se toimii

Kolme muutosta stable-diffusion.cpp:n `master-1088-32d516c`-versioon (kaikki ovat kytkimiä; taulukko tiedostossa [`patches/README.md`](patches/README.md) listaa jokaisen ympäristömuuttujineen):

1. **Refiner ajetaan kerran askelta kohden.** Ryhmän nimeä käytettiin kahdesti, joten neljä refiner-lohkoa laskettiin toisen kerran. Korjauksen jälkeen askeleet 2–8 ovat noin 1.3 s nopeampia kukin (22.0–20.7 s), ja kuva on pikselitarkasti sama (3 kuvaa tarkistettu).
2. **VAE cuDNN:n kautta, float32-tarkkuudella.** Viimeinen vaihe (latentin muuttaminen pikseleiksi) käyttää nyt NVIDIAn cuDNN:n float32-konvoluutiota. Meidän kortillamme se pudotti VAE:n ajan 23–27 s:sta 10–15 s:iin ja nosti PSNR:n vertailukohtaan nähden 38–43 dB:stä 45–49 dB:iin (isot laatat).
3. **Ensin yhtenä kappaleena.** Moottori yrittää nyt dekoodata koko kuvan yhtenä kappaleena, kun muistitarkistus sanoo sen mahtuvan (marginaali 256 MiB), putoaa kahteen isoon laattaan ja sitten pieniin laattoihin. Yhtenä kappaleena VAE vei noin 8–16 s ja PSNR vertailukohtaan nähden oli 71–73 dB. Jos pakotettu varavaihtoehto tulee käyttöön, kuvassa on samat pikselit kuin laatoilla dekoodatussa (tarkistettu `PIXEL_SHA256`:lla). Mitä tapahtui, kirjoitetaan tiedostoon `run.json` (`stages.vae_path`: `full`, `tile`, `floor` tai `retry`).

Lisäksi: `--eager-load` (lukee mallisivut etukäteen; 241.2 s -> 220.3 s samalla kuvalla, kehitysbuild, yksi ajo kummallakin) kuuluu kiinteään komentoon.

<a id="what-it-runs"></a>
## Mitä se ajaa

| Osa | Tiedosto | Lähde |
|---|---|---|
| Diffuusiomalli | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), pohja [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Tekstienkooderi | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), FLUX.1-tyyppinen autoenkooderi |
| Moottori | `sd-cli.exe`, stable-diffusion.cpp `32d516c` ja patchit hakemistossa [`patches/`](patches) | tämän repositorion v0.3.0-julkaisu (`sinirsiz-foto-engine-v0.3.0-win-x64-cuda12.8-sm61.zip`) |
| CUDA-runtime | `cudart`, `cublas`, `cublasLt` (12.8), muokkaamattomat | zip wan22-pascal-4gb:n v0.1.0-julkaisusta |
| cuDNN (asennetaan oletuksena; `--no-cudnn` ohittaa sen) | 8 DLL-tiedostoa, versio 9.10.2.21 (CUDA 11 -build) | NVIDIAn oma palvelin, NVIDIAn lisenssillä; ei säilytetä täällä |

Kiinteät asetukset: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`.
Emme vähennä askelia, lisää negatiivista kehotetta (negative prompt) emmekä ota välimuistia käyttöön: malli on tislattu (distilled) 8 askeleelle eikä käytä negatiivisia kehotteita (katso [kehotteet](docs/PROMPTS.md)).

## Rajoitukset (lue ennen kuin luotat tähän)

- **Vain Windows.** Valmiiksi käännetty moottori ja nämä skriptit toimivat vain Windowsissa.
- **Yksi kortti, yksi kone.** Mitattu vain GTX 1050 Ti 4 GB:n kannettavalla (i7-7700HQ, 16 GB RAM, Windows 10, ajuri 581.29, mallit SSD-levyllä). Muut GPU:t ja ajurit, koneet joissa on alle 16 GB RAM-muistia, Linux ja macOS: **ei testattu**.
- Muut näytönohjaimet ja järjestelmät (mikä polku on olemassa, sekä yhteisön testi AMD-kortilla Linuxissa, jota emme itse ajaneet): [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md).
- **Moottori on käännetty vain Pascalille (sm_61).** Muut arkkitehtuurit tarvitsevat oman buildin ([`docs/BUILD.md`](docs/BUILD.md)); emme testanneet sellaista.
- **cuDNN:** mittasimme cuDNN 9.10.2.21:n CUDA 11 -buildilla. CUDA 12 -buildissa on eri tiedostot, eikä sitä mitattu.
- **Muisti on tiukalla.** Vapaa RAM putoaa muutamaan sataan MiB:iin; sulje muut ohjelmat ja aja yksi kuva kerrallaan. Emme ole nähneet GPU-muistin loppuvan sen jälkeen, kun moottorin muistitarkistus meni läpi, emmekä testanneet, mitä silloin tapahtuu.
- **Koot:** vain 768x1344, 1344x768 ja 1024x1024 testattiin. Suuremmat koot tulostavat varoituksen ja voivat jäädä ilman muistia.
- Kehotteen noudattaminen on osittaista: kuva ei aina noudata kehotettaan kaikissa yksityiskohdissa. Kuvien sisällä olevaa tekstiä ja oikeita nähtävyyksiä ei arvioitu.
- PSNR:n vertailukohta on oman moottorimme suorittimella tekemä dekoodaus, ei riippumaton toteutus.
- Tiedoston [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) luvut ovat kukin yhdestä ajosta, ellei toisin mainita.

## Lisenssi ja maininta

- Tämän repositorion skriptit ja dokumentit: [Apache-2.0](LICENSE) ja [`NOTICE`](NOTICE)-tiedosto. Moottorin patchit hakemistossa [`patches/`](patches) ovat MIT-lisensoituja, kuten koodikin, jota ne muokkaavat.
- stable-diffusion.cpp ja ggml ovat MIT-lisensoituja. Moottoriin käännetyn kolmannen osapuolen koodin ilmoitukset ovat hakemistossa [`licenses/`](licenses) ja tiedostossa [`THIRD_PARTY.md`](THIRD_PARTY.md).
- Mallitiedostoja ei säilytetä täällä; ne ladataan yllä mainituista lähteistä niiden omilla lisensseillä (Hugging Face ilmoittaa kaikille Apache-2.0:n, luettu 2026-11-13). Mallikortti ei sano mitään siitä, kuka omistaa luodut kuvat, emmekä me väitä asiasta mitään.
- **cuDNN ja CUDA-runtime ovat NVIDIAn omaisuutta**, eikä tämän repositorion lisenssi koske niitä. cuDNN ladataan NVIDIAn palvelimelta NVIDIAn lisenssillä (`--no-cudnn` ohittaa sen); CUDA-runtimen DLL-tiedostot ovat erillisessä muokkaamattomassa zipissä (CUDA Toolkit EULA, Attachment A). Yksityiskohdat ja se, mitä emme voineet varmistaa: [`THIRD_PARTY.md`](THIRD_PARTY.md).
- **Maininta.** `NOTICE`-tiedoston säilyttäminen kopioiden ja johdannaisteosten mukana on ehto (Apache-2.0, kohta 4). Sen lisäksi rivi, kuten "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey", otetaan ilolla vastaan, mutta sitä ei vaadita.
- Lue [`ETHICS.md`](ETHICS.md): jokainen kuva on synteettinen, ja vastaat itse siitä, mitä julkaiset.

## Osallistuminen

Hyödyllisintä, mitä voit tehdä, on **testata oma korttisi** ja kertoa meille, mitä tapahtui: GPU:n nimi, ajuri, RAM, `run.json` ja lokin viimeiset rivit (issue-lomake "Hardware test report"). Korjaukset dokumentteihin ja skripteihin ovat myös tervetulleita; katso [`CONTRIBUTING.md`](CONTRIBUTING.md). Tietoturvailmoitukset menevät [`SECURITY.md`](SECURITY.md)-tiedostossa kuvatun yksityisen reitin kautta.

[Asennusopas tekoälyagenteille](AGENTS.md) · [Mittaukset](docs/MEASUREMENTS.md) · [Vianetsintä](docs/TROUBLESHOOTING.md) · [Moottorin buildaus](docs/BUILD.md) · [Patchit](patches/README.md) · [Kehotteet](docs/PROMPTS.md) · [Kolmannen osapuolen](THIRD_PARTY.md) · [Muutosloki](CHANGELOG.md)

Tämä sivu on lokalisoitu tekoälyn avulla; korjaukset ovat erittäin tervetulleita, katso [CONTRIBUTING.md](CONTRIBUTING.md).
