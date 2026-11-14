[Türkçe](README.tr.md) · [English](README.md) · **Deutsch** · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**Text-zu-Bild mit Z-Image-Turbo (Q8_0 GGUF) in 768x1344 auf einer GTX 1050 Ti mit 4 GB (Pascal, sm_61), mit stable-diffusion.cpp, unter Windows.** Gemessen auf einem Laptop mit 16 GB RAM, auf dem der Prozess etwa 11 GB RAM belegt. Derselbe Seed liefert dieselben Pixel, Pixel für Pixel; die Messungen und die Engine-Patches sind veröffentlicht, die Downloads sind per sha256 festgelegt, und ein KI-Coding-Agent kann die Installation Schritt für Schritt durchführen.

*Inoffiziell. Nicht verbunden mit Tongyi-MAI (Z-Image), leejet (stable-diffusion.cpp) oder NVIDIA.*

## Hier starten

Ein fertiges Paket ist vorhanden, probiere es also zuerst aus. Wenn deine Hardware anders ist oder ein Schritt scheitert, ist alles Übrige offen: Die Patches, das Build-Rezept und die Messungen liegen in diesem Repository, du kannst also für deine eigene Karte bauen oder sie anpassen.

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

Schritt 2 lädt etwa 12.2 GB herunter und dauerte bei uns einmal 29 Minuten, mit unserer Verbindung; er gibt zuerst einen „Preflight“-Block aus (deine GPU, dein RAM und der freie Plattenplatz neben dem, was wir gemessen haben; er informiert nur).
Gemessen wurde nur die Laptop-Karte GTX 1050 Ti mit 4 GB (Pascal, Compute Capability 6.1). Andere Karten wurden nicht getestet.
Wenn du einen KI-Coding-Agenten verwendest (Claude Code, Codex, Cursor und ähnliche), verweise ihn auf [`AGENTS.md`](AGENTS.md).

## Auf einen Blick

Gegenüber dem Aufbau von v0.1.0: Ein Bild dauert 193–228 s statt 261.6 s, die VAE-Stufe dauert 8.3–15.9 s statt 29.8 bis 36.3 s, derselbe Seed liefert dieselben Pixel, und hinter jeder Zahl in dieser README stehen ein Befehl und eine Datei.

768x1344, Seed 42, 8 Schritte, derselbe Rechner. Die Zahlen für v0.1.0 stammen aus der README von v0.1.0 (Clean-Root-Test und fünf Läufe); die Zahlen für v0.2.0 stammen aus dem Clean-Root-Test dieser Version.

| | v0.1.0 (nie veröffentlicht; alter Aufbau) | v0.2.0 |
|---|---|---|
| Zeit für ein Bild (ein Lauf von `generate.py`) | 261.6 s | 193–228 s |
| VAE-Decodierung (letzte Stufe) | 29.8 bis 36.3 s | 8.3–15.9 s |
| Nähe zu einer Referenz-Decodierung (PSNR, höher ist näher) | 38 bis 43 dB | 71 bis 73 dB |
| GPU-Speicher, Spitze (nvidia-smi) | 2949 bis 2957 MiB | 3057–3059 MiB |
| Prozessspeicher, Spitze | 10.5 bis 10.9 GB (wie damals aufgezeichnet) | 10 667–10 915 MiB |
| Niedrigster beobachteter freier RAM | 331 bis 576 MiB | 418–545 MiB |

So liest man das: Die Referenz ist dasselbe Latent, auf der CPU in einem Stück als float32 decodiert; der PSNR vergleicht unsere GPU-Decodierung damit (3 Bilder). Er sagt, wie nah die VAE-Stufe an dieser Referenz liegt. Er sagt nicht, wie gut ein Bild aussieht. Die Bilder von v0.2.0 sind bei gleichem Prompt und gleichem Seed nicht Byte für Byte identisch mit denen von v0.1.0, weil sich der VAE-Pfad absichtlich geändert hat. Methode und nicht Gemessenes: [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md).

## Beispiele

**Mit diesem Repository von KI erzeugt** (Z-Image-Turbo Q8_0, Seed 42, 8 Schritte). Das sind keine echten Fotos; Wahrzeichen und Details
können falsch sein, und ein Bild folgt seinem Prompt nicht immer in jedem Detail. Die genauen Prompts stehen in [`prompts/`](prompts) und [`docs/PROMPTS.md`](docs/PROMPTS.md).

| | | |
|---|---|---|
| ![Eiffelturm zur goldenen Stunde](docs/examples/eiffel.jpg) | ![Türkisches Teeglas](docs/examples/turkish_tea.jpg) | ![Älterer Fischer](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![Dorf am Hang](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![Istanbul aus der Luft](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. Kein echtes Foto; Wahrzeichen können falsch sein.

## Schnellstart

Voraussetzungen: Windows 10/11, eine NVIDIA-GPU mit 4 GB, ein Treiber, der CUDA 12.8 unterstützt (gemessen wurde mit Treiber 581.29; ältere Treiber wurden nicht getestet; die CUDA-Laufzeit selbst wird für dich heruntergeladen), Python 3.10 oder neuer,
git, etwa 14 GB freier Plattenplatz (die Downloads umfassen mit cuDNN etwa 12.2 GB; die Angabe zum freien Platz ist eine Schätzung) und 16 GB RAM (gemessen wurde mit diesem Wert; weniger wurde nicht getestet).

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- `setup.py` gibt zuerst einen „Preflight“-Block aus (deine GPU, dein RAM und der freie Plattenplatz neben dem, was wir gemessen haben; er informiert nur und blockiert nie). Danach lädt es von den festgelegten Adressen in [`models.lock.json`](models.lock.json) herunter und prüft jede Datei per sha256. Es gibt `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK`, dann `CUDNN_OK` oder `CUDNN_SKIPPED` und zuletzt `SETUP_OK` aus.
  Ohne `--models-dir` und `--bin-dir` nutzt es `models/` und `bin/` im Stammordner des Repositorys; lege die Modelle auf eine SSD (gemessen wurde nur mit SSD).
  Du kannst jederzeit mit Strg+C abbrechen und denselben Befehl erneut ausführen: Die Downloads setzen sich aus den `.part`-Dateien fort.
- **cuDNN wird standardmäßig installiert und ist nicht Teil dieses Repositorys.** Es ist NVIDIA-Software unter NVIDIAs eigener Lizenz ([Lizenztext](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)), für Systeme mit NVIDIA-GPUs. Es wird vom Server von NVIDIA heruntergeladen, ohne dass eine Zahlung verlangt wird und ohne Anmeldung, und wir haben in der Lizenz keine Klausel gefunden, die die kommerzielle oder private Nutzung einschränkt. `setup.py` zeigt die Adresse der Lizenz an, lädt die Datei herunter und kopiert nur acht DLLs neben `sd-cli.exe`. Die Lizenz von NVIDIA besagt, dass niemand, der ihre Bedingungen nicht akzeptiert, sie herunterladen, installieren oder nutzen darf; in diesem Fall führe `python scripts/setup.py --no-cudnn` aus. Ohne cuDNN funktioniert alles mit dem langsameren VAE-Pfad von v0.1.0 (`--vae legacy`), und `generate.py` weist darauf hin.
- `generate.py` schreibt `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, `run.json` (Zeit, Stufen, welcher VAE-Pfad lief, GPU-Speicher-Spitze, der genaue Befehl) und `log.txt` und gibt `IMAGE_OK <path>` aus.

## Verwendung

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| Option | Bedeutung |
|---|---|
| `--prompt "<text>"` oder `--prompt-file <txt>` | der Prompt (eines von beiden ist erforderlich) |
| `--width`, `--height` | Vielfache von 16, 256 bis 2048; Standard 768x1344; getestet: 768x1344, 1344x768, 1024x1024 |
| `--seed` | Standard 42 |
| `--out`, `--name` | Wurzel des Ausgabeordners (Standard `outputs/`) und ein kurzer Name für den Lauf-Ordner |
| `--models-dir`, `--bin-dir` | wohin `setup.py` die Modelle und die Engine gelegt hat |
| `--vae auto` (Standard) | cuDNN float32; zuerst in einem Stück, dann zwei große Kacheln, dann die kleine Standardkachel |
| `--vae tiled` | cuDNN float32, immer zwei große Kacheln |
| `--vae legacy` | der Pfad von v0.1.0: kein cuDNN, kleine Kacheln. Wird automatisch (mit einer Warnung) verwendet, wenn die cuDNN-DLLs fehlen |

Schritte (8), cfg (1.0), Sampler und Scheduler sind absichtlich fest; siehe [Was läuft](#what-it-runs).

## Selbst überprüfen

- `generate.py` gibt als eine der letzten Zeilen `PIXEL_SHA256 <hex>` aus: einen Hash der decodierten Pixel. Führe denselben Befehl zweimal aus und vergleiche die beiden Bilder: `python scripts/compare.py <run A>/image.png <run B>/image.png` sollte `SAME_PIXELS` ausgeben.
- Der `PIXEL_SHA256` der fünf Beispiele auf unserem Rechner steht in [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md). Der Datei-Hash einer PNG kann abweichen, auch wenn die Pixel gleich sind, weil die PNG die Erzeugungsparameter als Text enthält; vergleiche Pixel, nicht Dateien.
- Ehrliche Grenze: Wir haben nicht gemessen, ob eine andere Karte oder ein anderer Treiber dieselben Pixel liefert.

## Warum es in 4 GB passt

- **Was die Modellautoren sagen.** Die Modellkarte von Z-Image-Turbo sagt, das Modell „fits comfortably within 16G VRAM consumer devices“ (passt bequem auf Consumer-Karten mit 16 GB VRAM) ([Modellkarte](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)). Das ist eine Aussage über Karten mit 16 GB. Die offizielle README nennt außerdem stable-diffusion.cpp als Option eines Drittanbieters und zitiert es mit „as little as 4GB of VRAM“ (mit nur 4 GB VRAM) ([README](https://github.com/Tongyi-MAI/Z-Image)); das ist eine Aussage des Projekts stable-diffusion.cpp, keine Anforderung des Z-Image-Teams.
- **Was wir gemessen haben.** Z-Image-Turbo Q8_0 (eine Datei von 6.6 GB) mit einem Qwen3-4B-Q8_0-Textencoder, 768x1344: Die GPU-Spitze, alle 2 s von nvidia-smi abgetastet (eine kurze Spitze kann verpasst werden), lag auf einer Karte mit 4096 MiB bei 2949 bis 2957 MiB (Engine v0.1.0) und bei 3057–3059 MiB (Engine v0.2.0). Die Gewichte (10 509 MiB; das Engine-Log gibt es als MB aus) bleiben im Arbeitsspeicher; die Engine kopiert das Netz jeweils ein Segment (einen Abschnitt des Netzes) auf einmal auf die GPU: 36 Segmente, wie in der Logzeile `z_image using 36 segments`.
- **Was es kostet.** Zeit und Arbeitsspeicher: 193–228 s pro Bild, und der Engine-Prozess belegt auf einem Rechner mit 16 GB etwa 10 667–10 915 MiB RAM (einschließlich der per Memory-Mapping eingeblendeten Modellseiten), sodass der freie RAM während des Laufs auf wenige hundert MiB sinkt.
- **Setups anderer.** Andere berichten von Z-Image auf Karten mit 4 GB mit stärkerer Quantisierung oder kleineren Größen (zum Beispiel empfiehlt die Wiki-Seite von stable-diffusion.cpp für Karten mit 4 GB Q3_K oder Q4_0 bei 1024x512). Dort, wo wir gesucht haben (Liste und Datum in [`docs/RELATED.md`](docs/RELATED.md)), haben wir kein veröffentlichtes Setup gefunden, das alle vier Punkte vereint: eine Karte mit 4 GB, Q8_0, 768x1344 oder größer sowie gemessene Zeit und gemessenen GPU-Speicher. Das ist eine Aussage darüber, wo wir gesucht haben, nicht über alle Orte.
- **Wer was macht.** Dass es in 4 GB passt, leistet stable-diffusion.cpp selbst: `--offload-to-cpu`, `--mmap`, die Arbeit in Abschnitten und Flash Attention (ohne sie verlangte ein Lauf 4205 MB und passte nicht). Unsere Patches dienen der Geschwindigkeit und einer besseren VAE-Stufe, nicht dem Hineinpassen. Die ungepatchte Upstream-Engine haben wir auf dieser Karte nicht ausgeführt, deshalb können wir nicht sagen, ob sie passt.

## Wie es funktioniert

Drei Änderungen auf stable-diffusion.cpp `master-1088-32d516c` (alle sind Schalter; die Tabelle in [`patches/README.md`](patches/README.md) führt jede mit ihrer Umgebungsvariable auf):

1. **Der Refiner läuft einmal pro Schritt.** Ein Gruppenname wurde doppelt verwendet, sodass vier Refiner-Blöcke ein zweites Mal berechnet wurden. Mit der Korrektur sind die Schritte 2 bis 8 jeweils etwa 1.3 s schneller (22.0 auf 20.7 s), bei pixelgleichem Bild (3 Bilder geprüft).
2. **VAE über cuDNN, in float32.** Die letzte Stufe (das Latent in Pixel umwandeln) nutzt jetzt die float32-Faltung von NVIDIA cuDNN. Auf unserer Karte sank die VAE-Zeit damit von 23 bis 27 s auf 10 bis 15 s, und der PSNR gegenüber der Referenz stieg von 38 bis 43 dB auf 45 bis 49 dB (große Kacheln).
3. **Zuerst in einem Stück.** Die Engine versucht jetzt, das ganze Bild in einem Stück zu decodieren, wenn die Speicherprüfung sagt, dass es passt (Reserve 256 MiB), weicht sonst auf zwei große Kacheln aus und danach auf kleine Kacheln. In einem Stück brauchte die VAE etwa 8–16 s, und der PSNR gegenüber der Referenz lag bei 71 bis 73 dB. Wenn ein erzwungener Rückfall eintritt, hat das Bild dieselben Pixel wie das gekachelte (mit `PIXEL_SHA256` geprüft). Was passiert ist, steht in `run.json` (`stages.vae_path`: `full`, `tile`, `floor` oder `retry`).

Außerdem: `--eager-load` (liest die Modellseiten vorab ein; 241.2 s auf 220.3 s beim selben Bild, Entwicklungs-Build, je ein Lauf) ist Teil des festen Befehls.

<a id="what-it-runs"></a>
## Was läuft

| Teil | Datei | Quelle |
|---|---|---|
| Diffusionsmodell | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), Basis [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Textencoder | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), Autoencoder vom Typ FLUX.1 |
| Engine | `sd-cli.exe`, stable-diffusion.cpp `32d516c` mit den Patches in [`patches/`](patches) | das Release v0.2.0 dieses Repositorys (`sinirsiz-foto-engine-v0.2.0-win-x64-cuda12.8-sm61.zip`) |
| CUDA-Laufzeit | `cudart`, `cublas`, `cublasLt` (12.8), unverändert | Zip aus dem Release v0.1.0 von wan22-pascal-4gb |
| cuDNN (standardmäßig installiert; `--no-cudnn` überspringt es) | 8 DLLs, Version 9.10.2.21 (CUDA-11-Build) | NVIDIAs eigener Server, unter NVIDIAs Lizenz; hier nicht gespeichert |

Feste Einstellungen: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`.
Wir senken die Schritte nicht, fügen keinen Negativ-Prompt hinzu und aktivieren kein Caching: Das Modell ist auf 8 Schritte destilliert und verwendet keine Negativ-Prompts (siehe [Prompts](docs/PROMPTS.md)).

## Grenzen (lesen, bevor du dich darauf verlässt)

- **Nur Windows.** Die vorgebaute Engine und diese Skripte gibt es nur für Windows.
- **Eine Karte, ein Rechner.** Gemessen nur auf einem Laptop mit GTX 1050 Ti 4 GB (i7-7700HQ, 16 GB RAM, Windows 10, Treiber 581.29, Modelle auf einer SSD). Andere GPUs und Treiber, Rechner mit weniger als 16 GB RAM, Linux und macOS: **nicht getestet**.
- **Die Engine ist nur für Pascal (sm_61) gebaut.** Andere Architekturen brauchen einen eigenen Build ([`docs/BUILD.md`](docs/BUILD.md)); wir haben keinen getestet.
- **cuDNN:** Wir haben mit dem CUDA-11-Build von cuDNN 9.10.2.21 gemessen. Der CUDA-12-Build hat andere Dateien und wurde nicht gemessen.
- **Der Speicher ist knapp.** Der freie RAM sinkt auf wenige hundert MiB; schließe andere Programme und erzeuge jeweils ein Bild. Wir haben nicht erlebt, dass der GPU-Speicher ausging, nachdem die Speicherprüfung der Engine bestanden war, und wir haben nicht getestet, was dann passiert.
- **Größen:** Getestet wurden nur 768x1344, 1344x768 und 1024x1024. Größere Formate geben eine Warnung aus und können den Speicher sprengen.
- Die Treue zum Prompt ist nur teilweise gegeben: Ein Bild folgt seinem Prompt nicht immer in jedem Detail. Text in Bildern und reale Wahrzeichen wurden nicht bewertet.
- Die PSNR-Referenz ist die CPU-Decodierung unserer eigenen Engine, keine unabhängige Implementierung.
- Die Zahlen in [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) stammen, sofern nichts anderes dasteht, aus je einem Lauf.

## Lizenz und Namensnennung

- Die Skripte und Dokumente dieses Repositorys: [Apache-2.0](LICENSE) mit einer [`NOTICE`](NOTICE)-Datei. Die Engine-Patches in [`patches/`](patches) stehen unter MIT, wie der Code, den sie ändern.
- stable-diffusion.cpp und ggml stehen unter MIT. Die Hinweise zum Drittanbieter-Code, der in die Engine einkompiliert ist, stehen in [`licenses/`](licenses) und [`THIRD_PARTY.md`](THIRD_PARTY.md).
- Modelldateien werden hier nicht gespeichert; sie werden von den oben genannten Quellen unter deren eigenen Lizenzen heruntergeladen (Hugging Face nennt für alle Apache-2.0, gelesen am 2026-11-13). Die Modellkarte sagt nichts darüber, wem erzeugte Bilder gehören, und wir erheben dazu keinen Anspruch.
- **cuDNN und die CUDA-Laufzeit sind Eigentum von NVIDIA** und fallen nicht unter die Lizenz dieses Repositorys. cuDNN wird vom Server von NVIDIA unter NVIDIAs Lizenz heruntergeladen (`--no-cudnn` überspringt es); die DLLs der CUDA-Laufzeit liegen in einem eigenen, unveränderten Zip (CUDA Toolkit EULA, Attachment A). Einzelheiten und was wir nicht überprüfen konnten: [`THIRD_PARTY.md`](THIRD_PARTY.md).
- **Namensnennung.** Die Datei `NOTICE` bei Kopien und abgeleiteten Werken beizubehalten ist die Bedingung (Apache-2.0, Abschnitt 4). Darüber hinaus freuen wir uns über eine Zeile wie "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey"; sie ist erwünscht, aber nicht vorgeschrieben.
- Bitte lies [`ETHICS.md`](ETHICS.md): Jedes Bild ist synthetisch, und für das, was du veröffentlichst, bist du verantwortlich.

## Mitmachen

Am meisten hilft es, **deine Karte zu testen** und uns zu schreiben, was passiert ist: Name der GPU, Treiber, RAM, die `run.json` und die letzten Zeilen des Logs (das Issue-Formular „Hardware test report“). Korrekturen an den Dokumenten und an den Skripten sind ebenfalls willkommen; siehe [`CONTRIBUTING.md`](CONTRIBUTING.md). Sicherheitsmeldungen gehen über den privaten Weg in [`SECURITY.md`](SECURITY.md).

[Installationsanleitung für KI-Agenten](AGENTS.md) · [Messungen](docs/MEASUREMENTS.md) · [Fehlerbehebung](docs/TROUBLESHOOTING.md) · [Die Engine bauen](docs/BUILD.md) · [Patches](patches/README.md) · [Prompts](docs/PROMPTS.md) · [Drittanbieter](THIRD_PARTY.md) · [Änderungsprotokoll](CHANGELOG.md)

Diese Seite wurde mit Hilfe von KI lokalisiert; Korrekturen sind sehr willkommen, siehe [`CONTRIBUTING.md`](CONTRIBUTING.md).
