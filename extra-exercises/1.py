"""
Exercise: Guess the Number Game

Write a Python program that simulates a "Guess the Number" game. Here are the requirements:

    The program should generate a random number between 1 and 100 (inclusive).

    The user should be allowed to guess the number. After each guess, the program should provide feedback if the guess 
    is too high or too low.

    The user should continue guessing until they correctly guess the number.

    After the user guesses the number correctly, the program should print a congratulatory message and indicate the 
    number of attempts it took.
"""

# Imports.
import random

# Declare variable with random number.
randomNumber = random.randint(1, 100)

print(randomNumber) # for testing

# Declare variable to keep track of attemps.
attempts = 0

# Ask for user input.
guess = int(input("Guess the number: "))

# Check if guess is correct.
while True:
    if randomNumber == guess:
        print(f"Your guess was {guess}. The random number is {randomNumber}, meaning you guessed correctly! Congratulations! It took you {attempts} attempts.")
        break
    elif randomNumber < guess:
        print(f"Your guess was {guess}, which is incorrect. The number is lower than {guess}.")
        guess = int(input("Guess the number: "))
        attempts += 1
    elif randomNumber > guess:
        print(f"Your guess was {guess}, which is incorrect. The number is higher than {guess}.")
        guess = int(input("Guess the number: "))
        attempts += 1
    else:
        print("Something went wrong.")