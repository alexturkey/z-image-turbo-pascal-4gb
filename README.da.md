[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · **Dansk** · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**Z-Image-Turbo (Q8_0 GGUF) tekst-til-billede i 768x1344 på et 4 GB GTX 1050 Ti (Pascal, sm_61) med stable-diffusion.cpp på Windows.** Målt på en bærbar med 16 GB RAM, hvor processen bruger omkring 11 GB RAM. Samme seed giver de samme pixels, pixel for pixel. Målingerne og motorens patches er offentliggjort, downloadene er låst med sha256, og en AI-kodeagent kan installere det trin for trin.

*Uofficiel. Ikke tilknyttet Tongyi-MAI (Z-Image), leejet (stable-diffusion.cpp) eller NVIDIA.*

## Start her

Der findes en færdig pakke, så prøv den først. Hvis din hardware er en anden, eller et trin fejler, er alt det øvrige åbent: patches, byggeopskrift og målinger ligger i dette repository, så du kan bygge til dit eget kort eller tilpasse dem.

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

Trin 2 henter omkring 12.2 GB og tog 29 minutter én gang på vores forbindelse. Først skrives en "Preflight"-blok (din GPU, dit RAM og din ledige disk ved siden af det, vi målte; den informerer kun).
Kun den bærbares GTX 1050 Ti 4 GB (Pascal, compute capability 6.1) er målt. Andre kort er ikke testet.
Hvis du bruger en AI-kodeagent (Claude Code, Codex, Cursor og lignende), så peg den på [`AGENTS.md`](AGENTS.md).

## Overblik

Sammenlignet med v0.1.0-opsætningen: Et billede tager 193–228 s i stedet for 261.6 s, VAE-trinnet tager 8.3–15.9 s i stedet for 29.8 til 36.3 s, samme seed giver de samme pixels, og hvert tal i denne README har en kommando og en fil bag sig.

768x1344, seed 42, 8 trin, samme maskine. Tallene for v0.1.0 stammer fra v0.1.0-README'en (test fra ren rod og fem kørsler). Tallene for v0.2.0 stammer fra testen fra ren rod i denne udgave.

| | v0.1.0 (aldrig offentliggjort; gammel opsætning) | v0.2.0 |
|---|---|---|
| Tid til ét billede (én `generate.py`-kørsel) | 261.6 s | 193–228 s |
| VAE-afkodning (sidste trin) | 29.8 til 36.3 s | 8.3–15.9 s |
| Nærhed til en referenceafkodning (PSNR, højere er bedre) | 38 til 43 dB | 71 til 73 dB |
| Højeste GPU-hukommelse (nvidia-smi) | 2949 til 2957 MiB | 3057–3059 MiB |
| Proceshukommelse, højeste | 10.5 til 10.9 GB (som den blev noteret dengang) | 10 667–10 915 MiB |
| Mindste ledige RAM set | 331 til 576 MiB | 418–545 MiB |

Sådan læses tabellen: Referencen er den samme latent, afkodet på CPU'en som ét float32-stykke. PSNR sammenligner vores GPU-afkodning med den (3 billeder). Den fortæller, hvor tæt VAE-trinnet ligger på referencen. Den fortæller ikke, hvor godt et billede ser ud. Billederne fra v0.2.0 er ikke byte-identiske med dem fra v0.1.0 for samme prompt og seed, fordi VAE-vejen med vilje er ændret. Metode og det, der ikke er målt: [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md).

## Eksempler

**AI-genereret med dette repository** (Z-Image-Turbo Q8_0, seed 42, 8 trin). Det er ikke rigtige fotografier. Seværdigheder og detaljer
kan være unøjagtige, og et billede følger ikke altid sin prompt i alle detaljer. De nøjagtige prompts står i [`prompts/`](prompts) og [`docs/PROMPTS.md`](docs/PROMPTS.md).

| | | |
|---|---|---|
| ![Eiffeltårnet ved gyldent lys](docs/examples/eiffel.jpg) | ![Tyrkisk teglas](docs/examples/turkish_tea.jpg) | ![Ældre fisker](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![Landsby på en bjergskråning](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![Istanbul fra luften](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. Ikke et rigtigt foto. Seværdigheder kan være unøjagtige.

## Kom i gang

Krav: Windows 10/11, en NVIDIA-GPU med 4 GB, en driver der understøtter CUDA 12.8 (driver 581.29 er målt, ældre drivere er ikke testet; selve CUDA-runtime hentes for dig), Python 3.10 eller nyere,
git, omkring 14 GB ledig disk (downloadene fylder omkring 12.2 GB med cuDNN; tallet for ledig disk er et skøn) og 16 GB RAM (det, der er målt; mindre er ikke testet).

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- `setup.py` skriver først en "Preflight"-blok (din GPU, dit RAM og din ledige disk ved siden af det, vi målte; den informerer kun og blokerer aldrig). Derefter henter den fra de låste adresser i [`models.lock.json`](models.lock.json) og kontrollerer hver fil med sha256. Den skriver `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK`, så `CUDNN_OK` eller `CUDNN_SKIPPED` og til sidst `SETUP_OK`.
  Uden `--models-dir` og `--bin-dir` bruger den `models/` og `bin/` i repositoryets rod. Læg modellerne på en SSD (kun en SSD er målt).
  Stop den når som helst med Ctrl+C og kør samme kommando igen: Downloads fortsætter fra `.part`-filer.
- **cuDNN installeres som standard og er ikke en del af dette repository.** Det er NVIDIA-software under NVIDIAs egen licens ([licenstekst](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)), til systemer med NVIDIA-grafikkort. Det hentes fra NVIDIAs server uden betaling og uden login, og vi fandt ingen bestemmelse i licensen, der begrænser erhvervsmæssig eller privat brug. `setup.py` viser licensadressen, henter filen og kopierer kun otte DLL-filer ved siden af `sd-cli.exe`. NVIDIAs licens siger, at den, der ikke accepterer vilkårene, ikke må downloade, installere eller bruge den; i så fald kører du `python scripts/setup.py --no-cudnn`. Uden cuDNN virker alt med den langsommere VAE-vej fra v0.1.0 (`--vae legacy`), og `generate.py` siger det.
- `generate.py` skriver `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, `run.json` (tid, trin, hvilken VAE-vej der kørte, højeste GPU-hukommelse, den nøjagtige kommando) og `log.txt`, og skriver `IMAGE_OK <path>`.

## Brug

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| Indstilling | Betydning |
|---|---|
| `--prompt "<text>"` eller `--prompt-file <txt>` | prompten (én af de to er påkrævet) |
| `--width`, `--height` | multipla af 16, 256 til 2048. Standard er 768x1344. Testet: 768x1344, 1344x768, 1024x1024 |
| `--seed` | standard 42 |
| `--out`, `--name` | rodmappe til output (standard `outputs/`) og et kort navn til kørslens mappe |
| `--models-dir`, `--bin-dir` | hvor `setup.py` lagde modellerne og motoren |
| `--vae auto` (standard) | cuDNN float32. Prøver først ét stykke, så to store fliser, så den lille standardflise |
| `--vae tiled` | cuDNN float32, altid to store fliser |
| `--vae legacy` | vejen fra v0.1.0: ingen cuDNN, små fliser. Bruges automatisk (med en advarsel), når cuDNN-DLL-filerne mangler |

Trin (8), cfg (1.0), sampler og scheduler er med vilje faste. Se [Hvad den kører](#what-it-runs).

## Tjek det selv

- `generate.py` skriver `PIXEL_SHA256 <hex>` som en af de sidste linjer: en hash af de afkodede pixels. Kør samme kommando to gange og sammenlign de to billeder: `python scripts/compare.py <run A>/image.png <run B>/image.png` skal skrive `SAME_PIXELS`.
- `PIXEL_SHA256` for de fem eksempler på vores maskine står i [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md). Filhashen for en PNG kan være en anden, selv når pixelsene er de samme, fordi PNG'en indeholder genereringsparametrene som tekst. Sammenlign pixels, ikke filer.
- Ærlig begrænsning: Vi har ikke målt, om et andet kort eller en anden driver giver de samme pixels.

## Hvorfor det passer i 4 GB

- **Hvad modelforfatterne siger.** Modelkortet for Z-Image-Turbo siger, at modellen "fits comfortably within 16G VRAM consumer devices" ([modelkort](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)). Det er en udtalelse om kort med 16 GB. Den officielle README nævner også stable-diffusion.cpp som en mulighed fra tredjepart og citerer den for "as little as 4GB of VRAM" ([README](https://github.com/Tongyi-MAI/Z-Image)). Det er stable-diffusion.cpp-projektets egen påstand, ikke et krav fra Z-Image-teamet.
- **Hvad vi målte.** Z-Image-Turbo Q8_0 (en fil på 6.6 GB) med en Qwen3-4B Q8_0 som tekstencoder, 768x1344: GPU-toppen, målt af nvidia-smi hvert 2. sekund (en kort spids kan blive overset), var 2949 til 2957 MiB (v0.1.0-motoren) og 3057–3059 MiB (v0.2.0-motoren) på et kort med 4096 MiB. Vægtene (10 509 MiB; motorens log skriver det som MB) bliver i systemets RAM. Motoren kopierer netværket til GPU'en ét segment ad gangen (en skive af netværket): 36 segmenter, som i loglinjen `z_image using 36 segments`.
- **Hvad det koster.** Tid og systemhukommelse: 193–228 s pr. billede, og motorprocessen holder omkring 10 667–10 915 MiB RAM (inklusive hukommelseskortlagte modelsider) på en maskine med 16 GB, så den ledige RAM falder til nogle få hundrede MiB, mens den kører.
- **Andres opsætninger.** Andre beretter om Z-Image på kort med 4 GB med lavere kvantisering eller mindre størrelser (for eksempel anbefaler wikisiden i stable-diffusion.cpp for kort med 4 GB Q3_K eller Q4_0 i 1024x512). Der, hvor vi har kigget (liste og dato i [`docs/RELATED.md`](docs/RELATED.md)), fandt vi ikke en offentliggjort opsætning, der kombinerer alle fire: et kort med 4 GB, Q8_0, 768x1344 eller større og målt tid og GPU-hukommelse. Det er en udtalelse om, hvor vi har kigget, ikke om alle steder.
- **Hvem gør hvad.** At det passer i 4 GB kommer fra stable-diffusion.cpp selv: `--offload-to-cpu`, `--mmap`, arbejde i skiver og flash attention (med den slået fra krævede en kørsel 4205 MB og passede ikke). Vores patches er til hastighed og til et bedre VAE-trin, ikke til at få det til at passe. Vi har ikke kørt den upatchede upstream-motor på dette kort, så vi kan ikke sige, om den passer.

## Sådan virker det

Tre ændringer oven på stable-diffusion.cpp `master-1088-32d516c` (alle kan slås til og fra; tabellen i [`patches/README.md`](patches/README.md) viser hver enkelt med sin miljøvariabel):

1. **Refineren kører én gang pr. trin.** Et gruppenavn blev brugt to gange, så fire refiner-blokke blev regnet en ekstra gang. Rettes det, bliver trin 2 til 8 omkring 1.3 s hurtigere hver (22.0 til 20.7 s) med et billede med identiske pixels (3 billeder kontrolleret).
2. **VAE gennem cuDNN, i float32.** Sidste trin (latent bliver til pixels) bruger nu NVIDIAs cuDNN float32-foldning. På vores kort bragte det VAE-trinnet fra 23 til 27 s til 10 til 15 s og flyttede PSNR mod referencen fra 38 til 43 dB til 45 til 49 dB (store fliser).
3. **Ét stykke først.** Motoren prøver nu at afkode hele billedet i ét stykke, når hukommelsestjekket siger, at det kan være der (margin 256 MiB), falder tilbage til to store fliser og derefter til små fliser. I ét stykke tog VAE-trinnet omkring 8–16 s, og PSNR mod referencen var 71 til 73 dB. Hvis motoren tvinges til at falde tilbage, har billedet de samme pixels som det flisede (kontrolleret med `PIXEL_SHA256`). Hvad der skete, står i `run.json` (`stages.vae_path`: `full`, `tile`, `floor` eller `retry`).

Desuden: `--eager-load` (læser modelsiderne ind på forhånd; 241.2 s til 220.3 s på samme billede, udviklingsbuild, én kørsel hver) er en del af den faste kommando.

<a id="what-it-runs"></a>
## Hvad den kører

| Del | Fil | Kilde |
|---|---|---|
| Diffusionsmodel | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), base [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Tekstencoder | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), autoencoder af FLUX.1-typen |
| Motor | `sd-cli.exe`, stable-diffusion.cpp `32d516c` med patchene i [`patches/`](patches) | v0.2.0-udgivelsen af dette repository (`sinirsiz-foto-engine-v0.2.0-win-x64-cuda12.8-sm61.zip`) |
| CUDA-runtime | `cudart`, `cublas`, `cublasLt` (12.8), uændret | zip fra udgivelsen wan22-pascal-4gb v0.1.0 |
| cuDNN (installeres som standard; `--no-cudnn` springer det over) | 8 DLL-filer, version 9.10.2.21 (CUDA 11-build) | NVIDIAs egen server, under NVIDIAs licens. Ligger ikke her |

Faste indstillinger: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`.
Vi sænker ikke antallet af trin, tilføjer ingen negativ prompt og slår ikke caching til: Modellen er destilleret til 8 trin og bruger ikke negative prompts (se [prompts](docs/PROMPTS.md)).

## Begrænsninger (læs, før du stoler på det)

- **Kun Windows.** Den færdige motor og disse scripts findes kun til Windows.
- **Ét kort, én maskine.** Målt kun på en bærbar med GTX 1050 Ti 4 GB (i7-7700HQ, 16 GB RAM, Windows 10, driver 581.29, modeller på en SSD). Andre GPU'er og drivere, maskiner med mindre end 16 GB RAM, Linux og macOS: **ikke testet**.
- Andre kort og systemer (hvilken vej der findes, og en fællesskabstest på et AMD-kort under Linux, som vi ikke selv har kørt): [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md).
- **Motoren er kun bygget til Pascal (sm_61).** Andre arkitekturer kræver et build af din egen ([`docs/BUILD.md`](docs/BUILD.md)). Vi har ikke testet et.
- **cuDNN:** Vi målte med CUDA 11-buildet af cuDNN 9.10.2.21. CUDA 12-buildet har andre filer og blev ikke målt.
- **Hukommelsen er knap.** Den ledige RAM falder til nogle få hundrede MiB. Luk andre programmer, og kør ét billede ad gangen. Vi har ikke set GPU-hukommelsen løbe tør, efter at motorens hukommelsestjek var bestået, og vi har ikke testet, hvad der sker, hvis det skete.
- **Størrelser:** Kun 768x1344, 1344x768 og 1024x1024 er testet. Større størrelser skriver en advarsel og kan løbe tør for hukommelse.
- Prompten følges kun delvist: Et billede følger ikke altid sin prompt i alle detaljer. Tekst i billeder og rigtige seværdigheder er ikke vurderet.
- PSNR-referencen er vores egen motors CPU-afkodning, ikke en uafhængig implementering.
- Tallene i [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) kommer fra én kørsel hver, medmindre der står andet.

## Licens og kreditering

- Dette repositorys scripts og dokumenter: [Apache-2.0](LICENSE) med en [`NOTICE`](NOTICE)-fil. Motorens patches i [`patches/`](patches) er MIT, ligesom den kode, de ændrer.
- stable-diffusion.cpp og ggml er MIT. Notitser om tredjepartskoden, der er kompileret ind i motoren, findes i [`licenses/`](licenses) og [`THIRD_PARTY.md`](THIRD_PARTY.md).
- Modelfilerne ligger ikke her. De hentes fra kilderne ovenfor under deres egne licenser (Hugging Face angiver Apache-2.0 for dem alle, læst den 2026-11-13). Modelkortet siger intet om, hvem der ejer de genererede billeder, og vi gør ingen påstand om det.
- **cuDNN og CUDA-runtime tilhører NVIDIA** og er ikke omfattet af dette repositorys licens. cuDNN hentes fra NVIDIAs server under NVIDIAs licens (`--no-cudnn` springer det over). CUDA-runtime-DLL-filerne ligger i en separat uændret zip (CUDA Toolkit EULA, Attachment A). Detaljer og det, vi ikke kunne kontrollere: [`THIRD_PARTY.md`](THIRD_PARTY.md).
- **Kreditering.** At `NOTICE`-filen følger med kopier og afledte værker, er betingelsen (Apache-2.0, afsnit 4). Ud over det sætter vi pris på en linje som "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey", men det er ikke et krav.
- Læs gerne [`ETHICS.md`](ETHICS.md): Hvert billede er syntetisk, og du er selv ansvarlig for det, du udgiver.

## Bidrag

Det mest nyttige, du kan gøre, er at **teste dit kort** og fortælle os, hvad der skete: GPU'ens navn, driver, RAM, `run.json` og de sidste linjer af loggen (formularen "Hardware test report"). Rettelser til dokumenterne og til scripts er også velkomne. Se [`CONTRIBUTING.md`](CONTRIBUTING.md). Sikkerhedsmeldinger går via den private vej i [`SECURITY.md`](SECURITY.md).

[Installationsguide til AI-agenter](AGENTS.md) · [Målinger](docs/MEASUREMENTS.md) · [Fejlfinding](docs/TROUBLESHOOTING.md) · [Byg motoren](docs/BUILD.md) · [Patches](patches/README.md) · [Prompts](docs/PROMPTS.md) · [Tredjepart](THIRD_PARTY.md) · [Ændringslog](CHANGELOG.md)

Denne side er oversat og tilpasset med hjælp fra AI, og rettelser er meget velkomne: se [`CONTRIBUTING.md`](CONTRIBUTING.md).
