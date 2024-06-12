import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb+srv://roni:mongodb1234@cluster0.u22cj9y.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# result = mycollection.find().sort('name') # name kolonuna göre sıralandı
# result = mycollection.find().sort('name', 1) #  1 yazılırsa artan sırada
# result = mycollection.find().sort('name', -1) #  -1 yazılırsa azalan sırada
# result = mycollection.find().sort('price', -1) # artan, azalan fiyatta sıralama
result = mycollection.find().sort([('name', 1), ('price', -1)]) # önce name'e göre, sıralanan elemanlar arasında da fiyat azalan şekilde sıralanır


for i in result:
    print(i)