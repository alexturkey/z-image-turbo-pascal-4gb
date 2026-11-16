[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · **한국어** · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**Z-Image-Turbo (Q8_0 GGUF)로 768x1344 텍스트-이미지 변환을, 4 GB GTX 1050 Ti (Pascal, sm_61)에서 stable-diffusion.cpp로, Windows에서 실행합니다.** RAM 16 GB 노트북에서 측정했으며, 프로세스는 RAM을 약 11 GB 사용합니다. 같은 시드는 픽셀 단위로 같은 픽셀을 만듭니다. 측정값과 엔진 패치는 공개되어 있고, 다운로드는 sha256으로 고정되어 있으며, AI 코딩 에이전트가 설치를 단계별로 진행할 수 있습니다.

*비공식 프로젝트입니다. Tongyi-MAI (Z-Image), leejet (stable-diffusion.cpp), NVIDIA와는 제휴 관계가 없습니다.*

## 시작하기

미리 만들어 둔 패키지가 있으니 먼저 그것을 써 보세요. 하드웨어가 다르거나 어느 단계에서 막히면 나머지는 모두 공개되어 있습니다. 패치, 빌드 방법, 측정값이 이 저장소에 있으므로 자신의 그래픽 카드에 맞게 빌드하거나 고쳐 쓸 수 있습니다.

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

2단계는 약 12.2 GB를 내려받으며, 저희 회선에서 한 번 실행했을 때 29분이 걸렸습니다. 먼저 "Preflight" 블록을 출력합니다(내 GPU, RAM, 남은 디스크 용량을 저희가 측정한 값과 나란히 보여 주며, 알려 주기만 합니다).
GTX 1050 Ti 4 GB 노트북 카드(Pascal, compute capability 6.1)만 측정했습니다. 다른 카드는 테스트하지 않았습니다.
AI 코딩 에이전트(Claude Code, Codex, Cursor 등)를 쓴다면 [`AGENTS.md`](AGENTS.md)를 보게 하세요.

## 한눈에 보기

v0.1.0 구성과 비교하면, 이미지 한 장에 261.6 s 대신 193–228 s가 걸리고, VAE 단계는 29.8 ~ 36.3 s 대신 8.3–15.9 s가 걸립니다. 같은 시드는 같은 픽셀을 만들며, 이 README의 모든 숫자에는 그 뒤에 명령어와 파일이 있습니다.

768x1344, 시드 42, 8 스텝, 같은 컴퓨터입니다. v0.1.0 수치는 v0.1.0 README(클린 루트 테스트와 5회 실행)에서, v0.2.0 수치는 이번 릴리스의 클린 루트 테스트에서 가져왔습니다.

| | v0.1.0 (미공개, 이전 구성) | v0.2.0 |
|---|---|---|
| 이미지 한 장에 걸리는 시간 (`generate.py` 1회 실행) | 261.6 s | 193–228 s |
| VAE 디코딩 (마지막 단계) | 29.8 ~ 36.3 s | 8.3–15.9 s |
| 기준 디코딩과의 근접도 (PSNR, 높을수록 가까움) | 38 ~ 43 dB | 71 ~ 73 dB |
| GPU 메모리 최고치 (nvidia-smi) | 2949 ~ 2957 MiB | 3057–3059 MiB |
| 프로세스 메모리, 최고치 | 10.5 ~ 10.9 GB (당시 기록 그대로) | 10 667–10 915 MiB |
| 관측된 가장 낮은 여유 RAM | 331 ~ 576 MiB | 418–545 MiB |

읽는 방법: 기준은 같은 latent를 CPU에서 float32 한 덩어리로 디코딩한 결과입니다. PSNR은 저희 GPU 디코딩을 그 기준과 비교한 값입니다(이미지 3장). VAE 단계가 그 기준에 얼마나 가까운지를 알려 줄 뿐, 이미지가 얼마나 좋아 보이는지는 알려 주지 않습니다. 같은 프롬프트와 시드라도 v0.2.0 이미지는 v0.1.0과 바이트 단위로 같지 않습니다. VAE 경로를 의도적으로 바꿨기 때문입니다. 측정 방법과 측정하지 않은 부분: [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md).

## 예시

**이 저장소로 AI가 생성한 이미지** (Z-Image-Turbo Q8_0, 시드 42, 8 스텝). 실제 사진이 아니며, 건물과 세부 묘사는
부정확할 수 있고, 이미지가 모든 세부에서 프롬프트를 그대로 따르지 않을 수도 있습니다. 정확한 프롬프트는 [`prompts/`](prompts)와 [`docs/PROMPTS.md`](docs/PROMPTS.md)에 있습니다.

| | | |
|---|---|---|
| ![황금빛 시간대의 에펠탑](docs/examples/eiffel.jpg) | ![튀르키예식 찻잔](docs/examples/turkish_tea.jpg) | ![나이 든 어부](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![언덕 비탈의 마을](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![하늘에서 본 이스탄불](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. 실제 사진이 아니며, 건물이 부정확할 수 있습니다.

## 빠른 설치

요구 사항: Windows 10/11, 4 GB NVIDIA GPU, CUDA 12.8을 지원하는 드라이버(드라이버 581.29로 측정했고 그보다 오래된 드라이버는 테스트하지 않았습니다. CUDA 런타임 자체는 자동으로 내려받습니다), Python 3.10 이상,
git, 여유 디스크 약 14 GB(cuDNN 포함 다운로드가 약 12.2 GB이며, 여유 디스크 수치는 추정치입니다), RAM 16 GB(측정한 사양이며 그보다 적은 경우는 테스트하지 않았습니다).

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- `setup.py`는 먼저 "Preflight" 블록을 출력합니다(내 GPU, RAM, 남은 디스크 용량을 저희가 측정한 값과 나란히 보여 주며, 알려 주기만 할 뿐 아무것도 막지 않습니다). 그다음 [`models.lock.json`](models.lock.json)에 고정된 주소에서 내려받고 모든 파일을 sha256으로 검사합니다. `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK`, 이어서 `CUDNN_OK` 또는 `CUDNN_SKIPPED`를 출력하고, 마지막으로 `SETUP_OK`를 출력합니다.
  `--models-dir`과 `--bin-dir`를 주지 않으면 저장소 루트의 `models/`와 `bin/`를 사용합니다. 모델은 SSD에 두세요(SSD에서만 측정했습니다).
  Ctrl+C로 언제든 중단하고 같은 명령을 다시 실행할 수 있으며, 다운로드는 `.part` 파일부터 이어집니다.
- **cuDNN은 기본으로 설치되며 이 저장소에 포함되어 있지 않습니다.** NVIDIA 자체 라이선스가 적용되는 NVIDIA 소프트웨어이며, NVIDIA GPU가 있는 시스템용입니다. NVIDIA 서버에서 결제나 로그인 없이 내려받을 수 있고, 라이선스에서 상업적 또는 개인적 사용을 제한하는 조항은 저희가 찾지 못했습니다([라이선스 전문](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)). `setup.py`는 라이선스 주소를 보여 주고, 파일을 내려받아 DLL 여덟 개만 `sd-cli.exe` 옆에 복사합니다. NVIDIA의 라이선스에는 그 조건에 동의하지 않는 사람은 내려받거나 설치하거나 사용해서는 안 된다고 적혀 있습니다. 그런 경우에는 `python scripts/setup.py --no-cudnn`을 실행하세요. cuDNN 없이도 모든 것이 더 느린 v0.1.0 VAE 경로(`--vae legacy`)로 동작하며, `generate.py`가 그 사실을 알려 줍니다.
- `generate.py`는 `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, `run.json`(시간, 단계, 어느 VAE 경로가 실행되었는지, GPU 메모리 최고치, 실제 명령어), `log.txt`를 쓰고 `IMAGE_OK <path>`를 출력합니다.

## 사용법

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| 옵션 | 의미 |
|---|---|
| `--prompt "<text>"` 또는 `--prompt-file <txt>` | 프롬프트 (둘 중 하나는 필수) |
| `--width`, `--height` | 16의 배수, 256 ~ 2048, 기본값 768x1344, 테스트한 크기: 768x1344, 1344x768, 1024x1024 |
| `--seed` | 기본값 42 |
| `--out`, `--name` | 출력 폴더의 루트(기본값 `outputs/`)와 실행 폴더에 붙일 짧은 이름 |
| `--models-dir`, `--bin-dir` | `setup.py`가 모델과 엔진을 둔 위치 |
| `--vae auto` (기본값) | cuDNN float32. 먼저 한 덩어리로, 안 되면 큰 타일 두 개로, 그다음 작은 기본 타일로 |
| `--vae tiled` | cuDNN float32, 항상 큰 타일 두 개 |
| `--vae legacy` | v0.1.0 경로: cuDNN 없음, 작은 타일. cuDNN DLL이 없으면 (경고와 함께) 자동으로 사용됩니다 |

스텝(8), cfg(1.0), 샘플러, 스케줄러는 의도적으로 고정되어 있습니다. [무엇을 실행하는가](#what-it-runs)를 참고하세요.

## 직접 확인하기

- `generate.py`는 마지막 줄 중 하나로 `PIXEL_SHA256 <hex>`를 출력합니다. 디코딩된 픽셀의 해시입니다. 같은 명령을 두 번 실행해 두 이미지를 비교해 보세요. `python scripts/compare.py <run A>/image.png <run B>/image.png`는 `SAME_PIXELS`를 출력해야 합니다.
- 저희 컴퓨터에서 얻은 예시 이미지 다섯 개의 `PIXEL_SHA256`은 [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md)에 있습니다. PNG에는 생성 파라미터가 텍스트로 들어 있기 때문에, 픽셀이 같아도 PNG 파일 해시는 다를 수 있습니다. 파일이 아니라 픽셀을 비교하세요.
- 솔직한 한계: 다른 카드나 드라이버에서도 같은 픽셀이 나오는지는 측정하지 않았습니다.

## 4 GB에 들어가는 이유

- **모델 제작자의 설명.** Z-Image-Turbo 모델 카드에는 모델이 "fits comfortably within 16G VRAM consumer devices"(16 GB VRAM 소비자용 장치에 여유 있게 들어간다)라고 적혀 있습니다([모델 카드](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)). 이것은 16 GB 카드에 대한 서술입니다. 공식 README는 stable-diffusion.cpp도 서드파티 선택지로 나열하며 "as little as 4GB of VRAM"(VRAM 4 GB만으로도)이라고 인용합니다([README](https://github.com/Tongyi-MAI/Z-Image)). 이는 stable-diffusion.cpp 프로젝트의 주장이지 Z-Image 팀의 요구 사항이 아닙니다.
- **저희가 측정한 것.** Z-Image-Turbo Q8_0(6.6 GB 파일)과 Qwen3-4B Q8_0 텍스트 인코더, 768x1344에서 nvidia-smi가 2 s마다 샘플링한 GPU 최고치(짧은 급등은 놓칠 수 있습니다)는 4096 MiB 카드에서 2949 ~ 2957 MiB(v0.1.0 엔진), 3057–3059 MiB(v0.2.0 엔진)였습니다. 가중치(10 509 MiB, 엔진 로그에는 MB로 출력됨)는 시스템 RAM에 남아 있고, 엔진은 네트워크를 한 번에 한 세그먼트(네트워크의 한 조각)씩 GPU로 복사합니다. 로그의 `z_image using 36 segments` 줄처럼 36개 세그먼트입니다.
- **치르는 비용.** 시간과 시스템 메모리입니다. 이미지 한 장에 193–228 s가 걸리고, 16 GB 컴퓨터에서 엔진 프로세스가 RAM을 약 10 667–10 915 MiB(메모리 매핑된 모델 페이지 포함) 차지하므로, 실행 중에는 여유 RAM이 수백 MiB로 떨어집니다.
- **다른 사람들의 구성.** 다른 사용자들은 4 GB 카드에서 더 낮은 양자화나 더 작은 크기로 Z-Image를 돌렸다고 보고합니다(예를 들어 4 GB 카드용 stable-diffusion.cpp 위키 페이지는 1024x512에서 Q3_K 또는 Q4_0을 권합니다). 저희가 찾아본 곳([`docs/RELATED.md`](docs/RELATED.md)에 목록과 날짜)에서는 4 GB 카드, Q8_0, 768x1344 이상, 측정된 시간과 GPU 메모리라는 네 가지를 모두 갖춘 공개 구성을 찾지 못했습니다. 이것은 저희가 찾아본 곳에 대한 서술이며, 모든 곳에 대한 서술이 아닙니다.
- **누가 무엇을 하는가.** 4 GB에 들어가게 하는 것은 stable-diffusion.cpp 자체입니다. `--offload-to-cpu`, `--mmap`, 조각 단위 처리, 그리고 flash attention이 그 역할을 합니다(flash attention을 끄면 한 번의 실행에 4205 MB가 필요해 들어가지 않았습니다). 저희 패치는 속도와 더 나은 VAE 단계를 위한 것이지 메모리에 맞추기 위한 것이 아닙니다. 패치하지 않은 업스트림 엔진은 이 카드에서 실행해 보지 않았으므로, 그것이 들어가는지는 말할 수 없습니다.

## 동작 원리

stable-diffusion.cpp `master-1088-32d516c` 위에 세 가지를 바꿨습니다(모두 스위치이며, [`patches/README.md`](patches/README.md)의 표에 각각의 환경 변수가 정리되어 있습니다).

1. **리파이너는 스텝마다 한 번만 실행됩니다.** 그룹 이름이 두 번 쓰이는 바람에 리파이너(refiner) 블록 네 개가 한 번 더 계산되고 있었습니다. 이를 고치자 2 ~ 8번째 스텝이 각각 약 1.3 s 빨라졌고(22.0 s에서 20.7 s), 이미지는 픽셀 단위로 같습니다(이미지 3장 확인).
2. **cuDNN을 통한 VAE, float32.** 마지막 단계(latent를 픽셀로 바꾸는 단계)가 이제 NVIDIA cuDNN의 float32 합성곱을 사용합니다. 저희 카드에서는 VAE가 23 ~ 27 s에서 10 ~ 15 s로 줄었고, 기준 대비 PSNR이 38 ~ 43 dB에서 45 ~ 49 dB로 올랐습니다(큰 타일 사용).
3. **먼저 한 덩어리로.** 이제 엔진은 메모리 검사에서 들어간다고 판단하면(여유 256 MiB) 이미지 전체를 한 덩어리로 디코딩해 보고, 안 되면 큰 타일 두 개로, 그다음 작은 타일로 물러납니다. 한 덩어리일 때 VAE는 약 8–16 s가 걸렸고 기준 대비 PSNR은 71 ~ 73 dB였습니다. 강제로 물러난 경우에도 타일 방식과 같은 픽셀이 나옵니다(`PIXEL_SHA256`으로 확인). 실제로 일어난 일은 `run.json`에 기록됩니다(`stages.vae_path`: `full`, `tile`, `floor` 또는 `retry`).

추가로, `--eager-load`(모델 페이지를 미리 읽음. 같은 이미지에서 241.2 s가 220.3 s로, 개발 빌드, 각각 한 번 실행)는 고정 명령에 포함되어 있습니다.

<a id="what-it-runs"></a>
## 무엇을 실행하는가

| 구성 요소 | 파일 | 출처 |
|---|---|---|
| 디퓨전 모델 | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), 기반 모델 [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| 텍스트 인코더 | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), FLUX.1 계열 오토인코더 |
| 엔진 | `sd-cli.exe`, stable-diffusion.cpp `32d516c`에 [`patches/`](patches)의 패치를 적용 | 이 저장소의 v0.2.0 릴리스 (`sinirsiz-foto-engine-v0.2.0-win-x64-cuda12.8-sm61.zip`) |
| CUDA 런타임 | `cudart`, `cublas`, `cublasLt` (12.8), 수정하지 않음 | wan22-pascal-4gb v0.1.0 릴리스의 zip |
| cuDNN (기본으로 설치됨, `--no-cudnn`으로 건너뜀) | DLL 8개, 버전 9.10.2.21 (CUDA 11 빌드) | NVIDIA 자체 서버, NVIDIA의 라이선스에 따라 받음. 여기에는 저장하지 않음 |

고정 설정: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`.
스텝 수를 줄이거나, 네거티브 프롬프트를 넣거나, 캐싱을 켜지 않습니다. 이 모델은 8 스텝용으로 증류되었고 네거티브 프롬프트를 사용하지 않습니다([프롬프트](docs/PROMPTS.md) 참고).

## 한계 (의존하기 전에 읽어 주세요)

- **Windows 전용.** 미리 빌드된 엔진과 이 스크립트들은 Windows 전용입니다.
- **카드 한 종류, 컴퓨터 한 대.** GTX 1050 Ti 4 GB 노트북(i7-7700HQ, RAM 16 GB, Windows 10, 드라이버 581.29, 모델은 SSD)에서만 측정했습니다. 다른 GPU와 드라이버, RAM이 16 GB 미만인 컴퓨터, Linux, macOS는 **테스트하지 않았습니다**.
- 다른 카드와 시스템(어떤 경로가 있는지, 그리고 우리가 직접 실행하지 않은 Linux의 AMD 카드 커뮤니티 테스트): [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md).
- **엔진은 Pascal (sm_61)용으로만 빌드되었습니다.** 다른 아키텍처는 직접 빌드해야 합니다([`docs/BUILD.md`](docs/BUILD.md)). 저희는 직접 빌드해 보지 않았습니다.
- **cuDNN:** cuDNN 9.10.2.21의 CUDA 11 빌드로 측정했습니다. CUDA 12 빌드는 파일 구성이 다르며 측정하지 않았습니다.
- **메모리가 빠듯합니다.** 여유 RAM이 수백 MiB까지 떨어지므로 다른 프로그램을 닫고 한 번에 이미지 한 장씩 만드세요. 엔진의 메모리 검사를 통과한 뒤에 GPU 메모리가 부족해지는 경우는 본 적이 없으며, 그럴 때 어떻게 되는지는 테스트하지 않았습니다.
- **크기:** 768x1344, 1344x768, 1024x1024만 테스트했습니다. 더 큰 크기는 경고를 출력하며 메모리가 부족해질 수 있습니다.
- 프롬프트 충실도는 부분적입니다. 이미지가 모든 세부에서 프롬프트를 그대로 따르지 않을 수 있습니다. 이미지 안의 글자와 실제 세계의 건물은 평가하지 않았습니다.
- PSNR 기준은 저희 엔진 자체의 CPU 디코딩이며, 독립된 구현이 아닙니다.
- [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md)의 수치는 별도 표기가 없으면 각각 한 번의 실행에서 나온 것입니다.

## 라이선스와 출처 표기

- 이 저장소의 스크립트와 문서: [Apache-2.0](LICENSE), [`NOTICE`](NOTICE) 파일 포함. [`patches/`](patches)의 엔진 패치는 수정 대상 코드와 같은 MIT입니다.
- stable-diffusion.cpp와 ggml은 MIT입니다. 엔진에 컴파일되어 들어간 서드파티 코드의 고지문은 [`licenses/`](licenses)와 [`THIRD_PARTY.md`](THIRD_PARTY.md)에 있습니다.
- 모델 파일은 여기에 저장하지 않으며, 위의 출처에서 각자의 라이선스에 따라 내려받습니다(Hugging Face에는 모두 Apache-2.0으로 표시되어 있으며, 2026-11-13에 확인했습니다). 모델 카드는 생성된 이미지의 소유자에 대해 아무 말도 하지 않으며, 저희도 이에 대해 어떤 주장도 하지 않습니다.
- **cuDNN과 CUDA 런타임은 NVIDIA의 자산**이며 이 저장소의 라이선스가 적용되지 않습니다. cuDNN은 NVIDIA 서버에서 NVIDIA의 라이선스에 따라 내려받습니다(`--no-cudnn`으로 건너뜀). CUDA 런타임 DLL은 별도의 수정하지 않은 zip에 들어 있습니다(CUDA Toolkit EULA, Attachment A). 자세한 내용과 저희가 확인하지 못한 부분: [`THIRD_PARTY.md`](THIRD_PARTY.md).
- **출처 표기.** 사본과 파생물에 `NOTICE` 파일을 함께 두는 것은 조건입니다(Apache-2.0, 4항). 그 밖에 "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey" 같은 한 줄을 넣어 주시면 감사하겠지만, 필수는 아닙니다.
- [`ETHICS.md`](ETHICS.md)를 읽어 주세요. 모든 이미지는 합성된 것이며, 게시하는 내용에 대한 책임은 게시하는 사람에게 있습니다.

## 기여하기

가장 도움이 되는 일은 **내 카드를 테스트**하고 결과를 알려 주는 것입니다. GPU 이름, 드라이버, RAM, `run.json`, 로그의 마지막 몇 줄을 보내 주세요("Hardware test report" 이슈 양식). 문서와 스크립트의 수정도 환영합니다. [`CONTRIBUTING.md`](CONTRIBUTING.md)를 참고하세요. 보안 제보는 [`SECURITY.md`](SECURITY.md)의 비공개 경로로 보내 주세요.

[AI 에이전트용 설치 안내](AGENTS.md) · [측정값](docs/MEASUREMENTS.md) · [문제 해결](docs/TROUBLESHOOTING.md) · [엔진 빌드](docs/BUILD.md) · [패치](patches/README.md) · [프롬프트](docs/PROMPTS.md) · [서드파티](THIRD_PARTY.md) · [변경 이력](CHANGELOG.md)

이 문서는 AI의 도움으로 한국어로 옮겼습니다. 어색한 표현이나 오류를 알려 주시면 큰 도움이 됩니다. 방법은 [`CONTRIBUTING.md`](CONTRIBUTING.md)를 참고하세요.
