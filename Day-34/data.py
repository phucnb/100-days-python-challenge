import requests
import json


URL = 'https://opentdb.com/api.php'

NUMBER_OF_QUESTIONS = 10
TYPE = 'boolean'

PARAMETERS = {
    'amount' : NUMBER_OF_QUESTIONS,
    'type' : TYPE
}

response = requests.get(url=URL, params=PARAMETERS)
# print(json.dumps(response.json(), indent=2))
question_data = response.json()['results']

