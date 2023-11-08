# main_parking.py
from parking_management import Car, CarParking, calculate_fee

def main():
    print("========== Set Capacity ==========")
    hr_parking_lot = CarParking(int(input("Enter the capacity of the parking lot: ")))

    while True:
        print("\nParking Management Menu:")
        print("[1] Park a car")
        print("[2] Remove a car and calculate the fee")
        print("[3] Check available parking spaces")
        print("[4] Check the parking status")
        print("[5] Exit")

        choice = input("Enter your choice from 1 to 5: ")

        if choice == "1":
            license_plate = input("Enter the car's license plate number: ")
            brand = input("Enter the car's brand: ")
            model = input("Enter the car's model: ")
            car = Car(license_plate, brand, model)
            hr_parking_lot.park_car(car)
        elif choice == "2":
            license_plate = input("Enter the car's license plate number: ")
            car = Car(license_plate, "", "")
            parking_duration = hr_parking_lot.remove_car(car)
            if parking_duration is not None:
                fee = calculate_fee(parking_duration, rate=0.2)
                print(f"Fee: €{fee:.2f}")
        elif choice == "3":
            print(f"Available parking spaces: {hr_parking_lot.available_spaces()}")
        elif choice == "4":
            hr_parking_lot.status()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()