"""
Assignment 6:
Write a function that takes a list of strings as input and returns a new list 
with only the strings that have more than 5 characters.
"""

listOfAnimalStrings = ["Dog", "Cat", "Mouse", "Cow", "Horse"]

def fiveCharsPlusOnly(listOfAnimalStrings):
    listOfFiveCharPlusAnimals = []
    for animal in listOfAnimalStrings:
        if len(animal) >= 5:
            listOfFiveCharPlusAnimals.append(animal)
    return print(listOfFiveCharPlusAnimals)

# Call function.
fiveCharsPlusOnly(listOfAnimalStrings)
