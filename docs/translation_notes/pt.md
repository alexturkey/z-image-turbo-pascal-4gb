# Português (pt): localization notes

Written by: W2 (Sonnet), 2026-11-14   Read by: R2 (Sonnet), 2026-11-14   Status: ok

## Address and tone
- Form of address (formal / informal) and why, for this country's developer READMEs: Brazilian Portuguese, "você" with third-person imperative ("experimente", "feche", "leia"). Variant decision: Brazil, because it has by far the larger Portuguese-speaking developer audience, and "você" is the normal voice of Brazilian developer documentation. European Portuguese readers understand it without trouble.
- Register (how technical, how warm): plain, calm, sourced; technical, friendly but not chatty. Established English terms are kept as Brazilian developers say them (prompt, seed, tile, patch, log, build, download, scheduler, sampler). No promotional words.

## Terms (this README uses these; same word everywhere in the file)
| English | Used here | Note (why, or what readers use instead) |
|---|---|---|
| GPU memory (VRAM) | memória da GPU ("VRAM" only inside the model-card quote and its explanation) | Brazilians say "VRAM" and "memória de vídeo"; "memória da GPU" fits the nvidia-smi context |
| text-to-image | geração de imagens a partir de texto | descriptive in the first sentence; "text encoder" stays English (component name) |
| tile (VAE tile) | tile | kept in English; plural "tiles" |
| seed | seed | Brazilian developers say "seed"; "semente" is not used |
| prompt | prompt | universal; "prompt negativo" for negative prompt |
| quantization | quantização | |
| setup / install | instalação (script name `setup.py` unchanged) | "Início rápido" for the quick start section |
| measured / not tested | medido / não testado | "não testado" is the normal phrase |
| open source license / NOTICE | licença; arquivo `NOTICE` | "condição" for NOTICE, "bem-vinda, mas não obrigatória" for the credit line |
| download, patch, refiner, latent, sampler, scheduler, flash attention | kept in English | usual in Brazilian technical text; "arquivo" (not "ficheiro") |
| pixel for pixel | pixel a pixel | |
| unofficial | não oficial | |

## Avoided
- Phrases that sound like advertising in this language/culture: "incrível", "revolucionário", "super fácil", "poderoso", "o melhor"; no exclamation marks.
- Literal translations that read wrongly: "raiz limpa" is kept as "teste em raiz limpa" because it names a test in the repository (clean-root); "uma peça só" used for "one piece" is understandable but the reader may prefer another wording.
- European Portuguese forms (ecrã, ficheiro, utilizador, "tu") are not used, by the variant decision.

## Formatting
- Numbers and decimal separator: Brazilian readers would expect a decimal comma (6,6) and a dot for thousands. The test requires the English forms, so 12.2 stays with a point and 6,577,440,704 keeps its commas. Numbers always carry a unit and sit in tables or short phrases, so the meaning stays clear.
- Script issues (right-to-left, line height, no spaces between words, table widths): none; Latin script. The `{{...}}` slots and their units are untouched.

## Back-translation check
- First paragraph back into English by the reader: Back-translated from the Portuguese only: "Text-to-image generation with Z-Image-Turbo (Q8_0 GGUF) at 768x1344 on a 4 GB GTX 1050 Ti (Pascal, sm_61), with stable-diffusion.cpp, on Windows. Measured on a notebook with 16 GB RAM, where the process uses about 11 GB RAM. The same seed generates the same pixels, pixel by pixel; measurements and engine patches are public, downloads are pinned with sha256 and an AI coding agent can do the installation step by step. Unofficial. No link with Tongyi-MAI, leejet or NVIDIA." Differences from the English: none in meaning.
- Four critical sections checked (first paragraph, quick start, limits, license) in languages chosen for the family: yes (first paragraph, quick start, limits, license all checked)

## Open points / corrections welcome
- "Hardware test report" (issue form name) kept in English, as in the Turkish example.
- "Em resumo" for "At a glance"; "Crédito" for "credit". The reader may prefer "Visão geral" for the first.
- Brazil was chosen; if the owner wants a separate Portugal version, it would need its own file and language bar entry.
- Reader (R2) agrees with Brazilian variant, "voce" form, terms and "Em resumo". cuDNN paragraph keeps: NVIDIA software, optional, asks once. Condition vs. request distinct ("condicao" vs. "bem-vinda, mas nao obrigatoria"). No added or softened claims found. Minor colloquialism "experimente ele" left as natural Brazilian usage.

## Round 2
- Round 2: "por padrão" for "by default"; "sem cadastro nem login" for "without sign-in"; "sem que seja pedido nenhum pagamento" (not "grátis"); "não encontramos" keeps "we found"; "não deve baixar, instalar nem usar" keeps the force of "must not".
- Round 2 reader check: three pieces and the two script-changed lines (256 MiB, 581.29) read natively; meaning, calm tone and rule 3 and 4 fine; no change needed.
