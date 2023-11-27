"""
Exercises 1:
Write a function that takes a number and returns the sum of all the numbers from 1 to that number.
"""

# Declare variable.
number = int(input("Enter a number: "))

# Declare function.
def sum_of_numbers(number):
    # Check if number is positive.
    if number < 0:
        print("The number is not positive.")
    # Check if number is 0.
    elif number == 0:
        print("The sum of numbers from 1 to 0 is 0.")
    # Calculate sum of numbers.
    else:
        sum = 0
        for i in range (1, number + 1):
            sum += i
        print(f"The sum of numbers from 1 to {number} is {sum}.")
# Call function.
sum_of_numbers(number)