import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data=data, columns=["Column1", "Column2", "Column3", "Column4", "Column5"])
result = df

result = df.columns # Dataframe içerisindeki kolon bilgilerini getirir.
result = df.head(10) # ilk 10 kaydı getirir.
result = df.tail(10) # son 10 kaydı getirir.
result = df["Column1"].head() # Sadece 1. kolonun ilk 5 kaydı gösterir.
result = df.Column1.head() # üstteki ile aynı şey
result = df[["Column1", "Column2"]].head() # iki kolonu alır ilk 5 kaydı alır.
result = df[5:15][["Column1", "Column2"]].head() # kayıtları öteleyip ilk 5 kaydı alır.
result = df[5:15][["Column1", "Column2"]].tail()

# Filtreleme için,
result = df > 50  # True False şeklinde karşımıza getirir.
result = df[df > 50] # Oluşturduğumuz filtreyi dataframe'e veririz. Bu sayede değerleri gösterir.
result = df[df % 2 == 0]
result = df["Column1"] > 50 # Sadece kolon 1 deki değerlere bakar
result = df[df["Column1"] > 50] # Sadece kolon 1 deki 50'den büyük olan kayıtları verir.
result = df[df["Column1"] > 50][["Column1", "Column2"]] # Burada ise ilk 2 kolonu getirsin diye filtreledik.
result = df[(df["Column1"] > 50) & (df["Column2"] <= 70)]
result = df[(df["Column1"] > 50) | (df["Column2"] > 50)][["Column1", "Column2"]] 
result = df.query("Column1 >= 50 & Column1 % 2 ==0")[["Column1", "Column2"]]  # Query fonksiyonuna koşullar verilebilir. Aynı zamanda kolon seçimi de yapılabilir.
result = df.query("Column1 >= 50 & Column1 | 2 ==0")[["Column1", "Column2"]]

print(result)
