import numpy as np
#1.	1. Numpy ile Matris İşlemleri
#- 5x5 boyutunda rastgele (0-100 arasında) tam sayılardan oluşan bir matris oluşturun.
#- Bu matrisin:
 # • Ortalama, standart sapma ve varyansını hesaplayın.
  #• En büyük ve en küçük değerlerini bulun.
 # • Köşegenindeki elemanların toplamını bulun.



matrisim = np.random.randint(0, 101, (5, 5))
print("matrisim:", matrisim)


ort = np.mean(matrisim)
std = np.std(matrisim)
var = np.var(matrisim)

print("ortalama:", ort)
print("standart sapma:", std)
print("varyans:", var)


enbuyuk = np.max(matrisim)
enkucuk = np.min(matrisim)
print("en büyük:", enbuyuk)
print("en küçük:", enkucuk)


kosegen_top = np.trace(matrisim)
print("köşegen toplamı:", kosegen_top)




puanlar = np.random.normal(50, 15, 1000)
puanlar = np.clip(puanlar, 0, 100)

print("öğrenci notları örnek:", puanlar[:10])

ort2 = np.mean(puanlar)
medyan = np.median(puanlar)
std2 = np.std(puanlar)

print("Ortalama:", ort2)
print("Medyan:", medyan)
print("Std:", std2)

elli_alti = np.sum(puanlar < 50)
print("50’den düşük alan öğrenci sayısı:", elli_alti)
