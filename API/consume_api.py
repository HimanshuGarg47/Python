import requests
import json

response = requests.get("https://api.stackexchange.com/2.3/comments?order=desc&sort=creation&site=stackoverflow")
print(response)
for data in response.json()['items']:
    print(data['owner']['profile_image'])
    # print(data["account_id"])