[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · **Norsk** · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**Z-Image-Turbo (Q8_0 GGUF) tekst-til-bilde i 768x1344 på et 4 GB GTX 1050 Ti (Pascal, sm_61) med stable-diffusion.cpp på Windows.** Målt på en bærbar PC med 16 GB RAM, hvor prosessen bruker omtrent 11 GB RAM. Samme seed gir de samme pikslene, piksel for piksel. Målingene og motorens patcher er publisert, nedlastingene er låst med sha256, og en AI-kodeagent kan installere det steg for steg.

*Uoffisiell. Ikke tilknyttet Tongyi-MAI (Z-Image), leejet (stable-diffusion.cpp) eller NVIDIA.*

## Start her

Det finnes en ferdig pakke, så prøv den først. Hvis maskinvaren din er en annen, eller et steg feiler, er alt det andre åpent: patchene, byggeoppskriften og målingene ligger i dette repoet, så du kan bygge for ditt eget kort eller tilpasse dem.

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

Steg 2 laster ned omtrent 12.2 GB og tok 29 minutter én gang, på vår tilkobling. Først skrives en "Preflight"-blokk (GPU-en din, RAM-en din og ledig disk ved siden av det vi målte; den informerer bare).
Bare GTX 1050 Ti 4 GB i den bærbare PC-en (Pascal, compute capability 6.1) er målt. Andre kort er ikke testet.
Hvis du bruker en AI-kodeagent (Claude Code, Codex, Cursor og lignende), så pek den til [`AGENTS.md`](AGENTS.md).

## Oversikt

Sammenlignet med oppsettet i v0.1.0: Et bilde tar 188–193 s i stedet for 261.6 s, VAE-steget tar 12.5–21.7 s i stedet for 29.8 til 36.3 s, samme seed gir de samme pikslene, og hvert tall i denne README-en har en kommando og en fil bak seg.

768x1344, seed 42, 8 steg, samme maskin. Tallene for v0.1.0 er fra v0.1.0-README-en (test fra ren rot og fem kjøringer). Tallene for v0.3.0 er fra testen fra ren rot i denne utgivelsen.

| | v0.1.0 (aldri publisert; gammelt oppsett) | v0.3.0 |
|---|---|---|
| Tid for ett bilde (én `generate.py`-kjøring) | 261.6 s | 188–193 s |
| VAE-dekoding (siste steg) | 29.8 til 36.3 s | 12.5–21.7 s |
| Nærhet til en referansedekoding (PSNR, høyere er bedre) | 38 til 43 dB | 71 til 73 dB |
| Høyeste GPU-minne (nvidia-smi) | 2949 til 2957 MiB | 3057–3059 MiB |
| Prosessminne, høyeste | 10.5 til 10.9 GB (slik det ble notert da) | 10 489–11 203 MiB |
| Minste ledige RAM sett | 331 til 576 MiB | 303–532 MiB |

Slik leser du tabellen: Referansen er den samme latenten, dekodet på CPU-en som ett float32-stykke. PSNR sammenligner GPU-dekodingen vår med den (3 bilder). Den sier hvor nær VAE-steget ligger referansen. Den sier ikke hvor bra et bilde ser ut. Bildene fra v0.2.0 er ikke byte-identiske med dem fra v0.1.0 for samme prompt og seed, fordi VAE-veien er endret med vilje. Metode og det som ikke er målt: [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md).

## Eksempler

**AI-generert med dette repoet** (Z-Image-Turbo Q8_0, seed 42, 8 steg). Dette er ikke ekte fotografier. Severdigheter og detaljer
kan være unøyaktige, og et bilde følger ikke alltid prompten sin i alle detaljer. De nøyaktige promptene står i [`prompts/`](prompts) og [`docs/PROMPTS.md`](docs/PROMPTS.md).

| | | |
|---|---|---|
| ![Eiffeltårnet i gyllent lys](docs/examples/eiffel.jpg) | ![Tyrkisk teglass](docs/examples/turkish_tea.jpg) | ![Eldre fisker](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![Landsby i en åsside](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![Istanbul fra luften](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. Ikke et ekte foto. Severdigheter kan være unøyaktige.

## Kom i gang

Krav: Windows 10/11, en NVIDIA-GPU med 4 GB, en driver som støtter CUDA 12.8 (driver 581.29 er målt, eldre drivere er ikke testet; selve CUDA-runtime lastes ned for deg), Python 3.10 eller nyere,
git, omtrent 14 GB ledig disk (nedlastingene er omtrent 12.2 GB med cuDNN; tallet for ledig disk er et anslag) og 16 GB RAM (det som er målt; mindre er ikke testet).

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- `setup.py` skriver først en "Preflight"-blokk (GPU-en din, RAM-en din og ledig disk ved siden av det vi målte; den informerer bare og blokkerer aldri). Deretter laster den ned fra de låste adressene i [`models.lock.json`](models.lock.json) og kontrollerer hver fil med sha256. Den skriver `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK`, så `CUDNN_OK` eller `CUDNN_SKIPPED`, og til slutt `SETUP_OK`.
  Uten `--models-dir` og `--bin-dir` bruker den `models/` og `bin/` i roten av repoet. Legg modellene på en SSD (bare en SSD er målt).
  Stopp den når som helst med Ctrl+C og kjør den samme kommandoen på nytt: Nedlastingene fortsetter fra `.part`-filer.
- **cuDNN installeres som standard og er ikke en del av dette repoet.** Det er NVIDIA-programvare under NVIDIAs egen lisens ([lisenstekst](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)), for systemer med NVIDIA-skjermkort. Det lastes ned fra NVIDIAs server uten betaling og uten innlogging, og vi fant ingen bestemmelse i lisensen som begrenser kommersiell eller privat bruk. `setup.py` viser lisensadressen, laster ned filen og kopierer bare åtte DLL-filer ved siden av `sd-cli.exe`. NVIDIAs lisens sier at den som ikke godtar vilkårene, ikke må laste ned, installere eller bruke den; i så fall kjører du `python scripts/setup.py --no-cudnn`. Uten cuDNN fungerer alt med den tregere VAE-veien fra v0.1.0 (`--vae legacy`), og `generate.py` sier fra om det.
- `generate.py` skriver `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, `run.json` (tid, steg, hvilken VAE-vei som kjørte, høyeste GPU-minne, den nøyaktige kommandoen) og `log.txt`, og skriver `IMAGE_OK <path>`.

## Bruk

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| Valg | Betydning |
|---|---|
| `--prompt "<text>"` eller `--prompt-file <txt>` | prompten (én av de to er påkrevd) |
| `--width`, `--height` | multipler av 16, 256 til 2048. Standard er 768x1344. Testet: 768x1344, 1344x768, 1024x1024 |
| `--seed` | standard 42 |
| `--out`, `--name` | rotmappe for utdata (standard `outputs/`) og et kort navn på kjøremappen |
| `--models-dir`, `--bin-dir` | hvor `setup.py` la modellene og motoren |
| `--vae auto` (standard) | cuDNN float32. Prøver først ett stykke, så to store flis, så den lille standardflisen |
| `--vae tiled` | cuDNN float32, alltid to store flis |
| `--vae legacy` | veien fra v0.1.0: ingen cuDNN, små flis. Brukes automatisk (med en advarsel) når cuDNN-DLL-filene mangler |

Steg (8), cfg (1.0), sampler og scheduler er faste med vilje. Se [Hva den kjører](#what-it-runs).

## Sjekk det selv

- `generate.py` skriver `PIXEL_SHA256 <hex>` som en av de siste linjene: en hash av de dekodede pikslene. Kjør samme kommando to ganger og sammenlign de to bildene: `python scripts/compare.py <run A>/image.png <run B>/image.png` skal skrive `SAME_PIXELS`.
- `PIXEL_SHA256` for de fem eksemplene på maskinen vår står i [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md). Filhashen til en PNG kan være en annen selv når pikslene er de samme, fordi PNG-en inneholder genereringsparametrene som tekst. Sammenlign piksler, ikke filer.
- Ærlig begrensning: Vi har ikke målt om et annet kort eller en annen driver gir de samme pikslene.

## Hvorfor det får plass i 4 GB

- **Hva modellforfatterne sier.** Modellkortet for Z-Image-Turbo sier at modellen "fits comfortably within 16G VRAM consumer devices" ([modellkort](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)). Det er en uttalelse om kort med 16 GB. Den offisielle README-en nevner også stable-diffusion.cpp som et alternativ fra tredjepart og siterer det for "as little as 4GB of VRAM" ([README](https://github.com/Tongyi-MAI/Z-Image)). Det er stable-diffusion.cpp-prosjektets eget utsagn, ikke et krav fra Z-Image-teamet.
- **Hva vi målte.** Z-Image-Turbo Q8_0 (en fil på 6.6 GB) med Qwen3-4B Q8_0 som tekstencoder, 768x1344: GPU-toppen, målt av nvidia-smi hvert 2. sekund (en kort topp kan bli oversett), var 2949 til 2957 MiB (v0.1.0-motoren) og 3057–3059 MiB (v0.2.0-motoren) på et kort med 4096 MiB. Vektene (10 509 MiB; motorens logg skriver det som MB) blir liggende i systemets RAM. Motoren kopierer nettverket til GPU-en ett segment om gangen (en skive av nettverket): 36 segmenter, som i logglinjen `z_image using 36 segments`.
- **Hva det koster.** Tid og systemminne: 188–193 s per bilde, og motorprosessen holder omtrent 10 489–11 203 MiB RAM (medregnet minnekartlagte modellsider) på en maskin med 16 GB, så ledig RAM synker til noen få hundre MiB mens den kjører.
- **Andres oppsett.** Andre forteller om Z-Image på kort med 4 GB med lavere kvantisering eller mindre størrelser (for eksempel anbefaler wikisiden i stable-diffusion.cpp for kort med 4 GB Q3_K eller Q4_0 i 1024x512). Der vi har sett etter (liste og dato i [`docs/RELATED.md`](docs/RELATED.md)) fant vi ikke noe publisert oppsett som kombinerer alle fire: et kort med 4 GB, Q8_0, 768x1344 eller større, og målt tid og GPU-minne. Det er en uttalelse om hvor vi har sett etter, ikke om alle steder.
- **Hvem gjør hva.** At det får plass i 4 GB kommer fra stable-diffusion.cpp selv: `--offload-to-cpu`, `--mmap`, arbeid i skiver og flash attention (med den slått av trengte en kjøring 4205 MB og fikk ikke plass). Patchene våre er for hastighet og for et bedre VAE-steg, ikke for å få det til å passe. Vi har ikke kjørt den upatchede upstream-motoren på dette kortet, så vi kan ikke si om den får plass.

## Slik fungerer det

Tre endringer oppå stable-diffusion.cpp `master-1088-32d516c` (alle er brytere; tabellen i [`patches/README.md`](patches/README.md) viser hver enkelt med miljøvariabelen sin):

1. **Refineren kjører én gang per steg.** Et gruppenavn ble brukt to ganger, så fire refiner-blokker ble regnet ut en ekstra gang. Rettes det, blir steg 2 til 8 omtrent 1.3 s raskere hver (22.0 til 20.7 s) med et bilde med identiske piksler (3 bilder kontrollert).
2. **VAE gjennom cuDNN, i float32.** Siste steg (latenten blir til piksler) bruker nå NVIDIAs cuDNN float32-konvolusjon. På kortet vårt gikk VAE-steget fra 23 til 27 s ned til 10 til 15 s, og PSNR mot referansen flyttet seg fra 38 til 43 dB til 45 til 49 dB (store flis).
3. **Ett stykke først.** Motoren prøver nå å dekode hele bildet i ett stykke når minnesjekken sier at det får plass (margin 256 MiB), faller tilbake til to store flis og deretter til små flis. I ett stykke tok VAE-steget omtrent 8–16 s, og PSNR mot referansen var 71 til 73 dB. Hvis motoren tvinges til å falle tilbake, har bildet de samme pikslene som det flisede (kontrollert med `PIXEL_SHA256`). Hva som skjedde, står i `run.json` (`stages.vae_path`: `full`, `tile`, `floor` eller `retry`).

I tillegg: `--eager-load` (leser modellsidene inn på forhånd; 241.2 s til 220.3 s på samme bilde, utviklingsbygg, én kjøring hver) er en del av den faste kommandoen.

<a id="what-it-runs"></a>
## Hva den kjører

| Del | Fil | Kilde |
|---|---|---|
| Diffusjonsmodell | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), base [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Tekstencoder | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), autoenkoder av FLUX.1-typen |
| Motor | `sd-cli.exe`, stable-diffusion.cpp `32d516c` med patchene i [`patches/`](patches) | v0.3.0-utgivelsen av dette repoet (`sinirsiz-foto-engine-v0.3.0-win-x64-cuda12.8-sm61.zip`) |
| CUDA-runtime | `cudart`, `cublas`, `cublasLt` (12.8), uendret | zip fra utgivelsen wan22-pascal-4gb v0.1.0 |
| cuDNN (installeres som standard; `--no-cudnn` hopper over det) | 8 DLL-filer, versjon 9.10.2.21 (CUDA 11-bygg) | NVIDIAs egen server, under NVIDIAs lisens. Ligger ikke her |

Faste innstillinger: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`.
Vi reduserer ikke antall steg, legger ikke til noen negativ prompt og slår ikke på caching: Modellen er destillert for 8 steg og bruker ikke negative prompter (se [prompter](docs/PROMPTS.md)).

## Begrensninger (les før du stoler på det)

- **Bare Windows.** Den ferdige motoren og disse skriptene finnes bare for Windows.
- **Ett kort, én maskin.** Målt bare på en bærbar PC med GTX 1050 Ti 4 GB (i7-7700HQ, 16 GB RAM, Windows 10, driver 581.29, modeller på en SSD). Andre GPU-er og drivere, maskiner med mindre enn 16 GB RAM, Linux og macOS: **ikke testet**.
- Andre kort og systemer (hvilken vei som finnes, og en fellesskapstest på et AMD-kort under Linux som vi ikke har kjørt selv): [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md).
- **Motoren er bare bygget for Pascal (sm_61).** Andre arkitekturer trenger et eget bygg ([`docs/BUILD.md`](docs/BUILD.md)). Vi har ikke testet noe slikt.
- **cuDNN:** Vi målte med CUDA 11-bygget av cuDNN 9.10.2.21. CUDA 12-bygget har andre filer og ble ikke målt.
- **Minnet er knapt.** Ledig RAM synker til noen få hundre MiB. Lukk andre programmer, og kjør ett bilde om gangen. Vi har ikke sett GPU-minnet gå tomt etter at motorens minnesjekk var bestått, og vi har ikke testet hva som skjer hvis det skulle skje.
- **Størrelser:** Bare 768x1344, 1344x768 og 1024x1024 er testet. Større størrelser skriver en advarsel og kan gå tom for minne.
- Prompten følges bare delvis: Et bilde følger ikke alltid prompten sin i alle detaljer. Tekst i bilder og ekte severdigheter er ikke vurdert.
- PSNR-referansen er vår egen motors CPU-dekoding, ikke en uavhengig implementasjon.
- Tallene i [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) kommer fra én kjøring hver, med mindre noe annet står der.

## Lisens og kreditering

- Skriptene og dokumentene i dette repoet: [Apache-2.0](LICENSE) med en [`NOTICE`](NOTICE)-fil. Motorpatchene i [`patches/`](patches) er MIT, som koden de endrer.
- stable-diffusion.cpp og ggml er MIT. Merknader om tredjepartskoden som er kompilert inn i motoren, ligger i [`licenses/`](licenses) og [`THIRD_PARTY.md`](THIRD_PARTY.md).
- Modellfilene ligger ikke her. De lastes ned fra kildene ovenfor under sine egne lisenser (Hugging Face oppgir Apache-2.0 for dem alle, lest 2026-11-13). Modellkortet sier ingenting om hvem som eier de genererte bildene, og vi hevder ingenting om det.
- **cuDNN og CUDA-runtime tilhører NVIDIA** og omfattes ikke av lisensen til dette repoet. cuDNN lastes ned fra NVIDIAs server under NVIDIAs lisens (`--no-cudnn` hopper over det). CUDA-runtime-DLL-filene ligger i en egen uendret zip (CUDA Toolkit EULA, Attachment A). Detaljer og det vi ikke kunne kontrollere: [`THIRD_PARTY.md`](THIRD_PARTY.md).
- **Kreditering.** At `NOTICE`-filen følger med kopier og avledede verk, er betingelsen (Apache-2.0, avsnitt 4). Utover det setter vi pris på en linje som "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey", men det er ikke et krav.
- Les gjerne [`ETHICS.md`](ETHICS.md): Hvert bilde er syntetisk, og du er selv ansvarlig for det du publiserer.

## Bidra

Det mest nyttige du kan gjøre, er å **teste kortet ditt** og fortelle oss hva som skjedde: GPU-ens navn, driver, RAM, `run.json` og de siste linjene i loggen (skjemaet "Hardware test report"). Rettelser i dokumentene og i skriptene er også velkomne. Se [`CONTRIBUTING.md`](CONTRIBUTING.md). Sikkerhetsmeldinger går via den private veien i [`SECURITY.md`](SECURITY.md).

[Installasjonsguide for AI-agenter](AGENTS.md) · [Målinger](docs/MEASUREMENTS.md) · [Feilsøking](docs/TROUBLESHOOTING.md) · [Bygge motoren](docs/BUILD.md) · [Patcher](patches/README.md) · [Prompter](docs/PROMPTS.md) · [Tredjepart](THIRD_PARTY.md) · [Endringslogg](CHANGELOG.md)

Denne siden er lokalisert med hjelp fra AI, og rettelser er veldig velkomne: se [`CONTRIBUTING.md`](CONTRIBUTING.md).
