"""
Exercise 4:
Write a Python program that takes an integer as input from the user and prints whether it is a prime number or not.
"""

"""
A prime number is a number that is only divisible by 1 and itself. 
For example; 2, 3, 5, 7, 11, 13, 17, 19, 23, etc. are prime numbers.
"""

# Declare variables
integer = int(input("Enter an integer: "))

# Check if the integer is less than 2
if integer < 2:
    print("The number is not a prime number.")
else:
    # Assume number is prime until shown it is not. 
    is_prime = True
    # Check divisibility by all numbers up to the square root of the number.
    for i in range(2, int(integer ** 0.5) + 1):
        if (integer % i) == 0:
            is_prime = False
            break
    if is_prime:
        print("The number is a prime number.")
    else:
        print("The number is not a prime number.")