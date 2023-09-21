"""
First, write a function that takes a letter and check whether it is a vowel or not. 
Then use that function in another function to count the number of vowels in a string.
"""
# Declare variable.
string = input("Enter a string: ")

# Declare function. 
def is_vowel(string):
    # Declare variable.
    vowels = "aeiouAEIOU"
    # Check if string is a vowel.
    if string in vowels:
        return True
    else:
        return False

# Declare function.
def count_vowels(string):
    # Declare variable.
    count = 0
    # Loop through string.
    for i in string:
        # Check if string is a vowel.
        if is_vowel(i):
            # Increase count by 1.
            count += 1
    # Return count.
    return count

# Call function.
print(f'The number of vowels in "{string}" is {count_vowels(string)}.')