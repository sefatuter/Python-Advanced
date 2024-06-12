x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

#1- Kullanıcıdan alınan 2 saysının çarpımı ile x,y,z toplamının farkı nedir?

# n1 = int(input(("Enter first num: ")))
# n2 = int(input(("Enter second num: ")))

# result = (n1 * n2)-(x+y+z)
# print(result)

#2- y'nin x'e kalansız bölümünü hesaplayınız

result = y // x
print(result)

#3- (x,y,z) toplamının mod 3'ü nedir?

result = (x+y+z) % 3
print(result)

#4- y'nin x. kuvvetini hesaplayınız

result = y ** x
print(result)

#5- x, *y, z = numbers işlemine göre z'nin küpü kaçtır?

x, *y, z = numbers

result = z ** 3
print(result)


#6 x, *y, z = numbers işlemine göre y'nin değerlerinin toplamı kaçtır?

x, *y, z = numbers

result = y[0] + y[1] + y[2]
print(result)
