# def square(num): return num**2
square = lambda num: num ** 2 # üsttekiyle aynı sonucu verir, bir değişkenin içine atılıp

numbers = [1,3,5,9,10,4]

# map metodu ile dizi içindeki her bir elemana ulaşıp fonksiyon içinden geçirebiliriz
result = list(map(square, numbers))
# listeye çevrilmeli!
print(result)

for item in map(square, numbers): 
    print(item) # döngü ile yazdırılması

# ya liste ya da enumerate edilmeli

result = list(map(lambda num: num ** 2, numbers))
print(result) # squarein yaptığı işlemi isimsiz bir fonksiyonla yaptık: lambda expression.

result = square(7)
print(result)

# map fonksiyonu dizinin elemanlarını tek tek fonksiyona gönderir.

# def checkEven(num): return num % 2 == 0

checkEven = lambda num: num % 2 == 0

# liste içindeki çift sayıları çeker
# result = list(filter(checkEven, numbers)) # farklı bir yolu aşağıda
#result = list(filter(lambda num: num%2==0, numbers)) # yine aynı sonucu verir, farklı yolu aşağıda

result = checkEven(numbers[2])
print(result)


print(result)


