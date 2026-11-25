[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · **Italiano** · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**Generazione di immagini da testo con Z-Image-Turbo (Q8_0 GGUF) a 768x1344 su una GTX 1050 Ti da 4 GB (Pascal, sm_61), con stable-diffusion.cpp, su Windows.** Misurato su un portatile con 16 GB di RAM, dove il processo usa circa 11 GB di RAM. Lo stesso seed dà gli stessi pixel, pixel per pixel; le misure e le patch del motore sono pubbliche, i download sono fissati con sha256 e un agente di programmazione AI può eseguire l'installazione passo per passo.

*Non ufficiale. Nessun legame con Tongyi-MAI (Z-Image), leejet (stable-diffusion.cpp) o NVIDIA.*

## Da dove iniziare

Esiste un pacchetto già pronto, quindi provalo per primo. Se il tuo hardware è diverso o un passaggio non riesce, tutto il resto è aperto: le patch, la ricetta di compilazione e le misure sono in questo repository, così puoi compilare per la tua scheda o adattarle.

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

Il passo 2 scarica circa 12.2 GB e, una volta, sulla nostra connessione ha richiesto 29 minuti; per prima cosa stampa un blocco "Preflight" (la tua GPU, la RAM e lo spazio libero su disco accanto a quanto abbiamo misurato; serve solo a informare).
È stata misurata soltanto la scheda del portatile GTX 1050 Ti da 4 GB (Pascal, compute capability 6.1). Le altre schede non sono state testate.
Se usi un agente di programmazione AI (Claude Code, Codex, Cursor e simili), indirizzalo a [`AGENTS.md`](AGENTS.md).

## In breve

Rispetto all'impostazione della v0.1.0: un'immagine richiede 188–193 s invece di 261.6 s, la fase VAE richiede 12.5–21.7 s invece di 29.8 fino a 36.3 s, lo stesso seed dà gli stessi pixel e dietro ogni numero di questo README c'è un comando e un file.

768x1344, seed 42, 8 passi, stessa macchina. I numeri della v0.1.0 vengono dal README della v0.1.0 (test a radice pulita e cinque esecuzioni); quelli della v0.3.0 vengono dal test a radice pulita di questa release.

| | v0.1.0 (mai pubblicata; vecchia impostazione) | v0.3.0 |
|---|---|---|
| Tempo per un'immagine (un'esecuzione di `generate.py`) | 261.6 s | 188–193 s |
| Decodifica VAE (ultima fase) | da 29.8 a 36.3 s | 12.5–21.7 s |
| Vicinanza a una decodifica di riferimento (PSNR, più alto è meglio) | da 38 a 43 dB | da 71 a 73 dB |
| Picco di memoria GPU (nvidia-smi) | da 2949 a 2957 MiB | 3057–3059 MiB |
| Memoria del processo, picco | da 10.5 a 10.9 GB (come registrato allora) | 10 489–11 203 MiB |
| RAM libera minima osservata | da 331 a 576 MiB | 303–532 MiB |

Come leggerla: il riferimento è lo stesso latent decodificato sulla CPU in un unico blocco float32; il PSNR confronta con esso la nostra decodifica su GPU (3 immagini). Dice quanto la fase VAE è vicina a quel riferimento. Non dice quanto sia bella un'immagine. Le immagini della v0.2.0 non sono identiche byte per byte a quelle della v0.1.0 con lo stesso prompt e lo stesso seed, perché il percorso VAE è cambiato di proposito. Metodo e parti non misurate: [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md).

## Esempi

**Generate con l'AI con questo repository** (Z-Image-Turbo Q8_0, seed 42, 8 passi). Non sono fotografie reali; monumenti e dettagli
possono essere inesatti, e un'immagine non sempre segue il prompt in ogni dettaglio. I prompt esatti sono in [`prompts/`](prompts) e in [`docs/PROMPTS.md`](docs/PROMPTS.md).

| | | |
|---|---|---|
| ![Torre Eiffel all'ora d'oro](docs/examples/eiffel.jpg) | ![Bicchiere di tè turco](docs/examples/turkish_tea.jpg) | ![Pescatore anziano](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![Villaggio sul pendio](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![Istanbul vista dall'alto](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. Non è una foto reale; i monumenti possono essere inesatti.

## Avvio rapido

Requisiti: Windows 10/11, una GPU NVIDIA da 4 GB, un driver che supporti CUDA 12.8 (è stato misurato il driver 581.29; i driver più vecchi non sono stati testati; il runtime CUDA vero e proprio viene scaricato per te), Python 3.10 o successivo,
git, circa 14 GB di disco libero (i download sono circa 12.2 GB con cuDNN; il dato sul disco libero è una stima) e 16 GB di RAM (è quanto è stato misurato; con meno non è stato testato).

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- `setup.py` stampa prima un blocco "Preflight" (la tua GPU, la RAM e lo spazio libero su disco accanto a quanto abbiamo misurato; serve solo a informare e non blocca mai nulla). Poi scarica dagli indirizzi fissati in [`models.lock.json`](models.lock.json) e verifica ogni file con sha256. Stampa `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK`, poi `CUDNN_OK` oppure `CUDNN_SKIPPED` e infine `SETUP_OK`.
  Senza `--models-dir` e `--bin-dir` usa `models/` e `bin/` nella radice del repository; metti i modelli su un SSD (è stato misurato solo con un SSD).
  Fermalo quando vuoi con Ctrl+C e rilancia lo stesso comando: i download riprendono dai file `.part`.
- **cuDNN viene installato per impostazione predefinita e non fa parte di questo repository.** È software NVIDIA, con la licenza di NVIDIA ([testo della licenza](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)), per sistemi con GPU NVIDIA. Si scarica dal server di NVIDIA senza che venga richiesto alcun pagamento e senza registrazione né accesso, e nella licenza non abbiamo trovato alcuna clausola che limiti l'uso commerciale o personale. `setup.py` mostra l'indirizzo della licenza, scarica il file e copia solo otto DLL accanto a `sd-cli.exe`. La licenza di NVIDIA dice che chi non ne accetta i termini non deve scaricare, installare né usare il software; in quel caso esegui `python scripts/setup.py --no-cudnn`. Senza cuDNN tutto funziona con il percorso VAE più lento della v0.1.0 (`--vae legacy`), e `generate.py` te lo dice.
- `generate.py` scrive `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, `run.json` (tempo, fasi, quale percorso VAE è stato eseguito, picco di memoria GPU, il comando esatto) e `log.txt`, e stampa `IMAGE_OK <path>`.

## Uso

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| Opzione | Significato |
|---|---|
| `--prompt "<text>"` oppure `--prompt-file <txt>` | il prompt (uno dei due è obbligatorio) |
| `--width`, `--height` | multipli di 16, da 256 a 2048; predefinito 768x1344; testati: 768x1344, 1344x768, 1024x1024 |
| `--seed` | predefinito 42 |
| `--out`, `--name` | cartella radice dell'output (predefinita `outputs/`) e un nome breve per la cartella dell'esecuzione |
| `--models-dir`, `--bin-dir` | dove `setup.py` ha messo i modelli e il motore |
| `--vae auto` (predefinito) | cuDNN float32; prima prova in un unico blocco, poi due tile grandi, poi il tile piccolo predefinito |
| `--vae tiled` | cuDNN float32, sempre due tile grandi |
| `--vae legacy` | il percorso della v0.1.0: senza cuDNN, tile piccoli. Usato in automatico (con un avviso) quando mancano le DLL di cuDNN |

I passi (8), il cfg (1.0), il sampler e lo scheduler sono fissi di proposito; vedi [Cosa esegue](#what-it-runs).

## Verifica da solo

- `generate.py` stampa `PIXEL_SHA256 <hex>` tra le ultime righe: un hash dei pixel decodificati. Esegui due volte lo stesso comando e confronta le due immagini: `python scripts/compare.py <run A>/image.png <run B>/image.png` dovrebbe stampare `SAME_PIXELS`.
- Il `PIXEL_SHA256` dei cinque esempi sulla nostra macchina è in [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md). L'hash del file di un PNG può essere diverso anche quando i pixel sono gli stessi, perché il PNG contiene i parametri di generazione come testo; confronta i pixel, non i file.
- Limite onesto: non abbiamo misurato se un'altra scheda o un altro driver dia gli stessi pixel.

## Perché entra in 4 GB

- **Cosa dicono gli autori del modello.** La model card di Z-Image-Turbo dice che il modello "fits comfortably within 16G VRAM consumer devices" (entra comodamente in dispositivi consumer con 16 GB di VRAM) ([model card](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)). È un'affermazione sulle schede da 16 GB. Il README ufficiale elenca anche stable-diffusion.cpp come opzione di terze parti e lo cita per "as little as 4GB of VRAM" (anche solo 4 GB di VRAM) ([README](https://github.com/Tongyi-MAI/Z-Image)); è un'affermazione del progetto stable-diffusion.cpp, non un requisito del team di Z-Image.
- **Cosa abbiamo misurato.** Z-Image-Turbo Q8_0 (un file da 6.6 GB) con un text encoder Qwen3-4B Q8_0, 768x1344: il picco della GPU, campionato da nvidia-smi ogni 2 s (un picco breve può sfuggire), è stato tra 2949 e 2957 MiB (motore v0.1.0) e 3057–3059 MiB (motore v0.2.0) su una scheda da 4096 MiB. I pesi (10 509 MiB; il log del motore lo stampa come MB) restano nella RAM di sistema; il motore copia la rete sulla GPU un segmento alla volta (una fetta della rete): 36 segmenti, come nella riga di log `z_image using 36 segments`.
- **Quanto costa.** Tempo e memoria di sistema: 188–193 s per immagine, e il processo del motore occupa circa 10 489–11 203 MiB di RAM (comprese le pagine del modello mappate in memoria) su una macchina da 16 GB, quindi mentre lavora la RAM libera scende a poche centinaia di MiB.
- **Le configurazioni di altri.** Altri riferiscono di far girare Z-Image su schede da 4 GB con quantizzazione più bassa o dimensioni più piccole (per esempio la pagina wiki di stable-diffusion.cpp per le schede da 4 GB consiglia Q3_K o Q4_0 a 1024x512). Nei posti dove abbiamo cercato (elenco e data in [`docs/RELATED.md`](docs/RELATED.md)) non abbiamo trovato una configurazione pubblicata che metta insieme tutti e quattro: una scheda da 4 GB, Q8_0, 768x1344 o più grande, e tempo e memoria GPU misurati. È un'affermazione sui posti dove abbiamo cercato, non su ogni posto.
- **Chi fa cosa.** Se entra in 4 GB è merito di stable-diffusion.cpp stesso: `--offload-to-cpu`, `--mmap`, il lavoro a fette e la flash attention (con essa disattivata, un'esecuzione richiedeva 4205 MB e non entrava). Le nostre patch servono alla velocità e a una fase VAE migliore, non a farlo entrare. Non abbiamo eseguito il motore originale senza patch su questa scheda, quindi non possiamo dire se entri.

## Come funziona

Tre modifiche sopra stable-diffusion.cpp `master-1088-32d516c` (sono tutte interruttori; la tabella in [`patches/README.md`](patches/README.md) le elenca una per una con la relativa variabile d'ambiente):

1. **Il refiner viene eseguito una volta per passo.** Un nome di gruppo era usato due volte, quindi quattro blocchi del refiner venivano calcolati una seconda volta. Correggendolo, i passi da 2 a 8 sono più veloci di circa 1.3 s ciascuno (da 22.0 a 20.7 s) con un'immagine identica pixel per pixel (3 immagini verificate).
2. **VAE con cuDNN, in float32.** L'ultima fase (trasformare il latent in pixel) usa ora la convoluzione float32 di cuDNN di NVIDIA. Sulla nostra scheda ha ridotto il VAE da 23-27 s a 10-15 s e ha portato il PSNR rispetto al riferimento da 38-43 dB a 45-49 dB (con tile grandi).
3. **Prima in un unico blocco.** Il motore ora prova a decodificare l'intera immagine in un unico blocco quando il controllo della memoria dice che ci sta (margine 256 MiB), ripiega su due tile grandi e poi su tile piccoli. In un unico blocco il VAE ha richiesto circa 8–16 s e il PSNR rispetto al riferimento è stato tra 71 e 73 dB. Se avviene un ripiego forzato, l'immagine ha gli stessi pixel di quella a tile (verificato con `PIXEL_SHA256`). Cosa è successo viene scritto in `run.json` (`stages.vae_path`: `full`, `tile`, `floor` oppure `retry`).

Inoltre: `--eager-load` (legge in anticipo le pagine del modello; da 241.2 s a 220.3 s sulla stessa immagine, build di sviluppo, una sola esecuzione ciascuna) fa parte del comando fisso.

<a id="what-it-runs"></a>
## Cosa esegue

| Componente | File | Fonte |
|---|---|---|
| Modello di diffusione | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), base [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Text encoder | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), autoencoder di tipo FLUX.1 |
| Motore | `sd-cli.exe`, stable-diffusion.cpp `32d516c` con le patch in [`patches/`](patches) | la release v0.3.0 di questo repository (`sinirsiz-foto-engine-v0.3.0-win-x64-cuda12.8-sm61.zip`) |
| Runtime CUDA | `cudart`, `cublas`, `cublasLt` (12.8), non modificati | zip della release v0.1.0 di wan22-pascal-4gb |
| cuDNN (installato per impostazione predefinita; `--no-cudnn` lo salta) | 8 DLL, versione 9.10.2.21 (build per CUDA 11) | server di NVIDIA, con la licenza di NVIDIA; non è conservato qui |

Impostazioni fisse: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`.
Non riduciamo i passi, non aggiungiamo un negative prompt e non attiviamo la cache: il modello è distillato per 8 passi e non usa negative prompt (vedi [prompt](docs/PROMPTS.md)).

## Limiti (leggi prima di fare affidamento)

- **Solo Windows.** Il motore precompilato e questi script sono solo per Windows.
- **Una scheda, una macchina.** Misurato solo su un portatile con GTX 1050 Ti da 4 GB (i7-7700HQ, 16 GB di RAM, Windows 10, driver 581.29, modelli su SSD). Altre GPU e altri driver, macchine con meno di 16 GB di RAM, Linux e macOS: **non testati**.
- Altre schede e sistemi (quale strada esiste, e un test della community su una scheda AMD con Linux che non abbiamo eseguito noi): [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md).
- **Il motore è compilato solo per Pascal (sm_61).** Le altre architetture richiedono una compilazione tua ([`docs/BUILD.md`](docs/BUILD.md)); non ne abbiamo testata nessuna.
- **cuDNN:** abbiamo misurato con la build per CUDA 11 di cuDNN 9.10.2.21. La build per CUDA 12 ha file diversi e non è stata misurata.
- **La memoria è al limite.** La RAM libera scende a poche centinaia di MiB; chiudi gli altri programmi e genera un'immagine alla volta. Non abbiamo visto la memoria GPU esaurirsi dopo che il controllo della memoria del motore era passato, e non abbiamo testato cosa succede in quel caso.
- **Dimensioni:** sono state testate solo 768x1344, 1344x768 e 1024x1024. Le dimensioni maggiori stampano un avviso e possono esaurire la memoria.
- La fedeltà al prompt è parziale: un'immagine non sempre segue il prompt in ogni dettaglio. Il testo dentro le immagini e i monumenti reali non sono stati valutati.
- Il riferimento del PSNR è la decodifica su CPU del nostro stesso motore, non un'implementazione indipendente.
- I numeri in [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) vengono da una sola esecuzione ciascuno, salvo diversa indicazione.

## Licenza e crediti

- Gli script e i documenti di questo repository: [Apache-2.0](LICENSE) con un file [`NOTICE`](NOTICE). Le patch del motore in [`patches/`](patches) sono MIT, come il codice che modificano.
- stable-diffusion.cpp e ggml sono MIT. Le note sul codice di terze parti compilato nel motore sono in [`licenses/`](licenses) e in [`THIRD_PARTY.md`](THIRD_PARTY.md).
- I file dei modelli non sono conservati qui; vengono scaricati dalle fonti indicate sopra, con le rispettive licenze (Hugging Face indica Apache-2.0 per tutti, letto il 2026-11-13). La model card non dice nulla su a chi appartengano le immagini generate, e noi non avanziamo alcuna pretesa in merito.
- **cuDNN e il runtime CUDA sono proprietà di NVIDIA** e non sono sotto la licenza di questo repository. cuDNN viene scaricato dal server di NVIDIA con la licenza di NVIDIA (`--no-cudnn` lo salta); le DLL del runtime CUDA sono in uno zip separato e non modificato (CUDA Toolkit EULA, Attachment A). Dettagli e ciò che non abbiamo potuto verificare: [`THIRD_PARTY.md`](THIRD_PARTY.md).
- **Crediti.** Conservare il file `NOTICE` insieme alle copie e alle opere derivate è la condizione (Apache-2.0, sezione 4). Oltre a questo, una riga come "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey" è gradita, non obbligatoria.
- Leggi [`ETHICS.md`](ETHICS.md): ogni immagine è sintetica e sei tu il responsabile di ciò che pubblichi.

## Contribuire

La cosa più utile che puoi fare è **testare la tua scheda** e raccontarci com'è andata: nome della GPU, driver, RAM, il `run.json` e le ultime righe del log (il modulo di segnalazione "Hardware test report"). Sono benvenute anche le correzioni ai documenti e agli script; vedi [`CONTRIBUTING.md`](CONTRIBUTING.md). Le segnalazioni di sicurezza passano dal canale privato descritto in [`SECURITY.md`](SECURITY.md).

[Guida all'installazione per agenti AI](AGENTS.md) · [Misure](docs/MEASUREMENTS.md) · [Risoluzione dei problemi](docs/TROUBLESHOOTING.md) · [Compilare il motore](docs/BUILD.md) · [Patch](patches/README.md) · [Prompt](docs/PROMPTS.md) · [Terze parti](THIRD_PARTY.md) · [Registro delle modifiche](CHANGELOG.md)

Questa pagina è stata localizzata con l'aiuto dell'AI; le correzioni sono molto gradite, vedi [`CONTRIBUTING.md`](CONTRIBUTING.md).
