#1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme
#   durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu
#   lise ya da üniversite olmalıdır.

# name = input('Enter your name: ')
# age = int(input('Enter your age: '))
# edc = input('Enter your education: ')

# if age >= 18:
#     if (edc.lower() == 'lise') or (edc.lower() == 'üniversite'):
#         print(f'{name} You can get your driving license!')
#     else:
#         print('You can\'t get your driving license!! (Level of education is not enough)')
# else:
#     print('You can\'t get your driving license!!(Age is not old enough)')



#2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#   not aralığına karşılık gelen not bilgisini yazdırınız.
#   0-24    =>  0
#   25-44   =>  1
#   45-54   =>  2
#   55-69   =>  3
#   70-84   =>  4
#   85-100  =>  5

# y1 = float(input('Birinci yazılı notunu giriniz: '))
# y2 = float(input('İkinci yazılı notunu giriniz: '))
# s = float(input('Sözlü notunu giriniz: '))

# ort = (y1+y2+s) / 3

# if ort >= 0 and ort <= 24:
#     print(f'Notunuz: 0, ortalamanız {ort}')
# elif ort >= 25 and ort <= 44:
#     print(f'Notunuz: 1, ortalamanız {ort}')
# elif ort >= 45 and ort <= 54:
#     print(f'Notunuz: 2, ortalamanız {ort}')
# elif ort >= 55 and ort <= 69:
#     print(f'Notunuz: 3, ortalamanız {ort}')
# elif ort >= 70 and ort <= 84:
#     print(f'Notunuz: 4, ortalamanız {ort}')
# elif ort >= 85 and ort <= 100:
#     print(f'Notunuz: 5, ortalamanız {ort}')
# else:
#     print('Yanlış bilgi girdiniz!')


#3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#   göre hesaplayınız.
#   1.  Bakım   =>  1.yıl
#   2.  Bakım   =>  2.yıl
#   3.  Bakım   =>  3.yıl
#   ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
#   *** datetime modülünü kullanmanız gerekiyor.

import datetime

date = input('Trafiğe çıkış tarihini giriniz (GG/AA/YYYY): ')
date = date.split('/')

# print(date)
trafigeCikis = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
today = datetime.datetime.now()
fark = today - trafigeCikis
# print(fark.days)
date = fark.days

if(date > 0) and (date <= 365):
    print('1. Bakım aralığı')
elif(date > 365) and (date <= 2*365):
    print('2. Bakım yapılmış.')
elif(date > 365*2) and (date <= 365*3):
    print('3. Bakım yapılmış.')
else:
    print('Hatalı süre.')

print(f'{fark.days} gün boyunca araç trafiktedir.')


