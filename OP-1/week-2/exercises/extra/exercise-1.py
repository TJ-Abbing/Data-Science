"""
Exercises 1:
Write a Python program that prompts the user for their age and then prints a message based on 
their age. If the user is 18 or older, print "You are an adult." 
If the user is younger than 18, print "You are a minor." 
Use an if-else statement to accomplish this.
"""

# Declare variable.
input_age = int(input("Enter your age: "))

# Check if variable is greater than or equal to 18.
if input_age >= 18:
    print("You are an adult.")
# Check if variable is less than 18.
elif input_age < 18:
    print("You are a minor.")
# If neither of the above conditions are met, print an error message.
else:
    print("Something went wrong.")