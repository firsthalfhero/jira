
import jira_connect
import json
from mongo_connector import mongo_insert_one_worklog


def check_keys_match(issue_key_api, issue_key_value):
    if issue_key_value == issue_key_api:
        pass
    else:
        print("Key from query and api do not match")


def get_issue_by_key(issue_key_value):
    # #TODO get key from search make it dynamic
    # issue_key_value = "AMR-15"

    query = "issue/" + issue_key_value + "?renderedFields=\"worklogs\""

    jira_instance = "ADR"

    data = jira_connect.jira_connect_method(jira_instance, query)
    data = json.loads(data)

    issue_key_api = data['key']
    check_keys_match(issue_key_api, issue_key_value)

    worklogs = data['fields']['worklog']['worklogs']

    for worklogList in worklogs:
        dict(worklogList)
        # get values
        timeSpent = [(value) for keys, value in worklogList.items() if keys == 'timeSpent']
        created = [(value) for keys, value in worklogList.items() if keys == 'created']
        updated = [(value) for keys, value in worklogList.items() if keys == 'updated']
        started = [(value) for keys, value in worklogList.items() if keys == 'started']
        timeSpentSeconds = [(keys, value) for keys, value in worklogList.items() if keys == 'timeSpentSeconds']
        _id = [(value) for keys, value in worklogList.items() if keys == 'id']
        _id = str(_id)
        # get the name of the author
        author = [(keys, value) for keys, value in worklogList.items() if keys == 'author']
        author = dict(author)
        name = (author['author']['name'])

        # return values
        record = (dict({
            # _id, name, created, updated, started, timeSpent, timeSpentSeconds}))
            'key': issue_key_api,
            # '_id': _id,
            'name': name,
            'created': created,
            'updated': updated,
            'started': started,
            'timeSpent': timeSpent,
            'timeSpentSeconds': timeSpentSeconds
        }))
        print(record)

        response = mongo_insert_one_worklog(record)
        print(response)
        continue
    return 'Done'


print(get_issue_by_key('AMR-15'))
