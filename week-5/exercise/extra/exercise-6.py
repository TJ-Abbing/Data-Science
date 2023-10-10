"""
Assignment 6:
Write a function that takes a list of strings as input and returns a new list 
with only the strings that have more than 5 characters.
"""

listOfAnimalStrings = ["Dog", "Cat", "Mouse", "Cow", "Horse"]

def fiveCharsPlusOnly(listOfAnimalStrings):
    listOfFiveCharplus = []
    for animal in listOfAnimalStrings:
        if animal.len >= 5:
            listOfFiveCharplus.append[animal]

# Call function.
fiveCharsPlusOnly(listOfAnimalStrings)
