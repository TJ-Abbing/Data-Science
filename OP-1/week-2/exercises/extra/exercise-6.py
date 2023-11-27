"""
Exercises 6:
Write a Python program that takes three integers as input from the user 
and prints the largest of them.
"""

# Declare variables.
input_integer_1 = int(input("Enter integer #1: "))
input_integer_2 = int(input("Enter integer #2: "))
input_integer_3 = int(input("Enter integer #3: "))

# Comparison dictionary.
comparison = {
    # Check if the first variable is greater than the second variable and the third variable.
    input_integer_1 > input_integer_2 and input_integer_1 > input_integer_3 : "The first integer is the largest.",
    # Check if the second variable is greater than the first variable and the third variable.
    input_integer_2 > input_integer_1 and input_integer_2 > input_integer_3 : "The second integer is the largest.",
    # Check if the third variable is greater than the first variable and the second variable.
    input_integer_3 > input_integer_1 and input_integer_3 > input_integer_2 : "The third integer is the largest."
}

# Print the first True value in the comparison dictionary. 
# If no True value is found, print an error message.
print(comparison.get(True, "Something went wrong."))