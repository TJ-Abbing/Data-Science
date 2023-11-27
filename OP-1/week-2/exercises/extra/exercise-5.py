"""
Exercises 5:
Write a Python program that takes two numbers as input from the user and prints whether 
their sum is greater than, less than, or equal to 10.
"""

# Declare variable.
input_number = int(input("Enter a number: "))

# Comparison dictionary.
comparison = {
    # Check if the variable is less than 10.
    input_number < 10 : "The input number is less than 10.",
    # Check if the variable is equal to 10.
    input_number == 10 : "The input number is equal to 10.",
    # Check if the variable is greater than 10.
    input_number > 10 : "The input number is greater than 10."
}

# Print the first True value in the comparison dictionary.
# If no True value is found, print an error message.
print(comparison.get(True, "Something went wrong."))