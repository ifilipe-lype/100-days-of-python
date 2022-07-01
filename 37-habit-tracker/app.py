from email import header
from urllib import response
import requests


user_payload = {
    "token": "dfds9028423dfs09fd$#32dsf",
    "username": "hoshiko",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_payload = {
    "id": "example1",
    "name": "Example Graph #1",
    "unit": "Tries",
    "type": "int",
    "color": "shibafu"
}

graph_track_payload = {
    "date": "20220701",
    "quantity": "5",
}

PIXELA_API_USER_URL = "https://pixe.la/v1/users"
GRAPH_API_URL = f"{PIXELA_API_USER_URL}/{user_payload.get('username')}/graphs"

# Creates a user
#response = requests.post(url=PIXELA_API_USER_URL, json=user_payload)

# Creates a user's graph
# response = requests.post(url=GRAPH_API_URL, json=graph_payload, headers={
#     "X-USER-TOKEN": user_payload.get("token")
# });

# print(response.json())

# Creates a track on a graph
response = requests.post(url=f"{GRAPH_API_URL}/{graph_payload.get('id')}", json=graph_track_payload, headers={
    "X-USER-TOKEN": user_payload.get("token")
});

print(response.json())


