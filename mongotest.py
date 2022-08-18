import pymongo
client = pymongo.MongoClient("mongodb+srv://priyanka_k:nilpriya@cluster0.ayedtpc.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name":"shudhanshu",
    "email" : "shudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1 ['test']
coll.insert_one(d)