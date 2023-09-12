"""
Exercises 2:
Write a Python program that takes an integer as input_integer from the user and prints 
whether it is even or odd.
"""

input_integer = int(input("Enter an integer: "))
if input_integer % 2 == 0:
    print("The integer you provided is an even number")
elif input_integer % 2 != 0:
    print("The integer you provided is an odd number")
else:
    print("Something went wrong.")