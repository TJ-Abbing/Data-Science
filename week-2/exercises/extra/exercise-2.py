"""
Exercises 2:
Write a Python program that takes an integer as input_integer from the user and prints 
whether it is even or odd.
"""

# Declare variable.
input_integer = int(input("Enter an integer: "))

# Check if variable is an even number.
if input_integer % 2 == 0:
    print("The integer you provided is an even number")
# Check if variable is an odd number.
elif input_integer % 2 != 0:
    print("The integer you provided is an odd number")
# If neither of the above conditions are met, print an error message.
else:
    print("Something went wrong.")