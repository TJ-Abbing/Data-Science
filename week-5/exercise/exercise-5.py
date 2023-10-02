""""
Write a function that finds and returns the largest element in a list of numbers.
"""

# Declare function.
def largest_element(list_of_numbers):
    # Declare variable to hold the largest element.
    largest_element = list_of_numbers[0]
    # Loop through the list of numbers.
    for number in list_of_numbers:
        # Check if the number is larger than the largest element.
        if number > largest_element:
            # Set the largest element to the number.
            largest_element = number
    # Return the largest element.
    return largest_element

# Declare list of numbers.
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Call function.
print(largest_element(list_of_numbers))