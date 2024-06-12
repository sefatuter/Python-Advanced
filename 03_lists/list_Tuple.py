list = [1, 2, 3]
tuple = (1, 'iki', 3) # tuple liste bu şekilde oluşturulur veya parantezsiz

# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])

# print(len(tuple))
# print(len(list))

list = ['ali', 'veli']
tuple = ('damla', 'ayse')
names = ('demet', 'aysel', 'ali') + tuple

print(names)

list[0] = 'ahmet' # bu işlem çalışır
# tuple[0] = 'deniz' # bu işlem çalışmaz "TypeError: 'tuple' object does not support item assignment"
# tuple'da elemanlar atandıktan sonra bu değiştirilemez.

print(tuple.count('damla'))
print(tuple.index('damla'))

print(list)
print(tuple)





