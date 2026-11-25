# HARITA tablosu: E:/sinirsiz_foto/gecici/ortusme2_iz/iz_on.csv
adim penceresi = TIMESTEP_EMBEDDING'ten bir sonrakine (adim sayisi 8); penceredeki TUM K sayilir; K=6317 H=3920 G=1933

| adim | adim ms (cihaz) | matmul ms | dikkat ms | diger op ms | BOSLUK ms | bosluk: kopya ile ust uste ms | bosluk: kopyasiz idle ms | >50 ms bosluk adet (en buyuk ms) | kopya H ms (adet, MB) | host launch ms (G toplam) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 20266.4 | 10983.5 | 7234.7 | 541.0 | 1507.2 | 317.0 | 1190.2 | 3 (273) | 1093.9 (476, 6349 MB) | 36.2 |
| 2 | 19271.4 | 10967.3 | 7207.4 | 531.7 | 564.9 | 25.3 | 539.6 | 0 (0) | 895.9 (405, 5272 MB) | 14.0 |
| 3 | 19399.4 | 11035.9 | 7249.7 | 533.1 | 580.7 | 26.4 | 554.3 | 0 (0) | 896.5 (405, 5272 MB) | 13.7 |
| 4 | 19554.8 | 11133.7 | 7308.9 | 535.5 | 576.7 | 25.7 | 551.1 | 0 (0) | 898.7 (405, 5272 MB) | 13.6 |
| 5 | 19571.3 | 11138.1 | 7322.1 | 535.8 | 575.4 | 24.7 | 550.7 | 0 (0) | 899.0 (405, 5272 MB) | 14.3 |
| 6 | 19602.9 | 11142.2 | 7343.3 | 535.8 | 581.6 | 27.2 | 554.3 | 0 (0) | 912.9 (405, 5272 MB) | 14.7 |
| 7 | 19598.7 | 11129.2 | 7348.7 | 535.2 | 585.7 | 26.8 | 558.9 | 0 (0) | 908.4 (405, 5272 MB) | 13.4 |
| 8 | 52549.4 | 11469.4 | 7365.5 | 28353.0 | 5361.6 | 91.4 | 5270.2 | 3 (3792) | 965.1 (541, 5365 MB) | 31143.4 |

Adim [2, 3] ortalamasi: 19.34 sn = matmul 11.00 + dikkat 7.23 + diger op 0.53 + bosluk 0.57 (bosluktan 0.03 sn kopya ile ust uste, 0.55 sn kopyasiz idle); toplam 19.34 sn (adimla fark 0.0%)
