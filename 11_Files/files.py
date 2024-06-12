# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi, dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w": (Write) Yazma modu. Dosyayı konumda oluşturur. içeriği siler ve yeniden ekleme yapar.
# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
# "r": (Read) okuma. varsayılan. dosya konumda yoksa hata verir.

# Dosyayı açtıktan sonra kapatmayı unutma close()

# file = open("newfile.txt", "w", encoding='utf-8') # encoding türkçe karakterleri tanımasını sağlar
# file = open("C:/Users/SefaPc/Desktop/newfile.txt", "w")
# file.close()

# file = open("newfile.txt", "a", encoding='utf-8') # cursor bulunduğu yerden dosya içeriğine ekleme yapmaya devam eder.

# file = open("newfile.txt", "x", encoding='utf-8') # dosya zaten var olduğu için hata verir.
# file.write('asd')

# file.close()

#-------> Dosyadan bilgi okuma

# try:
#     file = open("newfile.txt", "r") # dosya konumda yoksa exception gösterir çünkü okuma modunda
#     print(file)

# except FileNotFoundError:
#     print('Dosya okuma hatası.')

# finally:
#     file.close()

file = open("newfile.txt", "r", encoding='utf-8')

#----->  for döngüsü
# for i in file:
#     print(i, end="") #end ile araya bir boşluk eklenmeden elde ederiz.

#----->  read() fonksiyonu

# content1 = file.read() # en sona kadar okur
# print("--içerik 1--")
# print(content1)

# content2 = file.read() # dosya henüz kapanmadığından cursor en sondadır ve okuyacak bir şey kalmamıştır.
# print("--içerik 2--")
# print(content2)

# content = file.read(5) # ilk 5 karakteri okur
# content = file.read(3) # cursorun kaldığı yerden itibaren  3 karakter okur
# print(content)

#-----> readline() fonksiyonu
    
# content = file.readline() # ile her seferinde 1 satır okur

# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="") # boşluk ekler

#-----> readlines() fonksiyonu

# liste = file.readlines() # bütün satırları okur
# print(liste)
# print(liste[0], liste[1])

# file.close()











