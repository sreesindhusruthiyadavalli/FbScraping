import facebook
import requests
token = '' #user access token here
graph = facebook.GraphAPI(access_token=token )
#version="2.11"
group_id = '349554945138653'

#groups_feed = graph.get_object(id=group_id)


groups_feed = requests.get("https://graph.facebook.com/v2.11/" + group_id +"/feed?access_token=" + token)
print(groups_feed.json()) # to get the feed data per page

# To give the name, value pair for each feed.
lst = ['story', 'id' , 'updated_time', 'message']

for x in groups_feed.json()['data']:
    try:
        for y in lst:
            print (y + ":" + x[y])
    except KeyError as e:
        print(e)
