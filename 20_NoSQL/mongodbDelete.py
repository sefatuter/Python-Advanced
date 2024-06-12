import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb+srv://roni:mongodb1234@cluster0.u22cj9y.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")

mydb = myclient["node-app"]
mycollection = mydb["products"]


#--> delete_one()
'''
for i in mycollection.find():
    print(i)
    
print('-'*70)

mycollection.delete_one({'name': 'Iphone X'})

for i in mycollection.find():
    print(i)
''' 
    
#--> delete_many()

for i in mycollection.find():
    print(i)
    
print('-'*70)

result = mycollection.delete_many({'name': 'Iphone 11'})

for i in mycollection.find():
    print(i)
    
print(f'{result.deleted_count} adet kayit silindi.')



