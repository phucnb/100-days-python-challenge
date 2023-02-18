import requests
import json
import datetime as dt
import time
import smtplib
LONG = -79.662560
LAT = 43.604400

PARAMETER = {
    'lat' : LAT,
    'long' : LONG,
    'formatted' : 0
}
URL = 'https://api.sunrise-sunset.org/json'
ISS_URL = 'http://api.open-notify.org/iss-now.json'

EMAIL = 'cs50.for.life@gmail.com'
PASSWORD = 'cbcknfofigqasncr'
RECEIVER = 'contact@phucnb.com'

def is_iss_here():
    response = requests.get(url=ISS_URL).json()
    iss_long = response['iss_position']['longitude']
    iss_lat = response['iss_position']['latitude']
    return True if (LONG - 5 <= float(iss_long) <= LONG + 5) and (LAT - 5 <= float(iss_lat) <= LAT + 5) else False

def is_night() -> bool:
    response = requests.get(url=URL, params=PARAMETER).json()
    sunrise = response['results']['sunrise'].split("T")[1].split('+')[0].split(":")[0]
    sunset = response['results']['sunset'].split("T")[1].split('+')[0].split(":")[0]
    now = dt.datetime.now().hour
    
    return True if now > int(sunset) or now <= int(sunrise) else False
       
while True:
    time.sleep(60)
    if is_iss_here() and is_night():
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=RECEIVER, msg=f"Subject: ISS OUT SIDE \n\nISS OUTSIDE")
            connection.close()
            print("Email Sent")


