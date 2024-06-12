#1- Girilen iki sayıdan hangisi büyüktür?

n1 = int(input("Enter first num: "))
n2 = int(input("Enter second num: "))

result = n1 > n2
if result == True:
    print(n1, ">", n2)
else:
    print(n2, ">", n1)

result = (n1 > n2)
print(f'n1: {n1} n2: {n2} den büyüktür : {result}')


#2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalamayı hesaplayınız
#   Eger ortalama 50 ve üstündeyse geçti değilse kaldı yazdır.

vize1 = float(input("Enter first midterm grade: "))
vize2 = float(input("Enter second midterm grade: "))

final = float(input("Enter final grade: "))

ort = (((vize1+vize2)/2)*0.6) + (final * 0.4)

if ort >= 50:
    print(ort, "passed!")
else:
    print(ort, "failed!")


print(f'not ortalamanız: {ort} ve dersten geçme durumunuz: {ort>=50}')


#3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

num = int(input("Enter number: "))

if num % 2 == 0:
    print(num, "is even number")
else:
    print(num, "odd number")

print(f'Girdiginiz sayi {num} çifttir: {result == (num % 2 == 0)}')


#4- Girilen bir sayının negatif, pozitif durumunu yazdırın.

num = int(input("Enter number: "))

if num > 0:
    print(num, "positive!")
else:
    print(num, "negative!")

print(f'Girdiginiz sayi {num} pozitif olma durumu: {num > 0}')


#5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#   (email: email@sadikturan.com parola: abc123)

email = input("Enter email: ")
passw = input("Enter pass: ")

result1 = (email == 'email@sadikturan.com')
result2 = (passw == 'abc123')

print(f'Girdiginiz mail dogrulugu: {result1}, password: {result2}')

