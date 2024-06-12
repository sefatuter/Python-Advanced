# liste = ["1", "2", "5a", "10b", "abc"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz.

# for x in liste:
#     try:
#        result = int(x)
#        print(result)
#     except ValueError:
#         continue
    
# 2: Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı
# olduğundan emin olunuz aksi halde hata mesajı yazın.

# while True:
#     x = input('sayı: ')
        
#     if x == 'q':
#         print('Quit')
#         break
#     try:
#         result = float(x)
#         print('Your num ', result)
    
#     except ValueError as e:
#         print('Cannot enter this!')
    

# 3: Girilen parola içindeki türkçe karakter hatası veriniz.

# psw = input('Password : ')

# def checkPass(psw):
#     tr_char = 'şçğüöıİ'
#     for i in psw:
#         if i in tr_char:
#             raise TypeError('Pass cannot consider turkish words.')      
#         else:
#             pass
#     print('Accepted pass.')


# try:
#     checkPass(psw)
# except TypeError as err:
#     print(err)


# 4: Faktöriyel fonksiyonu oluşturup fonksiyona gelen değerler için
# hata mesajları verin.

def factor(x):
    x = int(x)
    
    if x < 0:
        raise ValueError('Negative value')
    
    result = 1
    
    for i in range(1,x+1):
        result *= i
    return result


for x in [5,10,3,-1,-3,'10a']:
    try:
        y = factor(x)
    except ValueError as err:
        print(err)
        continue

    print(y)