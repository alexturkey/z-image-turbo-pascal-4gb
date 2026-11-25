[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · **Polski** · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**Generowanie obrazów z tekstu modelem Z-Image-Turbo (Q8_0 GGUF) w rozdzielczości 768x1344 na karcie GTX 1050 Ti z 4 GB pamięci (Pascal, sm_61), przez stable-diffusion.cpp, w systemie Windows.** Pomiary wykonano na laptopie z 16 GB RAM-u; proces zajmuje około 11 GB pamięci RAM. Ten sam seed daje te same piksele, piksel w piksel; pomiary i łatki silnika są opublikowane, pobierane pliki są przypięte przez sha256, a agent AI do programowania może przeprowadzić instalację krok po kroku.

*Projekt nieoficjalny. Niepowiązany z Tongyi-MAI (Z-Image), leejet (stable-diffusion.cpp) ani NVIDIA.*

## Zacznij tutaj

Gotowa paczka istnieje, więc najpierw wypróbuj ją. Jeśli masz inny sprzęt albo któryś krok się nie powiedzie, reszta jest otwarta: łatki, przepis na kompilację i pomiary są w tym repozytorium, więc możesz zbudować silnik pod własną kartę albo dostosować przepis.

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

Krok 2 pobiera około 12.2 GB; u nas, na naszym łączu, zajął raz 29 minut. Najpierw wypisuje blok "Preflight" (twoja karta, RAM i wolne miejsce na dysku obok tego, co zmierzyliśmy; blok tylko informuje).
Zmierzono wyłącznie laptopową kartę GTX 1050 Ti 4 GB (Pascal, compute capability 6.1). Innych kart nie testowano.
Jeśli korzystasz z agenta AI do programowania (Claude Code, Codex, Cursor i podobnych), wskaż mu plik [`AGENTS.md`](AGENTS.md).

## W skrócie

W porównaniu z układem v0.1.0: jeden obraz powstaje w 188–193 s zamiast 261.6 s, etap VAE trwa 12.5–21.7 s zamiast 29.8 do 36.3 s, ten sam seed daje te same piksele, a za każdą liczbą w tym README stoi polecenie i plik.

768x1344, seed 42, 8 kroków, ta sama maszyna. Liczby dla v0.1.0 pochodzą z README wersji v0.1.0 (test na czystym katalogu głównym i pięć uruchomień); liczby dla v0.3.0 pochodzą z testu na czystym katalogu głównym tego wydania.

| | v0.1.0 (nieopublikowana; stary układ) | v0.3.0 |
|---|---|---|
| Czas jednego obrazu (jedno uruchomienie `generate.py`) | 261.6 s | 188–193 s |
| Dekodowanie VAE (ostatni etap) | 29.8 do 36.3 s | 12.5–21.7 s |
| Zgodność z dekodowaniem wzorcowym (PSNR, wyżej znaczy bliżej) | 38 do 43 dB | 71 do 73 dB |
| Szczyt pamięci GPU (nvidia-smi) | 2949 do 2957 MiB | 3057–3059 MiB |
| Pamięć procesu, szczyt | 10.5 do 10.9 GB (tak, jak zapisano wtedy) | 10 489–11 203 MiB |
| Najniższa zaobserwowana wolna pamięć RAM | 331 do 576 MiB | 303–532 MiB |

Jak to czytać: wzorzec to ten sam latent zdekodowany na CPU w jednym kawałku, w float32; PSNR porównuje z nim nasze dekodowanie na GPU (3 obrazy). Mówi, jak blisko tego wzorca jest etap VAE. Nie mówi, jak dobrze obraz wygląda. Obrazy z v0.2.0 nie są identyczne bajt w bajt z v0.1.0 dla tego samego promptu i seeda, bo ścieżka VAE została zmieniona celowo. Metoda i to, czego nie zmierzono: [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md).

## Przykłady

**Wygenerowane przez AI za pomocą tego repozytorium** (Z-Image-Turbo Q8_0, seed 42, 8 kroków). To nie są prawdziwe fotografie; budowle i szczegóły
mogą być niedokładne, a obraz nie zawsze odtwarza prompt w każdym szczególe. Dokładne prompty są w [`prompts/`](prompts) i [`docs/PROMPTS.md`](docs/PROMPTS.md).

| | | |
|---|---|---|
| ![Wieża Eiffla o złotej godzinie](docs/examples/eiffel.jpg) | ![Szklanka tureckiej herbaty](docs/examples/turkish_tea.jpg) | ![Starszy rybak](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![Wioska na zboczu wzgórza](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![Stambuł z lotu ptaka](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. To nie jest prawdziwe zdjęcie; budowle mogą być niedokładne.

## Szybki start

Wymagania: Windows 10/11, karta NVIDIA z 4 GB pamięci, sterownik obsługujący CUDA 12.8 (zmierzono ze sterownikiem 581.29; starszych sterowników nie testowano; sam runtime CUDA jest pobierany za ciebie), Python 3.10 lub nowszy,
git, około 14 GB wolnego miejsca na dysku (pobierane pliki to około 12.2 GB razem z cuDNN; wartość wolnego miejsca jest szacunkowa) oraz 16 GB RAM-u (tyle zmierzono; mniej nie było testowane).

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- `setup.py` najpierw wypisuje blok "Preflight" (twoja karta, RAM i wolne miejsce na dysku obok tego, co zmierzyliśmy; tylko informuje i niczego nie blokuje). Następnie pobiera pliki z przypiętych adresów w [`models.lock.json`](models.lock.json) i sprawdza każdy z nich przez sha256. Wypisuje `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK`, potem `CUDNN_OK` albo `CUDNN_SKIPPED`, a na końcu `SETUP_OK`.
  Bez `--models-dir` i `--bin-dir` używa katalogów `models/` i `bin/` w głównym katalogu repozytorium; umieść modele na dysku SSD (mierzono tylko SSD).
  Możesz przerwać w dowolnej chwili przez Ctrl+C i uruchomić to samo polecenie ponownie: pobieranie jest kontynuowane z plików `.part`.
- **cuDNN jest instalowany domyślnie i nie jest częścią tego repozytorium.** To oprogramowanie NVIDIA na własnej licencji NVIDIA ([tekst licencji](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)), dla systemów z kartami NVIDIA. Pobiera się z serwera NVIDIA bez żądania opłaty i bez logowania, a w licencji nie znaleźliśmy zapisu, który ograniczałby użycie komercyjne lub osobiste. `setup.py` pokazuje adres licencji, pobiera plik i kopiuje obok `sd-cli.exe` tylko osiem plików DLL. Licencja NVIDIA stanowi, że kto nie akceptuje jej warunków, nie może go pobierać, instalować ani używać; w takim przypadku uruchom `python scripts/setup.py --no-cudnn`. Bez cuDNN wszystko działa wolniejszą ścieżką VAE z v0.1.0 (`--vae legacy`), a `generate.py` informuje o tym.
- `generate.py` zapisuje `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, `run.json` (czas, etapy, którą ścieżką VAE przeszło generowanie, szczyt pamięci GPU, dokładne polecenie) i `log.txt`, a na końcu wypisuje `IMAGE_OK <path>`.

## Użycie

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| Opcja | Znaczenie |
|---|---|
| `--prompt "<text>"` lub `--prompt-file <txt>` | prompt (wymagana jest jedna z dwóch opcji) |
| `--width`, `--height` | wielokrotności 16, od 256 do 2048; domyślnie 768x1344; testowane: 768x1344, 1344x768, 1024x1024 |
| `--seed` | domyślnie 42 |
| `--out`, `--name` | katalog główny wyników (domyślnie `outputs/`) i krótka nazwa katalogu uruchomienia |
| `--models-dir`, `--bin-dir` | gdzie `setup.py` umieścił modele i silnik |
| `--vae auto` (domyślnie) | cuDNN float32; najpierw w jednym kawałku, potem dwoma dużymi kafelkami, potem małym kafelkiem domyślnym |
| `--vae tiled` | cuDNN float32, zawsze dwa duże kafelki |
| `--vae legacy` | ścieżka z v0.1.0: bez cuDNN, małe kafelki. Używana automatycznie (z ostrzeżeniem), gdy brakuje bibliotek DLL cuDNN |

Kroki (8), cfg (1.0), sampler i scheduler są celowo stałe; zobacz [Co jest uruchamiane](#what-it-runs).

## Sprawdź sam

- `generate.py` wypisuje `PIXEL_SHA256 <hex>` w jednym z ostatnich wierszy: to skrót zdekodowanych pikseli. Uruchom to samo polecenie dwa razy i porównaj oba obrazy: `python scripts/compare.py <run A>/image.png <run B>/image.png` powinno wypisać `SAME_PIXELS`.
- `PIXEL_SHA256` pięciu przykładów na naszej maszynie znajduje się w [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md). Skrót pliku PNG może się różnić, nawet gdy piksele są takie same, bo PNG przechowuje parametry generowania jako tekst; porównuj piksele, a nie pliki.
- Uczciwe ograniczenie: nie mierzyliśmy, czy inna karta lub inny sterownik daje te same piksele.

## Dlaczego mieści się w 4 GB

- **Co mówią autorzy modelu.** Karta modelu Z-Image-Turbo podaje, że model "fits comfortably within 16G VRAM consumer devices" (mieści się swobodnie w konsumenckich urządzeniach z 16 GB pamięci graficznej) ([karta modelu](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)). To stwierdzenie o kartach 16 GB. Oficjalne README wymienia też stable-diffusion.cpp jako opcję zewnętrzną i przytacza je ze słowami "as little as 4GB of VRAM" (zaledwie 4 GB pamięci graficznej) ([README](https://github.com/Tongyi-MAI/Z-Image)); to deklaracja projektu stable-diffusion.cpp, a nie wymóg zespołu Z-Image.
- **Co zmierzyliśmy.** Z-Image-Turbo Q8_0 (plik 6.6 GB) z enkoderem tekstu Qwen3-4B Q8_0, 768x1344: szczyt pamięci GPU, próbkowany przez nvidia-smi co 2 s (krótki skok może umknąć), wyniósł 2949 do 2957 MiB (silnik v0.1.0) i 3057–3059 MiB (silnik v0.2.0) na karcie z 4096 MiB. Wagi (10 509 MiB; log silnika wypisuje to jako MB) pozostają w pamięci RAM; silnik kopiuje sieć na GPU po jednym segmencie (wycinku sieci): 36 segmentów, jak w wierszu logu `z_image using 36 segments`.
- **Ile to kosztuje.** Czas i pamięć systemową: 188–193 s na obraz, a proces silnika zajmuje około 10 489–11 203 MiB RAM-u (razem ze stronami modelu mapowanymi w pamięci) na maszynie z 16 GB, więc w trakcie pracy wolny RAM spada do kilkuset MiB.
- **Konfiguracje innych osób.** Inni zgłaszają uruchamianie Z-Image na kartach 4 GB z niższą kwantyzacją lub mniejszymi rozmiarami (na przykład strona wiki stable-diffusion.cpp dla kart 4 GB zaleca Q3_K lub Q4_0 przy 1024x512). Tam, gdzie szukaliśmy (lista i data w [`docs/RELATED.md`](docs/RELATED.md)), nie znaleźliśmy opublikowanej konfiguracji łączącej wszystkie cztery warunki: kartę 4 GB, Q8_0, 768x1344 lub więcej oraz zmierzony czas i pamięć GPU. To stwierdzenie o tym, gdzie szukaliśmy, a nie o wszystkich miejscach.
- **Kto za co odpowiada.** Zmieszczenie się w 4 GB zapewnia sam stable-diffusion.cpp: `--offload-to-cpu`, `--mmap`, praca na wycinkach i flash attention (przy wyłączonym uruchomienie potrzebowało 4205 MB i się nie zmieściło). Nasze łatki służą szybkości i lepszemu etapowi VAE, a nie temu, żeby się zmieścić. Nie uruchamialiśmy oryginalnego silnika bez łatek na tej karcie, więc nie wiemy, czy by się zmieścił.

## Jak to działa

Trzy zmiany na bazie stable-diffusion.cpp `master-1088-32d516c` (wszystkie są przełącznikami; tabela w [`patches/README.md`](patches/README.md) wymienia każdą z nich wraz ze zmienną środowiskową):

1. **Refiner działa raz na krok.** Nazwa grupy została użyta dwa razy, przez co cztery bloki refinera liczyły się drugi raz. Po poprawce kroki od 2 do 8 są szybsze o około 1.3 s każdy (z 22.0 do 20.7 s), a obraz jest identyczny piksel w piksel (sprawdzono na 3 obrazach).
2. **VAE przez cuDNN, w float32.** Ostatni etap (zamiana latentu na piksele) używa teraz splotu float32 z NVIDIA cuDNN. Na naszej karcie skrócił VAE z 23–27 s na 10–15 s i podniósł PSNR względem wzorca z 38–43 dB na 45–49 dB (przy dużych kafelkach).
3. **Najpierw jeden kawałek.** Silnik próbuje teraz zdekodować cały obraz w jednym kawałku, gdy kontrola pamięci wskazuje, że się zmieści (zapas 256 MiB), potem wraca do dwóch dużych kafelków, a następnie do małych. W jednym kawałku VAE trwało około 8–16 s, a PSNR względem wzorca wyniósł 71 do 73 dB. Jeśli nastąpi wymuszony powrót do kafelków, obraz ma te same piksele co ten z kafelków (sprawdzono przez `PIXEL_SHA256`). To, co się wydarzyło, jest zapisane w `run.json` (`stages.vae_path`: `full`, `tile`, `floor` lub `retry`).

Ponadto: `--eager-load` (wczytuje strony modelu z góry; z 241.2 s na 220.3 s na tym samym obrazie, wersja rozwojowa, po jednym uruchomieniu) jest częścią stałego polecenia.

<a id="what-it-runs"></a>
## Co jest uruchamiane

| Element | Plik | Źródło |
|---|---|---|
| Model dyfuzyjny | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), baza [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Enkoder tekstu | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), autoenkoder typu FLUX.1 |
| Silnik | `sd-cli.exe`, stable-diffusion.cpp `32d516c` z łatkami z [`patches/`](patches) | wydanie v0.3.0 tego repozytorium (`sinirsiz-foto-engine-v0.3.0-win-x64-cuda12.8-sm61.zip`) |
| Runtime CUDA | `cudart`, `cublas`, `cublasLt` (12.8), bez zmian | zip z wydania wan22-pascal-4gb v0.1.0 |
| cuDNN (instalowany domyślnie; `--no-cudnn` go pomija) | 8 plików DLL, wersja 9.10.2.21 (kompilacja dla CUDA 11) | serwer NVIDIA, na warunkach licencji NVIDIA; nie jest tu przechowywany |

Stałe ustawienia: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`.
Nie zmniejszamy liczby kroków, nie dodajemy negatywnego promptu i nie włączamy cache'owania: model jest destylowany do 8 kroków i nie używa negatywnych promptów (zobacz [prompty](docs/PROMPTS.md)).

## Ograniczenia (przeczytaj, zanim zaczniesz na tym polegać)

- **Tylko Windows.** Gotowy silnik i te skrypty działają wyłącznie w systemie Windows.
- **Jedna karta, jedna maszyna.** Zmierzono tylko na laptopie z GTX 1050 Ti 4 GB (i7-7700HQ, 16 GB RAM-u, Windows 10, sterownik 581.29, modele na dysku SSD). Inne karty graficzne i sterowniki, maszyny z mniej niż 16 GB RAM-u, Linux i macOS: **nie testowano**.
- Inne karty i systemy (jaka ścieżka istnieje oraz test społeczności na karcie AMD pod Linuksem, którego sami nie uruchamialiśmy): [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md).
- **Silnik jest zbudowany tylko dla Pascala (sm_61).** Inne architektury wymagają własnej kompilacji ([`docs/BUILD.md`](docs/BUILD.md)); żadnej nie testowaliśmy.
- **cuDNN:** mierzyliśmy z kompilacją cuDNN 9.10.2.21 dla CUDA 11. Kompilacja dla CUDA 12 ma inne pliki i nie była mierzona.
- **Pamięci jest mało.** Wolny RAM spada do kilkuset MiB; zamknij inne programy i generuj jeden obraz naraz. Nie widzieliśmy, żeby pamięć GPU się skończyła po przejściu kontroli pamięci przez silnik, i nie testowaliśmy, co się wtedy dzieje.
- **Rozmiary:** testowano tylko 768x1344, 1344x768 i 1024x1024. Większe rozmiary wypisują ostrzeżenie i mogą wyczerpać pamięć.
- Zgodność z promptem jest częściowa: obraz nie zawsze odtwarza prompt w każdym szczególe. Tekstu wewnątrz obrazów i rzeczywistych budowli nie oceniano.
- Wzorzec PSNR to dekodowanie na CPU naszego własnego silnika, a nie niezależna implementacja.
- Liczby w [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) pochodzą z jednego uruchomienia każda, chyba że zapisano inaczej.

## Licencja i uznanie autorstwa

- Skrypty i dokumenty tego repozytorium: [Apache-2.0](LICENSE) wraz z plikiem [`NOTICE`](NOTICE). Łatki silnika w [`patches/`](patches) są na licencji MIT, tak jak kod, który zmieniają.
- stable-diffusion.cpp i ggml są na licencji MIT. Informacje o kodzie zewnętrznym skompilowanym w silniku znajdują się w [`licenses/`](licenses) i [`THIRD_PARTY.md`](THIRD_PARTY.md).
- Plików modeli tu nie ma; są pobierane z podanych wyżej źródeł na ich własnych licencjach (Hugging Face podaje Apache-2.0 dla wszystkich, odczytano 2026-11-13). Karta modelu nic nie mówi o tym, do kogo należą wygenerowane obrazy, i my też niczego w tej sprawie nie twierdzimy.
- **cuDNN i runtime CUDA są własnością NVIDIA** i nie podlegają licencji tego repozytorium. cuDNN jest pobierany z serwera NVIDIA na warunkach licencji NVIDIA (`--no-cudnn` go pomija); biblioteki DLL runtime CUDA znajdują się w osobnym, niezmienionym zipie (CUDA Toolkit EULA, Attachment A). Szczegóły i to, czego nie udało nam się zweryfikować: [`THIRD_PARTY.md`](THIRD_PARTY.md).
- **Uznanie autorstwa.** Zachowanie pliku `NOTICE` razem z kopiami i pracami pochodnymi jest warunkiem (Apache-2.0, sekcja 4). Ponad to będziemy wdzięczni za linijkę w rodzaju "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey", ale to prośba, nie wymóg.
- Przeczytaj, proszę, [`ETHICS.md`](ETHICS.md): każdy obraz jest syntetyczny, a za to, co publikujesz, odpowiadasz ty.

## Współtworzenie

Najbardziej pomocne jest **przetestowanie własnej karty** i napisanie nam, co się stało: nazwa GPU, sterownik, RAM, `run.json` i ostatnie wiersze logu (formularz zgłoszenia "Hardware test report"). Poprawki dokumentów i skryptów też są mile widziane; zobacz [`CONTRIBUTING.md`](CONTRIBUTING.md). Zgłoszenia dotyczące bezpieczeństwa wysyłaj prywatną drogą opisaną w [`SECURITY.md`](SECURITY.md).

[Instrukcja instalacji dla agentów AI](AGENTS.md) · [Pomiary](docs/MEASUREMENTS.md) · [Rozwiązywanie problemów](docs/TROUBLESHOOTING.md) · [Budowanie silnika](docs/BUILD.md) · [Łatki](patches/README.md) · [Prompty](docs/PROMPTS.md) · [Komponenty zewnętrzne](THIRD_PARTY.md) · [Lista zmian](CHANGELOG.md)

Ta strona została zlokalizowana z pomocą AI; poprawki są bardzo mile widziane, zobacz [`CONTRIBUTING.md`](CONTRIBUTING.md).
