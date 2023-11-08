# parking_management.py
from datetime import datetime

class Car:
    
    def __init__(self, license_plate, brand, model):
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
    
class CarParking:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.available_spots = capacity
        self.parked_cars = {}  

    def park_car(self, car):
            
        # Check whether there are any available spots left.
        if self.available_spots <= 0:
            print("Parking lot is full. No available spaces.")
        elif self.available_spots >= 1:
            # Check whether the car in question is already parked.
            for parked_car in self.parked_cars.values():
                if parked_car['license_plate'] == car.license_plate: 
                    print(f"Car with license plate {car.license_plate} is already parked!")
                    return
        # Park car if enough spots & not already parked.
        parked_at = datetime.now()
        self.available_spots -= 1
        
        car_dict = car.__dict__
        car_dict['parked_at'] = parked_at.strftime('%Y-%m-%d %H:%M:%S')
        
        self.parked_cars[car.license_plate] = car_dict
        print(f"Car with license plate {car.license_plate} is parked.")

    def remove_car(self, car):

        parked_cars_copy = self.parked_cars.copy()
        for parked_car in parked_cars_copy.values():
            if parked_car['license_plate'] == car.license_plate:
                parked_at = datetime.strptime(parked_car['parked_at'], '%Y-%m-%d %H:%M:%S')
                parking_duration_minutes = round((datetime.now() - parked_at).total_seconds() / 60)
                del self.parked_cars[car.license_plate]
                print(f"Car with license plate {car.license_plate} is exiting. Parking duration: {parking_duration_minutes} minutes.")
                return
        print(f"Car with license plate {car.license_plate} is not in the parking lot.")
    
    # def available_spaces(self):
    #     # TODO
    
    # def status(self):
    #     # TODO

# def calculate_fee(duration, rate=0.2):
#     # TODO


# Example usage:
if __name__ == "__main__":
    Hogeschool_parking = CarParking(10)

    car1 = Car("ABC123", "Toyota", "Camry")
    car2 = Car("XYZ789", "Honda", "Civic")
    car3 = Car("LMN456", "Ford", "Fiesta")

    Hogeschool_parking.park_car(car1)
    Hogeschool_parking.park_car(car2)

    print(Hogeschool_parking.parked_cars)
    
    # print(Hogeschool_parking.available_spaces())

    # Hogeschool_parking.park_car(car3)

    Hogeschool_parking.remove_car(car1)
    Hogeschool_parking.remove_car(car2)

    # Hogeschool_parking.status()

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