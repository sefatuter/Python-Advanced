import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb+srv://roni:mongodb1234@cluster0.u22cj9y.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")

mydb = myclient["node-app"]

mycollection = mydb["products"]


# Tekli kayıt mı? Çoklu kayıt mı?

# result = mycollection.find_one() # Bulunan ilk kaydı alır.
# print(result)


# for i in mycollection.find(): # Database'deki bütün kayıtları getirir.
#     print(i) 

# find() - 1. parametre Query, 2. kolon seçme işlemi
    
# for i in mycollection.find({},{"_id":0, "name":1, "price":1}): # id kolonunu istemiyoruz, sadece name ve price istiyoruz
#     print(i)

# for i in mycollection.find({},{"_id":0}): # id kolonunu istemiyoruz, geri kalanlarını istiyoruz
#     print(i)

for i in mycollection.find({},{"name":1}): #  name alanını istedik, id ile ilgili bir işlem yapılmadığı için id de gelir. geri kalanı gelmez
    print(i)

