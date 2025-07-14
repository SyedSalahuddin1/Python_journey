import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)\
# print(response.text)
response.raise_for_status()
data = response.json()
# print(data)

iss_longitude = data["iss_position"]["longitude"]
iss_latitude = data["iss_position"]["latitude"]

iss_position = (iss_latitude, iss_longitude)

print(iss_position)
