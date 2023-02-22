import requests
import os
import datetime as dt

NUTRITIONIX_APP_ID = os.environ.get('NUTRITIONIX_APP_ID')
NUTRITIONIX_APP_KEY = os.environ.get('NUTRITIONIX_APP_KEY')
SHEETY_AUTH = os.environ.get('SHEETY_AUTH')

NUTRITIONIX_URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_URL = ''

nutritionix_header = {
    'x-app-id' : NUTRITIONIX_APP_ID,
    'x-app-key' : NUTRITIONIX_APP_KEY,
    'Content-Type' : 'application/json'
}

nutritionix_body = {
    'query' : '',
    'gender' : 'male',
    'weight_kg' : 60.0,
    'height_cm' : 163,
    'age' : 29
}

query = input("What exercise you did today: ")

nutritionix_body['query'] = query

nutritionix_response = requests.post(url=NUTRITIONIX_URL, json=nutritionix_body, headers=nutritionix_header)
nutritionix_data = nutritionix_response.json()['exercises'][0]
sheety_header = {
    'Authorization' : f"Basic {SHEETY_AUTH}"
}

sheety_body  = {
    'workout' : {
        'date' : dt.datetime.now().strftime("%d/%m/%Y"),
        'time' : dt.datetime.now().strftime("%H:%M:%S"),
        'exercise' : nutritionix_data['name'].title(),
        'duration' : nutritionix_data['duration_min'],
        'calories' : nutritionix_data['nf_calories'],
    }
}
sheety_response = requests.post(url=SHEETY_URL, headers=sheety_header, json=sheety_body)
print(sheety_response.text)

# sheety_body = {

# }

