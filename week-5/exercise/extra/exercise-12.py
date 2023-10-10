"""
Exercises 12:
Write a program that takes in a list of words as input and returns a new list 
containing only the words that start with a vowel.
"""

# Create a list of words
listOfWords = ["Door", "Guitar", "Book", "Water", "Window", "Apple", "Energy"]

# Define vowels.
vowels = "aeiou"

# Function that takes the list of words and creates a new list containing only the words that start with a vowel.
def startWithVowelCheck(listOfWords):

    listOfWordsStartingWithVowel = []

    for word in listOfWords:
            if word[0].lower() in vowels:
                listOfWordsStartingWithVowel.append(word)
    return print(listOfWordsStartingWithVowel)

# Call function.
startWithVowelCheck(listOfWords)