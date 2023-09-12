"""
Exercises 7:
Write a Python program that prompts the user for a temperature in Fahrenheit 
and then converts it to Celsius. 
The conversion formula is Celsius = (Fahrenheit - 32) * 5/9. 
Print the result. Use an if statement to check that the user input a valid number.
"""

# Declare variable.
toBeConverted = int(input("Enter a temperature in Fahrenheit: "))
converted = (toBeConverted - 32) * 5/9

# Print both variables.
print(f"{toBeConverted} degrees Fahrenheit is equal to {converted} degrees Celsius.")
