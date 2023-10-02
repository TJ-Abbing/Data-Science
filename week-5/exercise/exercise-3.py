"""
Write a function tuple_contians(my_tuple, value) that takes a tuple and a value as an input and 
returns True if the value is found in the tuple, otherwise returns False.
"""

# Declare function.
def tuple_contains(my_tuple, value):
    # Loop through the tuple.
    for element in my_tuple:
        # Check if the value is found in the tuple.
        if element == value:
            # Return True.
            return True
    # Return False.
    return False

# Call function.
print(tuple_contains((1, 2, 3, 4, 5), 3))
print(tuple_contains((1, 2, 3, 4, 5), 6))