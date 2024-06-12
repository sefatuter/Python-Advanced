import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5]
result = numbers[-1]
result = numbers[0:3] # 0 ile 3 (dahil değil) arasındaki değerleri yazdır
result = numbers[3:] # 3 ile sonuncuya kadar değerleri yazdır
result = numbers[::] # bütün liste
result = numbers[::-1] # listeyi ters çevir
result = numbers[::-2] # listeyi ters çevir ikişer ikişer atla

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]]) # 3x3
#print(numbers2)

result = numbers2[0]
result = numbers2[2] # 1. Dimensiondaki 3. eleman

result = numbers2[0,2] # 0. indeksteki arrayin, 2. indeksteki elemanı (10)
result = numbers2[2,1]

result = numbers2[:,:] # 1. : satırları temsil eder, 2. : sütunları temsil eder, bütün satır ve sütunları al
result = numbers2[:,2] # 3. sütun
result = numbers2[:,0] # 1. sütun
result = numbers2[:,0:2] # 0 ile 2. indeks arasındaki sütunları getir
result = numbers2[:2,:2]

# print(result)


arr1 = np.arange(0,10)
# arr2 = arr1 # referans kopyalaması
arr2 = arr1.copy() # yaptığımızda arr2 farklı adreste tanımlanan bir dizi olur

print(arr1)
print(arr2)
print("------------------------")

# arr2[0] = 20 # Değişikliği arr2 de yapsak da arr1 de değişir çünkü aynı adrese eşitledik
arr2[0] = 20

print(arr1)
print(arr2)







