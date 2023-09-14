"""
Write a program that uses a nested loop to print the multiplication 
table for numbers 1 through 10.
"""
# Declare variables.
res = 0 # Declare variable.
for i in range(1, 11): # Loop through the range of numbers from 1 to 10.
    for j in range(1, 11): # Loop through the range of numbers from 1 to 10.
        res = i * j # Multiply i by j and store the result in the res variable.
        print(f"{i} * {j} = {res}") # Print the result.`