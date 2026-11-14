# Prompts

The five prompts used for the example pictures are in [`prompts/`](../prompts). Use one with
`python scripts/generate.py --prompt-file prompts/<name>.txt ...`. Save your own prompt files as UTF-8 without BOM.
All pictures: seed 42, 8 steps, cfg 1.0, **no negative prompt**.

| File | Size | Subject |
|---|---|---|
| `prompts/eiffel.txt` | 768x1344 | Eiffel Tower at golden hour, low angle, Trocadero gardens |
| `prompts/turkish_tea.txt` | 768x1344 | Turkish tea glass, window, steam, macro |
| `prompts/fisherman.txt` | 768x1344 | Elderly fisherman portrait in a harbour at sunrise |
| `prompts/village.txt` | 768x1344 | Hillside village with round doors (prompt match partial) |
| `prompts/istanbul_aerial.txt` | 1344x768 | Aerial view of Istanbul at golden hour |

## Writing tips

From the model's own page (Hugging Face discussion "PROMPTING GUIDE" of Tongyi-MAI/Z-Image-Turbo, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/discussions/8):
- "Z-Image-Turbo works best with long and detailed prompts."
- "this model does not use negative prompts at all." It is a few-step distilled model that does not use classifier-free guidance, so put what you want in the positive prompt.
- The default maximum is 512 tokens (their statement for the reference pipeline; how this engine truncates longer text: not tested). The prompts here are 85 to 113 words long.

From our five prompts (observations, not tests):
- Plain English sentences work. Pattern used: kind of picture (photograph, aerial drone photograph, close-up), subject, concrete details, light, background, lens and look.
- Camera cues were part of every prompt (`35mm lens`, `85mm lens`, `Macro lens`, `Wide angle, high altitude`).
- Several named objects in one scene were drawn (Istanbul: mosque, strait, bridge), but we did not check them for accuracy; landmarks in the examples may be inaccurate.
- A detailed layout request was only partly followed: in `village.txt` the doors are meant to be built into the hills, and the picture shows separate huts instead. If a detail matters, try another `--seed` or describe it more simply.
- Text inside pictures: not tested.
- Other languages than English: not tested.

## Fixed generation settings

`--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --flash-attn on`.
Default size 768x1344 (portrait), 1344x768 for landscape; width and height multiples of 16.
Measured results: [MEASUREMENTS.md](MEASUREMENTS.md).

## Image rights

The example pictures are AI-generated with this repo and are not real photographs. The Z-Image-Turbo model card says nothing about ownership of generated pictures;
see the License section of the README.
