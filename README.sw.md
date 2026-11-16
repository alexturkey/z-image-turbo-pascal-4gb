[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · **Kiswahili**

# Sınırsız Foto

**Kutengeneza picha kutoka kwa maandishi (text-to-image) kwa Z-Image-Turbo (Q8_0 GGUF) katika 768x1344 kwenye GTX 1050 Ti ya GB 4 (Pascal, sm_61), kwa stable-diffusion.cpp, kwenye Windows.** Imepimwa kwenye kompyuta mpakato yenye RAM ya GB 16, ambapo mchakato hutumia takriban GB 11 za RAM. Seed ile ile hutoa pikseli zile zile, pikseli kwa pikseli; vipimo na viraka vya injini viko wazi, upakuaji umefungwa kwa sha256, na wakala wa AI wa kuandika msimbo anaweza kuisakinisha hatua kwa hatua.

*Si rasmi. Haina uhusiano na Tongyi-MAI (Z-Image), leejet (stable-diffusion.cpp) wala NVIDIA.*

## Anzia hapa

Kifurushi kilichotengenezwa tayari kipo, kwa hiyo kijaribu kwanza. Ikiwa vifaa vyako ni tofauti au hatua moja inashindwa, kila kitu kingine kiko wazi: viraka, mapishi ya kujenga na vipimo viko katika hazina hii, kwa hiyo unaweza kujenga kwa kadi yako mwenyewe au kuvirekebisha.

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

Hatua ya 2 hupakua takriban GB 12.2 na ilichukua dakika 29 mara moja, kwenye muunganisho wetu; kwanza huchapisha kizuizi cha "Preflight" (GPU yako, RAM na diski huru, kando ya kile tulichopima; hutoa taarifa tu).
Ni kadi ya kompyuta mpakato GTX 1050 Ti ya GB 4 tu (Pascal, compute capability 6.1) iliyopimwa. Kadi nyingine hazijajaribiwa.
Ukitumia wakala wa AI wa kuandika msimbo (Claude Code, Codex, Cursor na kama hao), mwelekeze kwenye [`AGENTS.md`](AGENTS.md).

## Kwa mtazamo mmoja

Ikilinganishwa na mpangilio wa v0.1.0: picha moja huchukua 193–228 s badala ya 261.6 s, hatua ya VAE huchukua 8.3–15.9 s badala ya 29.8 hadi 36.3 s, seed ile ile hutoa pikseli zile zile, na kila nambari katika README hii ina amri na faili nyuma yake.

768x1344, seed 42, hatua 8, mashine ile ile. Nambari za v0.1.0 zimetoka kwenye README ya v0.1.0 (jaribio la clean-root na mikimbio mitano); nambari za v0.2.0 zimetoka kwenye jaribio la clean-root la toleo hili.

| | v0.1.0 (haikuwahi kuchapishwa; mpangilio wa zamani) | v0.2.0 |
|---|---|---|
| Muda wa picha moja (uendeshaji mmoja wa `generate.py`) | 261.6 s | 193–228 s |
| VAE decode (hatua ya mwisho) | 29.8 hadi 36.3 s | 8.3–15.9 s |
| Ukaribu na decode ya marejeo (PSNR, juu zaidi ni karibu zaidi) | 38 hadi 43 dB | 71 hadi 73 dB |
| Kilele cha kumbukumbu ya GPU (nvidia-smi) | 2949 hadi 2957 MiB | 3057–3059 MiB |
| Kumbukumbu ya mchakato, kilele | 10.5 hadi 10.9 GB (kama ilivyorekodiwa wakati huo) | 10 667–10 915 MiB |
| RAM huru ya chini kabisa iliyoonekana | 331 hadi 576 MiB | 418–545 MiB |

Jinsi ya kusoma: marejeo ni latent ile ile iliyofunguliwa kwenye CPU kama kipande kimoja cha float32; PSNR hulinganisha decode yetu ya GPU nayo (picha 3). Inaonyesha hatua ya VAE iko karibu kiasi gani na marejeo hayo. Haisemi picha inaonekana nzuri kiasi gani. Picha za v0.2.0 hazifanani baiti kwa baiti na v0.1.0 kwa prompt na seed ile ile, kwa sababu njia ya VAE ilibadilishwa kwa makusudi. Mbinu na sehemu ambazo hazikupimwa: [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md).

## Mifano

**Imetengenezwa na AI kwa hazina hii** (Z-Image-Turbo Q8_0, seed 42, hatua 8). Hizi si picha halisi za kamera; alama za mahali na maelezo
yanaweza kuwa si sahihi, na picha haifuati prompt yake kila mara katika kila undani. Prompt kamili ziko katika [`prompts/`](prompts) na [`docs/PROMPTS.md`](docs/PROMPTS.md).

| | | |
|---|---|---|
| ![Mnara wa Eiffel wakati wa saa ya dhahabu](docs/examples/eiffel.jpg) | ![Glasi ya chai ya Kituruki](docs/examples/turkish_tea.jpg) | ![Mvuvi mzee](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![Kijiji kwenye mteremko wa kilima](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![Istanbul ikionekana kutoka angani](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. Si picha halisi ya kamera; alama za mahali zinaweza kuwa si sahihi.

## Kuanza haraka

Mahitaji: Windows 10/11, GPU ya NVIDIA yenye GB 4, dereva (driver) inayounga mkono CUDA 12.8 (dereva 581.29 ilipimwa; dereva za zamani zaidi hazikujaribiwa; CUDA runtime yenyewe hupakuliwa kwa ajili yako), Python 3.10 au mpya zaidi,
git, takriban GB 14 za diski huru (upakuaji ni takriban GB 12.2 pamoja na cuDNN; kiasi cha diski huru ni makadirio), na RAM ya GB 16 (kilichopimwa; kidogo zaidi hakijajaribiwa).

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- Kwanza `setup.py` huchapisha kizuizi cha "Preflight" (GPU yako, RAM na diski huru, kando ya kile tulichopima; hutoa taarifa tu na haizuii kamwe). Kisha hupakua kutoka anwani zilizofungwa katika [`models.lock.json`](models.lock.json) na kukagua kila faili kwa sha256. Huchapisha `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK`, kisha `CUDNN_OK` au `CUDNN_SKIPPED`, na mwishowe `SETUP_OK`.
  Bila `--models-dir` na `--bin-dir` hutumia `models/` na `bin/` kwenye mzizi wa hazina; weka modeli kwenye SSD (SSD pekee ndiyo ilipimwa).
  Iache wakati wowote kwa Ctrl+C na endesha amri ile ile tena: upakuaji huendelea kutoka kwenye faili za `.part`.
- **cuDNN husakinishwa kwa chaguo-msingi na si sehemu ya hazina hii.** Ni programu ya NVIDIA chini ya leseni ya NVIDIA yenyewe ([maandishi ya leseni](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)), kwa mifumo yenye GPU ya NVIDIA. Hupakuliwa kutoka seva ya NVIDIA bila kuombwa malipo na bila kuingia kwenye akaunti (hakuna akaunti inayohitajika), na hatukupata kifungu chochote katika leseni kinachopunguza matumizi ya kibiashara au ya kibinafsi. `setup.py` huonyesha anwani ya leseni, hupakua faili na kunakili DLL nane tu kando ya `sd-cli.exe`. Leseni ya NVIDIA inasema kwamba yeyote asiyekubali masharti yake haruhusiwi kuipakua, kuisakinisha wala kuitumia; katika hali hiyo, endesha `python scripts/setup.py --no-cudnn`. Bila cuDNN kila kitu kinafanya kazi kwa njia ya VAE ya v0.1.0 iliyo polepole zaidi (`--vae legacy`), na `generate.py` hukuambia hivyo.
- `generate.py` huandika `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, `run.json` (muda, hatua, njia ipi ya VAE iliyoendeshwa, kilele cha kumbukumbu ya GPU, amri kamili) na `log.txt`, na huchapisha `IMAGE_OK <path>`.

## Matumizi

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| Chaguo | Maana |
|---|---|
| `--prompt "<text>"` au `--prompt-file <txt>` | prompt (moja kati ya hizo mbili inahitajika) |
| `--width`, `--height` | mafungu ya 16, 256 hadi 2048; chaguo-msingi 768x1344; zilizojaribiwa: 768x1344, 1344x768, 1024x1024 |
| `--seed` | chaguo-msingi 42 |
| `--out`, `--name` | mzizi wa folda ya matokeo (chaguo-msingi `outputs/`) na jina fupi la folda ya uendeshaji |
| `--models-dir`, `--bin-dir` | mahali `setup.py` ilipoweka modeli na injini |
| `--vae auto` (chaguo-msingi) | cuDNN float32; jaribu kipande kimoja kwanza, kisha tile mbili kubwa, kisha tile ndogo ya chaguo-msingi |
| `--vae tiled` | cuDNN float32, kila mara tile mbili kubwa |
| `--vae legacy` | njia ya v0.1.0: bila cuDNN, tile ndogo. Hutumika kiotomatiki (pamoja na onyo) wakati DLL za cuDNN hazipo |

Hatua (8), cfg (1.0), sampler na scheduler zimewekwa kwa makusudi; tazama [Inaendesha nini](#what-it-runs).

## Ithibitishe mwenyewe

- `generate.py` huchapisha `PIXEL_SHA256 <hex>` kama mojawapo ya mistari yake ya mwisho: hashi ya pikseli zilizofunguliwa. Endesha amri ile ile mara mbili na ulinganishe picha hizo mbili: `python scripts/compare.py <run A>/image.png <run B>/image.png` inapaswa kuchapisha `SAME_PIXELS`.
- `PIXEL_SHA256` ya mifano mitano kwenye mashine yetu iko katika [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md). Hashi ya faili ya PNG inaweza kutofautiana hata pikseli zikiwa sawa, kwa sababu PNG hubeba vigezo vya uundaji kama maandishi; linganisha pikseli, si faili.
- Kikomo cha kweli: hatukupima ikiwa kadi nyingine au dereva nyingine hutoa pikseli zile zile.

## Kwa nini inatosha katika GB 4

- **Waandishi wa modeli wanasema nini.** Model card ya Z-Image-Turbo inasema modeli "fits comfortably within 16G VRAM consumer devices" (inatosha kwa raha kwenye vifaa vya watumiaji vyenye VRAM ya GB 16) ([model card](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)). Hiyo ni kauli kuhusu kadi za GB 16. README rasmi pia inaorodhesha stable-diffusion.cpp kama chaguo la mtu wa tatu na kuinukuu kwa "as little as 4GB of VRAM" (VRAM ya GB 4 tu) ([README](https://github.com/Tongyi-MAI/Z-Image)); hiyo ni dai la mradi wa stable-diffusion.cpp, si sharti la timu ya Z-Image.
- **Tulichopima.** Z-Image-Turbo Q8_0 (faili ya GB 6.6) pamoja na text encoder ya Qwen3-4B Q8_0, 768x1344: kilele cha GPU, kilichopimwa na nvidia-smi kila 2 s (kuruka kwa muda mfupi kunaweza kukosekana), kilikuwa 2949 hadi 2957 MiB (injini ya v0.1.0) na 3057–3059 MiB (injini ya v0.2.0) kwenye kadi ya 4096 MiB. Uzito wa modeli (10 509 MiB; kumbukumbu ya injini huuchapisha kama MB) hubaki kwenye RAM ya mfumo; injini hunakili mtandao hadi GPU sehemu moja kwa wakati mmoja (kipande cha mtandao): sehemu 36, kama mstari wa kumbukumbu `z_image using 36 segments`.
- **Gharama yake.** Muda na kumbukumbu ya mfumo: 193–228 s kwa kila picha, na mchakato wa injini hushikilia takriban 10 667–10 915 MiB za RAM (pamoja na kurasa za modeli zilizopangwa kwenye kumbukumbu) kwenye mashine ya GB 16, kwa hiyo RAM huru hushuka hadi mamia machache ya MiB inapoendesha.
- **Usanidi wa wengine.** Wengine wanaripoti Z-Image kwenye kadi za GB 4 kwa quantization ya chini zaidi au ukubwa mdogo zaidi (kwa mfano, ukurasa wa wiki wa stable-diffusion.cpp kwa kadi za GB 4 unapendekeza Q3_K au Q4_0 katika 1024x512). Mahali tulipotazama (orodha na tarehe katika [`docs/RELATED.md`](docs/RELATED.md)) hatukupata usanidi uliochapishwa unaounganisha yote manne: kadi ya GB 4, Q8_0, 768x1344 au kubwa zaidi, na muda na kumbukumbu ya GPU vilivyopimwa. Hiyo ni kauli kuhusu mahali tulipotazama, si kuhusu kila mahali.
- **Nani anafanya nini.** Kutosha katika GB 4 kunatokana na stable-diffusion.cpp yenyewe: `--offload-to-cpu`, `--mmap`, kufanya kazi kwa vipande, na flash attention (ikiwa imezimwa, uendeshaji mmoja ulihitaji MB 4205 na haukutosha). Viraka vyetu ni kwa ajili ya kasi na hatua bora ya VAE, si kwa ajili ya kutosha. Hatukuendesha injini ya upstream isiyo na viraka kwenye kadi hii, kwa hiyo hatuwezi kusema kama inatosha.

## Inavyofanya kazi

Mabadiliko matatu juu ya stable-diffusion.cpp `master-1088-32d516c` (yote ni swichi; jedwali katika [`patches/README.md`](patches/README.md) huorodhesha kila moja pamoja na environment variable yake):

1. **Refiner huendeshwa mara moja kwa kila hatua.** Jina la kundi lilitumika mara mbili, kwa hiyo vizuizi vinne vya refiner vilihesabiwa mara ya pili. Kurekebisha kunafanya hatua 2 hadi 8 kuwa za haraka takriban 1.3 s kila moja (22.0 hadi 20.7 s) na picha yenye pikseli zilezile (picha 3 zilikaguliwa).
2. **VAE kupitia cuDNN, katika float32.** Hatua ya mwisho (kugeuza latent kuwa pikseli) sasa inatumia convolution ya float32 ya cuDNN ya NVIDIA. Kwenye kadi yetu ilishusha VAE kutoka 23 hadi 27 s hadi 10 hadi 15 s na kupandisha PSNR dhidi ya marejeo kutoka 38 hadi 43 dB hadi 45 hadi 49 dB (tile kubwa).
3. **Kipande kimoja kwanza.** Injini sasa hujaribu kufungua picha nzima kwa kipande kimoja wakati ukaguzi wa kumbukumbu unasema inatosha (ukingo wa 256 MiB), hurudi kwenye tile mbili kubwa, kisha tile ndogo. Kwa kipande kimoja VAE ilichukua takriban 8–16 s na PSNR dhidi ya marejeo ilikuwa 71 hadi 73 dB. Kurudi nyuma kwa lazima kukitokea, picha ina pikseli zile zile kama ya tile (imekaguliwa kwa `PIXEL_SHA256`). Kilichotokea huandikwa katika `run.json` (`stages.vae_path`: `full`, `tile`, `floor` au `retry`).

Pia: `--eager-load` (husoma kurasa za modeli mapema; 241.2 s hadi 220.3 s kwenye picha ile ile, toleo la maendeleo, uendeshaji mmoja kila moja) ni sehemu ya amri iliyowekwa.

<a id="what-it-runs"></a>
## Inaendesha nini

| Sehemu | Faili | Chanzo |
|---|---|---|
| Modeli ya diffusion | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), msingi [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Text encoder | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), autoencoder ya aina ya FLUX.1 |
| Injini | `sd-cli.exe`, stable-diffusion.cpp `32d516c` pamoja na viraka katika [`patches/`](patches) | toleo la v0.2.0 la hazina hii (`sinirsiz-foto-engine-v0.2.0-win-x64-cuda12.8-sm61.zip`) |
| CUDA runtime | `cudart`, `cublas`, `cublasLt` (12.8), bila kubadilishwa | zip kutoka toleo la wan22-pascal-4gb v0.1.0 |
| cuDNN (husakinishwa kwa chaguo-msingi; `--no-cudnn` huruka) | DLL 8, toleo 9.10.2.21 (muundo wa CUDA 11) | seva ya NVIDIA yenyewe, chini ya leseni ya NVIDIA; haihifadhiwi hapa |

Mipangilio iliyowekwa: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`.
Hatupunguzi hatua, hatuongezi negative prompt wala hatuwashi caching: modeli ilitengenezwa (distilled) kwa hatua 8 na haitumii negative prompt (tazama [prompt](docs/PROMPTS.md)).

## Vikomo (soma kabla ya kuitegemea)

- **Windows pekee.** Injini iliyotengenezwa tayari na hati hizi ni za Windows pekee.
- **Kadi moja, mashine moja.** Imepimwa kwenye kompyuta mpakato moja tu ya GTX 1050 Ti GB 4 (i7-7700HQ, RAM ya GB 16, Windows 10, dereva 581.29, modeli kwenye SSD). GPU na dereva nyingine, mashine zenye RAM chini ya GB 16, Linux na macOS: **havijajaribiwa**.
- Kadi na mifumo mingine (njia ipi ipo, na jaribio la jumuiya kwenye kadi ya AMD chini ya Linux ambalo hatukuliendesha sisi wenyewe): [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md).
- **Injini imejengwa kwa Pascal (sm_61) pekee.** Miundo mingine inahitaji muundo wako mwenyewe ([`docs/BUILD.md`](docs/BUILD.md)); hatukujaribu hata mmoja.
- **cuDNN:** tulipima kwa muundo wa CUDA 11 wa cuDNN 9.10.2.21. Muundo wa CUDA 12 una faili tofauti na haukupimwa.
- **Kumbukumbu ni finyu.** RAM huru hushuka hadi mamia machache ya MiB; funga programu nyingine, tengeneza picha moja kwa wakati. Hatujaona kumbukumbu ya GPU ikiisha baada ya ukaguzi wa kumbukumbu wa injini kupita, na hatukujaribu kinachotokea hapo.
- **Ukubwa:** ni 768x1344, 1344x768 na 1024x1024 pekee ndizo zilizojaribiwa. Ukubwa mkubwa zaidi huchapisha onyo na unaweza kuishiwa na kumbukumbu.
- Ufuasi wa prompt ni wa sehemu: picha haifuati prompt yake kila mara katika kila undani. Maandishi ndani ya picha na alama halisi za mahali hazikutathminiwa.
- Marejeo ya PSNR ni decode ya CPU ya injini yetu wenyewe, si utekelezaji huru.
- Nambari katika [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) zinatokana na uendeshaji mmoja kila moja isipokuwa ikisema vinginevyo.

## Leseni na sifa

- Hati na nyaraka za hazina hii: [Apache-2.0](LICENSE) pamoja na faili ya [`NOTICE`](NOTICE). Viraka vya injini katika [`patches/`](patches) ni MIT, kama msimbo wanaoubadilisha.
- stable-diffusion.cpp na ggml ni MIT. Notisi za msimbo wa mtu wa tatu uliojumuishwa kwenye injini ziko katika [`licenses/`](licenses) na [`THIRD_PARTY.md`](THIRD_PARTY.md).
- Faili za modeli hazihifadhiwi hapa; hupakuliwa kutoka vyanzo vilivyo hapo juu chini ya leseni zake zenyewe (Hugging Face inaorodhesha Apache-2.0 kwa zote, ilisomwa tarehe 2026-11-13). Model card haisemi lolote kuhusu nani anamiliki picha zilizotengenezwa, na sisi hatudai lolote kuhusu hilo.
- **cuDNN na CUDA runtime ni mali ya NVIDIA** na haziko chini ya leseni ya hazina hii. cuDNN hupakuliwa kutoka seva ya NVIDIA chini ya leseni ya NVIDIA (`--no-cudnn` huruka hatua hii); DLL za CUDA runtime ziko katika zip tofauti isiyobadilishwa (CUDA Toolkit EULA, Attachment A). Maelezo na kile ambacho hatukuweza kuthibitisha: [`THIRD_PARTY.md`](THIRD_PARTY.md).
- **Sifa.** Kuweka faili ya `NOTICE` pamoja na nakala na kazi zilizotokana nayo ni sharti (Apache-2.0, kifungu cha 4). Zaidi ya hapo, mstari kama "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey" unakaribishwa kwa shukrani, lakini si wa lazima.
- Tafadhali soma [`ETHICS.md`](ETHICS.md): kila picha ni ya kutengenezwa (synthetic), na wewe unawajibika kwa unachochapisha.

## Kuchangia

Jambo lenye manufaa zaidi unaloweza kufanya ni **kujaribu kadi yako** na kutuambia kilichotokea: jina la GPU, dereva, RAM, `run.json` na mistari ya mwisho ya kumbukumbu (fomu ya tatizo "Hardware test report"). Marekebisho ya nyaraka na ya hati pia yanakaribishwa; tazama [`CONTRIBUTING.md`](CONTRIBUTING.md). Ripoti za usalama hupitia njia ya faragha katika [`SECURITY.md`](SECURITY.md).

[Mwongozo wa usakinishaji kwa mawakala wa AI](AGENTS.md) · [Vipimo](docs/MEASUREMENTS.md) · [Utatuzi wa matatizo](docs/TROUBLESHOOTING.md) · [Kujenga injini](docs/BUILD.md) · [Viraka](patches/README.md) · [Prompt](docs/PROMPTS.md) · [Mtu wa tatu](THIRD_PARTY.md) · [Orodha ya mabadiliko](CHANGELOG.md)

Ukurasa huu umetafsiriwa kwa msaada wa AI, na masahihisho yanakaribishwa sana; tazama [`CONTRIBUTING.md`](CONTRIBUTING.md).
