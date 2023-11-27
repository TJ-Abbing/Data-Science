"""
Exercise 6:
Write a Python function that takes a list of dictionaries and a key as input, and returns a new 
list containing only the dictionaries that have the given key.
"""

# Declare function.
def filterDictList(dict_list, key):

    # Declare empty list.
    filtered_list = []

    # Iterate over list.
    for dictionary in dict_list:

        # Check if key exists in dictionary.
        if key in dictionary:

            # Append dictionary to filtered list.
            filtered_list.append(dictionary)

    # Return filtered list.
    return filtered_list

# Call function.
print(filterDictList([{"name": "John", "age": 23}, {"name": "Jane", "age": 25}], "age"))