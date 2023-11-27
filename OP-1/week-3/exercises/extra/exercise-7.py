"""
Exercise 7:
Find if a number is a palindrome. A palindrome is a number that remains the same when reversed.
A few examples:
- The reverse of the number 84548 is also 84548. Therefore 84548 is a palindrome.
- The reverse of number 475 is 574. Therefore 475 is not a palindrome.

The number can have any amount of digits.
"""

# Declare variables.
integer = int(input("Enter an integer: "))

# Convert integer to string.
string = str(integer)

# Reverse string.
reverse = string[::-1]

# Check if string is equal to reverse.
if string == reverse:
    print("The number " + string + " is a palindrome.")
else:
    print("The number " + string + " is not a palindrome.")