#1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz

x = float(input("Bir sayı giriniz: "))

result = (0 < x) and (x < 100)
print(f'Girilen sayı 0-100 arasında olma durumu: {result}')

#2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

x = int(input("Bir sayı giriniz: "))

result = (x > 0) and (x % 2 == 0)
print(f'Girilen sayı pozitif ve çift olma durumu: {result}')

#3- Email ve parola bilgileri ile giriş kontrolü yapınız.

email = input("Email giriniz: ")
passw = input("Şifre giriniz: ")

result = (email == 'email@sadikturan.com') and (passw == '123abc')
print(f'Giriş kontrolü durumu: {result}')

#4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

n1 = float(input("Birinci sayı: "))
n2 = float(input("İkinci sayı: "))
n3 = float(input("Üçüncü sayı: "))

result = (n1 > n2) and (n1 > n3)
print(f'n1 en büyük sayıdır:    {result}')

result = (n2 > n1) and (n2 > n3)
print(f'n2 en büyük sayıdır:    {result}')

result = (n3 > n2) and (n3 > n1)
print(f'n3 en büyük sayıdır:    {result}')

#5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalamayı hesaplayınız
#   Eger ortalama 50 ve üstündeyse geçti değilse kaldı yazdır.
#   a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#   b-) Finalden 70 alındığında ortalamanın önemi olmasın.


vize1 = float(input("Enter first midterm grade: "))
vize2 = float(input("Enter second midterm grade: "))

final = float(input("Enter final grade: "))

ort = (((vize1+vize2)/2)*0.6) + (final * 0.4)

print(f'not ortalamanız: {ort} ve dersten geçme durumunuz: {(ort>=50 and final >= 50) or (final >= 70)}')


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

print(f'Zayıf           :{(indeks >= 0) and (indeks <= 18.4)}')
print(f'Normal          :{(indeks >= 18.5) and (indeks <= 24.9)}')
print(f'Fazla Kilolu    :{(indeks >= 25.0) and (indeks <= 29.9)}')
print(f'Şişman (Obez)   :{(indeks >= 30.0) and (indeks <= 34.9)}')