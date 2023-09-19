"""
Instructions
Assignment Week 3
Well-ordered numbers are numbers whose digits increase from left to right.
for example, the number 1234 is well-ordered as 1 but 4321 and 122 are not well-ordered.
Write a program that finds and reports the total number of well-ordered numbers between the given 
range (start to end).
1. The program should only accept numbers greater than 3 digits, so if the user enters a number 
less than 3 digits, print an error message and ask for another number.
2. Create an integer variable called total that holds the count of well-ordered numbers.
3. Create a string variable called numbers_list and each time you find a well-ordered number,
add it to this string with an extra space after.
4. At the end, print a message like this "The count of well-ordered numbers between 11O and 130
is 7 and these are the numbers: 123 124 125 126 127 128 129"

Tip: You can use the % and // operators to separate digits.

Note: Try to use f-string formatting that we practiced in the last session for the message you print at the end.
• Write your code and submit your Python file.
• You don't need to comment all the code, just the lines you think need extra explanation.
"""

# Declare variables.
start_value = int(input("Enter the start value: "))
end_value = int(input("Enter the end value: "))
total_well_ordered_numbers = 0
well_ordered_numbers = ""

# Check if the value has at least 3 digits.
if start_value < 100 or end_value < 100:
    print("The value has less than 3 digits.")
# Check if the start value is greater than the end value.
elif start_value > end_value:
    print("The start value is greater than the end value.")
# Check if the start value is equal to the end value.
elif start_value == end_value:
    print("The start value is equal to the end value.")
# Calculate the amount of well-ordered numbers.
else:
    # Loop through range of start value and end value.
    for i in range(start_value, end_value + 1):
        # Convert i to string.
        string = str(i)
        # Check if string is well-ordered.
        if string == "".join(sorted(string)):
            # Add string to well-ordered numbers.
            well_ordered_numbers += string + " "
            # Increase total well-ordered numbers by 1.
            total_well_ordered_numbers += 1
    # Print the amount of well-ordered numbers and the well-ordered numbers.
    print(f"The count of well-ordered numbers between {start_value} and {end_value} is {total_well_ordered_numbers} and the numbers are as follows: {well_ordered_numbers}")