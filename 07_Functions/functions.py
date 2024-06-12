#FUNCTIONS
def sayHello(name = 'user'):
    print('Hello ' + name)

sayHello('world')
#argümanlı fonksiyon oluşturma.

sayHello('Ada')

sayHello() # parametre gönderilmezse varsayılan olarak user yazdırılır

def sayHello(name = 'user'):
    return 'Hello ' + name # geri döndürür

msg = sayHello('Çınar')

print(msg)


def total(num1, num2):
    return num1 + num2

result = total(10,20)

print(result)


def yasHesapla(dogumYili):
    return 2024 - dogumYili

age1 = yasHesapla(2016)

print(age1)

def retirementYear(dogumYili, isim):
    '''
    DOCSTRING: Doğum yılınıza göre emekliliğinize kaç yıl kaldı
    INPUT: Doğum yılı
    OUTPUT: Hesaplanan yıl bilgisi
    '''
    yas = yasHesapla(dogumYili)
    retirement = 65 - yas
    
    if (retirement > 0):
        print(f'Emekliginize {retirement} yil kaldi.')
    else:
        print('Zaten emekli oldunuz.')

retirementYear(1943, 'Ali')

print(help(retirementYear)) #! help kullanimi !

list = [1,2,3]

print(help(list.append))