"""
Exercises 1:
Write a Python program that prompts the user for their age and then prints a message based on 
their age. If the user is 18 or older, print "You are an adult." 
If the user is younger than 18, print "You are a minor." 
Use an if-else statement to accomplish this.
"""

input_age = int(input("Enter your age: "))

if input_age >= 18:
    print("You are an adult.")
elif input_age < 18:
    print("You are a minor.")
else:
    print("Something went wrong.")