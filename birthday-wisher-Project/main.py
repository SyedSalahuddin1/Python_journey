# #################### Normal Starting Project ######################
import datetime as dt
import smtplib
import pandas
import random

my_email = "syedsalahuddin384@gmail.com"
my_password = "zhlrocmdpjympdvu"


now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
# new_dict = {new_key:new_value for (key,value) dict.items()}
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday:\n\n{contents}"
        )
