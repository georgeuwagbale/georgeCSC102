import pymongo

#client = pymongo.MongoClient("mongodb://localhost:27017/")

client = pymongo.MongoClient(
    "mongodb+srv://George:realghost16@cluster1.qvpms.mongodb.net/Bank?retryWrites=true&w=majority")
db = client.test
#print(client)
db = client.get_database("Bank")
collection = db.get_collection("customers")
print(client.list_database_names())
#print(db.list_collection_names())



print()
for a in collection.find():
    print(a)
collection.delete_many({})
old_pin_from_database = collection.find_one({"name": "Moses", "bvn": 806646, "account number": 20120612060},{"_id": 0, "name":1})
print(old_pin_from_database.get("name"))
collection.update_one({"name":"Ike"},{"$set":{"account type":"naira"}})
a = list[collection.find()]
