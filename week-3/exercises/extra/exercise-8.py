"""
Exercise 8:
Write a program with nested while loops that creates a string of palindromic numbers. 
As a reminder: a palindromic number is a “symmetrical” number that remains the same when reversed. 
For example 22, 33, 101, 111, 121, 999, 1001, 1221, 13031 are all palindrome numbers.

"""

# Declare variables.
start_value = int(input("Enter a start value: "))
end_value = int(input("Enter an end value: "))
palindromic_numbers = ""

# Check if start value is equal to end value.
if start_value == end_value:
    print("The start value and end value are equal.")
else:
    # Check if start value is greater than end value.
    if start_value > end_value:
        print("The start value is greater than the end value.")
    else:
        # Loop through range of start value and end value.
        for i in range(start_value, end_value + 1):
            # Convert i to string.
            string = str(i)
            # Reverse string.
            reverse = string[::-1]
            # Check if string is equal to reverse.
            if string == reverse:
                # Add string to palindromic numbers.
                palindromic_numbers += string + " "
        # Print palindromic numbers.
        print("The palindromic numbers are: " + palindromic_numbers)
