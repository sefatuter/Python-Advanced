# with open("newfile.txt", "r+", encoding='utf-8') as file:
#     print(file.read())

# with open("newfile.txt", "r+", encoding='utf-8') as file:
#     print(file.write('deneme')) #dosya baştan açıldığı için cursor baştan başlar
  
#---> Sayfa sonunda güncelleme
    
# with open("newfile.txt", "a", encoding='utf-8') as file:
#     file.write('\nlal qhq')

# with open("newfile.txt", "r", encoding='utf-8') as file:
#     print(file.read())
    
    
#----> Sayfa başında güncelleme

# with open("newfile.txt", "r+", encoding='utf-8') as file:
#     content = file.read()
#     content = "Efe turan\n" + content
#     file.seek(0) # cursoru başa döndürür
#     file.write(content)
#     print(content)
    
    
#-----> Sayfa ortasında güncelleme


with open("newfile.txt", "r+", encoding='utf-8') as file:
    list = file.readlines()
    list.insert(1, "Yılmaz al\n") # Verilen index numarasından hemen önce ekleme işlemini yapar.
    file.seek(0)
    # for i in list:
    #     file.write(i)
    file.writelines(list) # Yukarıdaki for döngüsüne alternatif
    
with open("newfile.txt", "r", encoding='utf-8') as file:
    print(file.read())



    