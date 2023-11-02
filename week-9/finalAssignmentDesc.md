# Final Assignment: Parking Management System

In this final assignment, you will create a Parking Management System using Python. The system consists of two Python files: parking_management.py and main_parking.py. The parking_management.py file contains classes and functions to manage car parking, while the main_parking.py script serves as a user interface to interact with the parking management system.

The system allows you to park cars, remove them, calculate parking fees, check available parking spaces, and view the parking status.

Your task is to complete and implement both Python files as described below:

## parking_management.py

This file contains the core logic and classes and function for managing a parking lot.

### Create a class Car with the following attributes:
Attributes:
1. license_plate (string): The license plate of the car.
2. brand (string): The brand of the car.
3. model (string): The model of the car.

### Create a class CarParking with the following attributes and methods:
Attributes:
1. capacity (integer): The maximum number of cars that can park in the lot.
2. parked_cars (dictionary): A dictionary to store the cars and their entry times.

Methods:
1. park_car(car): Parks a car in the lot if there is available space and records the entry time.
   - If the car is successfully parked:
     Output example:
     Car with license plate XYZ123 is parked.
   - If the car is already parked:
     Output example:
     Car with license plate XYZ123 is already parked!
   - If the parking lot is full:
     Output example:
     Parking lot is full. No available spaces.

2. remove_car(car): Removes a car from the lot, output a message, calculates the parking duration and returns it.
   - If the car is successfully removed:
     Output example:
     Car with license plate XYZ123 is exiting. Parking duration: 45.0 minutes.
     Note: remember that it still returns the parking duration.
   - If the car is not in the parking lot:
     Output example:
     Car with license plate XYZ789 is not in the parking lot.
     Note: remember that in this case it returns none.

3. available_spaces(): Returns the number of available parking spaces.

4. status(): Displays the current parking status.
   Output example:
   There are 3 cars parked out of 10.
   ABC123 entered at 12:30.
   XYZ789 entered at 12:45.
   LMN456 entered at 13:00.

5. Create a function called calculate_fee with 2 parameters, duration and rate which has a default value of 0.2. The function calculates the fee by multiplying the duration by the optional rate.

## main_parking.py

This script provides a user interface for interacting with the parking management system. It uses the classes and functions defined in parking_management.py.

- At the beginning, ask the user about the parking capacity and then create a parking lot with the desired capacity.

- The menu should allow the user to input their choice and perform the corresponding action. For example, when parking a car, the user should be prompted to enter the car's license plate, brand, and model.

- Ensure that the user is provided with appropriate feedback for each action, such as whether the car was parked successfully, the parking fee, available spaces, and the parking status.

- In the main function, implement a menu with the following options:
  1. Park a car
     - Example of User input:
       Enter your choice from 1 to 5: 1
       Enter the car's license plate: XYZ123
       Enter the car's brand: Ford
       Enter the car's model: Focus
     - Output:
       Car with license plate XYZ123 is parked.

  2. Remove a car and calculate the fee
     - Example of User input:
       Enter your choice from 1 to 5: 2
       Enter the car's license plate: XYZ123
     - Output (if the car is successfully removed):
       Car with license plate XYZ123 is exiting. Parking duration: 45.0 minutes.
       Parking fee: €9.0
     - Output (if the car is not in the parking lot):
       Car with license plate XYZ123 is not in the parking lot.

  3. Check available parking spaces
     - Output example:
       Available parking spaces: 7

  4. Check the parking status
     - Output example:
       There are 3 cars parked out of 10.
       ABC123 entered at 12:30.
       XYZ789 entered at 12:45.
       LMN456 entered at 13:00.

  5. Exit
     - Output:
       Exiting the parking management program.

## Usage Example

The parking_management.py file includes example usage to demonstrate how the classes should work. You can use this as a reference to understand how the system should behave.

## Instructions

1. Create a new Python file named parking_management.py and implement the Car class, CarParking class, and the calculate_fee function.

2. Create a new Python file named main_parking.py and implement the user interface to interact with the parking management system.

3. Test your system by running the main_parking.py script. Ensure that it provides the expected functionality and feedback for each menu option.

4. Submit both Python files (parking_management.py and main_parking.py).