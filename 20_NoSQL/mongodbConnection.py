#-->Yerel bilgisayardaki db'ye bağlantı.
'''
import pymongo
import pymongo.mongo_client

myclient = pymongo.MongoClient("mongodb://localhost:27017") # Bilgisayarla bağlantıyı sağla

mydb = myclient["node-app"] # Collection'u ara bulursa kullanacak, elimzle ekledik

print(myclient.list_database_names()) # Şu anda olan database'leri görüntüledik
'''


#--> Server üzerindeki db'ye bağlantı.
'''
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://roni:<PASSWORD>@cluster0.u22cj9y.mongodb.net/<DATABASE-NAME>?retryWrites=true&w=majority&appName=Cluster0")

mydb = myclient["node-app"]

print(myclient.list_database_names())
'''