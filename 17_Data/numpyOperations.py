import numpy as np

numbers1 = np.random.randint(10,100,6) # 6 sayı üret
numbers2 = np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

result = numbers1 + numbers2 # iki dizinin aynı indeksteki elemanlarını toplar
result = numbers1 + 10 # ilk dizinin her elemanına 10 ekler
result = numbers1 - 10
result = numbers1 - numbers2
result = numbers1 * numbers2
result = numbers1 / numbers2

result = np.sin(numbers1) # listenin sinüsü alınır
result = np.cos(numbers1)
result = np.sqrt(numbers1)
result = np.log(numbers1)

mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)

print(mnumbers1)
print(mnumbers2)

result = np.vstack((mnumbers1,mnumbers2)) # matrisleri dikey olarak birleştirir
result = np.hstack((mnumbers1,mnumbers2)) # matrisleri yatay olarak birleştirir

result = numbers1 >= 50 # bool döndürür listedeki sayıların her birine bakıp
result = numbers1 % 2 == 0 # iki ile bölümünden kalanın 0 olup olmadığına bakar listedeki her elemanın

print(numbers1[result]) # numbers1 de true aldığımız değerleri yazdırır yani listedeki çift sayıları

print(result)