#1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz

num = float(input('Bir sayı giriniz: '))

if num >= 0 and num <= 100:
    print('Sayı 0-100 arasındadır.')
else:
    print('Sayı 0-100 arasında değildir.')

#2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

x = int(input("Bir sayı giriniz: "))

if (x > 0) and (x % 2 == 0):
    print('Sayı pozitif çift sayıdır.')
else:
    print('Sayı pozitif çift sayı değildir.')

#3- Email ve parola bilgileri ile giriş kontrolü yapınız.

email = input("Email giriniz: ")
passw = input("Şifre giriniz: ")

if (email == 'email@sadikturan.com') and (passw == '123abc'):
    print('Giriş başarılı.')
else:
    print('Giriş başarısız.')

#4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

n1 = float(input("Birinci sayı: "))
n2 = float(input("İkinci sayı: "))
n3 = float(input("Üçüncü sayı: "))

if n1 > n2 and n1 > n3:
        print(f'{n1} sayısı en büyüktür')
elif n2 > n1 and n2 > n3:
        print(f'{n2} sayısı en büyüktür')
else:
        print(f'{n3} sayısı en büyüktür')

#5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalamayı hesaplayınız
#   Eger ortalama 50 ve üstündeyse geçti değilse kaldı yazdır.
#   a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#   b-) Finalden 70 alındığında ortalamanın önemi olmasın.


vize1 = float(input("Enter first midterm grade: "))
vize2 = float(input("Enter second midterm grade: "))

final = float(input("Enter final grade: "))

ort = (((vize1+vize2)/2)*0.6) + (final * 0.4)

if (ort>=50 and final >= 50):
    print(f'Not ortalamanız: {ort} Dersten başarılı bir şekilde geçtiniz.')
elif (final >= 70):
    print(f'Not ortalamanız: {ort} Dersten başarılı bir şekilde geçtiniz.')
else:
    print(f'Not ortalamanız: {ort} Dersten kaldınız.')
     

#6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız
#   Formül: (Kilo / boy uzunluğunun karesi)
#   Aşağıdaki tabloya göre kişi hangi gruba girmektedir?
#   0-18.4      => Zayıf
#   18.5-24.9   => Normal
#   25.0-29.9   => Fazla Kilolu
#   30.0-34.9   => Şişman (Obez)



name = input("Ad giriniz: ")
kg = float(input("Kilo giriniz: "))
hg = float(input("Boy giriniz(m): "))

indeks = (kg/(hg**2))

if (indeks >= 0) and (indeks <= 18.4):
    print(f'Zayıf {indeks}')
elif (indeks >= 18.5) and (indeks <= 24.9):
    print(f'Normal {indeks}')
elif (indeks >= 25.0) and (indeks <= 29.9):
    print(f'Fazla Kilolu {indeks}')
elif (indeks >= 30.0) and (indeks <= 34.9):
    print(f'Şişman (Obez) {indeks}')
else:
    print('Bilgileriniz hatalı.')

