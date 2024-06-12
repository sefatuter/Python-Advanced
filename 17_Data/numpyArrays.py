import numpy as np

# result = np.array([1,3,5,7,9])
result = np.arange(1,10) # 1 ile 10 arası (10 dahil değil) dizi oluşturur
result = np.arange(10,100,3) # 10 ile 100 arası 3 atlayarak
result = np.zeros(10) # 10 tane 0 olan dizi
result = np.ones(10) # 10 tane 1 olan dizi 
result = np.linspace(0,100, 5) # 0 ile 100 arası - 5 eşit parçaya böl
result = np.linspace(0,5,5) # float değerler ile böler
result = np.random.randint(0,10) # 0 ile 10 arasında (10 dahil değil) rastgele sayı üretir
result = np.random.randint(20)
result = np.random.randint(1,10,3) # rastgele dizi döndürmek için 3. parametre dizide kaç sayı olacağını belirler
result = np.random.rand(5) # float değerde 5 sayı
result = np.random.randn(5) # - değerler de katılır
# np_array = np.arange(50)
# np_multi = np_array.reshape(5,10)# 5x10 matris oluşturduk

# print(np_multi.sum(axis=1)) # satırların toplamını getirir
# print(np_multi.sum(axis=0)) # sütunların toplamını getirir

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
result = rnd_numbers.max() # en büyük sayıyı yazdır
result = rnd_numbers.min()
result = rnd_numbers.mean() # ortalama alır
result = rnd_numbers.argmax() # üretilen en büyük sayının kaçıncı indekste olduğu
result = rnd_numbers.argmin() # üretilen en küçük sayının kaçıncı indekste olduğu



print(result)

