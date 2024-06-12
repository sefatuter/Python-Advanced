numbers = []
for x in range(10):
    numbers.append(x) #ikisi de aynı sonuca varır listeye ekleme işlemi, alttaki de
print(numbers)

numbers = [x for x in range(10)] # for x in range(10) buradan aldığımız değeri soldaki x değerinde kullanıyoruz
print(numbers)

# 0 dan 10 a kadar olan sayıları range içerisinden for döngüsü
# ile alıyoruz teker teker x in içine atıp numbers dizisi içine atıyoruz. 

for x in range(10):
    print(x**2)

numbers = [ x**2 for x in range (10)] # for x in range(10) buradan aldığımız değeri soldaki x**2 değerinde kullanıyoruz
print(numbers)

numbers = [x*x for x in range(10) if x % 3 == 0] # x şayet 3'e bölünüyor ise her birinin karesini alıp listeye ekle 
print(numbers)


myString = 'Hello'
myList = []


for letter in myString:
    myList.append(letter)
print(myList) #hello'nun bir dizi şekline çevrilip yazdırılması


myList = [ letter for letter in myList]
print(myList) # aynı sonucun kısa hali

years = [1983, 1999, 2008, 1956, 1986]

ages = [2019-year for year in years]
print(ages)

results = [x if x%2==0 else 'TEK' for x in range(1, 10)]
print(results)
# sorduğumuz soru x'ten hemen sonra geliyor x'in listeye dahil olabilmesi için if koşulunun true olması gerekir.

result = []

for x in range(3):
    for y in range(3):
        result.append((x,y))
        
print(result)

# bunu basit şekilde yapma yolu

numbers = [ (x,y,z) for x in range(3) for y in range(3) for z in range(3)] # x için bir döngü oluşturduk ve y için bir döngü oluşturduk
        # x için olanı ilk döngüye y için olanı ikinci döngüye aldık (x, y)

print(numbers) # yine aynı sonucu verir

