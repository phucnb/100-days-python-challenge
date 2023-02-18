import requests
import json


parameters = {
    'lat' : 4223.604400,
    'long' : -739.662560,
    'formatted' : 0
}
URL = 'https://api.sunrise-sunset.org/json'
response = requests.get(URL, parameters).json()

sunrise = response['results']['sunrise'].split("T")[1].split('+')[0]

print(f"Sunrise at your location will be at: {sunrise}")