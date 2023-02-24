import requests, os, datetime
from pprint import pprint
from flight_data import FlightData

TEQUILA_APIKEY = os.environ.get('TEQUILA_APIKEY')
TEQUILA_HEADER = {
    'apikey' : TEQUILA_APIKEY
    }
TEQUILA_URL = 'https://api.tequila.kiwi.com'
FROM = 'LON'
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def search_iata(self, city_name):
        tequila_body = {
            'term' : city_name
        }

        response = requests.get(url=f'{TEQUILA_URL}/locations/query', headers=TEQUILA_HEADER, params=tequila_body)
        response.raise_for_status
        data = response.json()['locations'][0]
        return data['code']

    def search_flight_to(self, city=str, date_from=datetime, date_to=datetime):
        tequila_body = {
            'fly_from' : FROM,
            'fly_to' : city,
            'date_from' : date_from.strftime("%d/%m/%Y"),
            'date_to' : date_to.strftime("%d/%m/%Y"),
            'nights_in_dst_from' : '7',
            'nights_in_dst_to' : '30',
            'flight_type' : 'round',
            'one_for_city' : '1',
            'max_stopovers' : '0',
            'curr' : 'GBP',
        }

        response = requests.get(url=f"{TEQUILA_URL}/v2/search", headers=TEQUILA_HEADER, params=tequila_body)
        response.raise_for_status()
        data = response.json()['data'][0]
        flight = FlightData(
            price=data['price'],
            from_city=data['route'][0]['cityFrom'],
            to_city=data['route'][0]['cityTo'],
            from_city_airport=data['route'][0]['flyFrom'],
            to_city_airport=data['route'][0]['flyTo'],
            departure_date=data['route'][0]['local_departure'].replace('T', ' ').replace('.000Z',''),
            return_from_city=data['route'][1]['cityFrom'],
            return_to_city=data['route'][1]['cityTo'],
            return_from_city_airport=data['route'][1]['flyFrom'],
            return_to_city_airport=data['route'][1]['flyTo'],
            return_date=data['route'][1]['local_departure'].replace('T', ' ').replace('.000Z',''),
            )
        return flight
    