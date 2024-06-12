import pandas as pd

from numpy.random import randn

df = pd.DataFrame(randn(3,3), index=["A", "B", "C"], columns=["Column1", "Column2", "Column3"])

result = df
result = df["Column1"] # 1. Kolonu alırız
result = type(df["Column1"]) # kolon bir seri
result = df[["Column1", "Column2"]] # iki veya daha fazla kolon seçmek için liste halinde gönderim yapılmalı

# Satıra göre seçme işlemleri için
# loc["row", "column"] => loc["row"] => loc[:, "column"]
result = df.loc["A"] # A indeksini seri olarak verir
result = type(df.loc["A"])
result = df.loc[:,"Column1"]
result = df.loc[:,["Column1", "Column2"]] # result = df[["Column1", "Column2"]] ile aynı çalışır

result = df.loc[:, "Column1":"Column3"] # iki kolon arasındakileri alır (Başlangıç ve Bitiş DAHIL!)
result = df.loc[:,:"Column2"] # Başlangıçtan başla ...'e kadar git
result = df.loc["A":"C", :"Column2"] # A. indeksten başla C ye kadar git
result = df.loc[:"B",:"Column2"]

result = df.iloc[2] # 2. indekse karşılık gelen değerleri seri olarak döndürür

result = df.loc["A","Column2"] # Belirli bir indeks ve kolona karşılık gelen değeri alır
result = df.loc[["A","B"], ["Column1", "Column2"]] # A B satırlarının Column1 ve Column2 Değerlerini getir

df["Column4"] = pd.Series(randn(3), ["A", "B", "C"]) # Yeni kolon ekleme
df["Column5"] = df["Column1"] + df["Column3"] # Kolon 1 ile 3'ün toplamı 5 olarak yazdırılır

print(df.drop("Column5", axis=1)) # Axis değerini unutma. (x ve y koordinatını belirtir x = 0 "Soldan Sağa", y = 1"Yukardan aşağı")
# Orijinal dataframe içerisinde değişiklik yapılmadı. Yapılması istenirse "inplace=True"

result = df.drop("Column5", axis=1, inplace= True) # Droptan dönecek değer orijinal df üzerinde güncelleme yapar.

print(df)
print(result)

