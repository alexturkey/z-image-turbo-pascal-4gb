[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · **Nederlands** · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**Tekst-naar-beeld met Z-Image-Turbo (Q8_0 GGUF) op 768x1344 op een GTX 1050 Ti met 4 GB (Pascal, sm_61), met stable-diffusion.cpp, op Windows.** Gemeten op een laptop met 16 GB RAM, waarop het proces ongeveer 11 GB RAM gebruikt. Dezelfde seed geeft dezelfde pixels, pixel voor pixel; de metingen en de engine-patches zijn openbaar, de downloads liggen vast met sha256, en een AI-codeeragent kan het stap voor stap installeren.

*Onofficieel. Niet verbonden aan Tongyi-MAI (Z-Image), leejet (stable-diffusion.cpp) of NVIDIA.*

> **Gebruikt u een AI-codeeragent (Codex, Claude Code, Gemini, Cursor)?** Geef hem deze ene zin: “Lees `AGENTS_HIZLI.md` helemaal uit, voer eerst `python scripts/tani.py` uit, houd je voortgang bij in `DURUM.md` en vraag het me voordat je iets verwijdert of verplaatst, het systeem-Python of PATH wijzigt of een kwaliteitsinstelling verlaagt.” De agent diagnosticeert deze pc, schrijft een checklist en vraagt u bij elke beslissing om akkoord.

## Begin hier

Er is een kant-en-klaar pakket, probeer dat dus eerst. Als je hardware anders is of een stap mislukt, ligt de rest open: de patches, het bouwrecept en de metingen staan in deze repository, dus je kunt voor je eigen kaart bouwen of ze aanpassen.

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

Stap 2 downloadt ongeveer 12.2 GB en duurde bij ons één keer 29 minuten, op onze verbinding; hij toont eerst een "Preflight"-blok (je GPU, RAM en vrije schijfruimte naast wat wij hebben gemeten; het informeert alleen).
Alleen de GTX 1050 Ti 4 GB laptopkaart (Pascal, compute capability 6.1) is gemeten. Andere kaarten zijn niet getest.
Gebruik je een AI-codeeragent (Claude Code, Codex, Cursor en dergelijke), verwijs hem dan naar [`AGENTS.md`](AGENTS.md).

## In één oogopslag

Ten opzichte van de opzet van v0.1.0: een afbeelding duurt 188–193 s in plaats van 261.6 s, de VAE-fase duurt 12.5–21.7 s in plaats van 29.8 tot 36.3 s, dezelfde seed geeft dezelfde pixels, en achter elk getal in deze README staan een commando en een bestand.

768x1344, seed 42, 8 stappen, dezelfde machine. De getallen van v0.1.0 komen uit de README van v0.1.0 (clean-root-test en vijf runs); de getallen van v0.3.0 komen uit de clean-root-test van deze release.

| | v0.1.0 (nooit gepubliceerd; oude opzet) | v0.3.0 |
|---|---|---|
| Tijd voor één afbeelding (één run van `generate.py`) | 261.6 s | 188–193 s |
| VAE-decodering (laatste fase) | 29.8 tot 36.3 s | 12.5–21.7 s |
| Nabijheid tot een referentiedecodering (PSNR, hoger is dichterbij) | 38 tot 43 dB | 71 tot 73 dB |
| GPU-geheugen, piek (nvidia-smi) | 2949 tot 2957 MiB | 3057–3059 MiB |
| Procesgeheugen, piek | 10.5 tot 10.9 GB (zoals toen vastgelegd) | 10 489–11 203 MiB |
| Laagste vrije RAM gezien | 331 tot 576 MiB | 303–532 MiB |

Zo lees je dit: de referentie is dezelfde latent, op de CPU in één stuk als float32 gedecodeerd; de PSNR vergelijkt onze GPU-decodering daarmee (3 afbeeldingen). Hij zegt hoe dicht de VAE-fase bij die referentie ligt. Hij zegt niet hoe goed een afbeelding eruitziet. De afbeeldingen van v0.2.0 zijn bij dezelfde prompt en seed niet byte voor byte gelijk aan die van v0.1.0, omdat het VAE-pad met opzet is veranderd. Methode en het niet gemeten deel: [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md).

## Voorbeelden

**Met deze repo door AI gemaakt** (Z-Image-Turbo Q8_0, seed 42, 8 stappen). Dit zijn geen echte foto's; bekende bouwwerken en details
kunnen onjuist zijn, en een afbeelding volgt zijn prompt niet altijd in elk detail. De exacte prompts staan in [`prompts/`](prompts) en [`docs/PROMPTS.md`](docs/PROMPTS.md).

| | | |
|---|---|---|
| ![Eiffeltoren in het gouden uur](docs/examples/eiffel.jpg) | ![Turks theeglas](docs/examples/turkish_tea.jpg) | ![Oudere visser](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![Dorp op een heuvelhelling](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![Istanbul vanuit de lucht](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. Geen echte foto; bekende bouwwerken kunnen onjuist zijn.

## Snelstart

Vereisten: Windows 10/11, een NVIDIA-GPU met 4 GB, een driver die CUDA 12.8 ondersteunt (driver 581.29 is gemeten; oudere drivers zijn niet getest; de CUDA-runtime zelf wordt voor je gedownload), Python 3.10 of nieuwer,
git, ongeveer 14 GB vrije schijfruimte (de downloads zijn met cuDNN ongeveer 12.2 GB; het getal voor vrije schijfruimte is een schatting) en 16 GB RAM (wat is gemeten; minder is niet getest).

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- `setup.py` toont eerst een "Preflight"-blok (je GPU, RAM en vrije schijfruimte naast wat wij hebben gemeten; het informeert alleen en blokkeert nooit). Daarna downloadt het van de vastgelegde adressen in [`models.lock.json`](models.lock.json) en controleert het elk bestand met sha256. Het toont `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK`, dan `CUDNN_OK` of `CUDNN_SKIPPED`, en ten slotte `SETUP_OK`.
  Zonder `--models-dir` en `--bin-dir` gebruikt het `models/` en `bin/` in de hoofdmap van de repo; zet de modellen op een SSD (alleen een SSD is gemeten).
  Je kunt het altijd stoppen met Ctrl+C en hetzelfde commando opnieuw uitvoeren: downloads gaan verder vanaf de `.part`-bestanden.
- **cuDNN wordt standaard geïnstalleerd en maakt geen deel uit van deze repository.** Het is NVIDIA-software onder de eigen licentie van NVIDIA ([licentietekst](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)), voor systemen met NVIDIA-GPU's. Het wordt van de server van NVIDIA gedownload zonder dat er betaling wordt gevraagd en zonder inloggen, en we hebben in de licentie geen bepaling gevonden die het commerciële of persoonlijke gebruik beperkt. `setup.py` toont het adres van de licentie, downloadt het bestand en kopieert slechts acht DLL's naast `sd-cli.exe`. In de licentie van NVIDIA staat dat wie de voorwaarden niet accepteert het niet mag downloaden, installeren of gebruiken; voer in dat geval `python scripts/setup.py --no-cudnn` uit. Zonder cuDNN werkt alles met het tragere VAE-pad van v0.1.0 (`--vae legacy`), en `generate.py` meldt dat.
- `generate.py` schrijft `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, `run.json` (tijd, fasen, welk VAE-pad liep, piek van het GPU-geheugen, het exacte commando) en `log.txt`, en toont `IMAGE_OK <path>`.

## Gebruik

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| Optie | Betekenis |
|---|---|
| `--prompt "<text>"` of `--prompt-file <txt>` | de prompt (een van de twee is verplicht) |
| `--width`, `--height` | veelvouden van 16, 256 tot 2048; standaard 768x1344; getest: 768x1344, 1344x768, 1024x1024 |
| `--seed` | standaard 42 |
| `--out`, `--name` | hoofdmap van de uitvoer (standaard `outputs/`) en een korte naam voor de runmap |
| `--models-dir`, `--bin-dir` | waar `setup.py` de modellen en de engine heeft neergezet |
| `--vae auto` (standaard) | cuDNN float32; eerst in één stuk, dan twee grote tegels, dan de kleine standaardtegel |
| `--vae tiled` | cuDNN float32, altijd twee grote tegels |
| `--vae legacy` | het pad van v0.1.0: geen cuDNN, kleine tegels. Wordt automatisch (met een waarschuwing) gebruikt als de cuDNN-DLL's ontbreken |

Stappen (8), cfg (1.0), sampler en scheduler liggen met opzet vast; zie [Wat het draait](#what-it-runs).

## Controleer het zelf

- `generate.py` toont als een van de laatste regels `PIXEL_SHA256 <hex>`: een hash van de gedecodeerde pixels. Voer hetzelfde commando twee keer uit en vergelijk de twee afbeeldingen: `python scripts/compare.py <run A>/image.png <run B>/image.png` hoort `SAME_PIXELS` te tonen.
- De `PIXEL_SHA256` van de vijf voorbeelden op onze machine staat in [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md). De bestandshash van een PNG kan verschillen terwijl de pixels gelijk zijn, omdat de PNG de generatieparameters als tekst bevat; vergelijk pixels, geen bestanden.
- Eerlijke grens: we hebben niet gemeten of een andere kaart of driver dezelfde pixels geeft.

## Waarom het in 4 GB past

- **Wat de modelmakers zeggen.** De modelkaart van Z-Image-Turbo zegt dat het model "fits comfortably within 16G VRAM consumer devices" (past comfortabel op consumentenkaarten met 16 GB VRAM) ([modelkaart](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)). Dat is een uitspraak over kaarten van 16 GB. De officiële README noemt stable-diffusion.cpp bovendien als optie van een derde partij en citeert het met "as little as 4GB of VRAM" (met maar 4 GB VRAM) ([README](https://github.com/Tongyi-MAI/Z-Image)); dat is een bewering van het project stable-diffusion.cpp, geen eis van het Z-Image-team.
- **Wat wij hebben gemeten.** Z-Image-Turbo Q8_0 (een bestand van 6.6 GB) met een Qwen3-4B Q8_0 tekstencoder, 768x1344: de GPU-piek, elke 2 s bemonsterd door nvidia-smi (een korte piek kan gemist worden), was 2949 tot 2957 MiB (engine v0.1.0) en 3057–3059 MiB (engine v0.2.0) op een kaart van 4096 MiB. De gewichten (10 509 MiB; het engine-log toont dat als MB) blijven in het systeemgeheugen; de engine kopieert het netwerk telkens één segment (een deel van het netwerk) tegelijk naar de GPU: 36 segmenten, zoals in de logregel `z_image using 36 segments`.
- **Wat het kost.** Tijd en systeemgeheugen: 188–193 s per afbeelding, en het engine-proces houdt op een machine van 16 GB ongeveer 10 489–11 203 MiB RAM vast (inclusief via memory-mapping ingeladen modelpagina's), waardoor het vrije RAM tijdens de run zakt tot een paar honderd MiB.
- **Opzetten van anderen.** Anderen melden Z-Image op kaarten van 4 GB met lagere kwantisatie of kleinere formaten (de wikipagina van stable-diffusion.cpp voor kaarten van 4 GB raadt bijvoorbeeld Q3_K of Q4_0 aan bij 1024x512). Waar wij hebben gezocht (lijst en datum in [`docs/RELATED.md`](docs/RELATED.md)) vonden we geen gepubliceerde opzet die alle vier combineert: een kaart van 4 GB, Q8_0, 768x1344 of groter, en gemeten tijd en GPU-geheugen. Dat is een uitspraak over waar wij hebben gezocht, niet over overal.
- **Wie wat doet.** Dat het in 4 GB past, komt van stable-diffusion.cpp zelf: `--offload-to-cpu`, `--mmap`, werken in delen en flash attention (zonder flash attention had een run 4205 MB nodig en paste het niet). Onze patches zijn voor snelheid en voor een betere VAE-fase, niet om te passen. De ongepatchte upstream-engine hebben we op deze kaart niet gedraaid, dus we kunnen niet zeggen of die past.

## Hoe het werkt

Drie wijzigingen bovenop stable-diffusion.cpp `master-1088-32d516c` (het zijn allemaal schakelaars; de tabel in [`patches/README.md`](patches/README.md) toont ze stuk voor stuk met hun omgevingsvariabele):

1. **De refiner draait één keer per stap.** Een groepsnaam werd twee keer gebruikt, waardoor vier refiner-blokken een tweede keer werden berekend. Met de fix zijn stap 2 tot 8 elk ongeveer 1.3 s sneller (22.0 naar 20.7 s), met een pixelgelijke afbeelding (3 afbeeldingen gecontroleerd).
2. **VAE via cuDNN, in float32.** De laatste fase (de latent omzetten in pixels) gebruikt nu de float32-convolutie van NVIDIA cuDNN. Op onze kaart bracht dat de VAE van 23 tot 27 s terug naar 10 tot 15 s en verhoogde het de PSNR ten opzichte van de referentie van 38 tot 43 dB naar 45 tot 49 dB (grote tegels).
3. **Eerst in één stuk.** De engine probeert nu de hele afbeelding in één stuk te decoderen als de geheugencontrole zegt dat het past (marge 256 MiB), valt anders terug op twee grote tegels en daarna op kleine tegels. In één stuk duurde de VAE ongeveer 8–16 s en lag de PSNR ten opzichte van de referentie op 71 tot 73 dB. Als er een geforceerde terugval plaatsvindt, heeft de afbeelding dezelfde pixels als die met tegels (gecontroleerd met `PIXEL_SHA256`). Wat er gebeurde, staat in `run.json` (`stages.vae_path`: `full`, `tile`, `floor` of `retry`).

Verder: `--eager-load` (leest de modelpagina's vooraf in; 241.2 s naar 220.3 s op dezelfde afbeelding, ontwikkelbuild, telkens één run) maakt deel uit van het vaste commando.

<a id="what-it-runs"></a>
## Wat het draait

| Onderdeel | Bestand | Bron |
|---|---|---|
| Diffusiemodel | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), basis [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Tekstencoder | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), autoencoder van het type FLUX.1 |
| Engine | `sd-cli.exe`, stable-diffusion.cpp `32d516c` met de patches in [`patches/`](patches) | de release v0.3.0 van deze repository (`sinirsiz-foto-engine-v0.3.0-win-x64-cuda12.8-sm61.zip`) |
| CUDA-runtime | `cudart`, `cublas`, `cublasLt` (12.8), ongewijzigd | zip uit de release v0.1.0 van wan22-pascal-4gb |
| cuDNN (standaard geïnstalleerd; `--no-cudnn` slaat het over) | 8 DLL's, versie 9.10.2.21 (CUDA 11-build) | de eigen server van NVIDIA, onder de licentie van NVIDIA; hier niet opgeslagen |

Vaste instellingen: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`.
We verlagen de stappen niet, voegen geen negatieve prompt toe en zetten caching niet aan: het model is gedistilleerd voor 8 stappen en gebruikt geen negatieve prompts (zie [prompts](docs/PROMPTS.md)).

## Beperkingen (lees dit voordat je erop vertrouwt)

- **Alleen Windows.** De kant-en-klare engine en deze scripts zijn alleen voor Windows.
- **Eén kaart, één machine.** Alleen gemeten op een laptop met GTX 1050 Ti 4 GB (i7-7700HQ, 16 GB RAM, Windows 10, driver 581.29, modellen op een SSD). Andere GPU's en drivers, machines met minder dan 16 GB RAM, Linux en macOS: **niet getest**.
- Andere kaarten en systemen (welke weg er is, en een communitytest op een AMD-kaart onder Linux die we niet zelf hebben uitgevoerd): [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md).
- **De engine is alleen voor Pascal (sm_61) gebouwd.** Andere architecturen vragen een eigen build ([`docs/BUILD.md`](docs/BUILD.md)); wij hebben er geen getest.
- **cuDNN:** we hebben gemeten met de CUDA 11-build van cuDNN 9.10.2.21. De CUDA 12-build heeft andere bestanden en is niet gemeten.
- **Het geheugen is krap.** Het vrije RAM zakt tot een paar honderd MiB; sluit andere programma's en maak één afbeelding tegelijk. We hebben niet gezien dat het GPU-geheugen opraakte nadat de geheugencontrole van de engine was gepasseerd, en we hebben niet getest wat er dan gebeurt.
- **Formaten:** alleen 768x1344, 1344x768 en 1024x1024 zijn getest. Grotere formaten geven een waarschuwing en kunnen het geheugen overschrijden.
- De trouw aan de prompt is gedeeltelijk: een afbeelding volgt zijn prompt niet altijd in elk detail. Tekst in afbeeldingen en bestaande bouwwerken zijn niet beoordeeld.
- De PSNR-referentie is de CPU-decodering van onze eigen engine, geen onafhankelijke implementatie.
- De getallen in [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) komen, tenzij er anders staat, uit telkens één run.

## Licentie en naamsvermelding

- De scripts en documenten van deze repository: [Apache-2.0](LICENSE) met een [`NOTICE`](NOTICE)-bestand. De engine-patches in [`patches/`](patches) zijn MIT, net als de code die ze wijzigen.
- stable-diffusion.cpp en ggml zijn MIT. De vermeldingen voor de code van derden die in de engine is gecompileerd, staan in [`licenses/`](licenses) en [`THIRD_PARTY.md`](THIRD_PARTY.md).
- Modelbestanden worden hier niet opgeslagen; ze worden van de bovenstaande bronnen gedownload onder hun eigen licenties (Hugging Face vermeldt voor allemaal Apache-2.0, gelezen op 2026-11-13). De modelkaart zegt niets over wie de eigenaar is van gegenereerde afbeeldingen, en wij maken daar geen aanspraak op.
- **cuDNN en de CUDA-runtime zijn eigendom van NVIDIA** en vallen niet onder de licentie van deze repository. cuDNN wordt van de server van NVIDIA gedownload onder de licentie van NVIDIA (`--no-cudnn` slaat het over); de DLL's van de CUDA-runtime staan in een aparte, ongewijzigde zip (CUDA Toolkit EULA, Attachment A). Details en wat we niet konden verifiëren: [`THIRD_PARTY.md`](THIRD_PARTY.md).
- **Naamsvermelding.** Het bestand `NOTICE` behouden bij kopieën en afgeleide werken is de voorwaarde (Apache-2.0, sectie 4). Daarnaast stellen we een regel als "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey" op prijs; die is gewenst, niet verplicht.
- Lees alsjeblieft [`ETHICS.md`](ETHICS.md): elke afbeelding is synthetisch, en je bent zelf verantwoordelijk voor wat je publiceert.

## Bijdragen

Het nuttigste wat je kunt doen is **je kaart testen** en ons vertellen wat er gebeurde: naam van de GPU, driver, RAM, de `run.json` en de laatste regels van het log (het issueformulier "Hardware test report"). Verbeteringen aan de documenten en aan de scripts zijn ook welkom; zie [`CONTRIBUTING.md`](CONTRIBUTING.md). Beveiligingsmeldingen gaan via de privéroute in [`SECURITY.md`](SECURITY.md).

[Installatiegids voor AI-agenten](AGENTS.md) · [Metingen](docs/MEASUREMENTS.md) · [Problemen oplossen](docs/TROUBLESHOOTING.md) · [De engine bouwen](docs/BUILD.md) · [Patches](patches/README.md) · [Prompts](docs/PROMPTS.md) · [Derden](THIRD_PARTY.md) · [Wijzigingslogboek](CHANGELOG.md)

Deze pagina is met hulp van AI gelokaliseerd; correcties zijn zeer welkom, zie [`CONTRIBUTING.md`](CONTRIBUTING.md).
