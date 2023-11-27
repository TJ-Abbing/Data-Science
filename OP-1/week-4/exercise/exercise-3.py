"""
First, write a function that takes a letter and check whether it is a vowel or not. 
Then use that function in another function to count the number of vowels in a string.
"""
# Declare variable.
string = input("Enter a string: ")

# Declare function.
def is_vowel(possible_vowel):
    # Check if letter is a vowel.
    if possible_vowel in "aeiouAEIOUI":
        # Return True if vowel.
        return True
    # Return False if not a vowel.
    return False

# Declare function.
def count_vowels(string):
    # Declare variable.
    count = 0
    # Loop through string.
    for letter in string:
        # Check if letter is a vowel.
        if is_vowel(letter):
            # Increase count by 1 if vowel (=True).
            count += 1
    # Return count.
    return count

# Call function.
print(f'There are {count_vowels(string)} vowels in "{string}".')