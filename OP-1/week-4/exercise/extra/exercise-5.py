"""
Exercises 5:
Write a function that converts a decimal number to binary number.
"""

def decimal_to_binary(decimal_num):
    if decimal_num < 0:
        return "Negative numbers are not supported."

    if decimal_num == 0:
        return "0b0"

    binary_num = bin(decimal_num)
    return binary_num

# Test the function
decimal_num = int(input("Enter a decimal number: "))
binary_num = decimal_to_binary(decimal_num)
print(f"The binary representation of {decimal_num} is {binary_num}.")
