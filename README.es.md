[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · **Español** · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**Generación de imágenes a partir de texto con Z-Image-Turbo (Q8_0 GGUF) a 768x1344 en una GTX 1050 Ti de 4 GB (Pascal, sm_61), con stable-diffusion.cpp, en Windows.** Medido en un portátil con 16 GB de RAM, donde el proceso usa unos 11 GB de RAM. La misma semilla produce los mismos píxeles, píxel por píxel; las mediciones y los parches del motor son públicos, las descargas están fijadas con sha256 y un agente de programación con IA puede instalarlo paso a paso.

*No oficial. Sin relación con Tongyi-MAI (Z-Image), leejet (stable-diffusion.cpp) ni NVIDIA.*

## Empieza aquí

Hay un paquete ya preparado, así que pruébalo primero. Si tu hardware es distinto o algún paso falla, todo lo demás está abierto: los parches, la receta de compilación y las mediciones están en este repositorio, para que compiles el motor para tu propia tarjeta o lo adaptes.

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

El paso 2 descarga unos 12.2 GB y tardó 29 minutos una vez, con nuestra conexión; primero imprime un bloque "Preflight" (tu GPU, tu RAM y el disco libre junto a lo que medimos nosotros; solo informa).
Solo se midió la tarjeta portátil GTX 1050 Ti de 4 GB (Pascal, capacidad de cómputo 6.1). Otras tarjetas no se probaron.
Si usas un agente de programación con IA (Claude Code, Codex, Cursor y similares), indícale [`AGENTS.md`](AGENTS.md).

## De un vistazo

Frente a la disposición de v0.1.0: una imagen tarda 193–228 s en lugar de 261.6 s, la etapa del VAE tarda 8.3–15.9 s en lugar de 29.8 a 36.3 s, la misma semilla da los mismos píxeles, y detrás de cada número de este README hay un comando y un archivo.

768x1344, semilla 42, 8 pasos, la misma máquina. Los números de v0.1.0 salen del README de v0.1.0 (prueba en raíz limpia y cinco ejecuciones); los de v0.2.0 salen de la prueba en raíz limpia de esta versión.

| | v0.1.0 (nunca publicada; disposición antigua) | v0.2.0 |
|---|---|---|
| Tiempo para una imagen (una ejecución de `generate.py`) | 261.6 s | 193–228 s |
| Decodificación del VAE (última etapa) | 29.8 a 36.3 s | 8.3–15.9 s |
| Cercanía a una decodificación de referencia (PSNR, más alto es mejor) | 38 a 43 dB | 71 a 73 dB |
| Pico de memoria de la GPU (nvidia-smi) | 2949 a 2957 MiB | 3057–3059 MiB |
| Memoria del proceso, pico | 10.5 a 10.9 GB (según se registró entonces) | 10 667–10 915 MiB |
| RAM libre mínima observada | 331 a 576 MiB | 418–545 MiB |

Cómo leerlo: la referencia es el mismo latente decodificado en la CPU como una sola pieza en float32; el PSNR compara con ella nuestra decodificación en la GPU (3 imágenes). Indica cuán cerca está la etapa del VAE de esa referencia. No indica qué tan buena se ve una imagen. Las imágenes de v0.2.0 no son idénticas byte a byte a las de v0.1.0 con el mismo prompt y la misma semilla, porque el camino del VAE cambió a propósito. Método y partes sin medir: [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md).

## Ejemplos

**Generadas con IA con este repositorio** (Z-Image-Turbo Q8_0, semilla 42, 8 pasos). No son fotografías reales; los lugares emblemáticos y los detalles
pueden ser inexactos, y una imagen no siempre sigue su prompt en cada detalle. Los prompts exactos están en [`prompts/`](prompts) y [`docs/PROMPTS.md`](docs/PROMPTS.md).

| | | |
|---|---|---|
| ![Torre Eiffel en la hora dorada](docs/examples/eiffel.jpg) | ![Vaso de té turco](docs/examples/turkish_tea.jpg) | ![Pescador anciano](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![Pueblo en una ladera](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![Estambul vista desde el aire](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. No es una foto real; los lugares emblemáticos pueden ser inexactos.

## Inicio rápido

Requisitos: Windows 10/11, una GPU NVIDIA con 4 GB, un controlador compatible con CUDA 12.8 (se midió con el controlador 581.29; los controladores más antiguos no se probaron; el propio runtime de CUDA se descarga por ti), Python 3.10 o superior,
git, unos 14 GB de disco libre (las descargas son unos 12.2 GB con cuDNN; la cifra de disco libre es una estimación) y 16 GB de RAM (lo que se midió; con menos no se probó).

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- `setup.py` primero imprime un bloque "Preflight" (tu GPU, tu RAM y el disco libre junto a lo que medimos nosotros; solo informa y nunca bloquea). Después descarga desde las direcciones fijadas en [`models.lock.json`](models.lock.json) y comprueba cada archivo con sha256. Imprime `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK`, luego `CUDNN_OK` o `CUDNN_SKIPPED`, y por último `SETUP_OK`.
  Sin `--models-dir` y `--bin-dir` usa `models/` y `bin/` en la raíz del repositorio; pon los modelos en un SSD (solo se midió con SSD).
  Puedes detenerlo cuando quieras con Ctrl+C y volver a ejecutar el mismo comando: las descargas continúan desde los archivos `.part`.
- **cuDNN se instala por defecto y no forma parte de este repositorio.** Es software de NVIDIA bajo la licencia propia de NVIDIA ([texto de la licencia](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)), para equipos con GPU NVIDIA. Se descarga del servidor de NVIDIA sin que se pida ningún pago ni inicio de sesión, y no encontramos ninguna cláusula en la licencia que limite el uso comercial o personal. `setup.py` muestra la dirección de la licencia, descarga el archivo y copia solo ocho DLL junto a `sd-cli.exe`. La licencia de NVIDIA dice que quien no acepte sus términos no debe descargarlo, instalarlo ni usarlo; en ese caso ejecuta `python scripts/setup.py --no-cudnn`. Sin cuDNN todo funciona con el camino de VAE más lento de v0.1.0 (`--vae legacy`), y `generate.py` lo avisa.
- `generate.py` escribe `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, `run.json` (tiempo, etapas, qué camino de VAE se ejecutó, pico de memoria de la GPU, el comando exacto) y `log.txt`, e imprime `IMAGE_OK <path>`.

## Uso

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| Opción | Significado |
|---|---|
| `--prompt "<text>"` o `--prompt-file <txt>` | el prompt (se exige una de las dos) |
| `--width`, `--height` | múltiplos de 16, de 256 a 2048; por defecto 768x1344; probados: 768x1344, 1344x768, 1024x1024 |
| `--seed` | por defecto 42 |
| `--out`, `--name` | carpeta raíz de salida (por defecto `outputs/`) y un nombre corto para la carpeta de la ejecución |
| `--models-dir`, `--bin-dir` | dónde dejó `setup.py` los modelos y el motor |
| `--vae auto` (por defecto) | cuDNN float32; primero se intenta en una sola pieza, luego en dos mosaicos (tiles) grandes, después con el mosaico pequeño por defecto |
| `--vae tiled` | cuDNN float32, siempre dos mosaicos (tiles) grandes |
| `--vae legacy` | el camino de v0.1.0: sin cuDNN, mosaicos (tiles) pequeños. Se usa automáticamente (con una advertencia) cuando faltan las DLL de cuDNN |

Los pasos (8), el cfg (1.0), el sampler y el scheduler están fijados a propósito; consulta [Qué ejecuta](#what-it-runs).

## Compruébalo tú mismo

- `generate.py` imprime `PIXEL_SHA256 <hex>` en una de sus últimas líneas: un hash de los píxeles decodificados. Ejecuta el mismo comando dos veces y compara las dos imágenes: `python scripts/compare.py <run A>/image.png <run B>/image.png` debería imprimir `SAME_PIXELS`.
- El `PIXEL_SHA256` de los cinco ejemplos en nuestra máquina está en [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md). El hash del archivo PNG puede diferir aunque los píxeles sean los mismos, porque el PNG lleva los parámetros de generación como texto; compara píxeles, no archivos.
- Límite honesto: no medimos si otra tarjeta u otro controlador da los mismos píxeles.

## Por qué cabe en 4 GB

- **Lo que dicen los autores del modelo.** La ficha del modelo Z-Image-Turbo dice que el modelo "fits comfortably within 16G VRAM consumer devices" ([ficha del modelo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)), es decir, que cabe cómodamente en dispositivos de consumo con 16 GB de VRAM. Eso habla de tarjetas de 16 GB. El README oficial también menciona stable-diffusion.cpp como opción de terceros y lo cita por "as little as 4GB of VRAM" ("tan solo 4 GB de VRAM") ([README](https://github.com/Tongyi-MAI/Z-Image)); es una afirmación del proyecto stable-diffusion.cpp, no un requisito del equipo de Z-Image.
- **Lo que medimos.** Z-Image-Turbo Q8_0 (un archivo de 6.6 GB) con un codificador de texto Qwen3-4B Q8_0, a 768x1344: el pico de la GPU, muestreado por nvidia-smi cada 2 s (un pico breve puede escaparse), fue de 2949 a 2957 MiB (motor v0.1.0) y de 3057–3059 MiB (motor v0.2.0) en una tarjeta de 4096 MiB. Los pesos (10 509 MiB; el registro del motor lo imprime como MB) se quedan en la RAM del sistema; el motor copia la red a la GPU un segmento (un trozo de la red) cada vez: 36 segmentos, como en la línea de registro `z_image using 36 segments`.
- **Lo que cuesta.** Tiempo y memoria del sistema: 193–228 s por imagen, y el proceso del motor ocupa unos 10 667–10 915 MiB de RAM (incluidas las páginas del modelo mapeadas en memoria) en una máquina de 16 GB, así que la RAM libre baja a unos pocos cientos de MiB mientras se ejecuta.
- **Configuraciones de otras personas.** Otros cuentan que usan Z-Image en tarjetas de 4 GB con una cuantización más baja o tamaños menores (por ejemplo, la página de la wiki de stable-diffusion.cpp para tarjetas de 4 GB recomienda Q3_K o Q4_0 a 1024x512). En los lugares donde buscamos (lista y fecha en [`docs/RELATED.md`](docs/RELATED.md)) no encontramos una configuración publicada que combine las cuatro cosas: una tarjeta de 4 GB, Q8_0, 768x1344 o más, y tiempo y memoria de la GPU medidos. Eso es una afirmación sobre dónde buscamos, no sobre todas partes.
- **Quién hace qué.** Que quepa en 4 GB lo consigue el propio stable-diffusion.cpp: `--offload-to-cpu`, `--mmap`, trabajar por segmentos y flash attention (sin ella, una ejecución necesitó 4205 MB y no cupo). Nuestros parches son para ganar velocidad y mejorar la etapa del VAE, no para que quepa. No ejecutamos el motor original sin parches en esta tarjeta, así que no podemos decir si cabe.

## Cómo funciona

Tres cambios sobre stable-diffusion.cpp `master-1088-32d516c` (todos son interruptores; la tabla de [`patches/README.md`](patches/README.md) enumera cada uno con su variable de entorno):

1. **El refiner se ejecuta una vez por paso.** Un nombre de grupo se usaba dos veces, de modo que cuatro bloques del refiner se calculaban por segunda vez. Al corregirlo, los pasos 2 a 8 son unos 1.3 s más rápidos cada uno (de 22.0 a 20.7 s) con una imagen idéntica píxel por píxel (3 imágenes comprobadas).
2. **VAE con cuDNN, en float32.** La última etapa (convertir el latente en píxeles) usa ahora la convolución float32 de cuDNN de NVIDIA. En nuestra tarjeta pasó el VAE de 23 a 27 s a 10 a 15 s y subió el PSNR frente a la referencia de 38 a 43 dB a 45 a 49 dB (mosaicos grandes).
3. **Primero, una sola pieza.** El motor intenta ahora decodificar la imagen entera de una vez cuando la comprobación de memoria dice que cabe (margen de 256 MiB); si no, recurre a dos mosaicos grandes y después a mosaicos pequeños. En una sola pieza el VAE tardó unos 8–16 s y el PSNR frente a la referencia fue de 71 a 73 dB. Si se fuerza el paso a la alternativa (fallback), la imagen tiene los mismos píxeles que la de mosaicos (comprobado con `PIXEL_SHA256`). Lo ocurrido queda escrito en `run.json` (`stages.vae_path`: `full`, `tile`, `floor` o `retry`).

Además: `--eager-load` (lee las páginas del modelo por adelantado; de 241.2 s a 220.3 s en la misma imagen, compilación de desarrollo, una ejecución cada una) forma parte del comando fijo.

<a id="what-it-runs"></a>
## Qué ejecuta

| Parte | Archivo | Origen |
|---|---|---|
| Modelo de difusión | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), base [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Codificador de texto | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), autoencoder de tipo FLUX.1 |
| Motor | `sd-cli.exe`, stable-diffusion.cpp `32d516c` con los parches de [`patches/`](patches) | la versión v0.2.0 de este repositorio (`sinirsiz-foto-engine-v0.2.0-win-x64-cuda12.8-sm61.zip`) |
| Runtime de CUDA | `cudart`, `cublas`, `cublasLt` (12.8), sin modificar | zip de la versión v0.1.0 de wan22-pascal-4gb |
| cuDNN (se instala por defecto; `--no-cudnn` lo omite) | 8 DLL, versión 9.10.2.21 (compilación para CUDA 11) | el servidor propio de NVIDIA, bajo la licencia de NVIDIA; no se guarda aquí |

Ajustes fijos: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`.
No reducimos los pasos, no añadimos un prompt negativo ni activamos la caché: el modelo está destilado para 8 pasos y no usa prompts negativos (consulta [prompts](docs/PROMPTS.md)).

## Límites (léelos antes de fiarte)

- **Solo Windows.** El motor precompilado y estos scripts son solo para Windows.
- **Una tarjeta, una máquina.** Medido únicamente en un portátil con GTX 1050 Ti de 4 GB (i7-7700HQ, 16 GB de RAM, Windows 10, controlador 581.29, modelos en un SSD). Otras GPU y controladores, máquinas con menos de 16 GB de RAM, Linux y macOS: **no probados**.
- **El motor está compilado solo para Pascal (sm_61).** Otras arquitecturas necesitan una compilación propia ([`docs/BUILD.md`](docs/BUILD.md)); no probamos ninguna.
- **cuDNN:** medimos con la compilación para CUDA 11 de cuDNN 9.10.2.21. La compilación para CUDA 12 tiene archivos distintos y no se midió.
- **La memoria va justa.** La RAM libre baja a unos pocos cientos de MiB; cierra otros programas y genera una imagen cada vez. No hemos visto que la memoria de la GPU se agote después de superar la comprobación de memoria del motor, y no probamos qué pasa entonces.
- **Tamaños:** solo se probaron 768x1344, 1344x768 y 1024x1024. Los tamaños mayores muestran una advertencia y pueden quedarse sin memoria.
- La fidelidad al prompt es parcial: una imagen no siempre sigue su prompt en cada detalle. El texto dentro de las imágenes y los lugares emblemáticos reales no se evaluaron.
- La referencia del PSNR es la decodificación en CPU de nuestro propio motor, no una implementación independiente.
- Los números de [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) salen de una sola ejecución cada uno, salvo que se indique otra cosa.

## Licencia y créditos

- Los scripts y documentos de este repositorio: [Apache-2.0](LICENSE) con un archivo [`NOTICE`](NOTICE). Los parches del motor en [`patches/`](patches) son MIT, como el código que modifican.
- stable-diffusion.cpp y ggml son MIT. Los avisos del código de terceros compilado en el motor están en [`licenses/`](licenses) y [`THIRD_PARTY.md`](THIRD_PARTY.md).
- Los archivos de modelo no se guardan aquí; se descargan de las fuentes indicadas arriba bajo sus propias licencias (Hugging Face indica Apache-2.0 para todos ellos, consultado el 2026-11-13). La ficha del modelo no dice nada sobre a quién pertenecen las imágenes generadas, y nosotros no afirmamos nada al respecto.
- **cuDNN y el runtime de CUDA son propiedad de NVIDIA** y no están bajo la licencia de este repositorio. cuDNN se descarga del servidor de NVIDIA bajo la licencia de NVIDIA (`--no-cudnn` lo omite); las DLL del runtime de CUDA van en un zip aparte, sin modificar (CUDA Toolkit EULA, Attachment A). Detalles y lo que no pudimos verificar: [`THIRD_PARTY.md`](THIRD_PARTY.md).
- **Créditos.** Conservar el archivo `NOTICE` junto con las copias y las obras derivadas es la condición (Apache-2.0, sección 4). Más allá de eso, se agradece, sin que sea obligatoria, una línea como "Basado en Sınırsız Foto de Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey".
- Lee por favor [`ETHICS.md`](ETHICS.md): toda imagen es sintética, y eres responsable de lo que publiques.

## Contribuir

Lo más útil que puedes hacer es **probar tu tarjeta** y contarnos qué pasó: nombre de la GPU, controlador, RAM, el `run.json` y las últimas líneas del registro (el formulario de incidencia "Hardware test report"). También son bienvenidas las correcciones de los documentos y de los scripts; consulta [`CONTRIBUTING.md`](CONTRIBUTING.md). Los avisos de seguridad van por la vía privada descrita en [`SECURITY.md`](SECURITY.md).

[Guía de instalación para agentes de IA](AGENTS.md) · [Mediciones](docs/MEASUREMENTS.md) · [Solución de problemas](docs/TROUBLESHOOTING.md) · [Compilar el motor](docs/BUILD.md) · [Parches](patches/README.md) · [Prompts](docs/PROMPTS.md) · [Terceros](THIRD_PARTY.md) · [Registro de cambios](CHANGELOG.md)

Esta página se localizó con ayuda de IA; las correcciones son muy bienvenidas (consulta [`CONTRIBUTING.md`](CONTRIBUTING.md)).
