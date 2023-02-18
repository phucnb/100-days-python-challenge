import smtplib
from datetime import datetime
import random

def send_email(message) -> None:
    email = 'cs50.for.life@gmail.com'
    password = 'cbcknfofigqasncr'
    receiver = 'contact@phucnb.com'

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs=receiver, msg=f"Subject: {message} \n\n {message}")
    connection.close()

with open('quotes.txt', 'r') as file:
    data = file.readlines()

message = random.choice(data)
send_email(message)



