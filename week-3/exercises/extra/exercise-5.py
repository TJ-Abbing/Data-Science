"""
Exercise 5:
Find the largest whole number (GCD: greatest common divisor) that evenly divides the two numbers.
"""

# TODO

# Declare variables
first_integer = int(input("Enter the first integer: "))
second_integer = int(input("Enter the second integer: "))

# Check if the number is negative
if first_integer < 0 or second_integer < 0:
    print("Sorry, GCD does not exist for negative integers. Please enter a positive integer.")
# Check if the number is 0
elif first_integer == 0 or second_integer == 0:
    print("The GCD of 0 and", second_integer, "is", second_integer)
# Calculate the GCD
else:
    # Assume the GCD is the smaller number until shown it is not.
    gcd = min(first_integer, second_integer)
    while gcd > 0:
        if first_integer % gcd == 0 and second_integer % gcd == 0:
            break
        gcd = gcd - 1
    print("The GCD of", first_integer, "and", second_integer, "is", gcd)