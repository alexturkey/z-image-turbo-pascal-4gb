[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · **Português** · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**Geração de imagens a partir de texto com Z-Image-Turbo (Q8_0 GGUF) em 768x1344 numa GTX 1050 Ti de 4 GB (Pascal, sm_61), com stable-diffusion.cpp, no Windows.** Medido em um notebook com 16 GB de RAM, em que o processo usa cerca de 11 GB de RAM. A mesma seed gera os mesmos pixels, pixel a pixel; as medições e os patches do motor são públicos, os downloads são fixados com sha256 e um agente de programação com IA pode fazer a instalação passo a passo.

*Não oficial. Sem vínculo com a Tongyi-MAI (Z-Image), com o leejet (stable-diffusion.cpp) nem com a NVIDIA.*

## Comece por aqui

Existe um pacote pronto, então experimente ele primeiro. Se o seu hardware for diferente ou um passo falhar, todo o resto está aberto: os patches, a receita de compilação e as medições estão neste repositório, e você pode compilar para a sua placa ou adaptá-los.

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

O passo 2 baixa cerca de 12.2 GB e levou 29 minutos uma vez, na nossa conexão; antes de tudo ele imprime um bloco "Preflight" (a sua GPU, a RAM e o espaço livre em disco ao lado do que medimos; serve apenas para informar).
Só a placa de notebook GTX 1050 Ti de 4 GB (Pascal, compute capability 6.1) foi medida. As outras placas não foram testadas.
Se você usa um agente de programação com IA (Claude Code, Codex, Cursor e similares), aponte-o para [`AGENTS.md`](AGENTS.md).

## Em resumo

Em relação à estrutura da v0.1.0: uma imagem leva 193–228 s em vez de 261.6 s, a etapa do VAE leva 8.3–15.9 s em vez de 29.8 a 36.3 s, a mesma seed gera os mesmos pixels e por trás de cada número deste README há um comando e um arquivo.

768x1344, seed 42, 8 passos, mesma máquina. Os números da v0.1.0 vêm do README da v0.1.0 (teste em raiz limpa e cinco execuções); os da v0.2.0 vêm do teste em raiz limpa desta versão.

| | v0.1.0 (nunca publicada; estrutura antiga) | v0.2.0 |
|---|---|---|
| Tempo para uma imagem (uma execução de `generate.py`) | 261.6 s | 193–228 s |
| Decodificação do VAE (última etapa) | 29.8 a 36.3 s | 8.3–15.9 s |
| Proximidade de uma decodificação de referência (PSNR, quanto maior, melhor) | 38 a 43 dB | 71 a 73 dB |
| Pico de memória da GPU (nvidia-smi) | 2949 a 2957 MiB | 3057–3059 MiB |
| Memória do processo, pico | 10.5 a 10.9 GB (como registrado na época) | 10 667–10 915 MiB |
| Menor RAM livre observada | 331 a 576 MiB | 418–545 MiB |

Como ler: a referência é o mesmo latent decodificado na CPU em uma peça só, em float32; o PSNR compara com ela a nossa decodificação na GPU (3 imagens). Ele diz quão perto a etapa do VAE está dessa referência. Não diz se uma imagem é boa de ver. As imagens da v0.2.0 não são idênticas byte a byte às da v0.1.0 para o mesmo prompt e a mesma seed, porque o caminho do VAE mudou de propósito. Método e o que não foi medido: [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md).

## Exemplos

**Geradas por IA com este repositório** (Z-Image-Turbo Q8_0, seed 42, 8 passos). Não são fotografias reais; monumentos e detalhes
podem estar imprecisos, e uma imagem nem sempre segue o prompt em todos os detalhes. Os prompts exatos estão em [`prompts/`](prompts) e [`docs/PROMPTS.md`](docs/PROMPTS.md).

| | | |
|---|---|---|
| ![Torre Eiffel na hora dourada](docs/examples/eiffel.jpg) | ![Copo de chá turco](docs/examples/turkish_tea.jpg) | ![Pescador idoso](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![Vilarejo na encosta](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![Istambul vista do alto](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. Não é uma foto real; monumentos podem estar imprecisos.

## Início rápido

Requisitos: Windows 10/11, uma GPU NVIDIA de 4 GB, um driver que suporte CUDA 12.8 (o driver 581.29 foi medido; drivers mais antigos não foram testados; o próprio runtime do CUDA é baixado para você), Python 3.10 ou mais novo,
git, cerca de 14 GB de disco livre (os downloads somam cerca de 12.2 GB com cuDNN; o valor de disco livre é uma estimativa) e 16 GB de RAM (o que foi medido; com menos, não foi testado).

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- `setup.py` imprime primeiro um bloco "Preflight" (a sua GPU, a RAM e o espaço livre em disco ao lado do que medimos; serve apenas para informar e nunca bloqueia nada). Depois baixa dos endereços fixados em [`models.lock.json`](models.lock.json) e confere cada arquivo com sha256. Ele imprime `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK`, depois `CUDNN_OK` ou `CUDNN_SKIPPED` e, por fim, `SETUP_OK`.
  Sem `--models-dir` e `--bin-dir`, ele usa `models/` e `bin/` na raiz do repositório; coloque os modelos em um SSD (só com SSD foi medido).
  Interrompa quando quiser com Ctrl+C e rode o mesmo comando de novo: os downloads continuam a partir dos arquivos `.part`.
- **O cuDNN é instalado por padrão e não faz parte deste repositório.** É um software da NVIDIA, sob a licença da própria NVIDIA ([texto da licença](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)), para sistemas com GPU NVIDIA. Ele é baixado do servidor da NVIDIA sem que seja pedido nenhum pagamento e sem cadastro nem login, e não encontramos na licença nenhuma cláusula que limite o uso comercial ou pessoal. O `setup.py` mostra o endereço da licença, baixa o arquivo e copia só oito DLLs para junto de `sd-cli.exe`. A licença da NVIDIA diz que quem não aceita os termos dela não deve baixar, instalar nem usar o software; nesse caso, execute `python scripts/setup.py --no-cudnn`. Sem o cuDNN, tudo funciona com o caminho do VAE da v0.1.0, mais lento (`--vae legacy`), e o `generate.py` avisa isso.
- `generate.py` escreve `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, `run.json` (tempo, etapas, qual caminho do VAE rodou, pico de memória da GPU, o comando exato) e `log.txt`, e imprime `IMAGE_OK <path>`.

## Uso

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| Opção | Significado |
|---|---|
| `--prompt "<text>"` ou `--prompt-file <txt>` | o prompt (um dos dois é obrigatório) |
| `--width`, `--height` | múltiplos de 16, de 256 a 2048; padrão 768x1344; testados: 768x1344, 1344x768, 1024x1024 |
| `--seed` | padrão 42 |
| `--out`, `--name` | pasta raiz da saída (padrão `outputs/`) e um nome curto para a pasta da execução |
| `--models-dir`, `--bin-dir` | onde o `setup.py` colocou os modelos e o motor |
| `--vae auto` (padrão) | cuDNN float32; tenta primeiro uma peça só, depois dois tiles grandes, depois o tile pequeno padrão |
| `--vae tiled` | cuDNN float32, sempre dois tiles grandes |
| `--vae legacy` | o caminho da v0.1.0: sem cuDNN, tiles pequenos. Usado automaticamente (com um aviso) quando as DLLs do cuDNN estão ausentes |

Os passos (8), o cfg (1.0), o sampler e o scheduler são fixos de propósito; veja [O que ele executa](#what-it-runs).

## Confira você mesmo

- `generate.py` imprime `PIXEL_SHA256 <hex>` em uma das últimas linhas: um hash dos pixels decodificados. Rode o mesmo comando duas vezes e compare as duas imagens: `python scripts/compare.py <run A>/image.png <run B>/image.png` deve imprimir `SAME_PIXELS`.
- O `PIXEL_SHA256` dos cinco exemplos na nossa máquina está em [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md). O hash do arquivo de um PNG pode ser diferente mesmo quando os pixels são os mesmos, porque o PNG guarda os parâmetros de geração como texto; compare os pixels, não os arquivos.
- Limite honesto: não medimos se outra placa ou outro driver gera os mesmos pixels.

## Por que cabe em 4 GB

- **O que os autores do modelo dizem.** O model card do Z-Image-Turbo diz que o modelo "fits comfortably within 16G VRAM consumer devices" (cabe com folga em dispositivos de consumo com 16 GB de VRAM) ([model card](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)). Essa é uma afirmação sobre placas de 16 GB. O README oficial também lista o stable-diffusion.cpp como uma opção de terceiros e o cita com "as little as 4GB of VRAM" (com apenas 4 GB de VRAM) ([README](https://github.com/Tongyi-MAI/Z-Image)); essa é uma afirmação do projeto stable-diffusion.cpp, não um requisito da equipe do Z-Image.
- **O que medimos.** Z-Image-Turbo Q8_0 (um arquivo de 6.6 GB) com um text encoder Qwen3-4B Q8_0, 768x1344: o pico da GPU, amostrado pelo nvidia-smi a cada 2 s (um pico curto pode passar despercebido), ficou entre 2949 e 2957 MiB (motor v0.1.0) e em 3057–3059 MiB (motor v0.2.0) numa placa de 4096 MiB. Os pesos (10 509 MiB; o log do motor imprime como MB) ficam na RAM do sistema; o motor copia a rede para a GPU um segmento por vez (uma fatia da rede): 36 segmentos, como na linha de log `z_image using 36 segments`.
- **O que custa.** Tempo e memória do sistema: 193–228 s por imagem, e o processo do motor ocupa cerca de 10 667–10 915 MiB de RAM (incluindo as páginas do modelo mapeadas em memória) numa máquina de 16 GB, então a RAM livre cai para algumas centenas de MiB enquanto ele roda.
- **As configurações de outras pessoas.** Outras pessoas relatam rodar o Z-Image em placas de 4 GB com quantização mais baixa ou tamanhos menores (por exemplo, a página da wiki do stable-diffusion.cpp para placas de 4 GB recomenda Q3_K ou Q4_0 em 1024x512). Nos lugares onde procuramos (lista e data em [`docs/RELATED.md`](docs/RELATED.md)), não encontramos uma configuração publicada que combine os quatro itens: uma placa de 4 GB, Q8_0, 768x1344 ou maior, e tempo e memória da GPU medidos. Isso é uma afirmação sobre onde procuramos, não sobre todos os lugares.
- **Quem faz o quê.** Caber em 4 GB vem do próprio stable-diffusion.cpp: `--offload-to-cpu`, `--mmap`, o trabalho em fatias e a flash attention (com ela desligada, uma execução precisou de 4205 MB e não coube). Os nossos patches servem para ganhar velocidade e uma etapa de VAE melhor, não para caber. Não rodamos o motor original sem patches nesta placa, então não podemos dizer se ele cabe.

## Como funciona

Três mudanças sobre o stable-diffusion.cpp `master-1088-32d516c` (todas são chaves liga/desliga; a tabela em [`patches/README.md`](patches/README.md) lista cada uma com a sua variável de ambiente):

1. **O refiner roda uma vez por passo.** Um nome de grupo era usado duas vezes, e por isso quatro blocos do refiner eram calculados uma segunda vez. Com a correção, os passos 2 a 8 ficam cerca de 1.3 s mais rápidos cada um (de 22.0 para 20.7 s), com uma imagem idêntica pixel a pixel (3 imagens conferidas).
2. **VAE com cuDNN, em float32.** A última etapa (transformar o latent em pixels) agora usa a convolução float32 do cuDNN, da NVIDIA. Na nossa placa, isso levou o VAE de 23 a 27 s para 10 a 15 s e o PSNR em relação à referência de 38 a 43 dB para 45 a 49 dB (com tiles grandes).
3. **Uma peça só primeiro.** O motor agora tenta decodificar a imagem inteira de uma vez quando a verificação de memória diz que cabe (margem de 256 MiB); se não couber, recorre a dois tiles grandes e depois a tiles pequenos. Em uma peça só, o VAE levou cerca de 8–16 s e o PSNR em relação à referência foi de 71 a 73 dB. Se acontecer um recuo forçado, a imagem tem os mesmos pixels da feita com tiles (conferido com `PIXEL_SHA256`). O que aconteceu fica registrado em `run.json` (`stages.vae_path`: `full`, `tile`, `floor` ou `retry`).

Além disso: `--eager-load` (lê as páginas do modelo antecipadamente; de 241.2 s para 220.3 s na mesma imagem, build de desenvolvimento, uma execução cada) faz parte do comando fixo.

<a id="what-it-runs"></a>
## O que ele executa

| Parte | Arquivo | Origem |
|---|---|---|
| Modelo de difusão | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), base [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Text encoder | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), autoencoder do tipo FLUX.1 |
| Motor | `sd-cli.exe`, stable-diffusion.cpp `32d516c` com os patches em [`patches/`](patches) | a versão v0.2.0 deste repositório (`sinirsiz-foto-engine-v0.2.0-win-x64-cuda12.8-sm61.zip`) |
| Runtime do CUDA | `cudart`, `cublas`, `cublasLt` (12.8), sem modificação | zip da versão v0.1.0 do wan22-pascal-4gb |
| cuDNN (instalado por padrão; `--no-cudnn` pula) | 8 DLLs, versão 9.10.2.21 (build para CUDA 11) | servidor da própria NVIDIA, sob a licença da NVIDIA; não fica guardado aqui |

Configurações fixas: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`.
Não reduzimos os passos, não adicionamos prompt negativo e não ativamos cache: o modelo é destilado para 8 passos e não usa prompt negativo (veja [prompts](docs/PROMPTS.md)).

## Limites (leia antes de depender disto)

- **Somente Windows.** O motor pré-compilado e estes scripts são só para Windows.
- **Uma placa, uma máquina.** Medido apenas em um notebook com GTX 1050 Ti de 4 GB (i7-7700HQ, 16 GB de RAM, Windows 10, driver 581.29, modelos em um SSD). Outras GPUs e drivers, máquinas com menos de 16 GB de RAM, Linux e macOS: **não testados**.
- Outras placas e sistemas (que caminho existe, e um teste da comunidade numa placa AMD em Linux que não executamos nós mesmos): [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md).
- **O motor é compilado só para Pascal (sm_61).** Outras arquiteturas exigem uma compilação sua ([`docs/BUILD.md`](docs/BUILD.md)); não testamos nenhuma.
- **cuDNN:** medimos com a build para CUDA 11 do cuDNN 9.10.2.21. A build para CUDA 12 tem arquivos diferentes e não foi medida.
- **A memória é justa.** A RAM livre cai para algumas centenas de MiB; feche os outros programas e gere uma imagem por vez. Não vimos a memória da GPU acabar depois que a verificação de memória do motor passou, e não testamos o que acontece nesse caso.
- **Tamanhos:** apenas 768x1344, 1344x768 e 1024x1024 foram testados. Tamanhos maiores imprimem um aviso e podem esgotar a memória.
- A fidelidade ao prompt é parcial: uma imagem nem sempre segue o prompt em todos os detalhes. Texto dentro das imagens e monumentos do mundo real não foram avaliados.
- A referência do PSNR é a decodificação na CPU do nosso próprio motor, não uma implementação independente.
- Os números em [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) vêm de uma execução cada, a menos que esteja escrito o contrário.

## Licença e crédito

- Os scripts e documentos deste repositório: [Apache-2.0](LICENSE), com um arquivo [`NOTICE`](NOTICE). Os patches do motor em [`patches/`](patches) são MIT, como o código que eles modificam.
- stable-diffusion.cpp e ggml são MIT. Os avisos do código de terceiros compilado no motor estão em [`licenses/`](licenses) e em [`THIRD_PARTY.md`](THIRD_PARTY.md).
- Os arquivos dos modelos não ficam guardados aqui; eles são baixados das origens acima, sob as suas próprias licenças (o Hugging Face indica Apache-2.0 para todos, lido em 2026-11-13). O model card não diz nada sobre quem é o dono das imagens geradas, e nós não fazemos nenhuma afirmação sobre isso.
- **O cuDNN e o runtime do CUDA são propriedade da NVIDIA** e não estão sob a licença deste repositório. O cuDNN é baixado do servidor da NVIDIA, sob a licença da NVIDIA (`--no-cudnn` pula); as DLLs do runtime do CUDA ficam em um zip separado e sem modificação (CUDA Toolkit EULA, Attachment A). Detalhes e o que não conseguimos verificar: [`THIRD_PARTY.md`](THIRD_PARTY.md).
- **Crédito.** Manter o arquivo `NOTICE` junto com as cópias e os trabalhos derivados é a condição (Apache-2.0, seção 4). Além disso, uma linha como "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey" é bem-vinda, mas não obrigatória.
- Leia o [`ETHICS.md`](ETHICS.md): toda imagem é sintética, e você é responsável pelo que publica.

## Contribuindo

O mais útil que você pode fazer é **testar a sua placa** e contar o que aconteceu: nome da GPU, driver, RAM, o `run.json` e as últimas linhas do log (o formulário de issue "Hardware test report"). Correções nos documentos e nos scripts também são bem-vindas; veja [`CONTRIBUTING.md`](CONTRIBUTING.md). Relatos de segurança seguem pelo canal privado descrito em [`SECURITY.md`](SECURITY.md).

[Guia de instalação para agentes de IA](AGENTS.md) · [Medições](docs/MEASUREMENTS.md) · [Solução de problemas](docs/TROUBLESHOOTING.md) · [Compilando o motor](docs/BUILD.md) · [Patches](patches/README.md) · [Prompts](docs/PROMPTS.md) · [Terceiros](THIRD_PARTY.md) · [Histórico de mudanças](CHANGELOG.md)

Esta página foi localizada com a ajuda de IA; correções são muito bem-vindas, veja [`CONTRIBUTING.md`](CONTRIBUTING.md).
