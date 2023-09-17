"""
Exercise 3:
Write a nested while-loop that creates a triangle with base width and height. For example, if the base would be 3, the result will be:
321
32
3

"""

# Declare variables
base = int(input("Enter the base width and the height of the triangle: "))

# Check if the number is negative
if base < 0:
    print("Sorry, the triangle does not exist for negative integers. Please enter a positive integer.")
# Check if the number is 0
elif base == 0:
    print("The triangle does not exist for 0.")
# Calculate the triangle
else:
    temp = base
    while temp > 0:
        for i in range(base, base - temp, -1):
            print(i, end="")
        print()
        temp = temp - 1