import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb+srv://roni:mongodb1234@cluster0.u22cj9y.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")

mydb = myclient["node-app"]
mycollection = mydb["products"]


#-->  update_one()
# mycollection.update_one( # 1. parametre Query, 2. parametre değiştirmek istediğimiz $set
#     {'name': 'Iphone 6'},
#     {'$set':{
#         'name': 'Iphone 7',
#         'price': 2000
#     }}
    
# )

# for i in mycollection.find():
#     print(i)

#--> update_many()

query = {'name': 'Iphone 9'}
newVal = {'$set': {
    'name': 'Iphone X',
    'price': 7000
}}
# mycollection.update_many(
#     {'name': 'Iphone 7'},
#     {'$set':{
#         'name': 'Iphone 8',
#         'price': 5000
#     }}
    
# )

result = mycollection.update_many(query, newVal)

for i in mycollection.find():
    print(i)

print(f'{result.modified_count} adet kayit guncellendi.')

