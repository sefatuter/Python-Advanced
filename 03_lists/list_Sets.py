fruits = {'orange', 'apple', 'banana'}

# print(fruits[0]) indekslenemez

for x in fruits: # tek tek x e fruitleri eşitliyor
    print(x)

fruits.add('cherry')
fruits.update(['mango', 'grape', 'apple']) # rastgele ekler, aynı elemanı eklemez

fruits.remove('mango')
fruits.discard('apple')

print(fruits)

fruits.pop() # herhangi bir elemanı siler indekslenmediği için
print(fruits)

fruits.clear() # butun elemanları siler


# mylist = [1,2,5,4,4,2,1]
# print(mylist)
# print(set(mylist)) # tekrarlayan elemanları listeden çıkar. sete çevrildiğinde

