numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 's']

val = min(numbers)
val = max(numbers)
val = min(letters)
val = max(letters)

val = numbers[3:6]
val = numbers[:3]

numbers[4] = 40


numbers.append(49) # listeye ekleme yapmaya yarar
numbers.insert(3, 78) # hangi indexe hangi şeyin ekleneceğini belirler araya ekleme yapar 3 den sonra gibi
# numbers.insert(-1, 52) # sondan bi önceye ekler

# numbers.pop() # silme işlemi yapar indexe göre
numbers.pop(0)

numbers.remove(49) # silmek istenen karakteri verilir

numbers.sort() # liste sayısal büyüklük olarak sıralanır
letters.sort()

numbers.reverse() #liste ters çevrilir
letters.reverse()

print(numbers)
print(letters)

print(len(numbers))
print(len(letters))


print(numbers.count(10)) # listede 10 kaç tane var?
print(letters.count('a')) # listede 'a' kaç tane var

numbers.clear() # bütün elemanları siler
print(numbers)

