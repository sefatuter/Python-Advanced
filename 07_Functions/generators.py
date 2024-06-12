# 12. Functions_6


def cube():
    for i in range(5):
        yield i ** 3 # yield bir değer üretiyor ve bir yerde saklamıyor

# iterator = cube()
# print(cube())

#iterator = iter(generator)


# print(next(iterator)) # üzerinde dolaşabileceğimiz bir obje gönderiliyor
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

for i in cube(): # or iterator
    print(i)



liste = (i**3 for i in range(5)) # [] ' ları () ile değiştirdiğimizde generator'a dönüşür

print(liste)

print(next(liste))

for i in liste:
    print(i)