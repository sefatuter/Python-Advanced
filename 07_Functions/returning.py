# 12. Functions_2

def usalma(num):
    
    def inner(power):
        return num ** power
    
    return inner

two = usalma(2)   # 2. kuvvetini
print(two(3))

three = usalma(3) # 3. kuvvetini
print(three(3))



def yetkiSorgu(page):
    
    def inner(role):
        if role == 'Admin':
            return "{0} rolü {1} sayfasına ulaşabilir.".format(role, page)
        else:
            return "{0} rolü {1} sayfasına ulaşamaz.".format(role, page)

    return inner
    
user1 = yetkiSorgu("Product Edit")
print(user1('Admin'))
print(user1('User'))


def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    
    if islem_adi == 'Toplama':
        return toplam
    else:
        return carpma
    
    
toplama = islem('Toplama')
print(toplama(1,4,5,6,3,5))

carpma = islem('Carpma')
print(carpma(1,34,5,5))



