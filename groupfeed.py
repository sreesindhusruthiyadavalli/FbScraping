import facebook
import requests
token = 'EAANUNvRDB44BANKv4qNhc510QAZClA0FmHsi1lPh9dX4SZBSTzwjIqsSI3ejxZA2SO8sFNOjQfHXn4bl0nBvPn7ZAO4hISFwfzkvIJAQZB8o6UlASGIT2ZABQlg9L71m25fWwQc7DxP4MpFZCBN6AXLGz9OxhXhPBBYavemb2NkmVa7QnCPq87HFRpnV6r3l0oZD'
graph = facebook.GraphAPI(access_token=token )
#version="2.11"
group_id = '349554945138653'

#groups_feed = graph.get_object(id=group_id)


groups_feed = requests.get("https://graph.facebook.com/v2.11/" + group_id +"/feed?access_token=" + token)
print(groups_feed.json())
