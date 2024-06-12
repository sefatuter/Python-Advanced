# range metodu
for item in range(10): # 0 dan başlar 9 a kadar bir döngü oluşturur
    print(item)

for item in range(5,10): # 5 dan başlar 9 a kadar bir döngü oluşturur
    print(item)

for item in range(50,100,10): # 50 dan başlar 99 a kadar 10'ar, 10'ar gitsin
    print(item)

print(list(range(50,100,10))) # listeye çevirir ve printler

#c/c++ 'daki
#   for ( int i = 0; i < 10 ; i++){  ifadesine benzer
#   print(i)
#   }


# enumerate metodu

index = 0
greeting = 'Hello there'

for letter in greeting:
    print(f'index: {index} ,letter: {greeting[index]}') # {letter} veya greetings[index]
    index += 1
# her ulaştığımız kelimenin indexine de ulaşmak istersek eğer

for index, letter in enumerate(greeting):
    print(f'index: {index} ,letter: {letter}')

for item in enumerate(greeting):
    print(item) # enumaret'in bize yazdırdıkları

# zip metodu

list1 = [1,2,3,4,5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = [100, 200, 300, 400, 500]

print(list(zip(list1, list2, list3))) #eşleştirme yapılır 

# index numaralarına göre listeleri birleştirir

for item in zip(list1, list2, list3):
    print(item)

for a,b,c in zip(list1, list2, list3):
    print(a) # sadece listenin a değerleri yani 1,2,3,4,5 değerlerini gösterir
    print(b, c)