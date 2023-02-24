import requests
import os
from flight_data import FlightData

SHEETY_URL = 'https://api.sheety.co/042ed18ddf2c6ac1259e9de409f78eb7/flight/prices'
SHEETY_AUTH = os.environ.get('SHEETY_AUTH')
SHEETY_HEADER = {
    'Authorization' : f'Basic {SHEETY_AUTH}'
}


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.cities_data = self.get_cities_data()

    def get_cities_data(self):
        cities_response = requests.get(url=SHEETY_URL, headers=SHEETY_HEADER)
        return cities_response.json()

    def update_iata(self, row_id, iata):
        body = {
            'price': {
                'iataCode' : iata
            }
        }
        response = requests.put(url=f'{SHEETY_URL}/{row_id}', headers=SHEETY_HEADER, json=body)
        response.raise_for_status()        

    def update_flight(self, flight=FlightData, row_id=int):
        body = {
            'price' : {
                'departureOn': flight.departure_date,
                'fromAirport': flight.from_city_airport,
                'fromCity': flight.from_city,
                'lowestPrice': flight.price,
                'returnFromAirport': flight.return_from_city_airport,
                'returnFromCity': flight.return_to_city,
                'returnOn': flight.return_date,
                'returnToAirport': flight.return_to_city_airport,
                'returnToCity': flight.return_to_city,
                'toAirport': flight.to_city_airport,
                'toCity': flight.to_city
                }
        }
        response = requests.put(url=f'{SHEETY_URL}/{row_id}', headers=SHEETY_HEADER, json=body)
        response.raise_for_status()      
        