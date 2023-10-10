"""
Exercises 5:
Write a function that takes in a list of numbers as input and returns the sum of the squares of all the even numbers in the list.
"""

# Declare list.
list_numbers = [1, 2, 3, 4]

# Declare function.
def returnSquaresOfEvenNumbers(list_numbers):
    sum = 0
    for number in list_numbers:
        if number % 2 == 0:
            sum += number ** 2
    return sum

# Call function.
print(returnSquaresOfEvenNumbers(list_numbers))