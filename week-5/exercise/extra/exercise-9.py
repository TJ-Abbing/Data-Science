"""
Exercises 9:
Write a function that takes a tuple of numbers as input and 
calculates the average of those numbers.
"""

tupleOfNumbers = (0, 1, 2, 3 , 4, 5, 6, 7, 8, 9)

def calculateAverage(tupleOfNumbers):
    sum = 0
    for number in tupleOfNumbers:
        sum += number 
        average = sum / len(tupleOfNumbers)
    return print(f"The average of the tuple is {average}")

calculateAverage(tupleOfNumbers)