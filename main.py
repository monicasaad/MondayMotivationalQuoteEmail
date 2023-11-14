import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day_of_the_week = now.weekday()

# constants
MY_EMAIL = ""  # change to your email
MY_PASSWORD = ""  # set to generated app password from 2 step-verification settings

# send motivational quote if day of week is Monday
if day_of_the_week == 0:
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
        chosen_quote = random.choice(quotes)

    # connection = smtplib.SMTP("smtp.live.com")  # for hotmail
    # connection = smtplib.SMTP("smtp.mail.yahoo.com")  # for yahoo
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # for gmail, change for different domains
        connection.starttls()  # encrypt message if intercepted
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="", #set to forwarding email address
            msg=f"Subject:Motivational Monday Quote\n\n{chosen_quote}"
        )
