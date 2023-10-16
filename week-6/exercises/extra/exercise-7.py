"""
Exercise 7:
Write a Python function that takes a list as input and returns a new list with duplicates removed.
"""

# Declare function.
def remove_duplicates(list):

    # Declare empty list.
    duplicate_free_list = []

    # Iterate over list.
    for i in list:

        # Check if already exists in new list.
        if i in duplicate_free_list:
            print(f"The instance {i} is already in the duplicate free list, meaning that {i} will not be added.")
        elif i not in duplicate_free_list:
            duplicate_free_list.append(i)

    # Return duplicate free list.
    return duplicate_free_list

# Declare list.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]

# Call function.
print(remove_duplicates(list))