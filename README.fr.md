[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · **Français** · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**Génération d'images à partir de texte avec Z-Image-Turbo (Q8_0 GGUF) en 768x1344 sur une GTX 1050 Ti de 4 GB (Pascal, sm_61), avec stable-diffusion.cpp, sous Windows.** Mesuré sur un portable avec 16 GB de RAM, où le processus utilise environ 11 GB de RAM. La même graine donne les mêmes pixels, pixel pour pixel ; les mesures et les correctifs du moteur sont publiés, les téléchargements sont épinglés par sha256, et un agent de programmation IA peut l'installer pas à pas.

*Non officiel. Sans lien avec Tongyi-MAI (Z-Image), leejet (stable-diffusion.cpp) ni NVIDIA.*

## Pour commencer

Un paquet prêt à l'emploi existe : essayez-le d'abord. Si votre matériel est différent ou si une étape échoue, tout le reste est ouvert : les correctifs, la recette de compilation et les mesures sont dans ce dépôt, pour que vous compiliez le moteur pour votre propre carte ou que vous l'adaptiez.

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

L'étape 2 télécharge environ 12.2 GB et a pris 29 minutes une fois, sur notre connexion ; elle affiche d'abord un bloc « Preflight » (votre GPU, votre RAM et l'espace disque libre à côté de ce que nous avons mesuré ; il ne fait qu'informer).
Seule la carte portable GTX 1050 Ti de 4 GB (Pascal, capacité de calcul 6.1) a été mesurée. Les autres cartes n'ont pas été testées.
Si vous utilisez un agent de programmation IA (Claude Code, Codex, Cursor et similaires), indiquez-lui [`AGENTS.md`](AGENTS.md).

## En un coup d'œil

Par rapport à l'organisation de v0.1.0 : une image prend 193–228 s au lieu de 261.6 s, l'étape VAE prend 8.3–15.9 s au lieu de 29.8 à 36.3 s, la même graine donne les mêmes pixels, et chaque nombre de ce README s'appuie sur une commande et un fichier.

768x1344, graine 42, 8 étapes, même machine. Les nombres de v0.1.0 viennent du README de v0.1.0 (test en racine propre et cinq exécutions) ; ceux de v0.2.0 viennent du test en racine propre de cette version.

| | v0.1.0 (jamais publiée ; ancienne organisation) | v0.2.0 |
|---|---|---|
| Durée pour une image (une exécution de `generate.py`) | 261.6 s | 193–228 s |
| Décodage VAE (dernière étape) | 29.8 à 36.3 s | 8.3–15.9 s |
| Proximité avec un décodage de référence (PSNR, plus c'est haut, mieux c'est) | 38 à 43 dB | 71 à 73 dB |
| Pic de mémoire GPU (nvidia-smi) | 2949 à 2957 MiB | 3057–3059 MiB |
| Mémoire du processus, pic | 10.5 à 10.9 GB (tel qu'enregistré à l'époque) | 10 667–10 915 MiB |
| RAM libre la plus basse observée | 331 à 576 MiB | 418–545 MiB |

Comment lire ce tableau : la référence est le même latent décodé sur le CPU en une seule pièce en float32 ; le PSNR compare notre décodage GPU à cette référence (3 images). Il indique à quel point l'étape VAE est proche de cette référence. Il n'indique pas la qualité d'une image. Les images de v0.2.0 ne sont pas identiques octet pour octet à celles de v0.1.0 pour le même prompt et la même graine, parce que le chemin du VAE a été changé volontairement. Méthode et parties non mesurées : [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md).

## Exemples

**Générées par IA avec ce dépôt** (Z-Image-Turbo Q8_0, graine 42, 8 étapes). Ce ne sont pas de vraies photographies ; les monuments et les détails
peuvent être inexacts, et une image ne suit pas toujours son prompt dans chaque détail. Les prompts exacts sont dans [`prompts/`](prompts) et [`docs/PROMPTS.md`](docs/PROMPTS.md).

| | | |
|---|---|---|
| ![Tour Eiffel à l'heure dorée](docs/examples/eiffel.jpg) | ![Verre de thé turc](docs/examples/turkish_tea.jpg) | ![Pêcheur âgé](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![Village sur une colline](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![Istanbul vue du ciel](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. Ce n'est pas une vraie photo ; les monuments peuvent être inexacts.

## Démarrage rapide

Prérequis : Windows 10/11, un GPU NVIDIA de 4 GB, un pilote compatible avec CUDA 12.8 (le pilote 581.29 a été mesuré ; les pilotes plus anciens n'ont pas été testés ; le runtime CUDA lui-même est téléchargé pour vous), Python 3.10 ou plus récent,
git, environ 14 GB d'espace disque libre (les téléchargements font environ 12.2 GB avec cuDNN ; le chiffre d'espace libre est une estimation) et 16 GB de RAM (ce qui a été mesuré ; avec moins, non testé).

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- `setup.py` affiche d'abord un bloc « Preflight » (votre GPU, votre RAM et l'espace disque libre à côté de ce que nous avons mesuré ; il ne fait qu'informer et ne bloque jamais). Il télécharge ensuite depuis les adresses épinglées dans [`models.lock.json`](models.lock.json) et vérifie chaque fichier avec sha256. Il affiche `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK`, puis `CUDNN_OK` ou `CUDNN_SKIPPED`, et enfin `SETUP_OK`.
  Sans `--models-dir` et `--bin-dir`, il utilise `models/` et `bin/` à la racine du dépôt ; placez les modèles sur un SSD (seul un SSD a été mesuré).
  Arrêtez-le quand vous voulez avec Ctrl+C et relancez la même commande : les téléchargements reprennent à partir des fichiers `.part`.
- **cuDNN est installé par défaut et ne fait pas partie de ce dépôt.** C'est un logiciel de NVIDIA, sous la licence propre à NVIDIA ([texte de la licence](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)), pour les systèmes équipés de GPU NVIDIA. Il se télécharge depuis le serveur de NVIDIA sans qu'aucun paiement ni aucune connexion ne soit demandé, et nous n'avons trouvé dans la licence aucune clause qui limite l'usage commercial ou personnel. `setup.py` affiche l'adresse de la licence, télécharge le fichier et copie seulement huit DLL à côté de `sd-cli.exe`. La licence de NVIDIA dit que quiconque n'en accepte pas les termes ne doit pas le télécharger, l'installer ni l'utiliser ; dans ce cas, lancez `python scripts/setup.py --no-cudnn`. Sans cuDNN, tout fonctionne avec le chemin VAE plus lent de v0.1.0 (`--vae legacy`), et `generate.py` le signale.
- `generate.py` écrit `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, `run.json` (durée, étapes, chemin VAE utilisé, pic de mémoire GPU, commande exacte) et `log.txt`, et affiche `IMAGE_OK <path>`.

## Utilisation

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| Option | Signification |
|---|---|
| `--prompt "<text>"` ou `--prompt-file <txt>` | le prompt (l'un des deux est obligatoire) |
| `--width`, `--height` | multiples de 16, de 256 à 2048 ; par défaut 768x1344 ; testés : 768x1344, 1344x768, 1024x1024 |
| `--seed` | par défaut 42 |
| `--out`, `--name` | dossier racine de sortie (par défaut `outputs/`) et un nom court pour le dossier de l'exécution |
| `--models-dir`, `--bin-dir` | où `setup.py` a placé les modèles et le moteur |
| `--vae auto` (par défaut) | cuDNN float32 ; essaie d'abord en une seule pièce, puis deux grandes tuiles, puis la petite tuile par défaut |
| `--vae tiled` | cuDNN float32, toujours deux grandes tuiles |
| `--vae legacy` | le chemin de v0.1.0 : sans cuDNN, petites tuiles. Utilisé automatiquement (avec un avertissement) quand les DLL de cuDNN manquent |

Les étapes (8), le cfg (1.0), le sampler et le scheduler sont fixés volontairement ; voir [Ce qu'il exécute](#what-it-runs).

## Vérifiez par vous-même

- `generate.py` affiche `PIXEL_SHA256 <hex>` dans l'une de ses dernières lignes : une empreinte des pixels décodés. Lancez deux fois la même commande et comparez les deux images : `python scripts/compare.py <run A>/image.png <run B>/image.png` doit afficher `SAME_PIXELS`.
- Le `PIXEL_SHA256` des cinq exemples sur notre machine se trouve dans [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md). L'empreinte du fichier PNG peut différer même si les pixels sont les mêmes, car le PNG contient les paramètres de génération sous forme de texte ; comparez les pixels, pas les fichiers.
- Limite honnête : nous n'avons pas mesuré si une autre carte ou un autre pilote donne les mêmes pixels.

## Pourquoi cela tient dans 4 GB

- **Ce que disent les auteurs du modèle.** La fiche du modèle Z-Image-Turbo indique que le modèle « fits comfortably within 16G VRAM consumer devices » ([fiche du modèle](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)), c'est-à-dire qu'il tient confortablement dans les appareils grand public de 16 GB de VRAM. Cela concerne les cartes de 16 GB. Le README officiel cite aussi stable-diffusion.cpp comme option tierce et le mentionne pour « as little as 4GB of VRAM » (« avec seulement 4 GB de VRAM ») ([README](https://github.com/Tongyi-MAI/Z-Image)) ; c'est une affirmation du projet stable-diffusion.cpp, pas une exigence de l'équipe Z-Image.
- **Ce que nous avons mesuré.** Z-Image-Turbo Q8_0 (un fichier de 6.6 GB) avec un encodeur de texte Qwen3-4B Q8_0, en 768x1344 : le pic GPU, échantillonné par nvidia-smi toutes les 2 s (un pic bref peut échapper à la mesure), a été de 2949 à 2957 MiB (moteur v0.1.0) et de 3057–3059 MiB (moteur v0.2.0) sur une carte de 4096 MiB. Les poids (10 509 MiB ; le journal du moteur l'affiche en MB) restent dans la RAM du système ; le moteur copie le réseau vers le GPU un segment (une tranche du réseau) à la fois : 36 segments, comme dans la ligne de journal `z_image using 36 segments`.
- **Ce que cela coûte.** Du temps et de la mémoire système : 193–228 s par image, et le processus du moteur occupe environ 10 667–10 915 MiB de RAM (pages du modèle mappées en mémoire comprises) sur une machine de 16 GB ; la RAM libre tombe donc à quelques centaines de MiB pendant l'exécution.
- **Les configurations d'autres personnes.** D'autres rapportent faire tourner Z-Image sur des cartes de 4 GB avec une quantification plus basse ou des tailles plus petites (par exemple, la page du wiki de stable-diffusion.cpp consacrée aux cartes de 4 GB recommande Q3_K ou Q4_0 en 1024x512). Là où nous avons cherché (liste et date dans [`docs/RELATED.md`](docs/RELATED.md)), nous n'avons pas trouvé de configuration publiée qui réunisse les quatre éléments : une carte de 4 GB, Q8_0, 768x1344 ou plus grand, et durée et mémoire GPU mesurées. C'est un constat sur les endroits où nous avons cherché, pas sur tous les endroits.
- **Qui fait quoi.** Faire tenir le tout dans 4 GB vient de stable-diffusion.cpp lui-même : `--offload-to-cpu`, `--mmap`, le travail par tranches et la flash attention (sans elle, une exécution a eu besoin de 4205 MB et n'a pas tenu). Nos correctifs servent à la vitesse et à une meilleure étape VAE, pas à faire tenir le modèle. Nous n'avons pas fait tourner le moteur amont non modifié sur cette carte, nous ne pouvons donc pas dire s'il tient.

## Comment ça marche

Trois changements au-dessus de stable-diffusion.cpp `master-1088-32d516c` (ce sont tous des interrupteurs ; le tableau de [`patches/README.md`](patches/README.md) les liste un par un avec leur variable d'environnement) :

1. **Le refiner s'exécute une fois par étape.** Un nom de groupe était utilisé deux fois, si bien que quatre blocs du refiner étaient calculés une seconde fois. En corrigeant cela, les étapes 2 à 8 sont chacune environ 1.3 s plus rapides (de 22.0 à 20.7 s), avec une image identique pixel pour pixel (3 images vérifiées).
2. **VAE via cuDNN, en float32.** La dernière étape (transformer le latent en pixels) utilise désormais la convolution float32 de cuDNN de NVIDIA. Sur notre carte, le VAE est passé de 23 à 27 s à 10 à 15 s, et le PSNR par rapport à la référence est passé de 38 à 43 dB à 45 à 49 dB (grandes tuiles).
3. **D'abord en une seule pièce.** Le moteur tente désormais de décoder l'image entière d'un seul bloc quand la vérification de mémoire indique que cela tient (marge de 256 MiB), se replie sur deux grandes tuiles, puis sur de petites tuiles. En une seule pièce, le VAE a pris environ 8–16 s et le PSNR par rapport à la référence était de 71 à 73 dB. Si un repli forcé se produit, l'image a les mêmes pixels que celle obtenue par tuiles (vérifié avec `PIXEL_SHA256`). Ce qui s'est passé est écrit dans `run.json` (`stages.vae_path` : `full`, `tile`, `floor` ou `retry`).

Aussi : `--eager-load` (lit les pages du modèle à l'avance ; de 241.2 s à 220.3 s sur la même image, build de développement, une exécution chacun) fait partie de la commande fixe.

<a id="what-it-runs"></a>
## Ce qu'il exécute

| Élément | Fichier | Source |
|---|---|---|
| Modèle de diffusion | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), base [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Encodeur de texte | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), autoencodeur de type FLUX.1 |
| Moteur | `sd-cli.exe`, stable-diffusion.cpp `32d516c` avec les correctifs de [`patches/`](patches) | la version v0.2.0 de ce dépôt (`sinirsiz-foto-engine-v0.2.0-win-x64-cuda12.8-sm61.zip`) |
| Runtime CUDA | `cudart`, `cublas`, `cublasLt` (12.8), non modifiés | zip de la version v0.1.0 de wan22-pascal-4gb |
| cuDNN (installé par défaut ; `--no-cudnn` permet de s'en passer) | 8 DLL, version 9.10.2.21 (build CUDA 11) | serveur propre de NVIDIA, sous la licence de NVIDIA ; non stocké ici |

Réglages fixes : `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`.
Nous ne baissons pas le nombre d'étapes, n'ajoutons pas de prompt négatif et n'activons pas le cache : le modèle est distillé pour 8 étapes et n'utilise pas de prompts négatifs (voir [prompts](docs/PROMPTS.md)).

## Limites (à lire avant de vous y fier)

- **Windows uniquement.** Le moteur précompilé et ces scripts ne fonctionnent que sous Windows.
- **Une carte, une machine.** Mesuré uniquement sur un portable avec GTX 1050 Ti de 4 GB (i7-7700HQ, 16 GB de RAM, Windows 10, pilote 581.29, modèles sur un SSD). Autres GPU et pilotes, machines avec moins de 16 GB de RAM, Linux et macOS : **non testés**.
- Autres cartes et systèmes (quelle voie existe, et un test communautaire sur une carte AMD sous Linux que nous n'avons pas exécuté nous-mêmes) : [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md).
- **Le moteur n'est compilé que pour Pascal (sm_61).** Les autres architectures demandent une compilation personnelle ([`docs/BUILD.md`](docs/BUILD.md)) ; nous n'en avons testé aucune.
- **cuDNN :** nous avons mesuré avec le build CUDA 11 de cuDNN 9.10.2.21. Le build CUDA 12 contient d'autres fichiers et n'a pas été mesuré.
- **La mémoire est juste.** La RAM libre tombe à quelques centaines de MiB ; fermez les autres programmes, générez une image à la fois. Nous n'avons jamais vu la mémoire GPU manquer après que la vérification de mémoire du moteur a réussi, et nous n'avons pas testé ce qui se passerait alors.
- **Tailles :** seules 768x1344, 1344x768 et 1024x1024 ont été testées. Les tailles supérieures affichent un avertissement et peuvent manquer de mémoire.
- La fidélité au prompt est partielle : une image ne suit pas toujours son prompt dans chaque détail. Le texte à l'intérieur des images et les monuments réels n'ont pas été évalués.
- La référence du PSNR est le décodage CPU de notre propre moteur, pas une implémentation indépendante.
- Les nombres de [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) proviennent d'une seule exécution chacun, sauf mention contraire.

## Licence et crédit

- Les scripts et documents de ce dépôt : [Apache-2.0](LICENSE) avec un fichier [`NOTICE`](NOTICE). Les correctifs du moteur dans [`patches/`](patches) sont sous MIT, comme le code qu'ils modifient.
- stable-diffusion.cpp et ggml sont sous MIT. Les mentions du code tiers compilé dans le moteur se trouvent dans [`licenses/`](licenses) et [`THIRD_PARTY.md`](THIRD_PARTY.md).
- Les fichiers de modèle ne sont pas stockés ici ; ils sont téléchargés depuis les sources ci-dessus sous leurs propres licences (Hugging Face indique Apache-2.0 pour tous, consulté le 2026-11-13). La fiche du modèle ne dit rien de la propriété des images générées, et nous n'avançons rien à ce sujet.
- **cuDNN et le runtime CUDA sont la propriété de NVIDIA** et ne sont pas sous la licence de ce dépôt. cuDNN est téléchargé depuis le serveur de NVIDIA sous la licence de NVIDIA (`--no-cudnn` permet de s'en passer) ; les DLL du runtime CUDA se trouvent dans un zip séparé, non modifié (CUDA Toolkit EULA, Attachment A). Détails et ce que nous n'avons pas pu vérifier : [`THIRD_PARTY.md`](THIRD_PARTY.md).
- **Crédit.** Conserver le fichier `NOTICE` avec les copies et les travaux dérivés est la condition (Apache-2.0, section 4). Au-delà, une ligne telle que « Basé sur Sınırsız Foto par Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey » est appréciée, sans être exigée.
- Merci de lire [`ETHICS.md`](ETHICS.md) : chaque image est synthétique, et vous êtes responsable de ce que vous publiez.

## Contribuer

Le plus utile est de **tester votre carte** et de nous dire ce qui s'est passé : nom du GPU, pilote, RAM, le `run.json` et les dernières lignes du journal (le formulaire de ticket « Hardware test report »). Les corrections des documents et des scripts sont aussi les bienvenues ; voir [`CONTRIBUTING.md`](CONTRIBUTING.md). Les signalements de sécurité passent par la voie privée décrite dans [`SECURITY.md`](SECURITY.md).

[Guide d'installation pour agents IA](AGENTS.md) · [Mesures](docs/MEASUREMENTS.md) · [Dépannage](docs/TROUBLESHOOTING.md) · [Compiler le moteur](docs/BUILD.md) · [Correctifs](patches/README.md) · [Prompts](docs/PROMPTS.md) · [Tiers](THIRD_PARTY.md) · [Journal des modifications](CHANGELOG.md)

Cette page a été localisée avec l'aide de l'IA ; les corrections sont les bienvenues (voir [`CONTRIBUTING.md`](CONTRIBUTING.md)).
