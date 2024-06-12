names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

#1 "Cenk" ismini listenin sonuna ekleyiniz

names.append('Cenk')

#2 "Sena" ismini listenin başına ekleyiniz

names.insert(0, 'Sena')

#3 "Deniz" ismini listeden siliniz 

names.remove('Deniz')

#4 "Deniz" isminin indeksi nedir?

names.index('Hakan')

#5 "Ali" listenin bir elemanı mıdır?

result = 'Ali' in names
print(result)

#6 Liste elemanların1ı ters çevirin

names.reverse()

#7 Liste elemanlarını alfabetik olarak sıralayın

names.sort()

#8 years listesini rakamsal büyüklüğe göre sıralayınız.

years.sort()

#9 str = "Chevrolet, Dacia" karakter dizisini listeye çeviriniz.

str = "Chevrolet, Dacia"
list = str.split(', ')
print(list)

#10 years dizisinin en büyük ve en küçük elemanı nedir?

min = min(years)
max = max(years)
print(min, max)

#11 years dizisinde kaç tane 1998 elemanı vardır?

result = years.count(1998)
print(result)

#12 years dizisinin tüm elemanlarını siliniz

years.clear()

#13 kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız

brands = []

brand = input("Enter brand1: ")
brands.append(brand)

brand = input("Enter brand2: ")
brands.append(brand)

brand = input("Enter brand3: ")
brands.append(brand)

print(brands)

print(names)
print(years)