"""
Write a function that takes a list of integers as an argument and returns the sum of the even 
integers in the list.
"""

# Declare function.
def sum_even_integers(list_of_integers):
    # Declare variable to hold the sum of the even integers.
    sum_of_even_integers = 0
    # Loop through the list of integers.
    for integer in list_of_integers:
        # Check if the integer is even.
        if integer % 2 == 0:
            # Add the integer to the sum of the even integers.
            sum_of_even_integers += integer
    # Return the sum of the even integers.
    return sum_of_even_integers

# Call function.
print(sum_even_integers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))