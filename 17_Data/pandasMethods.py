import pandas as pd
import numpy as np

data = {
    'Column1': [1,2,3,4,5],
    'Column2': [10,20,10,45,25],
    'Column3': ['abc','bcaa','ade','ca','dea']
}

df = pd.DataFrame(data)

def power(x):
    return x * x

power2 = lambda x: x * x


result = df
result = df['Column2'].unique() # Tekrarlamayan değerleri getirir sadece.
result = df['Column2'].nunique() # kaç tane tekil bilgi istediğimiz kolon içerisinde mevcut.
result = df['Column2'].value_counts() # her bir elemanın kaç tane tekrarladığını belirtir.
result = df['Column1'] * 2
result = df['Column1'].apply(power) # apply ile fonksiyon kullanabiliriz teker teker kolon 1 deki değerleri göndeririz.
result = df['Column1'].apply(power2)
result = df['Column1'].apply(lambda x: x * x)
df['Column4'] = df['Column3'].apply(len) # her bir karakterin sayısını yazdırır
result = df.columns
result = len(df.columns)
result = len(df.index)
result = df.info

result = df.sort_values('Column2') # kolon 2'ye göre sıralayıp yazar
result = df.sort_values('Column3')
result = df.sort_values('Column3', ascending=False)

data = {
    'Ay': ['Mayıs', 'Haziran', 'Nisan', 'Mayıs', 'Haziran', 'Nisan', 'Mayıs', 'Haziran','Nisan'],
    'Kategori': ['Elektronik', 'Elektronik', 'Elektronik', 'Kitap', 'Kitap', 'Kitap', 'Giyim', 'Giyim', 'Giyim'],
    'Gelir': [20,30,15,14,32,42,12,36,52] 
}

df = pd.DataFrame(data)

df = df.pivot_table(index='Ay', columns='Kategori', values='Gelir')

print(df)