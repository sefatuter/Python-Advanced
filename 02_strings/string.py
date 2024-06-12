name = "sadik"
 # type: ignore

surname = "turan"
age = 36
promp = "My name is "

introduce = promp + name + ' ' +  surname + ' ' + '\nI am ' +  str(age) + ' years old.'
length = len(introduce)
print(introduce)

print(len(introduce))

print(introduce[0])
print(introduce[3])
print(introduce[length-1])

print(introduce[3:9]) #3. indeksten başla 9. indekse kadar yazdır
print(introduce[2:40:2]) # ikişer ikişer atlayarak yazar