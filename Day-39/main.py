from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
import datetime as dt
from dateutil.relativedelta import *


data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.cities_data['prices']

# Check if iata is empty, then update
for city in sheet_data:
    if not city['iataCode']:
        # Update
        city['iataCode'] = flight_search.search_iata(city['city'])
        data_manager.update_iata(row_id=city['id'], iata=city['iataCode'])
    

tomorrow = dt.datetime.now().date() + dt.timedelta(days=1)
six_month_from_tomorrow = tomorrow + relativedelta(months=+6)
flight_data = []
for dest in sheet_data:
    flight = flight_search.search_flight_to(city=dest['iataCode'], date_from=tomorrow, date_to=six_month_from_tomorrow)
    if dest['lowestPrice'] > flight.price:
        data_manager.update_flight(flight=flight, row_id=dest['id'])



