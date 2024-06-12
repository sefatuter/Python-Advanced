sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

#1- Sayilar listesindeki hangi sayilar 3'ün katıdır?

for i in sayilar:
    if(i % 3 == 0):
        print(i, '3\'un katidir.')
    else:
        print('kati degildir.')


#2- Sayilar listesinde sayıların toplamı kaçtır?
sum = 0
for i in sayilar:
    sum= sum + i
print(sum)

#3- Sayilar listesindeki tek sayıların karesini alınız

for i in sayilar:
    if(i % 2 != 0):
        print(i ** 2)

sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']

#4- Sehirlerden hangileri en fazla 5 karakterlidir?

sum = 0

for sehir in sehirler:
    if(len(sehir) <= 5):
        print(sehir)


urunler = [
    {'name': 'samsung s6', 'price': '3000'},
    {'name': 'samsung s7', 'price': '4000'},
    {'name': 'samsung s8', 'price': '5000'},
    {'name': 'samsung s9', 'price': '6000'},
    {'name': 'samsung s10', 'price': '7000'}
    ]

#5- Ürünlerin fiyatları toplamı nedir?
count = 0
sum = 0
for i in urunler:
    print(i['price'])
    count += 1
    sum = sum + int(i['price'])

print('Sum = ', sum)


#6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz.

for i in urunler:
    if(int(i['price']) <= 5000):
        print(i['name'], i['price'])

 