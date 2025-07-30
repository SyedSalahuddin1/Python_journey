# requests.get()
# requests.post()
# requests.put()
# requests.delete()

import requests
from datetime import datetime

username = "salah10"
token = "1234qwert890"
graph_id = "graph26"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": token,
    "username": username,
    "agreeTermsofService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graphs_config = {
    "id": graph_id,
    "name": "SM Detox Graph",
    "unit": "day",
    "type": "int",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": token
}

# response = requests.post(url=graph_endpoint, json=graphs_config, headers=headers)
# print(response.text)

pixela_creation = f"{pixela_endpoint}/{username}/graphs/{graph_id}"

today = datetime(year=2025, month=7, day=29)

pixela_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2",
}
#
# response = requests.post(url=pixela_creation, json=pixela_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "3",
}

response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)
