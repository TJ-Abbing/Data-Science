"""
Exercises 11:
Write a Python program that takes a string as input from the user and returns 
the number of vowels (a, e, i, o, u) in the string.
"""

# Take string as input from user
userString = input("Enter a string to calculate the number of vowels within it: ")

vowels = "aeiou"
space = " "

# Calculate number of vowels within string
def calculateNumOfVowels(userString):

    sumOfVowels = 0

    for char in userString:
        if char in vowels:
            print(f"The character {char} is a vowel.")
            sumOfVowels += 1
        elif char in space:
            print("You entered a space here.")
        elif char not in vowels:
            print(f"The character {char} is a consonant.")
    return print(sumOfVowels)

# Call function.
calculateNumOfVowels(userString)