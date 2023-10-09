"""
Exercises 4:
Write a program using the previous function to print twin primes less than 1000. 
If two consecutive odd numbers are both prime then they are known as twin primes
"""

# Function to check if a number is prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Find and print twin primes less than 1000
for num in range(3, 1000, 2):  # Start from 3 and only consider odd numbers
    if is_prime(num) and is_prime(num + 2):
        print(f"Twin primes: {num} and {num + 2}")