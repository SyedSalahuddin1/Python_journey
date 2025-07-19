import requests
import json

api_key = "9429457eba414edac06d616f02ccfbfe"
my_long = 77.594566
my_lat = 12.971599
owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": my_lat,
    "lon": my_long,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=owm_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        # print("Bring an umbrella.")
        will_rain = True
if will_rain:
    print("Bring an Umbrella.")

# with open("weather_data.json", "w") as data_file:
#     json.dump(weather_data, data_file, indent=4)

