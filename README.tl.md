[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · **Tagalog** · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**Z-Image-Turbo (Q8_0 GGUF) text-to-image sa 768x1344 gamit ang 4 GB na GTX 1050 Ti (Pascal, sm_61), sa pamamagitan ng stable-diffusion.cpp, sa Windows.** Sinukat ito sa isang laptop na may 16 GB na RAM, kung saan gumagamit ang proseso ng humigit-kumulang 11 GB ng RAM. Ang parehong seed ay nagbibigay ng parehong mga pixel, pixel por pixel; nakabukas ang mga sukat at ang mga patch ng engine, naka-pin ang mga download gamit ang sha256, at kayang i-install ng isang AI coding agent ito nang hakbang-hakbang.

*Hindi opisyal. Walang kaugnayan sa Tongyi-MAI (Z-Image), kay leejet (stable-diffusion.cpp) o sa NVIDIA.*

## Magsimula dito

May ready-made na package, kaya subukan mo muna iyon. Kung iba ang hardware mo o pumalya ang isang hakbang, bukas ang lahat ng iba pa: nasa repository na ito ang mga patch, ang build recipe at ang mga sukat, kaya puwede kang mag-build para sa sarili mong card o iangkop ang mga ito.

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

Nagda-download ang hakbang 2 ng humigit-kumulang 12.2 GB at inabot ito ng 29 minuto nang isang beses, sa koneksyon namin; naglalabas muna ito ng "Preflight" block (ang GPU, RAM at libreng disk mo, katabi ng mga sinukat namin; nagbibigay lang ito ng impormasyon).
Ang laptop card na GTX 1050 Ti 4 GB lang (Pascal, compute capability 6.1) ang sinukat. Hindi pa nasubukan ang ibang mga card.
Kung gumagamit ka ng AI coding agent (Claude Code, Codex, Cursor at mga katulad), ituro mo ito sa [`AGENTS.md`](AGENTS.md).

## Sa isang tingin

Kumpara sa layout ng v0.1.0: ang isang larawan ay tumatagal ng 188–193 s sa halip na 261.6 s, ang VAE stage ay tumatagal ng 12.5–21.7 s sa halip na 29.8 hanggang 36.3 s, ang parehong seed ay nagbibigay ng parehong mga pixel, at bawat numero sa README na ito ay may kasamang command at file na pinagmulan.

768x1344, seed 42, 8 hakbang, parehong makina. Ang mga numero ng v0.1.0 ay galing sa README ng v0.1.0 (clean-root test at limang takbo); ang mga numero ng v0.3.0 ay galing sa clean-root test ng release na ito.

| | v0.1.0 (hindi kailanman nailathala; lumang layout) | v0.3.0 |
|---|---|---|
| Oras para sa isang larawan (isang takbo ng `generate.py`) | 261.6 s | 188–193 s |
| VAE decode (huling stage) | 29.8 hanggang 36.3 s | 12.5–21.7 s |
| Pagkakalapit sa reference decode (PSNR, mas mataas ay mas malapit) | 38 hanggang 43 dB | 71 hanggang 73 dB |
| Peak na memorya ng GPU (nvidia-smi) | 2949 hanggang 2957 MiB | 3057–3059 MiB |
| Memorya ng proseso, peak | 10.5 hanggang 10.9 GB (ayon sa naitala noon) | 10 489–11 203 MiB |
| Pinakamababang libreng RAM na nakita | 331 hanggang 576 MiB | 303–532 MiB |

Paano basahin ito: ang reference ay ang parehong latent na na-decode sa CPU bilang isang pirasong float32; kinukumpara ng PSNR ang GPU decode namin sa reference na iyon (3 larawan). Sinasabi nito kung gaano kalapit ang VAE stage sa reference na iyon. Hindi nito sinasabi kung gaano kaganda ang isang larawan. Hindi byte-identical ang mga larawan ng v0.2.0 sa v0.1.0 para sa parehong prompt at seed, dahil sadyang binago ang VAE path. Paraan at mga bahaging hindi nasukat: [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md).

## Mga halimbawa

**Ginawa ng AI gamit ang repo na ito** (Z-Image-Turbo Q8_0, seed 42, 8 hakbang). Hindi ito mga tunay na litrato; maaaring mali ang mga landmark at detalye,
at hindi laging sinusunod ng larawan ang prompt nito sa bawat detalye. Nasa [`prompts/`](prompts) at [`docs/PROMPTS.md`](docs/PROMPTS.md) ang eksaktong mga prompt.

| | | |
|---|---|---|
| ![Eiffel Tower sa golden hour](docs/examples/eiffel.jpg) | ![Baso ng Turkish tea](docs/examples/turkish_tea.jpg) | ![Matandang mangingisda](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![Nayon sa gilid ng burol](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![Istanbul mula sa himpapawid](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. Hindi tunay na litrato; maaaring mali ang mga landmark.

## Mabilis na pag-install

Mga kailangan: Windows 10/11, isang NVIDIA GPU na may 4 GB, isang driver na sumusuporta sa CUDA 12.8 (driver 581.29 ang sinukat; hindi pa nasubukan ang mas lumang mga driver; ang CUDA runtime mismo ay dina-download para sa iyo), Python 3.10 o mas bago,
git, humigit-kumulang 14 GB na libreng disk (humigit-kumulang 12.2 GB ang mga download kasama ang cuDNN; tantiya lang ang bilang ng libreng disk), at 16 GB na RAM (ito ang sinukat; hindi pa nasubukan ang mas kaunti).

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- Naglalabas muna ang `setup.py` ng "Preflight" block (ang GPU, RAM at libreng disk mo, katabi ng mga sinukat namin; nagbibigay lang ito ng impormasyon at hindi kailanman humaharang). Pagkatapos ay nagda-download ito mula sa mga naka-pin na address sa [`models.lock.json`](models.lock.json) at sinusuri ang bawat file gamit ang sha256. Naglalabas ito ng `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK`, saka `CUDNN_OK` o `CUDNN_SKIPPED`, at sa huli `SETUP_OK`.
  Kapag walang `--models-dir` at `--bin-dir`, ginagamit nito ang `models/` at `bin/` sa root ng repo; ilagay ang mga model sa SSD (SSD lang ang sinukat).
  Puwede mo itong ihinto anumang oras gamit ang Ctrl+C at patakbuhin muli ang parehong command: nagpapatuloy ang mga download mula sa mga `.part` file.
- **Ini-install bilang default ang cuDNN at hindi ito bahagi ng repository na ito.** Software ito ng NVIDIA sa ilalim ng sariling lisensya ng NVIDIA ([teksto ng lisensya](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)), para sa mga system na may NVIDIA GPU. Dina-download ito mula sa server ng NVIDIA nang hindi humihingi ng bayad at walang sign-in (hindi kailangan ng account o login), at wala kaming nakitang sugnay sa lisensya na naglilimita sa komersyal o personal na paggamit. Ipinapakita ng `setup.py` ang address ng lisensya, dina-download ang file at walong DLL lang ang kinokopya sa tabi ng `sd-cli.exe`. Sinasabi ng lisensya ng NVIDIA na ang sinumang hindi tumatanggap sa mga tuntunin nito ay hindi dapat mag-download, mag-install o gumamit nito; sa ganoong kaso, patakbuhin ang `python scripts/setup.py --no-cudnn`. Kung wala ang cuDNN, gumagana pa rin ang lahat sa mas mabagal na VAE path ng v0.1.0 (`--vae legacy`), at sinasabi iyon ng `generate.py`.
- Sumusulat ang `generate.py` ng `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, `run.json` (oras, mga stage, aling VAE path ang tumakbo, peak na memorya ng GPU, ang eksaktong command) at `log.txt`, at naglalabas ng `IMAGE_OK <path>`.

## Paggamit

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| Opsyon | Kahulugan |
|---|---|
| `--prompt "<text>"` o `--prompt-file <txt>` | ang prompt (isa sa dalawa ang kailangan) |
| `--width`, `--height` | multiple ng 16, 256 hanggang 2048; default 768x1344; nasubukan: 768x1344, 1344x768, 1024x1024 |
| `--seed` | default 42 |
| `--out`, `--name` | root ng output folder (default `outputs/`) at maikling pangalan para sa folder ng takbo |
| `--models-dir`, `--bin-dir` | kung saan inilagay ng `setup.py` ang mga model at ang engine |
| `--vae auto` (default) | cuDNN float32; subukan muna ang isang piraso, saka dalawang malaking tile, saka ang maliit na default na tile |
| `--vae tiled` | cuDNN float32, laging dalawang malaking tile |
| `--vae legacy` | ang v0.1.0 path: walang cuDNN, maliliit na tile. Awtomatikong ginagamit (may babala) kapag wala ang mga cuDNN DLL |

Sadyang nakapirmi ang mga hakbang (8), cfg (1.0), sampler at scheduler; tingnan ang [Ano ang pinapatakbo nito](#what-it-runs).

## Suriin mo mismo

- Naglalabas ang `generate.py` ng `PIXEL_SHA256 <hex>` bilang isa sa mga huling linya nito: isang hash ng mga na-decode na pixel. Patakbuhin ang parehong command nang dalawang beses at ikumpara ang dalawang larawan: dapat maglabas ng `SAME_PIXELS` ang `python scripts/compare.py <run A>/image.png <run B>/image.png`.
- Nasa [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) ang `PIXEL_SHA256` ng limang halimbawa sa makina namin. Maaaring magkaiba ang file hash ng isang PNG kahit pareho ang mga pixel, dahil dala ng PNG ang mga parameter ng pagbuo bilang teksto; ikumpara ang mga pixel, hindi ang mga file.
- Tapat na limitasyon: hindi namin sinukat kung nagbibigay ng parehong mga pixel ang ibang card o driver.

## Bakit kasya ito sa 4 GB

- **Ano ang sinasabi ng mga may-akda ng model.** Sinasabi ng model card ng Z-Image-Turbo na ang model ay "fits comfortably within 16G VRAM consumer devices" (kasyang-kasya sa mga consumer card na may 16 GB na VRAM) ([model card](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)). Pahayag iyon tungkol sa mga card na 16 GB. Nakalista rin sa opisyal na README ang stable-diffusion.cpp bilang third-party na opsyon at sinisipi ito para sa "as little as 4GB of VRAM" (kasing-liit ng 4 GB na VRAM) ([README](https://github.com/Tongyi-MAI/Z-Image)); pahayag iyon ng proyektong stable-diffusion.cpp, hindi kinakailangan mula sa Z-Image team.
- **Ano ang sinukat namin.** Z-Image-Turbo Q8_0 (isang 6.6 GB na file) na may Qwen3-4B Q8_0 na text encoder, 768x1344: ang peak ng GPU, na kinuha ng nvidia-smi bawat 2 s (maaaring makaligtaan ang maikling pagtaas), ay 2949 hanggang 2957 MiB (engine ng v0.1.0) at 3057–3059 MiB (engine ng v0.2.0) sa card na 4096 MiB. Nananatili sa RAM ng sistema ang mga weight (10 509 MiB; ipinapakita ito ng log ng engine bilang MB); kinokopya ng engine ang network sa GPU nang isang segment (isang hiwa ng network) sa bawat pagkakataon: 36 na segment, tulad ng linya ng log na `z_image using 36 segments`.
- **Ano ang kapalit.** Oras at memorya ng sistema: 188–193 s bawat larawan, at humahawak ang proseso ng engine ng humigit-kumulang 10 489–11 203 MiB ng RAM (kasama ang mga memory-mapped na pahina ng model) sa makinang may 16 GB, kaya bumababa ang libreng RAM sa ilang daang MiB habang tumatakbo ito.
- **Mga setup ng iba.** May mga nag-uulat ng Z-Image sa mga card na 4 GB gamit ang mas mababang quantization o mas maliliit na sukat (halimbawa, inirerekomenda ng wiki page ng stable-diffusion.cpp para sa mga card na 4 GB ang Q3_K o Q4_0 sa 1024x512). Sa mga tiningnan namin (listahan at petsa sa [`docs/RELATED.md`](docs/RELATED.md)), wala kaming nakitang nailathalang setup na pinagsasama ang apat: isang card na 4 GB, Q8_0, 768x1344 o mas malaki, at nasukat na oras at memorya ng GPU. Pahayag iyon tungkol sa mga tiningnan namin, hindi tungkol sa lahat ng lugar.
- **Sino ang gumagawa ng ano.** Ang stable-diffusion.cpp mismo ang nagpapakasya nito sa 4 GB: `--offload-to-cpu`, `--mmap`, pagtatrabaho nang hiwa-hiwa, at flash attention (kapag nakapatay ito, humingi ang isang takbo ng 4205 MB at hindi kumasya). Para sa bilis at mas mahusay na VAE stage ang mga patch namin, hindi para kumasya. Hindi namin pinatakbo ang hindi-na-patch na upstream engine sa card na ito, kaya hindi namin masasabi kung kasya ito.

## Paano ito gumagana

Tatlong pagbabago sa ibabaw ng stable-diffusion.cpp `master-1088-32d516c` (lahat ay mga switch; inililista ng talahanayan sa [`patches/README.md`](patches/README.md) ang bawat isa kasama ang environment variable nito):

1. **Isang beses lang tumatakbo ang refiner sa bawat hakbang.** Dalawang beses nagamit ang isang pangalan ng grupo, kaya ikalawang beses na kinompyut ang apat na refiner block. Nang maayos ito, bumilis nang humigit-kumulang 1.3 s ang bawat isa sa mga hakbang 2 hanggang 8 (22.0 hanggang 20.7 s) na may larawang pareho ang mga pixel (3 larawan ang sinuri).
2. **VAE sa pamamagitan ng cuDNN, sa float32.** Ginagamit na ng huling stage (ang pag-convert ng latent sa mga pixel) ang cuDNN float32 convolution ng NVIDIA. Sa card namin, ibinaba nito ang VAE mula 23 hanggang 27 s tungong 10 hanggang 15 s at itinaas ang PSNR laban sa reference mula 38 hanggang 43 dB tungong 45 hanggang 49 dB (malalaking tile).
3. **Isang piraso muna.** Sinusubukan na ngayon ng engine na i-decode ang buong larawan nang isang piraso kapag sinabi ng memory check na kasya ito (margin na 256 MiB), bumabalik sa dalawang malaking tile, at pagkatapos ay sa maliliit na tile. Sa isang piraso, tumagal nang humigit-kumulang 8–16 s ang VAE at 71 hanggang 73 dB ang PSNR laban sa reference. Kung may sapilitang pagbalik sa mas maliit na paraan, pareho ang mga pixel ng larawan sa bersyong may tile (sinuri gamit ang `PIXEL_SHA256`). Nakasulat sa `run.json` ang nangyari (`stages.vae_path`: `full`, `tile`, `floor` o `retry`).

Dagdag pa: ang `--eager-load` (binabasa nang maaga ang mga pahina ng model; 241.2 s hanggang 220.3 s sa parehong larawan, development build, tig-isang takbo) ay bahagi ng nakapirming command.

<a id="what-it-runs"></a>
## Ano ang pinapatakbo nito

| Bahagi | File | Pinagmulan |
|---|---|---|
| Diffusion model | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), base [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Text encoder | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), autoencoder na uri ng FLUX.1 |
| Engine | `sd-cli.exe`, stable-diffusion.cpp `32d516c` kasama ang mga patch sa [`patches/`](patches) | ang v0.3.0 release ng repository na ito (`sinirsiz-foto-engine-v0.3.0-win-x64-cuda12.8-sm61.zip`) |
| CUDA runtime | `cudart`, `cublas`, `cublasLt` (12.8), hindi binago | zip mula sa wan22-pascal-4gb v0.1.0 release |
| cuDNN (ini-install bilang default; nilalaktawan ito ng `--no-cudnn`) | 8 DLL, bersyon 9.10.2.21 (CUDA 11 build) | sariling server ng NVIDIA, sa ilalim ng lisensya ng NVIDIA; hindi ito itinatabi rito |

Mga nakapirming setting: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`.
Hindi namin ibinababa ang mga hakbang, hindi kami nagdaragdag ng negative prompt at hindi namin pinapagana ang caching: na-distill ang model para sa 8 hakbang at hindi gumagamit ng negative prompt (tingnan ang [mga prompt](docs/PROMPTS.md)).

## Mga limitasyon (basahin bago umasa rito)

- **Windows lang.** Para sa Windows lang ang prebuilt na engine at ang mga script na ito.
- **Isang card, isang makina.** Sa isang laptop na GTX 1050 Ti 4 GB lang ito sinukat (i7-7700HQ, 16 GB na RAM, Windows 10, driver 581.29, mga model sa SSD). Ibang mga GPU at driver, mga makinang wala pang 16 GB na RAM, Linux at macOS: **hindi pa nasubukan**.
- Ibang card at sistema (aling daan ang mayroon, at isang community test sa AMD card sa Linux na hindi namin pinatakbo mismo): [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md).
- **Para sa Pascal (sm_61) lang ang pagkaka-build ng engine.** Kailangan ng sarili mong build ang ibang arkitektura ([`docs/BUILD.md`](docs/BUILD.md)); wala kaming sinubukan.
- **cuDNN:** sinukat namin gamit ang CUDA 11 build ng cuDNN 9.10.2.21. Iba ang mga file ng CUDA 12 build at hindi ito nasukat.
- **Masikip ang memorya.** Bumababa ang libreng RAM sa ilang daang MiB; isara ang ibang mga programa, at isang larawan lang ang gawin sa bawat pagkakataon. Wala kaming nakitang naubusan ng memorya ang GPU matapos pumasa ang memory check ng engine, at hindi namin sinubukan kung ano ang nangyayari kapag ganoon.
- **Mga sukat:** 768x1344, 1344x768 at 1024x1024 lang ang nasubukan. Naglalabas ng babala ang mas malalaking sukat at maaaring maubusan ng memorya.
- Bahagya lang ang pagsunod sa prompt: hindi laging sinusunod ng larawan ang prompt nito sa bawat detalye. Hindi sinuri ang teksto sa loob ng mga larawan at ang mga tunay na landmark.
- Ang reference ng PSNR ay ang CPU decode ng sarili naming engine, hindi isang independiyenteng implementasyon.
- Ang mga numero sa [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) ay galing sa tig-isang takbo maliban kung may ibang nakasaad.

## Lisensya at kredito

- Mga script at dokumento ng repository na ito: [Apache-2.0](LICENSE) na may kasamang [`NOTICE`](NOTICE) na file. Ang mga patch ng engine sa [`patches/`](patches) ay MIT, tulad ng code na binabago nila.
- Ang stable-diffusion.cpp at ggml ay MIT. Ang mga abiso para sa third-party na code na kinompile sa engine ay nasa [`licenses/`](licenses) at [`THIRD_PARTY.md`](THIRD_PARTY.md).
- Hindi itinatabi rito ang mga model file; dina-download ang mga ito mula sa mga pinagmulan sa itaas sa ilalim ng kani-kanilang lisensya (Apache-2.0 ang nakalista ng Hugging Face para sa lahat ng mga ito, binasa noong 2026-11-13). Walang sinasabi ang model card tungkol sa kung sino ang may-ari ng mga nabuong larawan, at wala rin kaming inaangking anuman tungkol dito.
- **Pag-aari ng NVIDIA ang cuDNN at ang CUDA runtime** at wala sila sa ilalim ng lisensya ng repository na ito. Dina-download ang cuDNN mula sa server ng NVIDIA sa ilalim ng lisensya ng NVIDIA (nilalaktawan ito ng `--no-cudnn`); ang mga DLL ng CUDA runtime ay nasa hiwalay at hindi binagong zip (CUDA Toolkit EULA, Attachment A). Mga detalye at kung ano ang hindi namin napatunayan: [`THIRD_PARTY.md`](THIRD_PARTY.md).
- **Kredito.** Ang pag-iingat ng `NOTICE` file kasama ng mga kopya at derivative na gawa ang kondisyon (Apache-2.0, section 4). Higit pa roon, malugod naming tatanggapin, ngunit hindi ito kinakailangan, ang isang linya tulad ng "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey".
- Pakibasa ang [`ETHICS.md`](ETHICS.md): sintetiko ang bawat larawan, at ikaw ang responsable sa anumang ilalathala mo.

## Pag-ambag

Ang pinakamakatutulong na magagawa mo ay **subukan ang card mo** at ipaalam sa amin ang nangyari: pangalan ng GPU, driver, RAM, ang `run.json` at ang mga huling linya ng log (ang "Hardware test report" na issue form). Malugod ding tinatanggap ang mga pagwawasto sa mga dokumento at sa mga script; tingnan ang [`CONTRIBUTING.md`](CONTRIBUTING.md). Dumadaan ang mga ulat sa seguridad sa pribadong ruta sa [`SECURITY.md`](SECURITY.md).

[Gabay sa pag-install para sa mga AI agent](AGENTS.md) · [Mga sukat](docs/MEASUREMENTS.md) · [Pag-troubleshoot](docs/TROUBLESHOOTING.md) · [Pag-build ng engine](docs/BUILD.md) · [Mga patch](patches/README.md) · [Mga prompt](docs/PROMPTS.md) · [Third-party](THIRD_PARTY.md) · [Talaan ng mga pagbabago](CHANGELOG.md)

Isinalokal ang pahinang ito sa tulong ng AI, at malugod na tinatanggap ang mga pagwawasto; tingnan ang [`CONTRIBUTING.md`](CONTRIBUTING.md).
