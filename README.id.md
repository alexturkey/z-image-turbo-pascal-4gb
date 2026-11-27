[Türkçe](README.tr.md) · [English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Norsk](README.nb.md) · [Svenska](README.sv.md) · [Suomi](README.fi.md) · [Ελληνικά](README.el.md) · [العربية](README.ar.md) · [עברית](README.he.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · **Bahasa Indonesia** · [Bahasa Melayu](README.ms.md) · [Tagalog](README.tl.md) · [မြန်မာ](README.my.md) · [ខ្មែរ](README.km.md) · [ລາວ](README.lo.md) · [Kiswahili](README.sw.md)

# Sınırsız Foto

**Z-Image-Turbo (Q8_0 GGUF) untuk membuat gambar dari teks (text-to-image) pada 768x1344, di GTX 1050 Ti 4 GB (Pascal, sm_61), dengan stable-diffusion.cpp, di Windows.** Diukur pada laptop dengan RAM 16 GB, tempat prosesnya memakai sekitar 11 GB RAM. Seed yang sama menghasilkan piksel yang sama, piksel demi piksel; hasil pengukuran dan patch mesinnya dipublikasikan, unduhannya dikunci dengan sha256, dan agen coding AI dapat memasangnya langkah demi langkah.

*Tidak resmi. Tidak berafiliasi dengan Tongyi-MAI (Z-Image), leejet (stable-diffusion.cpp), maupun NVIDIA.*

> **Memakai agen pemrograman AI (Codex, Claude Code, Gemini, Cursor)?** Berikan satu kalimat ini kepadanya: “Baca `AGENTS_HIZLI.md` sampai habis, jalankan `python scripts/tani.py` lebih dulu, catat kemajuanmu di `DURUM.md`, dan tanyakan kepada saya sebelum menghapus atau memindahkan apa pun, mengubah Python sistem atau PATH, atau menurunkan pengaturan kualitas.” Agen akan mendiagnosis PC ini, menulis daftar periksa, dan bertanya kepada Anda pada setiap keputusan.

## Mulai dari sini

Paket siap pakai tersedia, jadi coba itu dulu. Jika perangkat keras Anda berbeda atau ada langkah yang gagal, sisanya terbuka: patch, resep build, dan hasil pengukuran ada di repositori ini, sehingga Anda bisa membangun untuk kartu Anda sendiri atau menyesuaikannya.

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

Langkah 2 mengunduh sekitar 12.2 GB dan pernah memakan waktu 29 menit, satu kali, pada koneksi kami; langkah ini lebih dulu mencetak blok "Preflight" (GPU, RAM, dan sisa disk Anda di samping angka yang kami ukur; hanya memberi informasi).
Hanya kartu laptop GTX 1050 Ti 4 GB (Pascal, compute capability 6.1) yang diukur. Kartu lain tidak diuji.
Jika Anda memakai agen coding AI (Claude Code, Codex, Cursor, dan sejenisnya), arahkan ke [`AGENTS.md`](AGENTS.md).

## Sekilas

Dibandingkan dengan susunan v0.1.0: satu gambar butuh 188–193 s, bukan 261.6 s; tahap VAE butuh 12.5–21.7 s, bukan 29.8 sampai 36.3 s; seed yang sama menghasilkan piksel yang sama; dan setiap angka di README ini punya perintah dan berkas di baliknya.

768x1344, seed 42, 8 langkah (steps), mesin yang sama. Angka v0.1.0 berasal dari README v0.1.0 (uji clean-root dan lima kali jalan); angka v0.3.0 berasal dari uji clean-root rilis ini.

| | v0.1.0 (tidak pernah dipublikasikan; susunan lama) | v0.3.0 |
|---|---|---|
| Waktu untuk satu gambar (satu kali jalan `generate.py`) | 261.6 s | 188–193 s |
| Dekode VAE (tahap terakhir) | 29.8 sampai 36.3 s | 12.5–21.7 s |
| Kedekatan dengan dekode acuan (PSNR, makin tinggi makin dekat) | 38 sampai 43 dB | 71 sampai 73 dB |
| Puncak memori GPU (nvidia-smi) | 2949 sampai 2957 MiB | 3057–3059 MiB |
| Memori proses, puncak | 10.5 sampai 10.9 GB (sebagaimana tercatat saat itu) | 10 489–11 203 MiB |
| RAM bebas terendah yang terlihat | 331 sampai 576 MiB | 303–532 MiB |

Cara membacanya: acuan adalah latent yang sama yang didekode di CPU sebagai satu potongan float32; PSNR membandingkan dekode GPU kami dengan acuan itu (3 gambar). Angka ini menunjukkan seberapa dekat tahap VAE dengan acuan tersebut. Angka ini tidak menunjukkan seberapa bagus tampilan sebuah gambar. Gambar v0.2.0 tidak identik byte demi byte dengan v0.1.0 untuk prompt dan seed yang sama, karena jalur VAE sengaja diubah. Metode dan bagian yang tidak diukur: [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md).

## Contoh

**Dibuat dengan AI memakai repositori ini** (Z-Image-Turbo Q8_0, seed 42, 8 langkah). Ini bukan foto asli; landmark dan detailnya
bisa tidak akurat, dan sebuah gambar tidak selalu mengikuti prompt-nya dalam setiap detail. Prompt lengkapnya ada di [`prompts/`](prompts) dan [`docs/PROMPTS.md`](docs/PROMPTS.md).

| | | |
|---|---|---|
| ![Menara Eiffel saat golden hour](docs/examples/eiffel.jpg) | ![Gelas teh Turki](docs/examples/turkish_tea.jpg) | ![Nelayan lanjut usia](docs/examples/fisherman.jpg) |
| `prompts/eiffel.txt`, 768x1344 | `prompts/turkish_tea.txt`, 768x1344 | `prompts/fisherman.txt`, 768x1344 |
| ![Desa di lereng bukit](docs/examples/village.jpg) | | |
| `prompts/village.txt`, 768x1344 | | |

![Istanbul dari udara](docs/examples/istanbul_aerial.jpg)

`prompts/istanbul_aerial.txt`, 1344x768. Bukan foto asli; landmark bisa tidak akurat.

## Mulai cepat

Persyaratan: Windows 10/11, GPU NVIDIA 4 GB, driver yang mendukung CUDA 12.8 (driver 581.29 yang diukur; driver yang lebih lama tidak diuji; runtime CUDA-nya sendiri diunduhkan untuk Anda), Python 3.10 atau lebih baru,
git, sekitar 14 GB ruang disk kosong (unduhan sekitar 12.2 GB dengan cuDNN; angka ruang disk ini hanya perkiraan), dan RAM 16 GB (yang diukur; di bawah itu tidak diuji).

```powershell
git clone https://github.com/alexturkey/z-image-turbo-pascal-4gb.git
cd z-image-turbo-pascal-4gb
python scripts/setup.py
python scripts/generate.py --prompt-file prompts/eiffel.txt
```

- `setup.py` lebih dulu mencetak blok "Preflight" (GPU, RAM, dan sisa disk Anda di samping angka yang kami ukur; hanya memberi informasi dan tidak pernah memblokir). Setelah itu ia mengunduh dari alamat terkunci di [`models.lock.json`](models.lock.json) dan memeriksa setiap berkas dengan sha256. Ia mencetak `MODEL_OK <name>`, `ENGINE_OK`, `CUDART_OK`, lalu `CUDNN_OK` atau `CUDNN_SKIPPED`, dan terakhir `SETUP_OK`.
  Tanpa `--models-dir` dan `--bin-dir`, ia memakai `models/` dan `bin/` di root repositori; letakkan model di SSD (hanya SSD yang diukur).
  Hentikan kapan saja dengan Ctrl+C lalu jalankan perintah yang sama lagi: unduhan dilanjutkan dari berkas `.part`.
- **cuDNN dipasang secara default dan bukan bagian dari repositori ini.** Ini perangkat lunak NVIDIA di bawah lisensi NVIDIA sendiri ([teks lisensi](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/eula.html)), untuk sistem dengan GPU NVIDIA. Berkasnya diunduh dari server NVIDIA tanpa diminta pembayaran dan tanpa login, dan kami tidak menemukan klausul dalam lisensi yang membatasi penggunaan komersial maupun pribadi. `setup.py` menampilkan alamat lisensinya, mengunduh berkasnya, dan hanya menyalin delapan DLL ke samping `sd-cli.exe`. Lisensi NVIDIA menyatakan bahwa siapa pun yang tidak menerima ketentuannya tidak boleh mengunduh, memasang, atau menggunakannya; dalam hal itu jalankan `python scripts/setup.py --no-cudnn`. Tanpa cuDNN semuanya tetap berjalan dengan jalur VAE v0.1.0 yang lebih lambat (`--vae legacy`), dan `generate.py` memberi tahu hal itu.
- `generate.py` menulis `outputs/<YYYYmmdd_HHMMSS>_<name>/image.png`, `run.json` (waktu, tahap, jalur VAE mana yang berjalan, puncak memori GPU, perintah persisnya) dan `log.txt`, lalu mencetak `IMAGE_OK <path>`.

## Penggunaan

```powershell
python scripts/generate.py --prompt "A lighthouse on a cliff at dawn, realistic photograph"
python scripts/generate.py --prompt-file prompts/eiffel.txt --width 1344 --height 768 --seed 7 --vae auto
```

| Opsi | Arti |
|---|---|
| `--prompt "<text>"` atau `--prompt-file <txt>` | prompt (salah satu dari keduanya wajib) |
| `--width`, `--height` | kelipatan 16, 256 sampai 2048; bawaan 768x1344; yang diuji: 768x1344, 1344x768, 1024x1024 |
| `--seed` | bawaan 42 |
| `--out`, `--name` | root folder keluaran (bawaan `outputs/`) dan nama singkat untuk folder hasil jalan |
| `--models-dir`, `--bin-dir` | tempat `setup.py` menaruh model dan mesin |
| `--vae auto` (bawaan) | cuDNN float32; coba satu potongan dulu, lalu dua tile besar, lalu tile kecil bawaan |
| `--vae tiled` | cuDNN float32, selalu dua tile besar |
| `--vae legacy` | jalur v0.1.0: tanpa cuDNN, tile kecil. Dipakai otomatis (dengan peringatan) bila DLL cuDNN tidak ada |

Langkah (8), cfg (1.0), sampler, dan scheduler sengaja dibuat tetap; lihat [Apa yang dijalankan](#what-it-runs).

## Periksa sendiri

- `generate.py` mencetak `PIXEL_SHA256 <hex>` sebagai salah satu baris terakhirnya: hash dari piksel hasil dekode. Jalankan perintah yang sama dua kali lalu bandingkan kedua gambar: `python scripts/compare.py <run A>/image.png <run B>/image.png` seharusnya mencetak `SAME_PIXELS`.
- `PIXEL_SHA256` dari kelima contoh di mesin kami ada di [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md). Hash berkas sebuah PNG bisa berbeda meskipun pikselnya sama, karena PNG membawa parameter pembuatan sebagai teks; bandingkan piksel, bukan berkas.
- Batas yang jujur: kami tidak mengukur apakah kartu atau driver lain menghasilkan piksel yang sama.

## Mengapa muat di 4 GB

- **Kata penulis model.** Model card Z-Image-Turbo menyebut model ini "fits comfortably within 16G VRAM consumer devices" (muat dengan nyaman di perangkat konsumen dengan VRAM 16 GB) ([model card](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)). Itu pernyataan tentang kartu 16 GB. README resminya juga mencantumkan stable-diffusion.cpp sebagai opsi pihak ketiga dan mengutipnya untuk "as little as 4GB of VRAM" (VRAM sekecil 4 GB) ([README](https://github.com/Tongyi-MAI/Z-Image)); itu klaim proyek stable-diffusion.cpp, bukan persyaratan dari tim Z-Image.
- **Yang kami ukur.** Z-Image-Turbo Q8_0 (berkas 6.6 GB) dengan text encoder Qwen3-4B Q8_0, 768x1344: puncak GPU, dicuplik nvidia-smi tiap 2 s (lonjakan singkat bisa terlewat), adalah 2949 sampai 2957 MiB (mesin v0.1.0) dan 3057–3059 MiB (mesin v0.2.0) pada kartu 4096 MiB. Bobotnya (10 509 MiB; log mesin menuliskannya sebagai MB) tetap di RAM sistem; mesin menyalin jaringan ke GPU satu segmen (potongan dari jaringan) sekali waktu: 36 segmen, seperti pada baris log `z_image using 36 segments`.
- **Biayanya.** Waktu dan memori sistem: 188–193 s per gambar, dan proses mesin menahan sekitar 10 489–11 203 MiB RAM (termasuk halaman model yang dipetakan ke memori) pada mesin 16 GB, sehingga RAM bebas turun ke beberapa ratus MiB selama berjalan.
- **Pengaturan orang lain.** Orang lain melaporkan Z-Image di kartu 4 GB dengan kuantisasi yang lebih rendah atau ukuran yang lebih kecil (misalnya halaman wiki stable-diffusion.cpp untuk kartu 4 GB merekomendasikan Q3_K atau Q4_0 pada 1024x512). Di tempat-tempat yang kami periksa (daftar dan tanggalnya di [`docs/RELATED.md`](docs/RELATED.md)) kami tidak menemukan pengaturan terpublikasi yang menggabungkan keempatnya: kartu 4 GB, Q8_0, 768x1344 atau lebih besar, serta waktu dan memori GPU yang terukur. Ini pernyataan tentang tempat yang kami periksa, bukan tentang semua tempat.
- **Siapa mengerjakan apa.** Muat di 4 GB berasal dari stable-diffusion.cpp sendiri: `--offload-to-cpu`, `--mmap`, bekerja per potongan, dan flash attention (saat dimatikan, satu kali jalan membutuhkan 4205 MB dan tidak muat). Patch kami untuk kecepatan dan tahap VAE yang lebih baik, bukan agar muat. Kami tidak menjalankan mesin upstream tanpa patch di kartu ini, jadi kami tidak bisa mengatakan apakah ia muat.

## Cara kerjanya

Tiga perubahan di atas stable-diffusion.cpp `master-1088-32d516c` (semuanya berupa saklar; tabel di [`patches/README.md`](patches/README.md) mendaftar tiap perubahan beserta environment variable-nya):

1. **Refiner berjalan sekali per langkah.** Satu nama grup terpakai dua kali, sehingga empat blok refiner dihitung untuk kedua kalinya. Setelah diperbaiki, langkah 2 sampai 8 masing-masing sekitar 1.3 s lebih cepat (22.0 menjadi 20.7 s) dengan gambar yang identik piksel demi piksel (3 gambar diperiksa).
2. **VAE lewat cuDNN, dalam float32.** Tahap terakhir (mengubah latent menjadi piksel) kini memakai konvolusi float32 cuDNN milik NVIDIA. Di kartu kami, VAE turun dari 23 sampai 27 s menjadi 10 sampai 15 s, dan PSNR terhadap acuan naik dari 38 sampai 43 dB menjadi 45 sampai 49 dB (dengan tile besar).
3. **Satu potongan dulu.** Mesin kini mencoba mendekode seluruh gambar dalam satu potongan bila pemeriksaan memori menyatakan muat (margin 256 MiB), turun ke dua tile besar bila tidak, lalu ke tile kecil. Dalam satu potongan, VAE memakan sekitar 8–16 s dan PSNR terhadap acuan 71 sampai 73 dB. Jika terjadi penurunan paksa, gambarnya punya piksel yang sama dengan versi bertile (diperiksa dengan `PIXEL_SHA256`). Apa yang terjadi ditulis di `run.json` (`stages.vae_path`: `full`, `tile`, `floor` atau `retry`).

Selain itu: `--eager-load` (membaca halaman model di awal; 241.2 s menjadi 220.3 s pada gambar yang sama, build pengembangan, masing-masing satu kali jalan) termasuk dalam perintah tetap.

<a id="what-it-runs"></a>
## Apa yang dijalankan

| Bagian | Berkas | Sumber |
|---|---|---|
| Model difusi | `z_image_turbo-Q8_0.gguf` (6,577,440,704 B) | [leejet/Z-Image-Turbo-GGUF](https://huggingface.co/leejet/Z-Image-Turbo-GGUF), dasar [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| Text encoder | `Qwen3-4B-Instruct-2507-Q8_0.gguf` (4,280,405,600 B) | [unsloth/Qwen3-4B-Instruct-2507-GGUF](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) |
| VAE | `ae.safetensors` (335,304,388 B) | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo), autoencoder tipe FLUX.1 |
| Mesin | `sd-cli.exe`, stable-diffusion.cpp `32d516c` dengan patch di [`patches/`](patches) | rilis v0.3.0 repositori ini (`sinirsiz-foto-engine-v0.3.0-win-x64-cuda12.8-sm61.zip`) |
| Runtime CUDA | `cudart`, `cublas`, `cublasLt` (12.8), tanpa modifikasi | zip dari rilis v0.1.0 wan22-pascal-4gb |
| cuDNN (dipasang secara default; `--no-cudnn` melewatinya) | 8 DLL, versi 9.10.2.21 (build CUDA 11) | server NVIDIA sendiri, di bawah lisensi NVIDIA; tidak disimpan di sini |

Pengaturan tetap: `--cfg-scale 1.0 --steps 8 --sampling-method euler --scheduler simple --offload-to-cpu --mmap --eager-load --flash-attn on`.
Kami tidak menurunkan jumlah langkah, tidak menambahkan negative prompt, dan tidak mengaktifkan caching: model ini didistilasi untuk 8 langkah dan tidak memakai negative prompt (lihat [prompts](docs/PROMPTS.md)).

## Batasan (baca sebelum mengandalkannya)

- **Hanya Windows.** Mesin siap pakai dan skrip-skrip ini hanya untuk Windows.
- **Satu kartu, satu mesin.** Diukur hanya pada laptop GTX 1050 Ti 4 GB (i7-7700HQ, RAM 16 GB, Windows 10, driver 581.29, model di SSD). GPU dan driver lain, mesin dengan RAM kurang dari 16 GB, Linux, dan macOS: **tidak diuji**.
- Kartu dan sistem lain (jalur apa yang tersedia, dan uji komunitas pada kartu AMD di Linux yang tidak kami jalankan sendiri): [docs/OTHER_GPUS.md](docs/OTHER_GPUS.md).
- **Mesin hanya dibangun untuk Pascal (sm_61).** Arsitektur lain memerlukan build buatan Anda sendiri ([`docs/BUILD.md`](docs/BUILD.md)); kami tidak menguji satu pun.
- **cuDNN:** kami mengukur dengan build CUDA 11 dari cuDNN 9.10.2.21. Build CUDA 12 berisi berkas yang berbeda dan tidak diukur.
- **Memori sangat mepet.** RAM bebas turun ke beberapa ratus MiB; tutup program lain, jalankan satu gambar dalam satu waktu. Kami belum pernah melihat memori GPU habis setelah pemeriksaan memori mesin lolos, dan kami tidak menguji apa yang terjadi saat itu.
- **Ukuran:** hanya 768x1344, 1344x768, dan 1024x1024 yang diuji. Ukuran yang lebih besar mencetak peringatan dan bisa kehabisan memori.
- Kesesuaian dengan prompt hanya sebagian: sebuah gambar tidak selalu mengikuti prompt-nya dalam setiap detail. Teks di dalam gambar dan landmark dunia nyata tidak dievaluasi.
- Acuan PSNR adalah dekode CPU dari mesin kami sendiri, bukan implementasi independen.
- Angka di [`docs/MEASUREMENTS.md`](docs/MEASUREMENTS.md) berasal dari satu kali jalan masing-masing kecuali disebutkan lain.

## Lisensi dan kredit

- Skrip dan dokumen repositori ini: [Apache-2.0](LICENSE) dengan berkas [`NOTICE`](NOTICE). Patch mesin di [`patches/`](patches) berlisensi MIT, seperti kode yang mereka ubah.
- stable-diffusion.cpp dan ggml berlisensi MIT. Pemberitahuan untuk kode pihak ketiga yang dikompilasi ke dalam mesin ada di [`licenses/`](licenses) dan [`THIRD_PARTY.md`](THIRD_PARTY.md).
- Berkas model tidak disimpan di sini; berkas itu diunduh dari sumber di atas dengan lisensinya masing-masing (Hugging Face mencantumkan Apache-2.0 untuk semuanya, dibaca pada 2026-11-13). Model card tidak menyebut siapa pemilik gambar yang dihasilkan, dan kami tidak membuat klaim apa pun tentang itu.
- **cuDNN dan runtime CUDA adalah milik NVIDIA** dan tidak berada di bawah lisensi repositori ini. cuDNN diunduh dari server NVIDIA di bawah lisensi NVIDIA (`--no-cudnn` melewatinya); DLL runtime CUDA ada di zip terpisah yang tidak dimodifikasi (CUDA Toolkit EULA, Attachment A). Rincian dan hal yang tidak dapat kami verifikasi: [`THIRD_PARTY.md`](THIRD_PARTY.md).
- **Kredit.** Menyertakan berkas `NOTICE` bersama salinan dan karya turunan adalah syarat (Apache-2.0, bagian 4). Di luar itu, baris seperti "Based on Sınırsız Foto by Ali Haydar Öztürk (Ozturk), https://github.com/alexturkey" kami hargai, tetapi tidak diwajibkan.
- Mohon baca [`ETHICS.md`](ETHICS.md): setiap gambar bersifat sintetis, dan Anda bertanggung jawab atas apa yang Anda publikasikan.

## Berkontribusi

Hal paling berguna yang bisa Anda lakukan adalah **menguji kartu Anda** dan memberi tahu kami hasilnya: nama GPU, driver, RAM, `run.json`, dan baris-baris terakhir log (formulir issue "Hardware test report"). Perbaikan pada dokumen dan skrip juga kami sambut; lihat [`CONTRIBUTING.md`](CONTRIBUTING.md). Laporan keamanan dikirim lewat jalur privat di [`SECURITY.md`](SECURITY.md).

[Panduan pemasangan untuk agen AI](AGENTS.md) · [Pengukuran](docs/MEASUREMENTS.md) · [Pemecahan masalah](docs/TROUBLESHOOTING.md) · [Membangun mesin](docs/BUILD.md) · [Patch](patches/README.md) · [Prompts](docs/PROMPTS.md) · [Pihak ketiga](THIRD_PARTY.md) · [Changelog](CHANGELOG.md)

Halaman ini dilokalkan ke bahasa Indonesia dengan bantuan AI; koreksi sangat kami harapkan, lihat [`CONTRIBUTING.md`](CONTRIBUTING.md).
