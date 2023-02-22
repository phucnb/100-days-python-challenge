import requests
import datetime as dt
import os
from twilio.rest import Client

OWT_URL = 'https://api.openweathermap.org/data/2.5/weather'

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ["TWILIO_TOKEN"]

LAT = os.environ.get("LAT")
LONG = os.environ.get("LON")
OWT_APPID = os.environ.get("OWT_API_KEY")
OWT_UNITS = 'metric'
PHONE = os.environ.get("PHONE_NUMBER")


OWT_PARAMETERS = {
    'lat' : LAT,
    'lon' : LONG,
    'appid' : OWT_APPID,
    'units' : OWT_UNITS
}

owt_response = requests.get(url=OWT_URL, params=OWT_PARAMETERS).json()

weather = owt_response['weather'][0]['main']
weather_description = owt_response['weather'][0]['description']
temp = owt_response['main']['temp']
feels_like = owt_response['main']['feels_like']
wind = owt_response['wind']['speed']


year = dt.datetime.now().year
month = dt.datetime.now().strftime('%B')
day = dt.datetime.now().day
weekdate = dt.datetime.now().strftime('%A')
hour = dt.datetime.now().hour
min = dt.datetime.now().minute

weather_msg = f"Today is {weekdate}, {day} {month}, {year} at {hour}:{min}\n\
    Current Weather is : {weather} ({weather_description}), {temp}°C and feels like {feels_like}°C. Wind is {wind} meter/sec."

client = Client(TWILIO_SID, TWILIO_TOKEN)

message = client.messages.create(
  body=weather_msg,
  from_="+12706388747",
  to=PHONE
)

