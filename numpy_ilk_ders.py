
import numpy as np

sayilar = np.array(range(1, 101))

ciftler = sayilar[sayilar % 2 == 0]
tekler = sayilar[sayilar % 2 != 0]

cift_toplam = np.sum(ciftler)
tek_toplam = np.sum(tekler)

print("çift sayılar:", ciftler)
print("çiftlerin toplamı:", cift_toplam)

print("tek sayılar:", tekler)
print("teklerin toplamı:", tek_toplam)