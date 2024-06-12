#1 "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluştur.

car = ['Bmw', 'Mercedes', 'Opel', 'Mazda']

#2 Liste kaç elemanlıdır?

print(len(car))

#3 listenin ilk ve son elemanı nedir?

print(car[0])
print(car[len(car)-1])
print(car[-1])

#4 Mazda değerini toyota ile değiştir

car[-1] = 'Toyota'
print(car)

#5 Mercedes listenin bir elemanı mıdır?

result = 'Mercedes' in car # car in içinde 'Mercedes var mı diye kontrol eder
print(result)

#6 listenin -2 indeksindeki değer nedir?

print(car[-2])

#7 listenin ilk 3 elemanını alın

print(car[:3])

#8 listenin son 2 elemanı yerine "Toyota" ve "Renault" değerleri ekle

car[-2:] = ['Renault', 'Toyota']

#9 listenin üzerine "Audi" ve "Nissan" değerlerini ekle

# car.append('Audi')
# car.append('Nissan')
# print(car)  or; 

result = car + ['Audi', 'Nissan'] # listenin içeriği değişmedi fark ettiysen yeni result değişkenine atama yapıldı
                                  # listenin içeriği sadece liste metodlarıyla değiştiriliyor.
print(result)

#10 listenin son elemanını sil

# car.pop(len(car)-1)
# print(car)

del car[-1]
result = car
print(result)

#11 liste elemanlarını tersten yazdırın

# car.reverse()
# print(car)
print(car[::-1])

#12 aşağıda verilenleri bir liste içinde saklayınız

    # studentA: Yiğit Bilgi 2010, (70,60,70)
    # studentB: Sena Turan  1999, (80,80,70)
    # studentC: Ahmet Turan 1998, (80,70,90)

#studentA = ['StudentA']
#studentB = ['StudentB']
#studentC = ['StudentC']
#students = [studentA, studentB, studentC]

#students[0] = ["Yiğit Bilgi 2010, (70,60,70)"]
#students[1] = ["Sena Turan  1999, (80,80,70)"]
#students[2] = ["Ahmet Turan 1998, (80,70,90)"]

studentA = ['Yiğit', 'Bilgi', 2010, [70,60,70]]
studentB = ['Sena', 'Turan', 1999, [80,80,70]]
studentC = ['Ahmet', 'Turan', 1998, [80,70,90]]

#13 liste elemanlarını ekrana yazdırınız

result = studentA[0]
result = studentB[1]
result = studentC[3][2]
print(result)

result = f"{studentA[0]} {studentA[1]} {2024-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}."
print(result)

