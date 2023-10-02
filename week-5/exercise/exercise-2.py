"""
Write a function that takes a list of strings as an argument and returns a new list with the length
of each string.
"""

# Declare function.
def length_of_strings(list_of_strings):
    # Declare variable to hold the length of each string.
    length_of_each_string = []
    # Loop through the list of strings.
    for string in list_of_strings:
        # Add the length of the string to the length of each string.
        length_of_each_string.append(len(string))
    # Return the length of each string.
    return length_of_each_string

# Call function.
print(length_of_strings(["Greetings", "World"]))