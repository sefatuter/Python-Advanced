sayilar = [1,3,5,7,9,12,19,21]

#1- sayilar listesini while ile ekrana yazdırın.

# i = 0
# while(i < len(sayilar)):
#     print(sayilar[i])
#     i += 1


#2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
#   tek sayıları ekrana yazdırın

# n1 = int(input('Baslangıc degeri giriniz: '))
# n2 = int(input('Bitis degeri giriniz: '))
# 
# 
# while(n1 <= n2):
#     if(n1 % 2 != 0):
#         print(n1)
#     n1 += 1

#3- 1-100 arasındaki sayıları azalan şekilde yazdırın.

# i = 100
# 
# while(i >= 0):
#     print(i)
#     i -= 1

#4- Kullanıcıdan alacağınız 5 sayıyı ekrana sıralı bir şekilde yazdırın.

c = 0
nums = []
while(c < 5):
    num = int(input('sayi girinizz: '))
    nums.append(num)
    c += 1

nums.sort()
print(nums)
    

#5- Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız
#   ** ürün sayısını kullanıcıya sorun.
#   ** dictionary listesi yapısı (name, price) şeklinde olsun.
#   ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

quantity = int(input('Urun sayisini giriniz: '))
count = 0
urunler = []

while (count < quantity):
    name = input('Urun ismini giriniz: ')
    price = input('Urun fiyatini giriniz: ') 
    urunler.append({
        'name': name,
        'price': price
    })
    count += 1

for urun in urunler:
    print(f'Urun adı: {urun["name"]} - Urun Fiyati: {urun["price"]}')
