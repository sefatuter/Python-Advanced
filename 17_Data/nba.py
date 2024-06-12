import pandas as pd

#1- İlk 10 kaydı getiriniz.

df = pd.read_csv('C:/Users/SefaPc/Desktop/btkPythonL/17_Data/datasets/nba.csv')
df = pd.DataFrame(df)

# print(df.head(10))

#2- Toplam kaç kayıt vardır?

# print(len(df))

#3- Tüm oyuncuların toplam kilo ortalaması nedir?

result = df['weight'].mean()

#4- En yüksek kilo ne kadardır?

result = df['weight'].max()

#5- En yüksek kilolu oyuncu kimdir?

result = df.loc[df['weight'].argmax(), 'name']

#6- Kilosu 150-200 arasında olan oyuncuların isimleri ve oynadıkları takım?

result = df[(df["weight"] >= 150) & (df["weight"] <= 200)][['name', 'college']]


#7- "John Holland" isimli oyuncunun college hangisidir?

result = df[df.name.str.contains('John Holland')]['college']

#8- Takımlara göre oyuncuların ortalama başlama yılları bilgisi nedir?

result = df['year_start'].mean()

#9- Kaç farklı college mevcut?

result = len(df['college'].unique())

#10- İsmi içinde "and" geçen kayıtları bulunuz.

result = df[df.name.str.contains('and')]

print(result)
