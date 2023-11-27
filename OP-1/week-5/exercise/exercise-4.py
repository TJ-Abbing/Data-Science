"""
Write a function double_odd_numbers(number) that takes a list of numbers as input and returns
a new list where the odd numbers are doubled, and the even numbers remain unchanged.
"""

# Declare function.
def double_odd_numbers(list_of_numbers):   
    # Declare variable to hold the doubled odd numbers.
    doubled_odd_numbers = []
    # Loop through the list of numbers.
    for number in list_of_numbers:
        # Check if the number is odd.
        if number % 2 != 0:
            # Double the odd number.
            doubled_odd_numbers.append(number * 2)
        # Check if the number is even.
        elif number % 2 == 0:
            # Add the even number to the doubled odd numbers.
            doubled_odd_numbers.append(number)
    # Return the doubled odd numbers.
    return doubled_odd_numbers

# Call function.
print(double_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))