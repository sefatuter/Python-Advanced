''' -Sayı Tahmin Oyunu-
    
    1-100 arasında rasgele üretilecek bir sayıyı aşağı-yukarı ifadeleri ile
    buldurmaya çalışın. ( hak = 5)
    ** "random modülü" için "python random" şeklinde arama yapın.
    ** 100 üzerinden puanlama yapın. her soru 20 puan.
    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı
        üzerinden hesaplansın.
'''

import random

num = random.randint(1, 100)

print(num)

h = int(input('Kac hakkiniz olmasını istersiniz: '))
puan = 100/h
count = h

for x in range(h):
    guess = int(input(f'{x+1}.Tahmininiz: '))
    if(guess > num):
        print('Asagi')
        count -= 1
    elif(guess < num):
        print('Yukari')
        count -= 1
    elif(guess == num):
        print('Dogru Tahmin.')
        puan = count * puan
        print(f'{h-count+1}. Tahminizde bildiniz, {puan} puan kazandiniz.')
        break
    else:
        print('Gecerli sayi giriniz!')

