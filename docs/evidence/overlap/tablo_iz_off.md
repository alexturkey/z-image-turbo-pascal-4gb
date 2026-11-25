# HARITA tablosu: E:/sinirsiz_foto/gecici/ortusme_iz/iz_off.csv
adim penceresi = TIMESTEP_EMBEDDING'ten bir sonrakine (adim sayisi 8); penceredeki TUM K sayilir; K=6933 H=3936 G=2125

| adim | adim ms (cihaz) | matmul ms | dikkat ms | diger op ms | BOSLUK ms | bosluk: kopya ile ust uste ms | bosluk: kopyasiz idle ms | >50 ms bosluk adet (en buyuk ms) | kopya H ms (adet, MB) | host launch ms (G toplam) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 28005.4 | 11689.2 | 7708.0 | 585.3 | 8022.9 | 7333.6 | 689.3 | 30 (368) | 7333.8 (433, 5643 MB) | 26.3 |
| 2 | 22102.2 | 11709.2 | 7696.6 | 574.4 | 2122.0 | 1468.0 | 654.0 | 28 (61) | 1468.0 (407, 5276 MB) | 13.6 |
| 3 | 21937.6 | 11721.4 | 7678.9 | 576.0 | 1961.2 | 1289.2 | 672.0 | 18 (56) | 1289.4 (407, 5276 MB) | 12.4 |
| 4 | 21901.2 | 11725.0 | 7670.5 | 575.6 | 1930.1 | 1276.4 | 653.8 | 15 (56) | 1276.5 (407, 5276 MB) | 12.8 |
| 5 | 21872.2 | 11681.5 | 7690.5 | 574.5 | 1925.6 | 1265.0 | 660.6 | 13 (55) | 1265.2 (407, 5276 MB) | 12.6 |
| 6 | 22055.7 | 11833.0 | 7707.6 | 577.8 | 1937.3 | 1260.7 | 676.6 | 15 (54) | 1260.7 (407, 5276 MB) | 13.1 |
| 7 | 22072.3 | 11836.4 | 7710.3 | 578.3 | 1947.3 | 1275.1 | 672.2 | 11 (59) | 1275.2 (407, 5276 MB) | 12.5 |
| 8 | 32803.0 | 12101.5 | 7711.9 | 10659.4 | 2330.3 | 1315.6 | 1014.7 | 19 (404) | 1315.8 (541, 5365 MB) | 10527.9 |

Adim [2, 3] ortalamasi: 22.02 sn = matmul 11.72 + dikkat 7.69 + diger op 0.58 + bosluk 2.04 (bosluktan 1.38 sn kopya ile ust uste, 0.66 sn kopyasiz idle); toplam 22.02 sn (adimla fark 0.0%)
