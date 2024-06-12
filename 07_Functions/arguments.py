def changeName(n):
    n = 'ada'

name = 'yigit'

changeName(name)
print(name) # yigit olarak kalir



def change(n): # tanımlanan n parametresine sehirler dizisi gönderilir
    n[0] = 'istanbul' # dizinin ilk elemanı 'istanbul' yapılır, adres kopyalaması

sehirler = ['ankara','izmir']

change(sehirler)
print(sehirler)


n = sehirler # iki değişken de aynı adresi tutuyor
n[0] = 'kocaeli'
# yukarıda fonksiyonla yapılan işlemin açılımı
print(sehirler)

n = sehirler[:] # slicing, sehirler dizisi üzerindeki bilgileri al farklı liste oluştur
n[0] = 'bursa'

print(sehirler) # görüldüğü gibi sehirler değişmedi
print(n) # n değişti

def change(n):
    n[0] = 'bolu'

change(sehirler[:]) 

print(sehirler)

#--

def add(a, b, c = 0, d = 0):
    return sum((a, b, c))

print(add(10,20,30)) # iki parametreli de çalışır üç parametreli de ...


# tek tek yazmak yerine..

def add(*params): # * koyularak
    print(params) # tuple listesi şeklinde oluşturur
    return sum((params))

print(add(10,20,30,40,50))


def add(*params):
    print(type(params))
    print(params)
    sum = 0
    for n in params:
        sum = sum + n
    return sum

print(add(100,200,3,4,5))


# birden fazla farklı tipte veri göndermek için liste olmalı, dictionary

def displayUser(**args): # dictionary gelecegini bildirmek için ise *
    print(type(args))
    print(args)
    for key, value in args.items():
        print(f'{key} is {value}')

# bir dictionary oluşturuldu


displayUser(name = 'ali', age = 2, city = 'Ankara')
displayUser(name = 'veli', age = 22, city = 'bursa', phone = '5445122334')
displayUser(name = 'can', age = 32, city = 'istanbul', email = 'aliveli@gmail.com')

def myFunc(a, b, c, *args, **kwargs): # arguments, keyword arguments
    print('a= ',a)
    print('b= ', b)
    print('c= ', c)
    print('args= ', args)
    print('kwargs= ', kwargs)

myFunc(10,20,30,40,50, key1 = 'value1', key2 = 'value2')