[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · **Bahasa Melayu** · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**Z-Image-Turbo (Q8_0 GGUF) untuk menjana imej daripada teks (text-to-image) pada 768x1344, pada GTX 1050 Ti 4 GB (Pascal, sm_61), dengan stable-diffusion.cpp, di Windows.** Diukur pada komputer riba dengan RAM 16 GB, yang mana prosesnya menggunakan kira-kira 11 GB RAM. Seed yang sama menghasilkan piksel yang sama, piksel demi piksel; hasil ukuran dan tampalan (patch) enjinnya diterbitkan, muat turunnya dikunci dengan sha256, dan ejen pengekodan AI boleh memasangnya langkah demi langkah.

*Tidak rasmi. Tiada kaitan dengan Tongyi-MAI (Z-Image), leejet (stable-diffusion.cpp) atau NVIDIA.*

## Mula di sini

Pakej siap pakai disediakan, jadi cuba yang itu dahulu. Jika perkakasan anda berbeza atau ada langkah yang gagal, selebihnya terbuka: patch, resipi binaan dan hasil ukuran ada dalam repositori ini, jadi anda boleh membina untuk kad anda sendiri atau menyesuaikannya.

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

Langkah 2 memuat turun kira-kira 12.2 GB dan pernah mengambil masa 29 minit, sekali sahaja, pada sambungan kami; ia mencetak blok "Preflight" dahulu (GPU, RAM dan ruang cakera kosong anda di sebelah angka yang kami ukur; ia hanya memberi maklumat).
Hanya kad komputer riba GTX 1050 Ti 4 GB (Pascal, compute capability 6.1) yang diukur. Kad lain tidak diuji.
Jika anda menggunakan ejen pengekodan AI (Claude Code, Codex, Cursor dan seumpamanya), arahkan ia ke [`AGENTS.md`](AGENTS.md).

## Sepintas lalu

Berbanding susunan v0.1.0: satu imej mengambil 193–228 s, bukan 261.6 s; peringkat VAE mengambil 8.3–15.9 s, bukan 29.8 hingga 36.3 s; seed yang sama menghasilkan piksel yang sama; dan setiap angka dalam README ini mempunyai arahan dan fail di belakangnya.

768x1344, seed 42, 8 langkah (steps), mesin yang sama. Angka v0.1.0 datang daripada README v0.1.0 (ujian clean-root dan lima larian); angka v0.2.0 datang daripada ujian clean-root keluaran ini.

| | v0.1.0 (tidak pernah diterbitkan; susunan lama) | v0.2.0 |
|---|---|---|
| Masa untuk satu imej (satu larian `generate.py`) | 261.6 s | 193–228 s |
| Penyahkodan VAE (peringkat akhir) | 29.8 hingga 36.3 s | 8.3–15.9 s |
| Kedekatan dengan penyahkodan rujukan (PSNR, semakin tinggi semakin dekat) | 38 hingga 43 dB | 71 hingga 73 dB |
| Puncak memori GPU (nvidia-smi) | 2949 hingga 2957 MiB | 3057–3059 MiB |
| Memori proses, puncak | 10.5 hingga 10.9 GB (seperti yang direkodkan ketika itu) | 10 667–10 915 MiB |
| RAM kosong terendah yang dilihat | 331 hingga 576 MiB | 418–545 MiB |

Cara membacanya: rujukan ialah latent yang sama yang dinyahkod pada CPU sebagai satu keping float32; PSNR membandingkan penyahkodan GPU kami dengannya (3 imej). Ia menunjukkan betapa dekatnya peringkat VAE dengan rujukan itu. Ia tidak menunjukkan betapa cantiknya rupa sesuatu imej. Imej v0.2.0 tidak sama bait demi bait dengan v0.1.0 untuk prompt dan seed yang sama, kerana laluan VAE sengaja diubah. Kaedah dan bahagian yang tidak diukur: [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md).

## Contoh

**Dijana oleh AI dengan repositori ini** (Z-Image-Turbo Q8_0, seed 42, 8 langkah). Ini bukan foto sebenar; mercu tanda dan butirannya
mungkin tidak tepat, dan sesuatu imej tidak sentiasa mengikut prompt-nya dalam setiap butiran. Prompt yang tepat ada dalam [`prompts/`](prompts) dan [`docs/PROMPTS.md`](docs/PROMPTS.md).

| | | |
|---|---|---|
| ![Menara Eiffel pada waktu keemasan](docs/examples/eiffel.jpg) | ![Gelas teh Turki](docs/examples/turkish_tea.jpg) | ![Nelayan warga emas](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![Kampung di lereng bukit](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![Istanbul dari udara](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. Bukan foto sebenar; mercu tanda mungkin tidak tepat.

## Mula pantas

Keperluan: Windows 10/11, GPU NVIDIA 4 GB, pemacu yang menyokong CUDA 12.8 (pemacu 581.29 yang diukur; pemacu yang lebih lama tidak diuji; runtime CUDA itu sendiri dimuat turun untuk anda), Python 3.10 atau lebih baharu,
git, kira-kira 14 GB ruang cakera kosong (muat turun kira-kira 12.2 GB dengan cuDNN; angka ruang cakera kosong ialah anggaran), dan RAM 16 GB (yang diukur; kurang daripada itu tidak diuji).

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- `setup.py` mencetak blok "Preflight" dahulu (GPU, RAM dan ruang cakera kosong anda di sebelah angka yang kami ukur; ia hanya memberi maklumat dan tidak pernah menyekat). Kemudian ia memuat turun daripada alamat terkunci dalam [`models.lock.json`](models.lock.json) dan menyemak setiap fail dengan sha256. Ia mencetak `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK`, kemudian `CUDNN_OK` atau `CUDNN_SKIPPED`, dan akhir sekali `SETUP_OK`.
  Tanpa `--models-dir` dan `--bin-dir`, ia menggunakan `models/` dan `bin/` dalam root repositori; letakkan model pada SSD (hanya SSD yang diukur).
  Hentikannya pada bila-bila masa dengan Ctrl+C dan jalankan arahan yang sama sekali lagi: muat turun disambung daripada fail `.part`.
- **cuDNN dipasang secara lalai dan bukan sebahagian daripada repositori ini.** Ia perisian NVIDIA di bawah lesen NVIDIA sendiri ([teks lesen](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)), untuk sistem dengan GPU NVIDIA. Fail itu dimuat turun daripada pelayan NVIDIA tanpa bayaran diminta dan tanpa log masuk, dan kami tidak menemui klausa dalam lesen yang menghadkan penggunaan komersial mahupun peribadi. `setup.py` menunjukkan alamat lesen, memuat turun fail itu dan hanya menyalin lapan DLL ke sebelah `sd-cli.exe`. Lesen NVIDIA menyatakan bahawa sesiapa yang tidak menerima syaratnya tidak boleh memuat turun, memasang atau menggunakannya; dalam hal itu jalankan `python scripts/setup.py --no-cudnn`. Tanpa cuDNN semuanya masih berjalan dengan laluan VAE v0.1.0 yang lebih perlahan (`--vae legacy`), dan `generate.py` memberitahu perkara itu.
- `generate.py` menulis `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, `run.json` (masa, peringkat, laluan VAE mana yang berjalan, puncak memori GPU, arahan yang tepat) dan `log.txt`, serta mencetak `IMAGE_OK <path>`.

## Penggunaan

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| Pilihan | Maksud |
|---|---|
| `--prompt "<text>"` atau `--prompt-file <txt>` | prompt (salah satu daripada dua diperlukan) |
| `--width`, `--height` | gandaan 16, 256 hingga 2048; lalai 768x1344; yang diuji: 768x1344, 1344x768, 1024x1024 |
| `--seed` | lalai 42 |
| `--out`, `--name` | root folder output (lalai `outputs/`) dan nama pendek untuk folder larian |
| `--models-dir`, `--bin-dir` | tempat `setup.py` meletakkan model dan enjin |
| `--vae auto` (lalai) | cuDNN float32; cuba satu keping dahulu, kemudian dua jubin (tile) besar, kemudian jubin lalai yang kecil |
| `--vae tiled` | cuDNN float32, sentiasa dua jubin besar |
| `--vae legacy` | laluan v0.1.0: tanpa cuDNN, jubin kecil. Digunakan secara automatik (dengan amaran) apabila DLL cuDNN tiada |

Langkah (8), cfg (1.0), sampler dan scheduler sengaja ditetapkan; lihat [Apa yang dijalankan](#what-it-runs).

## Semak sendiri

- `generate.py` mencetak `PIXEL_SHA256 <hex>` sebagai salah satu baris terakhirnya: cincangan (hash) piksel yang dinyahkod. Jalankan arahan yang sama dua kali dan bandingkan kedua-dua imej: `python scripts/compare.py <run A>/image.png <run B>/image.png` sepatutnya mencetak `SAME_PIXELS`.
- `PIXEL_SHA256` bagi kelima-lima contoh pada mesin kami ada dalam [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md). Cincangan fail sesuatu PNG boleh berbeza walaupun pikselnya sama, kerana PNG membawa parameter penjanaan sebagai teks; bandingkan piksel, bukan fail.
- Had yang jujur: kami tidak mengukur sama ada kad atau pemacu lain menghasilkan piksel yang sama.

## Mengapa ia muat dalam 4 GB

- **Apa kata penulis model.** Model card Z-Image-Turbo menyatakan model ini "fits comfortably within 16G VRAM consumer devices" (muat dengan selesa pada peranti pengguna dengan VRAM 16 GB) ([model card](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)). Itu kenyataan tentang kad 16 GB. README rasminya juga menyenaraikan stable-diffusion.cpp sebagai pilihan pihak ketiga dan memetiknya untuk "as little as 4GB of VRAM" (VRAM serendah 4 GB) ([README](https://github.com/Tongyi-MAI/Z-Image)); itu tuntutan projek stable-diffusion.cpp, bukan syarat daripada pasukan Z-Image.
- **Apa yang kami ukur.** Z-Image-Turbo Q8_0 (fail 6.6 GB) dengan text encoder Qwen3-4B Q8_0, 768x1344: puncak GPU, disampel oleh nvidia-smi setiap 2 s (lonjakan singkat mungkin terlepas), ialah 2949 hingga 2957 MiB (enjin v0.1.0) dan 3057–3059 MiB (enjin v0.2.0) pada kad 4096 MiB. Pemberat (10 509 MiB; log enjin mencetaknya sebagai MB) kekal dalam RAM sistem; enjin menyalin rangkaian ke GPU satu segmen (satu keping rangkaian) pada satu masa: 36 segmen, seperti dalam baris log `z_image using 36 segments`.
- **Kosnya.** Masa dan memori sistem: 193–228 s bagi setiap imej, dan proses enjin memegang kira-kira 10 667–10 915 MiB RAM (termasuk halaman model yang dipetakan ke memori) pada mesin 16 GB, jadi RAM kosong jatuh kepada beberapa ratus MiB semasa ia berjalan.
- **Persediaan orang lain.** Orang lain melaporkan Z-Image pada kad 4 GB dengan kuantisasi yang lebih rendah atau saiz yang lebih kecil (contohnya halaman wiki stable-diffusion.cpp untuk kad 4 GB mengesyorkan Q3_K atau Q4_0 pada 1024x512). Di tempat yang kami periksa (senarai dan tarikh dalam [`docs/RELATED.md`](docs/RELATED.md)) kami tidak menemui persediaan terbit yang menggabungkan keempat-empatnya: kad 4 GB, Q8_0, 768x1344 atau lebih besar, serta masa dan memori GPU yang diukur. Ini kenyataan tentang tempat yang kami periksa, bukan tentang semua tempat.
- **Siapa buat apa.** Muat dalam 4 GB datang daripada stable-diffusion.cpp sendiri: `--offload-to-cpu`, `--mmap`, bekerja secara kepingan, dan flash attention (apabila dimatikan, satu larian memerlukan 4205 MB dan tidak muat). Patch kami adalah untuk kelajuan dan peringkat VAE yang lebih baik, bukan untuk muat. Kami tidak menjalankan enjin upstream tanpa patch pada kad ini, jadi kami tidak dapat mengatakan sama ada ia muat.

## Cara ia berfungsi

Tiga perubahan di atas stable-diffusion.cpp `master-1088-32d516c` (semuanya suis; jadual dalam [`patches/README.md`](patches/README.md) menyenaraikan setiap satu dengan environment variable-nya):

1. **Refiner berjalan sekali setiap langkah.** Satu nama kumpulan digunakan dua kali, jadi empat blok refiner dikira kali kedua. Selepas dibetulkan, langkah 2 hingga 8 masing-masing kira-kira 1.3 s lebih pantas (22.0 kepada 20.7 s) dengan imej yang sama piksel demi piksel (3 imej disemak).
2. **VAE melalui cuDNN, dalam float32.** Peringkat akhir (menukar latent kepada piksel) kini menggunakan konvolusi float32 cuDNN milik NVIDIA. Pada kad kami, VAE turun daripada 23 hingga 27 s kepada 10 hingga 15 s, dan PSNR terhadap rujukan naik daripada 38 hingga 43 dB kepada 45 hingga 49 dB (dengan jubin besar).
3. **Satu keping dahulu.** Enjin kini cuba menyahkod keseluruhan imej dalam satu keping apabila semakan memori menyatakan ia muat (margin 256 MiB), jatuh ke dua jubin besar jika tidak, kemudian ke jubin kecil. Dalam satu keping, VAE mengambil kira-kira 8–16 s dan PSNR terhadap rujukan ialah 71 hingga 73 dB. Jika berlaku penurunan paksa, imej itu mempunyai piksel yang sama dengan versi berjubin (disemak dengan `PIXEL_SHA256`). Apa yang berlaku ditulis dalam `run.json` (`stages.vae_path`: `full`, `tile`, `floor` atau `retry`).

Selain itu: `--eager-load` (membaca halaman model di awal; 241.2 s kepada 220.3 s pada imej yang sama, binaan pembangunan, satu larian setiap satu) merupakan sebahagian daripada arahan tetap.

<a id="what-it-runs"></a>
## Apa yang dijalankan

| Bahagian | Fail | Sumber |
|---|---|---|
| Model resapan (diffusion) | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), asas [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Text encoder | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), autoencoder jenis FLUX.1 |
| Enjin | `sd-cli.exe`, stable-diffusion.cpp `32d516c` dengan patch dalam [`patches/`](patches) | keluaran v0.2.0 repositori ini (`sinirsiz-foto-engine-v0.2.0-win-x64-cuda12.8-sm61.zip`) |
| Runtime CUDA | `cudart`, `cublas`, `cublasLt` (12.8), tidak diubah suai | zip daripada keluaran v0.1.0 wan22-pascal-4gb |
| cuDNN (dipasang secara lalai; `--no-cudnn` melangkaunya) | 8 DLL, versi 9.10.2.21 (binaan CUDA 11) | pelayan NVIDIA sendiri, di bawah lesen NVIDIA; tidak disimpan di sini |

Tetapan tetap: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`.
Kami tidak mengurangkan bilangan langkah, tidak menambah negative prompt dan tidak mengaktifkan caching: model ini disuling (distilled) untuk 8 langkah dan tidak menggunakan negative prompt (lihat [prompts](docs/PROMPTS.md)).

## Had (baca sebelum bergantung padanya)

- **Windows sahaja.** Enjin siap pakai dan skrip ini hanya untuk Windows.
- **Satu kad, satu mesin.** Diukur hanya pada komputer riba GTX 1050 Ti 4 GB (i7-7700HQ, RAM 16 GB, Windows 10, pemacu 581.29, model pada SSD). GPU dan pemacu lain, mesin dengan RAM kurang daripada 16 GB, Linux dan macOS: **tidak diuji**.
- **Enjin hanya dibina untuk Pascal (sm_61).** Seni bina lain memerlukan binaan anda sendiri ([`docs/BUILD.md`](docs/BUILD.md)); kami tidak menguji satu pun.
- **cuDNN:** kami mengukur dengan binaan CUDA 11 bagi cuDNN 9.10.2.21. Binaan CUDA 12 mempunyai fail yang berbeza dan tidak diukur.
- **Memori sangat terhad.** RAM kosong jatuh kepada beberapa ratus MiB; tutup program lain, jalankan satu imej pada satu masa. Kami belum pernah melihat memori GPU kehabisan selepas semakan memori enjin lulus, dan kami tidak menguji apa yang berlaku ketika itu.
- **Saiz:** hanya 768x1344, 1344x768 dan 1024x1024 yang diuji. Saiz yang lebih besar mencetak amaran dan mungkin kehabisan memori.
- Kesetiaan kepada prompt hanya separa: sesuatu imej tidak sentiasa mengikut prompt-nya dalam setiap butiran. Teks di dalam imej dan mercu tanda dunia sebenar tidak dinilai.
- Rujukan PSNR ialah penyahkodan CPU enjin kami sendiri, bukan pelaksanaan bebas.
- Angka dalam [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) datang daripada satu larian setiap satu melainkan dinyatakan sebaliknya.

## Lesen dan kredit

- Skrip dan dokumen repositori ini: [Apache-2.0](LICENSE) dengan fail [`NOTICE`](NOTICE). Patch enjin dalam [`patches/`](patches) berlesen MIT, seperti kod yang diubahnya.
- stable-diffusion.cpp dan ggml berlesen MIT. Notis untuk kod pihak ketiga yang dikompil ke dalam enjin ada dalam [`licenses/`](licenses) dan [`THIRD_PARTY.md`](THIRD_PARTY.md).
- Fail model tidak disimpan di sini; ia dimuat turun daripada sumber di atas di bawah lesen masing-masing (Hugging Face menyenaraikan Apache-2.0 untuk kesemuanya, dibaca pada 2026-11-13). Model card tidak menyatakan siapa pemilik imej yang dijana, dan kami tidak membuat sebarang tuntutan mengenainya.
- **cuDNN dan runtime CUDA ialah hak milik NVIDIA** dan tidak berada di bawah lesen repositori ini. cuDNN dimuat turun daripada pelayan NVIDIA di bawah lesen NVIDIA (`--no-cudnn` melangkaunya); DLL runtime CUDA berada dalam zip berasingan yang tidak diubah suai (CUDA Toolkit EULA, Attachment A). Butiran dan perkara yang tidak dapat kami sahkan: [`THIRD_PARTY.md`](THIRD_PARTY.md).
- **Kredit.** Mengekalkan fail `NOTICE` bersama salinan dan karya terbitan ialah syarat (Apache-2.0, bahagian 4). Di luar itu, baris seperti "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey" amat dihargai, tetapi tidak diwajibkan.
- Sila baca [`ETHICS.md`](ETHICS.md): setiap imej bersifat sintetik, dan anda bertanggungjawab ke atas apa yang anda terbitkan.

## Menyumbang

Perkara paling berguna yang boleh anda lakukan ialah **menguji kad anda** dan memberitahu kami apa yang berlaku: nama GPU, pemacu, RAM, `run.json` dan baris terakhir log (borang isu "Hardware test report"). Pembetulan pada dokumen dan skrip juga dialu-alukan; lihat [`CONTRIBUTING.md`](CONTRIBUTING.md). Laporan keselamatan dihantar melalui saluran persendirian dalam [`SECURITY.md`](SECURITY.md).

[Panduan pemasangan untuk ejen AI](AGENTS.md) · [Hasil ukuran](docs/MEASUREMENTS.md) · [Penyelesaian masalah](docs/TROUBLESHOOTING.md) · [Membina enjin](docs/BUILD.md) · [Patch](patches/README.md) · [Prompts](docs/PROMPTS.md) · [Pihak ketiga](THIRD_PARTY.md) · [Log perubahan](CHANGELOG.md)

Halaman ini disesuaikan ke dalam Bahasa Melayu dengan bantuan AI; pembetulan amat dialu-alukan, lihat [`CONTRIBUTING.md`](CONTRIBUTING.md).
