"""
Exercise 1:
Write a Python program that takes a positive integer as input from the user and prints the factorial of that number.
"""

# Declare variables
positive_integer = int(input("Enter a positive integer (number): "))
factorial = 1

# Check if the number is negative
if positive_integer < 0:
    print("Sorry, factorial does not exist for negative integers. Please enter a positive integer.")
# Check if the number is 0
elif positive_integer == 0:
    print("The factorial of 0 is 1.")
# Calculate the factorial
else:
    for i in range(1, positive_integer + 1): 
        factorial = factorial * i
    print("The factorial of", positive_integer, "is", factorial)