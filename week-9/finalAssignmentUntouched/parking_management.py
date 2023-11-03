# parking_management.py
from datetime import datetime

class Car:
    # TODO
    
class CarParking:
    def __init__(self, capacity):
        # TODO

    def park_car(self, car):
        # TODO

    def remove_car(self, car):
        # TODO

    def available_spaces(self):
        # TODO
    
    def status(self):
        # TODO

def calculate_fee(duration, rate=0.2):
    # TODO


# Example usage:
if __name__ == "__main__":
    Hogeschool_parking = CarParking(10)

    car1 = Car("ABC123", "Toyota", "Camry")
    car2 = Car("XYZ789", "Honda", "Civic")
    car3 = Car("LMN456", "Ford", "Fiesta")

    Hogeschool_parking.park_car(car1)
    Hogeschool_parking.park_car(car2)
    
    print(Hogeschool_parking.available_spaces())

    Hogeschool_parking.park_car(car3)

    Hogeschool_parking.remove_car(car1)
    Hogeschool_parking.remove_car(car2)

    Hogeschool_parking.status()

# This is the expected output after running this file itself.
"""
Car with license plate ABC123 is parked.
Car with license plate XYZ789 is parked.
8
Car with license plate LMN456 is parked.
Car with license plate ABC123 is exiting. Parking duration: 0.0 minutes.
Car with license plate XYZ789 is exiting. Parking duration: 0.0 minutes.
There are 1 cars parked out of 10.
LMN456 entered at 15:55.
"""