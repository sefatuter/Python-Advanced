import numpy as np


#1- (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturunuz.

numbers = np.array([10,15,30,45,60])
print(numbers)

#2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz.

numbers = np.arange(5,15)
print(numbers) 

#3- (50-100) arasında 5'er 5'er artacak numpy dizisi oluşturunuz.

numbers = np.arange(50,100,5)
print(numbers) 


#4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.

numbers = np.zeros(10)
print(numbers) 

#5- 10 elemanlı birlerden oluşan bir dizi oluşturunuz.

numbers = np.ones(10)
print(numbers) 

#6- (0-100) arasında eşit aralıklı 5 sayı üretin.

numbers = np.linspace(0,100, 5)
print(numbers)

#7- (10-30) arasında rastgele 5 tane tamsayı üretin.

numbers = np.random.randint(10,30,5)
print(numbers)

#8- [-1 ile 1] arasında 10 adet sayı üretin.

numbers = np.random.randn(10)
print(numbers)


#9- (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz.

numbersMat = np.random.randint(10,50,15).reshape(3,5)
print(numbersMat)

#10- üretilen matrisin satır ve sütun sayılarının toplamlarını hesaplayınız.

print(numbersMat.sum(axis=1))
print(numbersMat.sum(axis=0))

#11- üretilen matrisin en büyük, en küçük ve ortalaması nedir?
print(numbersMat.max())
print(numbersMat.min())
print(numbersMat.mean())

#12- üretilen matrisin en büyük değerinin indeksi kaçtır =

print(numbersMat.argmax())

#13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.

numbers = np.arange(10,20)
print(numbers[:3])

#14- üretilen dizinin elemanlarını tersten yazdırın.

print(numbers[::-1])

#15- üretilen matrisin ilk satırını seçiniz

print(numbersMat[0])

#16- üretilen matrisin 2.satır 3.sütunundaki elemanı hangisidir?

print(numbersMat[1,2])

#17- üretilen matrisin tüm satırlardaki ilk elemanı seçiniz.

print(numbersMat[:,:1])

#18- üretilen matrisin her bir elemanının karesini alınız.

numbersMat = numbersMat ** 2
print(numbersMat)

#19- üretilen matris elemanlarının hangisi pozitif çift sayıdır?
#   Aralığı (-50,+50) arasında yapınız.

numbers = np.random.randint(-50,50,15)
numbers = np.array(numbers)
numbersMat = numbers.reshape(3,5)
print(numbersMat)

positiveEven = numbersMat[(numbersMat > 0) & (numbersMat % 2 == 0)]
print("\nPozitif Çift Sayılar:")
print(positiveEven)




