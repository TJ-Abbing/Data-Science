"""
Exercises 10:
Write a Python program that takes a list of integers as input from the user 
and returns the average of all the numbers in the list.
"""

# Get string o integers from user input.
integerString = input("Enter the integers you want to know the average. Use a space each time you add an integer. Eg; 0 1 2. Enter integer(s): ")

# Split string and create a list of integer strings.
integerStringList = integerString.split()

# Create list of integers.
integerList = [int(integer) for integer in integerStringList]

# Calculate the average of all numbers in the list
def calculateAverageOfNums(integerList):
    sum = 0
    for int in integerList:
        sum += int
    average = sum / len(integerList)
    return print(f"The average of all numbers in the list is {average}")

# Call function.
calculateAverageOfNums(integerList)
    