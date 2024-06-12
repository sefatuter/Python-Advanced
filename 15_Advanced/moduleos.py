import os #işletim sistemiyle alakalı. Operating System
import datetime

# result = dir(os)
# result = os.name


#---> Klasör oluşturma

# os.chdir('C:\\') # C dizinine geçer
# # mkdir ile C dizinine bu klasörü oluşturur
# result = os.getcwd() # dosyanın hangi klasör içinde bulunduğunu söyler
# os.mkdir("newdirectory") # yeni klasör oluşturur
# os.makedirs("newdirectory/yeniklasör") # klasör içinde klasör oluşturma
# os.rename("newdirectory", "yeniklasor") # klasör adı değiştirme
# os.rmdir("newdirectory") # klasörü siler
# os.removedirs("yeniklasor/yeniklasor") # alt dizindeki klasörü siler


#---> Listeleme

# result = os.listdir() # şuanda etkin olan dizin içinde olan klasörleri gösterir
# result = os.listdir('C:\\') # C dizini altındaki bütün klasörleri gösterir

# filtreleme nasıl yapılır?
# for dosya in os.listdir():
#     if dosya.endswith('.py'): # Sadece .py uzantılı dosyaları buluruz
#         print(dosya)

#---> Dizin değiştirme

# os.chdir('..') # bir üst dizine geçer
# os.chdir('../..') # iki kere üst klasöre geçer


#---> Etkin dizin öğrenme
# result = os.getcwd()

# result = os.stat("c:\\Users\\SefaPc\\Desktop\\btkPythonL\\15_Advanced\moduleos.py") # bir dosya hakkında bilgi sahibi olmak için

# result = result.st_size/1024 # 1024 bölünerek boyutu bulunur
# result = datetime.datetime.fromtimestamp(result.st_ctime) # dosyanın oluşturulma zamanı
# result = datetime.datetime.fromtimestamp(result.st_atime) # son erişilme tarihi 
# result = datetime.datetime.fromtimestamp(result.st_mtime) # değiştirilme tarihi.


# os.system("notepad.exe") # sistem üzerinden bir dosyayı çalıştırır


#---> Path

result = os.path.abspath("moduleos.py") # dosyanın tam konumunu belirtir.
result = os.path.dirname("C:/Users/SefaPc/Desktop/btkPythonL/15_Advanced/moduleos.py") # tam konumu verilen bir dosyanın dizinini alır.
result = os.path.dirname(os.path.abspath("moduleos.py")) # adı verilen dosyanın tam yolunu bulur
result = os.path.exists("C:/Users/SefaPc/Desktop/btkPythonL/15_Advanced/moduleos.py") # Dosya orada mı değil mi?
result = os.path.exists("C:/Users/SefaPc/Desktop/btkPythonL") # klasör orada mı değil mi?
result = os.path.isdir("C:/Users/SefaPc/Desktop/btkPythonL") # bir klasör olup olmamasını kontrol eder
result = os.path.isdir("C:/Users/SefaPc/Desktop/btkPythonL") # klasör değil false
result = os.path.isfile("C:/Users/SefaPc/Desktop/btkPythonL/15_Advanced") # dizin mi yoksa bir dosya mı kontrol eder. false
result = os.path.join("C:\\","deneme") # c'nin altına bir deneme path'i oluşturur
result = os.path.split("C:\\deneme")
result = os.path.splitext("moduleos.py") # dosya ismi ile uzantısını ayırır
result = result[0]


print(result)


