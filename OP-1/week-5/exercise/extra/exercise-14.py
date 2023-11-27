"""
Exercises 14:
Write a program that takes a string as input from the user and checks whether 
it is a palindrome or not.
"""

# Take string from user's input.
userInputString = input("Enter a string: ")

# Check whether the string is a palindrome.
def palindromeCheck(userInputString):
    reversedString = userInputString[::-1]
    if userInputString == reversedString:
        print(f'As the reverse of "{userInputString}" is "{reversedString}", "{userInputString}" is a palindrome.')
    else:
        print(f'As the reverse of "{userInputString}" is "{reversedString}", "{userInputString}" is not a palindrome.')
# Call function.
palindromeCheck(userInputString)