[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · **Svenska** · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**Text-till-bild med Z-Image-Turbo (Q8_0 GGUF) i 768x1344 på ett GTX 1050 Ti med 4 GB (Pascal, sm_61), med stable-diffusion.cpp, på Windows.** Uppmätt på en bärbar dator med 16 GB RAM, där processen använder ungefär 11 GB RAM. Samma seed ger samma pixlar, pixel för pixel; mätningarna och motorpatcharna är publicerade, nedladdningarna är fastlåsta med sha256, och en AI-kodagent kan installera det steg för steg.

*Inofficiellt. Inte affilierat med Tongyi-MAI (Z-Image), leejet (stable-diffusion.cpp) eller NVIDIA.*

> **Använder du en AI-kodagent (Codex, Claude Code, Gemini, Cursor)?** Ge den den här enda meningen: ”Läs `AGENTS_HIZLI.md` till slutet, kör `python scripts/tani.py` först, för din framfart i `DURUM.md` och fråga mig innan du raderar eller flyttar något, ändrar systemets Python eller PATH eller sänker en kvalitetsinställning.” Agenten diagnostiserar den här datorn, skriver en checklista och frågar dig vid varje beslut.

## Börja här

Det finns ett färdigt paket, så prova det först. Om din hårdvara är en annan eller ett steg misslyckas är resten öppet: patcharna, bygganvisningen och mätningarna finns i det här repot, så du kan bygga för ditt eget kort eller anpassa dem.

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

Steg 2 laddar ner ungefär 12.2 GB och tog en gång 29 minuter på vår anslutning; det skriver först ut ett "Preflight"-block (ditt grafikkort, ditt RAM och ledigt diskutrymme bredvid det vi mätte; det informerar bara).
Bara det bärbara kortet GTX 1050 Ti 4 GB (Pascal, compute capability 6.1) har mätts. Andra kort har inte testats.
Om du använder en AI-kodagent (Claude Code, Codex, Cursor och liknande), peka den på [`AGENTS.md`](AGENTS.md).

## I korthet

Jämfört med upplägget i v0.1.0: en bild tar 188–193 s i stället för 261.6 s, VAE-steget tar 12.5–21.7 s i stället för 29.8 till 36.3 s, samma seed ger samma pixlar, och bakom varje siffra i den här README:n finns ett kommando och en fil.

768x1344, seed 42, 8 steg, samma maskin. Siffrorna för v0.1.0 kommer från README:n för v0.1.0 (clean-root-test och fem körningar); siffrorna för v0.3.0 kommer från clean-root-testet för den här versionen.

| | v0.1.0 (aldrig publicerad; gammalt upplägg) | v0.3.0 |
|---|---|---|
| Tid för en bild (en körning av `generate.py`) | 261.6 s | 188–193 s |
| VAE-avkodning (sista steget) | 29.8 till 36.3 s | 12.5–21.7 s |
| Närhet till en referensavkodning (PSNR, högre är närmare) | 38 till 43 dB | 71 till 73 dB |
| GPU-minne, topp (nvidia-smi) | 2949 till 2957 MiB | 3057–3059 MiB |
| Processminne, topp | 10.5 till 10.9 GB (som det registrerades då) | 10 489–11 203 MiB |
| Lägsta lediga RAM som sågs | 331 till 576 MiB | 303–532 MiB |

Så läser du detta: referensen är samma latent, avkodad på CPU:n i ett enda stycke som float32; PSNR jämför vår GPU-avkodning med den (3 bilder). Det visar hur nära VAE-steget ligger den referensen. Det visar inte hur bra en bild ser ut. Bilderna från v0.2.0 är inte byte för byte identiska med v0.1.0 för samma prompt och seed, eftersom VAE-vägen ändrades med avsikt. Metod och det som inte mättes: [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md).

## Exempel

**AI-genererat med det här repot** (Z-Image-Turbo Q8_0, seed 42, 8 steg). Det här är inga riktiga fotografier; landmärken och detaljer
kan vara felaktiga, och en bild följer inte alltid sin prompt i varje detalj. De exakta prompterna finns i [`prompts/`](prompts) och [`docs/PROMPTS.md`](docs/PROMPTS.md).

| | | |
|---|---|---|
| ![Eiffeltornet i gyllene timmen](docs/examples/eiffel.jpg) | ![Turkiskt tevglas](docs/examples/turkish_tea.jpg) | ![Äldre fiskare](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![By i en sluttning](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![Istanbul från luften](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. Inte ett riktigt foto; landmärken kan vara felaktiga.

## Snabbstart

Krav: Windows 10/11, ett NVIDIA-grafikkort med 4 GB, en drivrutin som stöder CUDA 12.8 (drivrutin 581.29 har mätts; äldre drivrutiner har inte testats; själva CUDA-körmiljön laddas ner åt dig), Python 3.10 eller nyare,
git, ungefär 14 GB ledigt diskutrymme (nedladdningarna är ungefär 12.2 GB med cuDNN; siffran för ledigt diskutrymme är en uppskattning) och 16 GB RAM (det som mättes; mindre har inte testats).

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- `setup.py` skriver först ut ett "Preflight"-block (ditt grafikkort, ditt RAM och ledigt diskutrymme bredvid det vi mätte; det informerar bara och blockerar aldrig). Sedan laddar det ner från de fastlåsta adresserna i [`models.lock.json`](models.lock.json) och kontrollerar varje fil med sha256. Det skriver ut `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK`, sedan `CUDNN_OK` eller `CUDNN_SKIPPED`, och till sist `SETUP_OK`.
  Utan `--models-dir` och `--bin-dir` används `models/` och `bin/` i repots rotmapp; lägg modellerna på en SSD (bara SSD har mätts).
  Du kan avbryta när som helst med Ctrl+C och köra samma kommando igen: nedladdningarna fortsätter från `.part`-filerna.
- **cuDNN installeras som standard och ingår inte i det här repot.** Det är NVIDIA-programvara under NVIDIA:s egen licens ([licenstext](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)), för system med NVIDIA-GPU:er. Det laddas ner från NVIDIA:s server utan att någon betalning begärs och utan inloggning, och vi hittade ingen klausul i licensen som begränsar kommersiell eller privat användning. `setup.py` visar licensadressen, laddar ner filen och kopierar bara åtta DLL-filer bredvid `sd-cli.exe`. NVIDIA:s licens säger att den som inte accepterar villkoren inte får ladda ner, installera eller använda det; kör i så fall `python scripts/setup.py --no-cudnn`. Utan cuDNN fungerar allt med den långsammare VAE-vägen från v0.1.0 (`--vae legacy`), och `generate.py` talar om det.
- `generate.py` skriver `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, `run.json` (tid, steg, vilken VAE-väg som kördes, topp för GPU-minnet, det exakta kommandot) och `log.txt`, och skriver ut `IMAGE_OK <path>`.

## Användning

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| Alternativ | Betydelse |
|---|---|
| `--prompt "<text>"` eller `--prompt-file <txt>` | prompten (en av de två krävs) |
| `--width`, `--height` | multiplar av 16, 256 till 2048; standard 768x1344; testade: 768x1344, 1344x768, 1024x1024 |
| `--seed` | standard 42 |
| `--out`, `--name` | rot för utdatamappen (standard `outputs/`) och ett kort namn på körningsmappen |
| `--models-dir`, `--bin-dir` | var `setup.py` lade modellerna och motorn |
| `--vae auto` (standard) | cuDNN float32; först i ett stycke, sedan två stora rutor, sedan den lilla standardrutan |
| `--vae tiled` | cuDNN float32, alltid två stora rutor |
| `--vae legacy` | vägen från v0.1.0: inget cuDNN, små rutor. Används automatiskt (med en varning) när cuDNN-DLL-filerna saknas |

Steg (8), cfg (1.0), sampler och scheduler är fasta med avsikt; se [Vad det kör](#what-it-runs).

## Kontrollera själv

- `generate.py` skriver ut `PIXEL_SHA256 <hex>` som en av de sista raderna: en hash av de avkodade pixlarna. Kör samma kommando två gånger och jämför de två bilderna: `python scripts/compare.py <run A>/image.png <run B>/image.png` ska skriva ut `SAME_PIXELS`.
- `PIXEL_SHA256` för de fem exemplen på vår maskin finns i [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md). Filhashen för en PNG kan skilja sig även när pixlarna är desamma, eftersom PNG-filen innehåller genereringsparametrarna som text; jämför pixlar, inte filer.
- Ärlig gräns: vi har inte mätt om ett annat kort eller en annan drivrutin ger samma pixlar.

## Varför det ryms i 4 GB

- **Vad modellförfattarna säger.** Modellkortet för Z-Image-Turbo säger att modellen "fits comfortably within 16G VRAM consumer devices" (ryms bekvämt på konsumentkort med 16 GB VRAM) ([modellkort](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)). Det är ett påstående om kort med 16 GB. Den officiella README:n listar dessutom stable-diffusion.cpp som ett alternativ från tredje part och citerar det med "as little as 4GB of VRAM" (med så lite som 4 GB VRAM) ([README](https://github.com/Tongyi-MAI/Z-Image)); det är ett påstående från projektet stable-diffusion.cpp, inget krav från Z-Image-teamet.
- **Vad vi mätte.** Z-Image-Turbo Q8_0 (en fil på 6.6 GB) med en Qwen3-4B Q8_0 textkodare, 768x1344: GPU-toppen, samplad av nvidia-smi var 2 s (en kort topp kan missas), var 2949 till 2957 MiB (motor v0.1.0) och 3057–3059 MiB (motor v0.2.0) på ett kort med 4096 MiB. Vikterna (10 509 MiB; motorns logg skriver ut det som MB) ligger kvar i systemminnet; motorn kopierar nätverket till GPU:n ett segment (en del av nätverket) i taget: 36 segment, som i loggraden `z_image using 36 segments`.
- **Vad det kostar.** Tid och systemminne: 188–193 s per bild, och motorprocessen håller ungefär 10 489–11 203 MiB RAM (inklusive minnesmappade modellsidor) på en maskin med 16 GB, så det lediga RAM:et sjunker till några hundra MiB medan den kör.
- **Andras upplägg.** Andra rapporterar Z-Image på kort med 4 GB med lägre kvantisering eller mindre storlekar (till exempel rekommenderar wikisidan i stable-diffusion.cpp för kort med 4 GB Q3_K eller Q4_0 i 1024x512). Där vi har letat (lista och datum i [`docs/RELATED.md`](docs/RELATED.md)) hittade vi inget publicerat upplägg som förenar alla fyra: ett kort med 4 GB, Q8_0, 768x1344 eller större, och uppmätt tid och GPU-minne. Det är ett påstående om var vi har letat, inte om överallt.
- **Vem gör vad.** Att det ryms i 4 GB beror på stable-diffusion.cpp självt: `--offload-to-cpu`, `--mmap`, att arbeta i delar och flash attention (utan den behövde en körning 4205 MB och rymdes inte). Våra patchar är till för hastighet och för ett bättre VAE-steg, inte för att det ska rymmas. Vi körde inte den opatchade upstream-motorn på det här kortet, så vi kan inte säga om den ryms.

## Hur det fungerar

Tre ändringar ovanpå stable-diffusion.cpp `master-1088-32d516c` (alla är omkopplare; tabellen i [`patches/README.md`](patches/README.md) listar var och en med sin miljövariabel):

1. **Refinern körs en gång per steg.** Ett gruppnamn användes två gånger, så fyra refiner-block räknades ut en andra gång. Med rättningen blir steg 2 till 8 ungefär 1.3 s snabbare vardera (22.0 till 20.7 s), med en pixelidentisk bild (3 bilder kontrollerade).
2. **VAE via cuDNN, i float32.** Det sista steget (att göra om latenten till pixlar) använder nu NVIDIA:s cuDNN-konvolution i float32. På vårt kort tog det ner VAE från 23 till 27 s till 10 till 15 s och höjde PSNR mot referensen från 38 till 43 dB till 45 till 49 dB (stora rutor).
3. **Först i ett stycke.** Motorn försöker nu avkoda hela bilden i ett stycke när minneskontrollen säger att det ryms (marginal 256 MiB), faller annars tillbaka på två stora rutor och sedan på små rutor. I ett stycke tog VAE ungefär 8–16 s och PSNR mot referensen var 71 till 73 dB. Om en tvingad reträtt sker har bilden samma pixlar som den rutade (kontrollerat med `PIXEL_SHA256`). Vad som hände skrivs i `run.json` (`stages.vae_path`: `full`, `tile`, `floor` eller `retry`).

Dessutom: `--eager-load` (läser in modellsidorna i förväg; 241.2 s till 220.3 s på samma bild, utvecklingsbygge, en körning vardera) ingår i det fasta kommandot.

<a id="what-it-runs"></a>
## Vad det kör

| Del | Fil | Källa |
|---|---|---|
| Diffusionsmodell | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), bas [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Textkodare | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), autoencoder av typen FLUX.1 |
| Motor | `sd-cli.exe`, stable-diffusion.cpp `32d516c` med patcharna i [`patches/`](patches) | releasen v0.3.0 av det här repot (`sinirsiz-foto-engine-v0.3.0-win-x64-cuda12.8-sm61.zip`) |
| CUDA-körmiljö | `cudart`, `cublas`, `cublasLt` (12.8), oförändrade | zip från releasen v0.1.0 av wan22-pascal-4gb |
| cuDNN (installeras som standard; `--no-cudnn` hoppar över det) | 8 DLL-filer, version 9.10.2.21 (CUDA 11-bygge) | NVIDIA:s egen server, under NVIDIA:s licens; lagras inte här |

Fasta inställningar: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`.
Vi sänker inte antalet steg, lägger inte till en negativ prompt och slår inte på cachning: modellen är destillerad för 8 steg och använder inga negativa prompter (se [prompter](docs/PROMPTS.md)).

## Begränsningar (läs innan du förlitar dig på det)

- **Bara Windows.** Den färdiga motorn och de här skripten finns bara för Windows.
- **Ett kort, en maskin.** Uppmätt bara på en bärbar dator med GTX 1050 Ti 4 GB (i7-7700HQ, 16 GB RAM, Windows 10, drivrutin 581.29, modeller på en SSD). Andra grafikkort och drivrutiner, maskiner med mindre än 16 GB RAM, Linux och macOS: **inte testat**.
- Andra kort och system (vilken väg som finns, och ett communitytest på ett AMD-kort under Linux som vi inte själva har kört): [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md).
- **Motorn är bara byggd för Pascal (sm_61).** Andra arkitekturer kräver ett eget bygge ([`docs/BUILD.md`](docs/BUILD.md)); vi har inte testat något sådant.
- **cuDNN:** vi mätte med CUDA 11-bygget av cuDNN 9.10.2.21. CUDA 12-bygget har andra filer och mättes inte.
- **Minnet är knappt.** Ledigt RAM sjunker till några hundra MiB; stäng andra program och kör en bild i taget. Vi har inte sett att GPU-minnet tagit slut efter att motorns minneskontroll godkänts, och vi testade inte vad som händer då.
- **Storlekar:** bara 768x1344, 1344x768 och 1024x1024 har testats. Större storlekar skriver ut en varning och kan få minnet att ta slut.
- Följsamheten mot prompten är ofullständig: en bild följer inte alltid sin prompt i varje detalj. Text i bilder och verkliga landmärken har inte utvärderats.
- PSNR-referensen är vår egen motors CPU-avkodning, inte en oberoende implementation.
- Siffrorna i [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) kommer från en körning vardera om inget annat anges.

## Licens och erkännande

- Det här repots skript och dokument: [Apache-2.0](LICENSE) med en [`NOTICE`](NOTICE)-fil. Motorpatcharna i [`patches/`](patches) är MIT, liksom koden de ändrar.
- stable-diffusion.cpp och ggml är MIT. Meddelandena för tredjepartskoden som kompilerats in i motorn finns i [`licenses/`](licenses) och [`THIRD_PARTY.md`](THIRD_PARTY.md).
- Modellfiler lagras inte här; de laddas ner från källorna ovan under sina egna licenser (Hugging Face anger Apache-2.0 för alla, läst 2026-11-13). Modellkortet säger ingenting om vem som äger genererade bilder, och vi gör inga anspråk på det.
- **cuDNN och CUDA-körmiljön tillhör NVIDIA** och omfattas inte av det här repots licens. cuDNN laddas ner från NVIDIA:s server under NVIDIA:s licens (`--no-cudnn` hoppar över det); CUDA-körmiljöns DLL-filer ligger i en separat, oförändrad zip (CUDA Toolkit EULA, Attachment A). Detaljer och det vi inte kunde verifiera: [`THIRD_PARTY.md`](THIRD_PARTY.md).
- **Erkännande.** Att behålla filen `NOTICE` vid kopior och härledda verk är villkoret (Apache-2.0, avsnitt 4). Utöver det sätter vi värde på en rad som "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey"; den är önskad, inte obligatorisk.
- Läs gärna [`ETHICS.md`](ETHICS.md): varje bild är syntetisk, och du ansvarar själv för det du publicerar.

## Bidra

Det mest användbara du kan göra är att **testa ditt kort** och berätta vad som hände: grafikkortets namn, drivrutin, RAM, `run.json` och de sista raderna i loggen (ärendeformuläret "Hardware test report"). Rättelser i dokumenten och i skripten är också välkomna; se [`CONTRIBUTING.md`](CONTRIBUTING.md). Säkerhetsrapporter går via den privata vägen i [`SECURITY.md`](SECURITY.md).

[Installationsguide för AI-agenter](AGENTS.md) · [Mätningar](docs/MEASUREMENTS.md) · [Felsökning](docs/TROUBLESHOOTING.md) · [Bygga motorn](docs/BUILD.md) · [Patchar](patches/README.md) · [Prompter](docs/PROMPTS.md) · [Tredje part](THIRD_PARTY.md) · [Ändringslogg](CHANGELOG.md)

Den här sidan har lokaliserats med hjälp av AI; rättelser är mycket välkomna, se [`CONTRIBUTING.md`](CONTRIBUTING.md).
