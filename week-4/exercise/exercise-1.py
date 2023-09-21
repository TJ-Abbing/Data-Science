# Write a function that takes a postive integer number and returns its factorial.

# Declare function.
def factorial(number):
# Check if number is postive.
    if number < 0:
        print("The number is not postive.")
    # Check if number is 0.
    elif number == 0:
        print("The factorial of 0 is 1.")
    # Calculate factorial.
    else:
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        print(f"The factorial of {number} is {factorial}.")
# Call function.
factorial(5)