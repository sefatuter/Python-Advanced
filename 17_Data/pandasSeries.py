import pandas as pd
import numpy as np

# Data
numbers = [20,30,40,50]
letters = ['a', 'b', 'c', 5]
dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
random_numbers = np.random.randint(10,100,6) # 10-100 arası 6 sayı
scalar = 5

# pandas_series = pd.Series() # Tek boyutlu bir liste, seri.
pandas_series = pd.Series(numbers) # Her bir elemana index atanıyor.
pandas_series = pd.Series(letters) # Aynı şekilde indexlere atanıyor.
pandas_series = pd.Series(scalar, [0,1,2,3]) # verdiğimiz 5 index sayısı kadar artırılır.
# Her bir eleman aynı tipte olmak zorunda değil

pandas_series = pd.Series(numbers, ['a', 'b', 'c', 'd']) # her bir liste elemanı buradaki key bilgileriyle eşleştirilir.
pandas_series = pd.Series(dict) # index belirtmeye gerek yok dict zaten key verileri var.
pandas_series = pd.Series(random_numbers)

pandas_series = pd.Series([20,30,40,5], ['a', 'b', 'c', 'd'])
result = pandas_series[0]
result = pandas_series[-1]
result = pandas_series[:2]
result = pandas_series[-2:]
result = pandas_series['a']
result = pandas_series['d']
result = pandas_series[['a', 'b']] # Iki köşeli parantez içinde verilirse birden fazla indeksten değer alınabilir.
result = pandas_series.ndim
result = pandas_series.dtype
result = pandas_series.shape
result = pandas_series.sum()
result = pandas_series.max()
result = pandas_series.min()
result = pandas_series + pandas_series # liste içindeki elemanlar toplanır
result = pandas_series + 40
result = np.sqrt(pandas_series)

result = pandas_series >= 50 # Bool
result = pandas_series % 2 == 0 # Cift sayilar
print(pandas_series[pandas_series % 2 == 0])

print(pandas_series)
print(result)

# Ex
opel2018 = pd.Series([20,30,40,10], ["astra", "corsa", "mokka", "insignia"])
opel2019 = pd.Series([40,30,20,10], ["astra", "corsa", "Grandland", "insignia"])

total = opel2018 + opel2019
print(total)

print(total["astra"])

# DataFrame ise Serilerin birleşmiş halidir.
