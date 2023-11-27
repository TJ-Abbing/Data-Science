# File: parking_management.py.

# Import statements.
from datetime import datetime

# Declare classes.
class Car:
    # Declare constructor.
    def __init__(self, license_plate, brand, model):
        self.license_plate = license_plate
        self.brand = brand
        self.model = model

class CarParking:
    # Declare constructor.
    def __init__(self, capacity):
        self.capacity = capacity
        self.available_spots = capacity
        self.parked_cars = {}

    # Declare methods.
    def park_car(self, car):
        if self.available_spots <= 0:
            print("Parking lot is full. No available spaces.")
        else:
            if car.license_plate in self.parked_cars:
                print(f"Car with license plate {car.license_plate} is already parked!")
            else:
                parked_at = datetime.now()
                self.available_spots -= 1
                car_dict = car.__dict__
                car_dict['parked_at'] = parked_at.strftime('%Y-%m-%d %H:%M:%S')
                self.parked_cars[car.license_plate] = car_dict
                print(f"Car with license plate {car.license_plate} is parked.")

    def remove_car(self, car):
        if car.license_plate in self.parked_cars:
            parked_at = datetime.strptime(self.parked_cars[car.license_plate]['parked_at'], '%Y-%m-%d %H:%M:%S')
            parking_duration_minutes = round((datetime.now() - parked_at).total_seconds() / 60)
            del self.parked_cars[car.license_plate]
            self.available_spots += 1
            print(f"Car with license plate {car.license_plate} is exiting. Parking duration: {parking_duration_minutes} minutes.")
            return parking_duration_minutes
        else:
            print(f"Car with license plate {car.license_plate} is not in the parking lot.")
            return None

    def available_spaces(self):
        return self.available_spots

    def status(self):
        print(f"There are {len(self.parked_cars)} cars parked out of {self.capacity}.")
        for car in self.parked_cars.values():
            print(f"{car['license_plate']} entered at {car['parked_at']}")

# Declare functions.
def calculate_fee(duration, rate=0.2):
    fee = duration * rate
    return fee