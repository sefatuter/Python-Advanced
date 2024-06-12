numbers = [1,2,3,4,5]

for num in numbers: # liste için for ... in ... kullanılır
    print('hello')

# listenin eleman sayısı kadar for döngüsünü döndürür

names = ['cinar', 'sadik', 'sena']

for name in names: # listenin içindeki her bir elemanı name içine kopyala
    print(f'my name is {name}.')

name = 'sadik turan'

for n in name:
    print(n) # bu durumda string ifadenin her bir elemanı tek tek yazdırılır
             # string de aslında bir listedir.

tuple = 1, 2, 3, 4, 5
tuple = [(1,2), (1,3), (3,5), (5,7)] # her bir liste elemanı ayrı alınır


for t,k in tuple:
    print(t, k)


d = {'k1': 1,
     'k2': 2,
     'k3': 3
     }
# key: value

for item in d: # key value için for .. in .. şeklinde kullanılır
    print(item)

for key, value in d.items():
    print(key, value)

# eleman gruplarına ulaşmak istersek .items()
