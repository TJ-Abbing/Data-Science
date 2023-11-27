"""
Using a loop, create a string 'res' that has all numbers between 
rn and n that are divisible by x.
"""
# Declare variables.
res = "" # Declare variable.
rn = int(input("Enter a number: ")) # Declare variable.
n = int(input("Enter another number: ")) # Declare variable.
x = int(input("Enter a third number: ")) # Declare variable.

# Loop through the range of numbers from rn to n.
for i in range(rn, n + 1):
    # Check if the current number is divisible by x.
    if i % x == 0:
        res += str(i) + " " # Add the current number to the res variable.
print(res) # Print the res variable.