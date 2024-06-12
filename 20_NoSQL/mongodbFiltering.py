import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb+srv://roni:mongodb1234@cluster0.u22cj9y.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# filter = {"name": "Iphone 8"}

# result = mycollection.find(filter) # 1. parametre Query, 2. kolon seçme işlemi

# for i in result:
#     print(i)


# result = mycollection.find_one(filter)
# result = mycollection.find_one({"_id": ObjectId("66570a52e6356aed7abc45ba")}) #Query ile arama, string bilgisini objectid yapmalıyız

# result = mycollection.find({
#     "name": {
#         "$in" : ["Iphone 8", "Iphone 9", "Iphone 14"] # Name alanına uyuyorsa bu verileri alır (include = $in)
#     }
# })


# result = mycollection.find({
#     "price": {
#         "$gte": 10000  # (greater than = $gt) (lower than = $lt) (greater than or equal = $gte) (lower than or equal = $lte) (equal = $eq)<->("price": 2000)
#     }
# })

#  https://www.mongodb.com/docs/manual/reference/operator/query/

#--> Regex

result = mycollection.find({
    "name": {"$regex": "^I"} # Name alanı I ile başlayanları getir
})


for i in result:
    print(i)