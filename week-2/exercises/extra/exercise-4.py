"""
Exercises 4:
Write a Python program that takes two numbers as input and determines which one is larger. 
If the numbers are equal, print a message saying so. 
Use comparison operators and if-else statements to accomplish this.
"""

input_number_1 = int(input("Enter a number: "))
input_number_2 = int(input("Enter another number: "))

comparison = {
    input_number_1 == input_number_2 : "The numbers are equal.",
    input_number_1 > input_number_2 : "The first number is greater.",
    input_number_1 < input_number_2 : "The second number is greater."
}

print(comparison.get(True, "Something went wrong."))