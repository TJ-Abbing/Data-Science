# Write a function that takes temperature in Fahrenheit and returns it in Celsius.

# Declare variable.
fahrenheit = int(input("Enter the temperature in Fahrenheit: "))

# Declare function.
def fahrenheit_to_celsius(fahrenheit):
    # Calculate celsius.
    celsius = (fahrenheit - 32) * 5 / 9
    # Return celsius.
    print(f"{fahrenheit} Fahrenheit is {celsius} Celsius.")

# Call function.
fahrenheit_to_celsius(fahrenheit)