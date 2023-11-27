"""
Exercise 5:
Write a Python function that takes two lists as input and returns a set containing the common 
elements between the two lists.
"""

# Declare function.
def compareLists(list_1, list_2):

    # Convert lists to sets.
    set_1 = set(list_1)
    set_2 = set(list_2)

    # Return the intersection of the two sets.
    return set_1.intersection(set_2)

# Call function.
print(compareLists([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))