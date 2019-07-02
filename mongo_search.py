import pymongo

mongoDBclient = pymongo.MongoClient("mongodb://localhost:27017/")

db = mongoDBclient['jira']

collection = db['worklogs']

# search_all = db.collection.find()

for record in db.collection.find():
    print(record)