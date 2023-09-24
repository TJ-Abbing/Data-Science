"""
Exercises 2:
Write a function that takes a number and returns the sum of all the odd numbers from 1 to that number.
"""

# Declare variable.
number = int(input("Enter a number: "))

# Declare function.
def sum_odd_numbers(number):
    # Check if number is negative.
    if number < 0:
        print("Number must be positive.")
    # Check if number is 0.
    elif number == 0:
        print("Can't be equal to 0.")
    # Calculate sum of odd numbers.
    else:
        # Check if number is even.
        if number % 2 == 0:
            return
        else:
            sum = 0
            for i in range (1, number + 1, 2):
                sum += i
            print(f"The sum of odd numbers from 1 to {number} is {sum}.")
# Call function.
sum_odd_numbers(number)