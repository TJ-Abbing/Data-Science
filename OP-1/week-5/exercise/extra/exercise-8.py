"""
Exercises 8:
Write a program that takes a list of integers as input from the user and returns 
a new list containing only the even numbers from the original list.
"""

# List of integers provided by user input
integersString = input(str("Please enter the integers you want in the list, seperated by spaces, Eg; 0 1 2, etc.: "))

# Split the list of integers provided by user input into a list of strings
integersStringList = integersString.split()

# Create a list 
integerList = [int(integerString) for integerString in integersStringList]

def acceptEvenOnly(integerList):

    evenIntegerList = []

    for int in integerList:
        if int <= 0:
            print(f"The integer {int} is smaller or equal to 0.")
        elif int % 2 != 0:
            print(f"The integer {int} is not even.")
        else:
            print(f"The integer {int} is even.")
            evenIntegerList.append(int)
    return print(evenIntegerList)

# Call function.
acceptEvenOnly(integerList)