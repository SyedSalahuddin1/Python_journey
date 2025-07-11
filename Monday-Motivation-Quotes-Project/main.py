import smtplib
import datetime as dt
import random

my_gmail = "salahcoder73@gmail.com"
password = "khzrnbxddkfikpdd"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(from_addr=my_gmail, to_addrs="syedsalahuddin384@gmail.com",
                            msg=f"Subject: Monday Motivation\n\n{quote}"
                            )
    print(quote)
