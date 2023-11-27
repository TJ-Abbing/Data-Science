"""
Iterate through all numbers from start to end:
for numbers divisible by 3, print "Fizz"
for numbers divisible by 5, print "Buzz"
numbers divisible by both 3 and 5, print "FizzBuzz"
for all other numbers, print the number itself
"""
# Declare variables.
start = int(input("Enter a number: ")) # Declare variable.
end = int(input("Enter another number: ")) # Declare variable.

# Loop through the range of numbers from start to end.
for i in range(start, end + 1):
    # Check if the current number is divisible by 3 and 5.
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Check if the current number is divisible by 3.
    elif i % 3 == 0:
        print("Fizz")
    # Check if the current number is divisible by 5.
    elif i % 5 == 0:
        print("Buzz")   
    # If none of the above conditions are met, print the current number.
    else:
        print(i)