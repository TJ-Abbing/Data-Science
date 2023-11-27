"""
Exercises 4:
Write a Python program that takes two numbers as input and determines which one is larger. 
If the numbers are equal, print a message saying so. 
Use comparison operators and if-else statements to accomplish this.
"""

# Declare variables.
input_number_1 = int(input("Enter a number: "))
input_number_2 = int(input("Enter another number: "))

# Comparison dictionary.
comparison = {
    # Check if the first variable is greater than the second variable.
    input_number_1 > input_number_2 : "The first number is greater.",
    # Check if the first variable is equal to the second variable.
    input_number_1 == input_number_2 : "The numbers are equal.",
    # Check if the first variable is less than the second variable.
    input_number_1 < input_number_2 : "The second number is greater."
}

# Print the first True value in the comparison dictionary. 
# If no True value is found, print an error message.
print(comparison.get(True, "Something went wrong."))