"""
Exercises 2:
Write a Python program that takes an integer as input from the user and prints 
whether it is even or odd.
"""

input = int(input("Enter an integer: "))
if input % 2 == 0:
    print("The integer you provided is an even number")
elif input % 2 != 0:
    print("The integer you provided is an odd number")