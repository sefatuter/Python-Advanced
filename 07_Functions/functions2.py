#1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

# def write(name, n):
#     for x in range(n):
#         print(name)

# name = input('Kelime giriniz: ')
# n = int(input('Kac kez yazılacagını giriniz: '))
# write(name, n)



#2- Kendine gönderilen sınırsız sayıdaki parametreyi listeye çeviren fonksiyonu yazın.

# def convertList(*params):
#     list1 = []

#     for p in params:
#         list1.append(p)

#     return list1

# print(convertList(10,20,30,40,11))



#3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun

# num = int(input('Asal sayi kontrolu icin sayi araligi giriniz ilk sayi: '))
# num2 = int(input('ikinci sayi: '))

# isPrime = True

# if(num == 1):
#     isPrime = False

# for i in range (num, num2):
#     for i in range (2, num):
#         if (num % i == 0):
#             isPrime = False
#             break
#     else:
#         isPrime = True
#     if isPrime:
#         print(num)

#     num += 1

#4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürün.


n = int(input('Tam bölenleri görmek icin sayiyi girin: '))

def bolen(n):
    pList = []
    for i in range (1, n+1):
        if (n % i == 0):
            print(f'{i} bir tam bölenidir.')
            pList.append(i)
    print(pList)

bolen(n)




