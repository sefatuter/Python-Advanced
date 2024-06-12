'''
Soru: Girilen bir sayının asal olup olmadığını bulun.
** Asal sayı 1 ve kendisi hariç tam böleni olmayan
   sayılara denir.

'''

'''
girilen sayinin yarisi alınsın 10/2
5
yarisindan itibaren geriye doğru bu sayilara bölelim hiçbiri bölünmez ise
bu asal sayidir ( 1 hariç)

'''

num = int(input('Asal sayi kontrolu icin sayi giriniz: '))

isPrime = True

if(num == 1):
    isPrime = False

for i in range (2, num):
    if (num % i == 0):
        isPrime = False
        break

if isPrime:
    print('Girilen sayi asaldir.')
else:
    print('Girilen sayi asal degildir')

