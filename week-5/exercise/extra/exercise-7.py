"""
Exercises 7:
Write a function that takes a list of numbers as input and returns a new list with only 
the even numbers.
"""

listOfNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def returnEvenNumbersOnly(listOfNumbers):

    listOfEvenNumbers = []

    print(f"Received a list with the following values; {listOfNumbers}.")

    for number in listOfNumbers:
        if number <= 0:
            print(f"The number {number} is lower or equal to 0.")
        elif number % 2 != 0:
            print(f"The number {number} is not even.")
        else:
            print(f"The number {number} is even.")
            listOfEvenNumbers.append(number)
    return print(f"The even numbers in the list you provided are as follows; {listOfEvenNumbers}")

# Call function.
returnEvenNumbersOnly(listOfNumbers)