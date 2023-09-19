"""
Exercise 6:
Find the Lowest Common Multiple (LCM) of the two numbers.
The LCM is the smallest positive integer that is divisible by both numbers.
HINT: 
1. the idea is to first find the maximum of the two numbers, and consider it as lcm. 
2. test that lcm is divisible by both numbers, if not increase lcm by adding maximum number and repeat step 2
"""

# Declare variables.
first_integer = int(input("Enter the first integer: "))
second_integer = int(input("Enter the second integer: "))

# Find the maximum of the two integers.
lcm = max(first_integer, second_integer)

# Check if the number is negative.
if first_integer < 0 or second_integer < 0:
    print("Sorry, LCM does not exist for negative integers. Please enter a positive integer.")
# Check if the number is 0.
if first_integer == 0 or second_integer == 0:
    print("The LCM of 0 and", second_integer, "is", second_integer)
# Calculate the LCM.
else:
    while lcm > 0:
        if lcm % first_integer == 0 and lcm % second_integer == 0:
            break
        lcm = lcm + 1
    print("The LCM of", first_integer, "and", second_integer, "is", lcm)