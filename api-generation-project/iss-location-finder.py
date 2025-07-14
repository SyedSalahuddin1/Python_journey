# import requests
# from datetime import datetime
# import smtplib
# import time
#
#
# MY_LAT = 15.317277
# MY_LONG = 75.713890
# MY_EMAIL = "syedsalahuddin384@gmail.com"
# MY_PASSWORD = "Qwertyuiop@90#"
#
#
# def is_iss_overhead():
#     response = requests.get(url="http://api.open-notify.org/iss-now.json")
#     response.raise_for_status()
#     data = response.json()
#
#     iss_latitude = float(data["iss_position"]["latitude"])
#     iss_longitude = float(data["iss_position"]["longitude"])
#
# # Your position is within +5 or -5 degrees of the ISS position.
#     if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
#         return True
#
#
# def is_night():
#     parameters = {
#         "lat": MY_LAT,
#         "lng": MY_LONG,
#         "formatted": 0,
#     }
#
#     response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
#     response.raise_for_status()
#     data = response.json()
#     sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
#     sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
#
#     time_now = datetime.now().hour
#
#     if time_now >= sunset or time_now <= sunrise:
#         return True
#
#
# while True:
#     time.sleep(60)
#     if is_iss_overhead() and is_night():
#         connection = smtplib.SMTP("smtp.gmail.com")
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=MY_EMAIL,
#             msg="Subject:LOOK UP \n\n The ISS is above you in the sky."
#         )
#
#
#
# # global sunrise
# # global sunset
# # print(sunrise)
# # print(sunset)
#
# # print(time_now)
#
# # If the ISS is close to my current position
# # ,and it is currently dark
# # Then send me an email to tell me to look up.
# # BONUS: run the code every 60 seconds.
#

import requests
from datetime import datetime
import smtplib
import time
import pytz

MY_LAT = 15.317277
MY_LONG = 75.713890
MY_EMAIL = "syedsalahuddin384@gmail.com"
MY_PASSWORD = "Qwertyuiop@90#"

ist = pytz.timezone("Asia/Kolkata")


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    # Convert sunrise and sunset from UTC to IST
    sunrise_utc = datetime.fromisoformat(data["results"]["sunrise"])
    sunset_utc = datetime.fromisoformat(data["results"]["sunset"])
    sunrise_ist = sunrise_utc.astimezone(ist).hour
    sunset_ist = sunset_utc.astimezone(ist).hour

    time_now = datetime.now(ist).hour

    if time_now >= sunset_ist or time_now <= sunrise_ist:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:LOOK UP \n\nThe ISS is above you in the sky."
        )
