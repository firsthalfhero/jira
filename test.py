import json

x = ({
            "worklog":{
                 "startAt":0,
                 "maxResults":20,
                 "total":16,
                 "worklogs":[
                    {
                       "self":"https://adrenalinmedia.atlassian.net/rest/api/2/issue/49678/worklog/29629",
                       "author":{
                          "self":"https://adrenalinmedia.atlassian.net/rest/api/2/user?accountId=557058%3A1c199c5f-1d94-465d-b32a-ac4591d36733",
                          "name":"TarynSligh",
                          "key":"tarynsligh",
                          "accountId":"557058:1c199c5f-1d94-465d-b32a-ac4591d36733",
                          "emailAddress":"taryn.sligh@adrenalinmedia.com.au",
                          "avatarUrls":{
                             "48x48":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:1c199c5f-1d94-465d-b32a-ac4591d36733/0f98855f-9536-41df-9b24-612ef457d06a/128?size=48&s=48",
                             "24x24":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:1c199c5f-1d94-465d-b32a-ac4591d36733/0f98855f-9536-41df-9b24-612ef457d06a/128?size=24&s=24",
                             "16x16":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:1c199c5f-1d94-465d-b32a-ac4591d36733/0f98855f-9536-41df-9b24-612ef457d06a/128?size=16&s=16",
                             "32x32":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:1c199c5f-1d94-465d-b32a-ac4591d36733/0f98855f-9536-41df-9b24-612ef457d06a/128?size=32&s=32"
                          },
                          "displayName":"TarynSligh",
                          "timeZone":"Australia/Sydney",
                          "accountType":"atlassian"
                       },
                       "updateAuthor":{
                          "self":"https://adrenalinmedia.atlassian.net/rest/api/2/user?accountId=557058%3A1c199c5f-1d94-465d-b32a-ac4591d36733",
                          "name":"TarynSligh",
                          "key":"tarynsligh",
                          "accountId":"557058:1c199c5f-1d94-465d-b32a-ac4591d36733",
                          "emailAddress":"taryn.sligh@adrenalinmedia.com.au",
                          "avatarUrls":{
                             "48x48":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:1c199c5f-1d94-465d-b32a-ac4591d36733/0f98855f-9536-41df-9b24-612ef457d06a/128?size=48&s=48",
                             "24x24":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:1c199c5f-1d94-465d-b32a-ac4591d36733/0f98855f-9536-41df-9b24-612ef457d06a/128?size=24&s=24",
                             "16x16":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:1c199c5f-1d94-465d-b32a-ac4591d36733/0f98855f-9536-41df-9b24-612ef457d06a/128?size=16&s=16",
                             "32x32":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:1c199c5f-1d94-465d-b32a-ac4591d36733/0f98855f-9536-41df-9b24-612ef457d06a/128?size=32&s=32"
                          },
                          "displayName":"TarynSligh",
                          "timeZone":"Australia/Sydney",
                          "accountType":"atlassian"
                       },
                       "comment":"UNSW country landing pages review",
                       "created":"2017-10-23T01:04:16.458-0500",
                       "updated":"2017-10-23T01:04:16.458-0500",
                       "started":"2017-10-23T01:03:00.000-0500",
                       "timeSpent":"20m",
                       "timeSpentSeconds":1200,
                       "id":"29629",
                       "issueId":"49678"
                    },
                    {
                       "self":"https://adrenalinmedia.atlassian.net/rest/api/2/issue/49678/worklog/30635",
                       "author":{
                          "self":"https://adrenalinmedia.atlassian.net/rest/api/2/user?accountId=557058%3A1c199c5f-1d94-465d-b32a-ac4591d36733",
                          "name":"TarynSligh",
                          "key":"tarynsligh",
                          "accountId":"557058:1c199c5f-1d94-465d-b32a-ac4591d36733",
                          "emailAddress":"taryn.sligh@adrenalinmedia.com.au",
                          "avatarUrls":{
                             "48x48":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:1c199c5f-1d94-465d-b32a-ac4591d36733/0f98855f-9536-41df-9b24-612ef457d06a/128?size=48&s=48",
                             "24x24":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:1c199c5f-1d94-465d-b32a-ac4591d36733/0f98855f-9536-41df-9b24-612ef457d06a/128?size=24&s=24",
                             "16x16":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:1c199c5f-1d94-465d-b32a-ac4591d36733/0f98855f-9536-41df-9b24-612ef457d06a/128?size=16&s=16",
                             "32x32":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:1c199c5f-1d94-465d-b32a-ac4591d36733/0f98855f-9536-41df-9b24-612ef457d06a/128?size=32&s=32"
                          },
                          "displayName":"TarynSligh",
                          "timeZone":"Australia/Sydney",
                          "accountType":"atlassian"
                       },
                       "updateAuthor":{
                          "self":"https://adrenalinmedia.atlassian.net/rest/api/2/user?accountId=557058%3A1c199c5f-1d94-465d-b32a-ac4591d36733",
                          "name":"TarynSligh",
                          "key":"tarynsligh",
                          "accountId":"557058:1c199c5f-1d94-465d-b32a-ac4591d36733",
                          "emailAddress":"taryn.sligh@adrenalinmedia.com.au",
                          "avatarUrls":{
                             "48x48":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:1c199c5f-1d94-465d-b32a-ac4591d36733/0f98855f-9536-41df-9b24-612ef457d06a/128?size=48&s=48",
                             "24x24":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:1c199c5f-1d94-465d-b32a-ac4591d36733/0f98855f-9536-41df-9b24-612ef457d06a/128?size=24&s=24",
                             "16x16":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:1c199c5f-1d94-465d-b32a-ac4591d36733/0f98855f-9536-41df-9b24-612ef457d06a/128?size=16&s=16",
                             "32x32":"https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:1c199c5f-1d94-465d-b32a-ac4591d36733/0f98855f-9536-41df-9b24-612ef457d06a/128?size=32&s=32"
                          },
                          "displayName":"TarynSligh",
                          "timeZone":"Australia/Sydney",
                          "accountType":"atlassian"
                       },
                       "comment":"NBN go App review and test \r\nInvision uploads ",
                       "created":"2017-11-28T16:55:14.462-0600",
                       "updated":"2017-11-28T16:55:14.462-0600",
                       "started":"2017-11-28T16:54:00.000-0600",
                       "timeSpent":"25m",
                       "timeSpentSeconds":1500,
                       "id":"30635",
                       "issueId":"49678"
                    }
                ]
        }
})

x = json.loads(x)
#
worklogs = x['worklogs']

for worklogList in worklogs:
    dict(worklogList)
    timeSpent = [(keys, value) for keys, value in worklogList.items() if keys == 'timeSpent']

    author = [(keys, value) for keys, value in worklogList.items() if keys == 'author']
    author = dict(author)
    name = (author['author']['name'])

    print(timeSpent, name)

# print(x)
#
# for key, value in x:
#     wl = {}
#     if key == 'name':
#        wl = {"name": value}


#
#
# for wl in x.find_all('name'):
#     name = {
#         "name":    wl.get('name'),
#     }
#     wl.append(name)
#

