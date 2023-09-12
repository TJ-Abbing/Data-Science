"""
Exercises 5:
Write a Python program that takes two numbers as input from the user and prints whether 
their sum is greater than, less than, or equal to 10.
"""

input_number = int(input("Enter a number: "))

comparison = {
    input_number < 10 : "The input number is less than 10.",
    input_number == 10 : "The input number is equal to 10.",
    input_number > 10 : "The input number is greater than 10."
}

print(comparison.get(True, "Something went wrong."))