# HARITA tablosu: E:/sinirsiz_foto/gecici/ortusme_iz/iz_on.csv
adim penceresi = TIMESTEP_EMBEDDING'ten bir sonrakine (adim sayisi 8); penceredeki TUM K sayilir; K=6933 H=3936 G=2125

| adim | adim ms (cihaz) | matmul ms | dikkat ms | diger op ms | BOSLUK ms | bosluk: kopya ile ust uste ms | bosluk: kopyasiz idle ms | >50 ms bosluk adet (en buyuk ms) | kopya H ms (adet, MB) | host launch ms (G toplam) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 20924.8 | 11782.5 | 7678.3 | 629.5 | 834.5 | 145.3 | 689.2 | 0 (0) | 949.1 (433, 5643 MB) | 63.2 |
| 2 | 20876.8 | 11841.3 | 7762.7 | 577.7 | 695.2 | 25.4 | 669.8 | 0 (0) | 891.9 (407, 5276 MB) | 15.3 |
| 3 | 20891.5 | 11847.7 | 7754.3 | 577.9 | 711.6 | 26.2 | 685.3 | 0 (0) | 891.6 (407, 5276 MB) | 14.5 |
| 4 | 20894.6 | 11853.5 | 7775.6 | 577.8 | 687.6 | 25.5 | 662.1 | 0 (0) | 894.5 (407, 5276 MB) | 15.0 |
| 5 | 20910.0 | 11847.5 | 7780.9 | 577.4 | 704.1 | 25.2 | 678.9 | 0 (0) | 891.8 (407, 5276 MB) | 14.1 |
| 6 | 20942.0 | 11859.0 | 7789.5 | 578.5 | 715.1 | 26.1 | 689.0 | 0 (0) | 893.0 (407, 5276 MB) | 14.0 |
| 7 | 20952.5 | 11863.0 | 7778.3 | 578.4 | 732.9 | 25.5 | 707.4 | 0 (0) | 891.0 (407, 5276 MB) | 14.9 |
| 8 | 28842.8 | 12133.6 | 7773.3 | 8056.2 | 879.7 | 42.7 | 836.9 | 1 (227) | 912.4 (541, 5365 MB) | 7763.3 |

Adim [2, 3] ortalamasi: 20.88 sn = matmul 11.84 + dikkat 7.76 + diger op 0.58 + bosluk 0.70 (bosluktan 0.03 sn kopya ile ust uste, 0.68 sn kopyasiz idle); toplam 20.88 sn (adimla fark 0.0%)
