# Related work: Z-Image on small GPUs

This page lists what we looked at when we asked "has someone published a measured Z-Image setup on a 4 GB card?". It is here so that you can check our statement in the README and so that other people's work is named with respect.
Search date: **2026-11-14**. We looked, we did not scan everything; a search never proves that something does not exist.

How the pages were read: web pages were opened with a summarizing tool (it returns a summary and quotes, not the full page), so a quote below is as the tool gave it. Items marked **search summary, page not opened** were only seen as a search-engine summary because the page could not be opened (an HTTP error); treat them as unverified.

## What we looked for

Four things together: (1) a card with 4 GB of GPU memory or less, (2) quantization Q8_0 or higher, (3) a picture size of 768x1344 or larger, (4) a measured time and measured GPU memory, published so that others can repeat it. Our setup has all four (see [`MEASUREMENTS.md`](MEASUREMENTS.md)).
Where we looked we did not find a published setup that combines all four. We do not claim that nobody did it.

## Where we looked

| Where | How | Result |
|---|---|---|
| Z-Image-Turbo model card and Diffusers page (Hugging Face) | opened | only "fits comfortably within 16G VRAM consumer devices"; no minimum, no 4 GB figure |
| Z-Image GitHub README, "community works" part | opened | lists stable-diffusion.cpp and quotes "as little as 4GB of VRAM" (a claim of that project, not of the Z-Image team) |
| Z-Image paper abstract (arXiv 2511.22699) | opened | "consumer-grade hardware"; no measurement table in the abstract |
| stable-diffusion.cpp wiki page for Z-Image on 4 GB | opened | recommends Q4_0 or Q3_K, Qwen3-4B Q4_K_M, picture size 1024x512; no time, no card name, no memory figure |
| stable-diffusion.cpp discussions, pull requests and issues (#1026, #1308, #1020, #1477, #1030) | opened | see the table below |
| Hugging Face discussions of the model card, first page | opened | two threads about running under 4 GB or less (#164 and one hidden thread whose body we could not read), no measurements |
| leejet GGUF model card | opened | file sizes (Q2_K 2.59 GB to Q8_0 6.58 GB); no memory measurement |
| Web searches (English, Chinese, Japanese): "Z-Image Turbo GTX 1050 Ti 4GB", "Z-Image 4G显存 1050Ti 运行 GGUF", "Z-Image Turbo VRAM 4GB GTX1650 GGUF Q8", "Z-Image Turbo 4GB VRAM Q8_0 768x1344 sd.cpp offload seconds per image GTX" and similar | search engine | blogs and guides; no card-named, timed measurement at 4 GB with Q8 |
| Not looked at | - | Reddit itself, ComfyUI-GGUF issues, diffusers issues, Civitai, Zhihu, video sites (YouTube, Bilibili), X, Discord, GitHub code search, the later pages of the Hugging Face discussions |

## What we found

| Source | Card | Quantization | Size | Time | GPU memory | Read how |
|---|---|---|---|---|---|---|
| [stable-diffusion.cpp wiki: Z-Image on 4 GB](https://github.com/leejet/stable-diffusion.cpp/wiki/How-to-Use-Z%E2%80%90Image-on-a-GPU-with-Only-4GB-VRAM) | not named | Q4_0 / Q3_K | 1024x512 | not given | not given | opened |
| [stable-diffusion.cpp discussion #1026](https://github.com/leejet/stable-diffusion.cpp/discussions/1026), a comment | not named | Q8_0 (model and text encoder) with offload | 1008x1792 | not given | not given | opened |
| same discussion, a comment | RX 470 4 GB (Vulkan, Linux) | Q4_K | 512x512 and 1024x1024 | 7 s/it and 35 s/it | not given | opened |
| same discussion, a comment | RX 580 4 GB (Vulkan, Linux) | Q3_K | 512x512 | about 20 s/it (later 16 and about 7 s/it) | not given | opened |
| [stable-diffusion.cpp pull request #1020](https://github.com/leejet/stable-diffusion.cpp/pull/1020) | not named | q4_0 / q4_1 | not given | not given | "~4G peak VRAM" (Vulkan) | opened |
| [stable-diffusion.cpp pull request #1477](https://github.com/leejet/stable-diffusion.cpp/pull/1477) | RTX 3060 12 GB | bf16 and Q8 | 688x1024, 1024x1024 | 115 to 335 s (several settings, batch 4) | partly | opened (12 GB card, not 4 GB) |
| [Hugging Face discussion #164](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/discussions) "Run under 4gb Vram" | not named | "without any quantization" | not given | not given | not given | opened; a claim, no measurement |
| [Z-Image-Turbo benchmark repository (miroleon)](https://github.com/miroleon/z-image-turbo-benchmark) | RTX 4070 Ti, 3090 Ti, 3080 Laptop and others | Q3 to Q5 | 1024x1024 | for example 19.72 s total on a 3080 Laptop (Q4 + Q5 text encoder) | not given | opened (not a 4 GB card) |
| A Reddit post mirrored on a third-party site (title says 4 GB VRAM and 16 GB RAM) | GTX 1050 Ti 4 GB | fp8 all-in-one file in ComfyUI | 1024x576 | "a little over 2 minutes" | not given | **search summary, page not opened** (the mirror returned HTTP 403) |
| A Chinese blog post (CSDN) | GTX 1050 Ti | a low-VRAM variant, not stated | 768x768 | not given | "<4.2GB" | **search summary, page not opened** (HTTP 521) |
| Two Chinese posts (smzdm), titles mention 4 GB | not named | not stated | not stated | not given | not given | opened, but only the titles carry the claim; no data in the text we could read |
| [Z-Image-Turbo-Windows (airesearch-official)](https://github.com/airesearch-official/Z-Image-Turbo-Windows) | not named | not stated | not stated | not given | not given | opened; has a "4GB (safest)" preset, no measurement |
| A blog guide and a "6 GB" guide listing a 1050 Ti as "challenging" | none named | Q3_K_S | not given | not given | not given | opened; no measurement |

Reading the table: there are people running Z-Image on 4 GB cards, with Q3 and Q4 quantizations at smaller sizes, on Vulkan and on AMD cards, and one comment reports a 1008x1792 Q8_0 run without card, time or memory. Thank you to everyone who shared this; our work builds on the same stable-diffusion.cpp.

## How our setup differs

| | Others (where we looked) | This repository |
|---|---|---|
| Quantization | Q2_K to Q4 on 4 GB; Q8 mostly on 8 GB or more | Q8_0 diffusion model and Q8_0 text encoder |
| Size | 512x512 to 1024x576 with measurements | 768x1344 (also 1344x768 and 1024x1024) |
| Measurement | mostly none, or seconds per step | whole-picture time, stage times, sampled GPU memory peak, lowest free RAM, `run.json` per run |
| Repeatability | not stated | same seed, same pixels (`PIXEL_SHA256`), pinned downloads, `compare.py` |
| Engine | upstream | upstream plus the patches in [`patches/`](../patches/README.md), published |

The cost of Q8_0 on a 4 GB card is system memory and time: see "Why it fits in 4 GB" in the [README](../README.md).

If you know a published setup that we missed, please open an issue; we will add it here with a link.
