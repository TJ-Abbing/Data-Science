"""
Exercise 2:
Calculate the sum of the digits of a positive number.
Ex: 1234 has 10 as sum of its digits ( 1+2+3+4=10 )
HINT: Chapter 3, BA8 and BA9 (break a number exercises) can give you inspiration for this exercise. In this exercise you will need a loop because you will need to find a general solution for breaking a number ( breaking a number with any number of characters )

Suggestion: Try solvnig this using % and //
"""

# Declare variables
positive_integer = int(input("Enter a positive integer (number): "))
sum_of_digits = 0

# Check if the number is negative
if positive_integer < 0:
    print("Sorry, sum of digits does not exist for negative integers. Please enter a positive integer.")
# Check if the number is 0
elif positive_integer == 0:
    print("The sum of digits of 0 is 0.")
# Calculate the sum of digits
else:
    while positive_integer > 0:
        sum_of_digits = sum_of_digits + positive_integer % 10
        positive_integer = positive_integer // 10
    print("The sum of digits is", sum_of_digits)