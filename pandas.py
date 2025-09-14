import pandas as pd
#Pandas Bölümü Bir CSV dosyası oluşturun ya da aşağıdaki gibi örnek bir DataFrame hazırlayın:
# Öğrenci Yaş Bölüm Matematik Fizik Kimya Ali 20 Bilgisayar 70 65 80 Ayşe 21 Fizik 60 75 85
# Mehmet 19 Kimya 80 70 65 Zeynep 22 Bilgisayar 90 85 95 Ahmet 20 Fizik 55 60 70 • Görevler:
# 3. 1. Veri setini Pandas DataFrame olarak oluşturun.
# 4. 2. Her ders için ortalama puanı bulun. 5.
# 3. En yüksek matematik notunu alan öğrenciyi bulun.
# 6. 4. Her öğrencinin not ortalamasını hesaplayan yeni bir sütun ekleyin.
# 7. 5. Bölümlere göre gruplayarak her bölümün ortalama başarılarını hesaplayın.
# 8. 6. Ortalaması 70’in üzerinde olan öğrencileri filtreleyin."

veri = {
    "Ogrenci": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Ahmet"],
    "Yas": [20, 21, 19, 22, 20],
    "Bolum": ["Bilgisayar", "Fizik", "Kimya", "Bilgisayar", "Fizik"],
    "Matematik": [70, 60, 80, 90, 55],
    "Fizik": [65, 75, 70, 85, 60],
    "Kimya": [80, 85, 65, 95, 70]
}

df = pd.DataFrame(veri)
print(df)


ders_ort = df[["Matematik", "Fizik", "Kimya"]].mean()
print("Derslerin ortalamaları:", ders_ort)


en_yuksek_mat = df.loc[df["Matematik"].idxmax()]
print("En yüksek matematik alan öğrenci:", en_yuksek_mat)


df["Ortalama"] = df[["Matematik", "Fizik", "Kimya"]].mean(axis=1)
print("Ortalama sütunu eklendi:", df)


bolum_ort = df.groupby("Bolum")[["Matematik", "Fizik", "Kimya", "Ortalama"]].mean()
print("Bölümlere göre ortalamalar:", bolum_ort)


yetmis_ustu = df[df["Ortalama"] > 70]
print("Ortalaması 70 üstü olan öğrenciler:", yetmis_ustu)