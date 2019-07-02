
import jira_connect
import json
import pymongo

#TODO get key from search make it dynamic
issue_key = "AMR-15"

query = "issue/"+issue_key+"?renderedFields=\"worklogs\""

data = jira_connect.jira_connect_method("ADR", query)
data = json.loads(data)

mongoDBclient = pymongo.MongoClient("mongodb://localhost:27017/")

db = mongoDBclient['jira']


worklogs = data['fields']['worklog']['worklogs']

print("\"Issue Key:\" ","\"",issue_key,"\"")

for worklogList in worklogs:
    dict(worklogList)
    timeSpent = [(keys, value) for keys, value in worklogList.items() if keys == 'timeSpent']

    author = [(keys, value) for keys, value in worklogList.items() if keys == 'author']
    author = dict(author)
    name = (author['author']['name'])
    created = [(keys, value) for keys, value in worklogList.items() if keys == 'created']
    updated = [(keys, value) for keys, value in worklogList.items() if keys == 'updated']
    started = [(keys, value) for keys, value in worklogList.items() if keys == 'started']
    timeSpent = [(keys, value) for keys, value in worklogList.items() if keys == 'timeSpent']
    _id = [(keys, value) for keys, value in worklogList.items() if keys == 'id']




# print("{")
# for wl in worklogs:
#     for key, value in wl.items():
#         if key == "author":
#             for key, value in wl['author'].items():
#                 if key == "name":
#                     print(" \"worklog\": {\"" + key + "\": ", "\"" + value + "\",")
#         if key == "timeSpentSeconds":
#             print("\"" + key + "\": ", "" + str(value) + ",")
#         if key == "created":
#             print("\""+key+"\": ", "\""+ value + "\",")
#         if key == "updated":
#                 print("\"" + key + "\": ", "\"" + value + "\",")
#         if key == "started":
#             print("\"" + key + "\": ", "\"" + value + "\",")
#         if key == "id":
#             print("\""+key+"\": ", "\""+ value + "\"},")
# print("}")




# old code to loop through to get the elements out of the response
# print("{")
# for wl in worklogs:
#     for key, value in wl.items():
#         if key == "author":
#             for key, value in wl['author'].items():
#                 if key == "name":
#                     print(" \"worklog\": {\"" + key + "\": ", "\"" + value + "\",")
#         if key == "timeSpentSeconds":
#             print("\"" + key + "\": ", "" + str(value) + ",")
#         if key == "created":
#             print("\""+key+"\": ", "\""+ value + "\",")
#         if key == "updated":
#                 print("\"" + key + "\": ", "\"" + value + "\",")
#         if key == "started":
#             print("\"" + key + "\": ", "\"" + value + "\",")
#         if key == "id":
#             print("\""+key+"\": ", "\""+ value + "\"},")
# print("}")