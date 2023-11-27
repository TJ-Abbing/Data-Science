"""
Exercises 13:
Write a function that takes a string as input and returns the string in reverse order.
"""

# Get string from user's input.
userString = input("Enter a string here and receive the reverse: ")

# Return the reverse of the string from the user's input.
reverseString = userString[::-1]

print(reverseString)