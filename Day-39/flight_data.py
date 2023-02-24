class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, from_city, from_city_airport, to_city, to_city_airport, departure_date, return_from_city, return_from_city_airport, return_to_city, return_to_city_airport, return_date):
        self.price = price
        self.from_city = from_city
        self.to_city = to_city
        self.from_city_airport = from_city_airport
        self.to_city_airport = to_city_airport
        self.departure_date = departure_date
        self.return_from_city = return_from_city
        self.return_to_city = return_to_city
        self.return_from_city_airport = return_from_city_airport
        self.return_to_city_airport = return_to_city_airport
        self.return_date = return_date

    def print_flight(self):
        print("----------")
        print(f'price: {self.price}')
        print(f'from_city: {self.from_city}')
        print(f'to_city: {self.to_city}')
        print(f'from_city_airport: {self.from_city_airport}')
        print(f'to_city_airport: {self.to_city_airport}')
        print(f'departure_date: {self.departure_date}')
        print(f'return_from_city: {self.return_from_city}')
        print(f'return_to_city: {self.return_to_city}')
        print(f'return_from_city_airport: {self.return_from_city_airport}')
        print(f'return_to_city_airport: {self.return_to_city_airport}')
        print(f'return_date: {self.return_date}')