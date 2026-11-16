[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · **日本語** · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**Windows 上で stable-diffusion.cpp を使い、VRAM 4 GB の GTX 1050 Ti（Pascal、sm_61）で Z-Image-Turbo（Q8_0 GGUF）による 768x1344 のテキストから画像への生成を動かします。** 計測は RAM 16 GB のノート PC で行い、プロセスは約 11 GB の RAM を使います。同じシードなら、ピクセル単位で同じ画像になります。計測結果とエンジンのパッチは公開しており、ダウンロードは sha256 で固定してあり、AI コーディングエージェントが手順に沿ってインストールすることもできます。

*非公式プロジェクトです。Tongyi-MAI（Z-Image）、leejet（stable-diffusion.cpp）、NVIDIA とは関係ありません。*

## まずここから

すぐ使えるパッケージを用意してあるので、まずはそれを試してください。ハードウェアが違う場合や途中で失敗した場合も、残りはすべて公開しています。パッチ、ビルド手順、計測結果はこのリポジトリにあり、自分のカード向けにビルドしたり、手順を調整したりできます。

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

手順 2 では約 12.2 GB をダウンロードします。私たちの回線では 1 回あたり 29 分かかりました。最初に "Preflight" ブロックを表示します（お使いの GPU、RAM、空きディスク容量を、私たちの計測値と並べて表示するだけで、情報提供のみです）。
計測したのは GTX 1050 Ti 4 GB のノート PC 用カード（Pascal、compute capability 6.1）だけです。ほかのカードは未検証です。
AI コーディングエージェント（Claude Code、Codex、Cursor など）を使う場合は、[`AGENTS.md`](AGENTS.md) を読ませてください。

## 数字で見る

v0.1.0 の構成と比べると、1 枚の生成に 193–228 s かかります（以前は 261.6 s）。VAE の段階は 8.3–15.9 s です（以前は 29.8 から 36.3 s）。同じシードなら同じピクセルになり、この README のすべての数字には、裏付けとなるコマンドとファイルがあります。

768x1344、シード 42、8 ステップ、同じマシンでの計測です。v0.1.0 の数字は v0.1.0 の README（クリーンルートでのテストと 5 回の実行）から、v0.2.0 の数字は今回のリリースのクリーンルートでのテストからです。

| | v0.1.0（未公開、旧構成） | v0.2.0 |
|---|---|---|
| 1 枚あたりの所要時間（`generate.py` の 1 回の実行） | 261.6 s | 193–228 s |
| VAE デコード（最後の段階） | 29.8 から 36.3 s | 8.3–15.9 s |
| 参照デコードへの近さ（PSNR、高いほど近い） | 38 から 43 dB | 71 から 73 dB |
| GPU メモリのピーク（nvidia-smi） | 2949 から 2957 MiB | 3057–3059 MiB |
| プロセスメモリのピーク | 10.5 から 10.9 GB（当時の記録のまま） | 10 667–10 915 MiB |
| 観測した最小の空き RAM | 331 から 576 MiB | 418–545 MiB |

読み方：参照とは、同じ latent を CPU で float32 のまま 1 つの塊としてデコードしたものです。PSNR は、私たちの GPU でのデコード結果をそれと比べた値です（3 枚）。VAE の段階がその参照にどれだけ近いかを示すもので、画像として良いかどうかを示すものではありません。同じプロンプトとシードでも、v0.2.0 の画像は v0.1.0 とバイト単位では一致しません。VAE の経路を意図的に変えたためです。計測方法と未計測の部分は [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) にあります。

## 作例

**このリポジトリで生成した AI 画像**（Z-Image-Turbo Q8_0、シード 42、8 ステップ）です。実際の写真ではありません。建物などのランドマークや細部は不正確なことがあり、画像がプロンプトのすべての細部に従うとは限りません。実際のプロンプトは [`prompts/`](prompts) と [`docs/PROMPTS.md`](docs/PROMPTS.md) にあります。

| | | |
|---|---|---|
| ![夕暮れどきのエッフェル塔](docs/examples/eiffel.jpg) | ![トルコ風の紅茶グラス](docs/examples/turkish_tea.jpg) | ![年老いた漁師](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`、768x1344 | `prompts/turkish_tea.txt`、768x1344 | `prompts/fisherman.txt`、768x1344 |
| ![丘の斜面の村](docs/examples/village.jpg) | | |
| `prompts/village.txt`、768x1344 | | |

![空から見たイスタンブール](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`、1344x768。実際の写真ではありません。ランドマークは不正確なことがあります。

## クイックスタート

必要なもの：Windows 10/11、VRAM 4 GB の NVIDIA GPU、CUDA 12.8 に対応したドライバ（計測したのはドライバ 581.29 で、それより古いドライバは未検証です。CUDA ランタイム自体は自動でダウンロードされます）、Python 3.10 以降、
git、約 14 GB の空きディスク容量（cuDNN を含むダウンロードは約 12.2 GB で、空きディスク容量の数字は見積もりです）、そして 16 GB の RAM（計測した構成で、それより少ない場合は未検証です）。

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- `setup.py` は最初に "Preflight" ブロックを表示します（お使いの GPU、RAM、空きディスク容量を私たちの計測値と並べて表示します。情報提供のみで、実行を止めることはありません）。続いて [`models.lock.json`](models.lock.json) に固定されたアドレスからダウンロードし、すべてのファイルを sha256 で検証します。`MODEL_OK <name>`、`ENGINE_OK`、`CUDART_OK` を表示し、次に `CUDNN_OK` か `CUDNN_SKIPPED`、最後に `SETUP_OK` を表示します。
  `--models-dir` と `--bin-dir` を指定しない場合は、リポジトリのルートにある `models/` と `bin/` を使います。モデルは SSD に置いてください（計測したのは SSD だけです）。
  Ctrl+C でいつでも止められ、同じコマンドをもう一度実行すれば、ダウンロードは `.part` ファイルから再開します。
- **cuDNN はデフォルトでインストールされ、このリポジトリには含まれません。** NVIDIA のソフトウェアで、NVIDIA 自身のライセンスが適用されます（[ライセンス全文](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)）。NVIDIA GPU を搭載したシステム向けです。NVIDIA のサーバーからのダウンロードでは、支払いも、サインインも求められません。私たちがライセンスの文面を読んだ範囲では、商用利用や個人利用を制限する条項は見つかりませんでした。`setup.py` はライセンスのアドレスを表示してファイルをダウンロードし、8 個の DLL だけを `sd-cli.exe` の隣にコピーします。NVIDIA のライセンスには、その条件に同意しない人はダウンロード、インストール、使用をしてはならない、と書かれています。その場合は `python scripts/setup.py --no-cudnn` を実行してください。cuDNN がなくてもすべて動作しますが、遅い v0.1.0 の VAE 経路（`--vae legacy`）になり、`generate.py` がそのことを表示します。
- `generate.py` は `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`、`run.json`（所要時間、各段階、どの VAE 経路が動いたか、GPU メモリのピーク、実際のコマンド）、`log.txt` を書き出し、`IMAGE_OK <path>` を表示します。

## 使い方

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| オプション | 意味 |
|---|---|
| `--prompt "<text>"` または `--prompt-file <txt>` | プロンプト（どちらか一方が必須） |
| `--width`、`--height` | 16 の倍数、256 から 2048。デフォルトは 768x1344。試したサイズ：768x1344、1344x768、1024x1024 |
| `--seed` | デフォルトは 42 |
| `--out`、`--name` | 出力フォルダのルート（デフォルトは `outputs/`）と、実行ごとのフォルダの短い名前 |
| `--models-dir`、`--bin-dir` | `setup.py` がモデルとエンジンを置いた場所 |
| `--vae auto`（デフォルト） | cuDNN float32。まず 1 つの塊で、次に大きなタイル 2 枚、最後に小さなデフォルトのタイルで試す |
| `--vae tiled` | cuDNN float32。常に大きなタイル 2 枚 |
| `--vae legacy` | v0.1.0 の経路：cuDNN なし、小さなタイル。cuDNN の DLL がないときは自動的に（警告つきで）使われる |

ステップ数（8）、cfg（1.0）、サンプラー、スケジューラは意図的に固定しています。[何を動かすか](#what-it-runs)を参照してください。

## 自分で確かめる

- `generate.py` は最後のほうの行で `PIXEL_SHA256 <hex>` を表示します。デコード後のピクセルのハッシュです。同じコマンドを 2 回実行して 2 枚の画像を比べてください。`python scripts/compare.py <run A>/image.png <run B>/image.png` は `SAME_PIXELS` を表示するはずです。
- 5 つの作例の `PIXEL_SHA256` は、私たちのマシンでの値が [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) にあります。PNG にはパラメータがテキストとして入っているため、ピクセルが同じでも PNG のファイルハッシュは異なることがあります。ファイルではなくピクセルを比べてください。
- 正直な限界：別のカードやドライバで同じピクセルになるかどうかは、計測していません。

## 4 GB に収まる理由

- **モデルの作者の説明。** Z-Image-Turbo のモデルカードには、このモデルは "fits comfortably within 16G VRAM consumer devices"（VRAM 16 GB の一般向けデバイスに余裕で収まる）と書かれています（[モデルカード](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)）。これは 16 GB のカードについての記述です。公式 README は stable-diffusion.cpp をサードパーティの選択肢として挙げ、"as little as 4GB of VRAM"（最小 4 GB の VRAM で）と紹介しています（[README](https://github.com/Tongyi-MAI/Z-Image)）。これは stable-diffusion.cpp プロジェクト側の主張であり、Z-Image チームが求める要件ではありません。
- **私たちが計測したこと。** Z-Image-Turbo Q8_0（6.6 GB のファイル）と Qwen3-4B Q8_0 のテキストエンコーダ、768x1344 の条件で、nvidia-smi が 2 s ごとにサンプリングした GPU のピーク（短いスパイクは見逃す可能性があります）は、4096 MiB のカードで 2949 から 2957 MiB（v0.1.0 のエンジン）と 3057–3059 MiB（v0.2.0 のエンジン）でした。重み（10 509 MiB。エンジンのログでは MB と表示されます）はシステム RAM に残り、エンジンはネットワークを 1 セグメント（ネットワークの一部分）ずつ GPU にコピーします。ログの行 `z_image using 36 segments` にあるとおり、36 セグメントです。
- **代償。** 時間とシステムメモリです。1 枚あたり 193–228 s かかり、16 GB のマシンではエンジンのプロセスが約 10 667–10 915 MiB の RAM を保持します（メモリマップされたモデルのページを含む）。そのため、実行中は空き RAM が数百 MiB まで下がります。
- **ほかの人たちの構成。** 4 GB のカードで、より低い量子化や小さいサイズで Z-Image を動かしたという報告もあります（たとえば stable-diffusion.cpp の wiki の 4 GB カード向けのページでは、1024x512 での Q3_K か Q4_0 を勧めています）。私たちが調べた範囲（一覧と日付は [`docs/RELATED.md`](docs/RELATED.md)）では、次の 4 つをすべて満たす公開済みの構成は見つかりませんでした。4 GB のカード、Q8_0、768x1344 かそれ以上のサイズ、そして計測された時間と GPU メモリです。これは私たちが調べた範囲についての記述であり、あらゆる場所についての記述ではありません。
- **誰が何をしているか。** 4 GB に収まるのは stable-diffusion.cpp 自体の働きによるものです。`--offload-to-cpu`、`--mmap`、スライス単位の処理、そして flash attention です（これを切ると、ある実行は 4205 MB を必要とし、収まりませんでした）。私たちのパッチは速度とより良い VAE の段階のためのもので、収めるためのものではありません。パッチを当てていない上流のエンジンはこのカードでは動かしていないので、収まるかどうかは言えません。

## 仕組み

stable-diffusion.cpp `master-1088-32d516c` の上に 3 つの変更を加えています（すべてスイッチです。各変更と環境変数の対応は [`patches/README.md`](patches/README.md) の表にあります）。

1. **refiner はステップごとに 1 回だけ動きます。** グループ名が 2 回使われていたため、4 つの refiner ブロックが 2 回目の計算をされていました。直した結果、2 から 8 ステップ目は 1 ステップあたり約 1.3 s 速くなり（22.0 s から 20.7 s）、画像のピクセルは一致しました（3 枚で確認）。
2. **VAE は cuDNN で、float32 で動かします。** 最後の段階（latent をピクセルに変える処理）で、NVIDIA の cuDNN の float32 畳み込みを使うようにしました。私たちのカードでは、VAE が 23 から 27 s だったものが 10 から 15 s になり、参照に対する PSNR は 38 から 43 dB から 45 から 49 dB に上がりました（大きなタイルの場合）。
3. **まず 1 つの塊で。** エンジンは、メモリのチェックで収まると判断した場合（余裕 256 MiB）、画像全体を 1 つの塊でデコードしようとします。だめなら大きなタイル 2 枚に、それでもだめなら小さなタイルに切り替えます。1 つの塊のときの VAE は約 8–16 s で、参照に対する PSNR は 71 から 73 dB でした。強制的に切り替わった場合でも、画像はタイル処理のものと同じピクセルになります（`PIXEL_SHA256` で確認）。何が起きたかは `run.json` に書かれます（`stages.vae_path`：`full`、`tile`、`floor`、`retry`）。

そのほか：`--eager-load`（モデルのページを先に読み込む。同じ画像で 241.2 s から 220.3 s、開発ビルド、各 1 回の実行）は固定コマンドの一部です。

<a id="what-it-runs"></a>
## 何を動かすか

| 部品 | ファイル | 入手元 |
|---|---|---|
| 拡散モデル | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF)、ベースモデルは [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| テキストエンコーダ | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo)、FLUX.1 系のオートエンコーダ |
| エンジン | `sd-cli.exe`、stable-diffusion.cpp `32d516c` に [`patches/`](patches) のパッチを適用したもの | このリポジトリの v0.2.0 リリース（`sinirsiz-foto-engine-v0.2.0-win-x64-cuda12.8-sm61.zip`） |
| CUDA ランタイム | `cudart`、`cublas`、`cublasLt`（12.8）、無改変 | wan22-pascal-4gb の v0.1.0 リリースの zip |
| cuDNN（デフォルトでインストール。`--no-cudnn` で省略） | DLL 8 個、バージョン 9.10.2.21（CUDA 11 ビルド） | NVIDIA 自身のサーバー（NVIDIA のライセンスが適用）。ここには置きません |

固定の設定：`--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`。
ステップ数を減らしたり、ネガティブプロンプトを加えたり、キャッシュを有効にしたりはしません。このモデルは 8 ステップ向けに蒸留されており、ネガティブプロンプトは使いません（[プロンプト](docs/PROMPTS.md)を参照）。

## 制限事項（頼る前にお読みください）

- **Windows のみ。** ビルド済みのエンジンとこれらのスクリプトは Windows 専用です。
- **1 種類のカード、1 台のマシン。** 計測したのは GTX 1050 Ti 4 GB のノート PC だけです（i7-7700HQ、RAM 16 GB、Windows 10、ドライバ 581.29、モデルは SSD）。ほかの GPU やドライバ、RAM が 16 GB 未満のマシン、Linux、macOS は**未検証**です。
- その他のカードとシステム(どの道があるか、および私たち自身は実行していない Linux 上の AMD カードでのコミュニティテスト): [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md)。
- **エンジンは Pascal（sm_61）向けにしかビルドしていません。** ほかのアーキテクチャでは自分でビルドする必要があります（[`docs/BUILD.md`](docs/BUILD.md)）。私たちは試していません。
- **cuDNN：** 計測したのは cuDNN 9.10.2.21 の CUDA 11 ビルドです。CUDA 12 ビルドはファイルが異なり、計測していません。
- **メモリに余裕はありません。** 空き RAM は数百 MiB まで下がります。ほかのプログラムは閉じて、画像は 1 枚ずつ生成してください。エンジンのメモリチェックを通ったあとに GPU メモリが足りなくなったことは見ていませんが、その場合に何が起きるかは試していません。
- **サイズ：** 試したのは 768x1344、1344x768、1024x1024 だけです。これより大きいサイズでは警告が表示され、メモリ不足になることがあります。
- プロンプトへの忠実さは部分的です。画像がプロンプトのすべての細部に従うとは限りません。画像内の文字や、現実世界のランドマークは評価していません。
- PSNR の参照は自分たちのエンジンの CPU デコードであり、独立した実装ではありません。
- [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) の数字は、特に記載がない限り、それぞれ 1 回の実行によるものです。

## ライセンスとクレジット

- このリポジトリのスクリプトとドキュメント：[Apache-2.0](LICENSE)、[`NOTICE`](NOTICE) ファイルつき。[`patches/`](patches) のエンジンパッチは、修正対象のコードと同じく MIT です。
- stable-diffusion.cpp と ggml は MIT です。エンジンにコンパイルされているサードパーティコードの表示は [`licenses/`](licenses) と [`THIRD_PARTY.md`](THIRD_PARTY.md) にあります。
- モデルファイルはここには置いていません。上記の入手元から、それぞれのライセンスのもとでダウンロードされます（Hugging Face ではすべて Apache-2.0 と表示されています。2026-11-13 に確認）。モデルカードには生成された画像の権利者についての記述はなく、私たちもそれについては何も主張しません。
- **cuDNN と CUDA ランタイムは NVIDIA の所有物**であり、このリポジトリのライセンスの対象ではありません。cuDNN は NVIDIA のサーバーから NVIDIA のライセンスに基づいてダウンロードされます（`--no-cudnn` で省略）。CUDA ランタイムの DLL は、別の無改変の zip に入っています（CUDA Toolkit EULA、Attachment A）。詳細と、確認できなかった点は [`THIRD_PARTY.md`](THIRD_PARTY.md) にあります。
- **クレジット。** コピーや派生物に `NOTICE` ファイルを付けたままにすることは条件です（Apache-2.0、第 4 条）。それ以上のこととして、"Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey" のような一行を添えていただけるとありがたいですが、必須ではありません。
- [`ETHICS.md`](ETHICS.md) をお読みください。すべての画像は合成されたものであり、公開する内容には公開する人が責任を負います。

## コントリビュート

いちばん役に立つのは、**お使いのカードで試して**結果を教えていただくことです。GPU の名前、ドライバ、RAM、`run.json`、ログの最後の数行を送ってください（"Hardware test report" の Issue フォーム）。ドキュメントやスクリプトの修正も歓迎します。[`CONTRIBUTING.md`](CONTRIBUTING.md) を参照してください。セキュリティに関する報告は、[`SECURITY.md`](SECURITY.md) にある非公開の窓口からお願いします。

[AI エージェント向けインストールガイド](AGENTS.md) · [計測結果](docs/MEASUREMENTS.md) · [トラブルシューティング](docs/TROUBLESHOOTING.md) · [エンジンのビルド](docs/BUILD.md) · [パッチ](patches/README.md) · [プロンプト](docs/PROMPTS.md) · [サードパーティ](THIRD_PARTY.md) · [変更履歴](CHANGELOG.md)

このページは AI の助けを借りて日本語化したものです。誤りや不自然な表現があれば、ぜひご指摘ください。詳しくは [`CONTRIBUTING.md`](CONTRIBUTING.md) をご覧ください。
