"""
Exercises 3:
Write a function that takes a number and returns True when it is a prime number, otherwise False.
"""

# Declare variable.
number = int(input("Enter a number: "))

# Declare function.
def is_prime(number):
    # Check if number is negative.
    if number < 0:
        print("Number must be positive.")
    # Check if number is 0.
    if number == 0:
        print("Number can't be equal to 0.")
    # Check if number is 1.
    if number == 1:
        print("Number can't be equal to 1.")
    # Check if number is prime.
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True	
    
# Call function.
print(is_prime(number))