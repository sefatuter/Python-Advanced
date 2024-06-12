import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://roni:mongodb1234@cluster0.u22cj9y.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")

mydb = myclient["node-app"]

mycollection = mydb["products"] # products isminde collection yoksa oluşturur.

# print(mydb.list_collection_names()) # Database içerisindeki collectionları sıralar
# print(myclient.list_database_names())

# products = {"name": "Iphone 7", "price": 2000}

# result = mycollection.insert_one(products) # insert_one 1 tane için

# print(result) # Obje geriye döndürüldü
# print(type(result)) # pymongo classı
# print(result.inserted_id) # primary key id objesi

#--> Birden fazla kaydı ekleme.

# productList = [
#     {"name": "Iphone 8", "price": 3000},
#     {"name": "Iphone 9", "price": 4000},
#     {"name": "Iphone X", "price": 5000},
#     {"name": "Iphone 11", "price": 6000},
#     {"name": "Iphone 12", "price": 7000},
#     {"name": "Iphone 13", "price": 8000},
# ]

# Bir şema oluşturmak zorunda değiliz, istediğimiz yapıda veriyi db'ye gönderebiliriz.
productList = [
    {"name": "Iphone 14", "price": 13000, "description": "good product"},
    {"name": "Iphone 15", "price": 14000, "categories": ['telephone', 'electronic']},
]


result = mycollection.insert_many(productList)

print(result.inserted_ids) # ids
