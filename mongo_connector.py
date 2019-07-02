import pymongo

def mongo_insert_one_worklog(record):

    mongoDBclient = pymongo.MongoClient("mongodb://localhost:27017/")

    db = mongoDBclient['jira']

    collection = db['worklogs']

    response = collection.insert_one(record)

    return response

#
# create_collection = db.create_collection(collection)
#
# print(create_collection)


# post = {
#     "name": "TarynSligh",
#     "created": "2017-10-23T01:04:16.458-0500",
#     "updated": "2017-10-23T01:04:16.458-0500",
#     "started": "2017-10-23T01:03:00.000-0500",
#     "timeSpentSeconds": 1200,
#     "_id": "29629"
#     }
