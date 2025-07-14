# import requests
# from _datetime import datetime
# MY_LAT = 15.317277
# MY_LONG = 75.713890
#
# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LONG,
#     "formatted": 0,
# }
#
# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()
# # print(data)
#
# sunrise = data["results"]["sunrise"]
# sunset = data["results"]["sunset"]
#
#
# sun_rise_set = (sunrise, sunset)
# print(sunrise)
# print(sunrise.split("T")[1].split(":")[0])
# print(sunset.split("T")[1].split(":")[0])
# time_now = datetime.now()
#
# print(time_now)


import requests
from datetime import datetime
import pytz

MY_LAT = 12.971599
MY_LONG = 77.594566

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

# Convert UTC to IST
utc = pytz.utc
ist = pytz.timezone("Asia/Kolkata")

sunrise_ist = datetime.fromisoformat(sunrise).astimezone(ist)
sunset_ist = datetime.fromisoformat(sunset).astimezone(ist)

print("Sunrise (IST):", sunrise_ist.time())
print("Sunset  (IST):", sunset_ist.time())

# Current time in IST
print("Now      (IST):", datetime.now(ist).time())
