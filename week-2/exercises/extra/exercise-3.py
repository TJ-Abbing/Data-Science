"""
Exercises 3:
Write a Python program that calculates the cost of a movie ticket based on the 
user's age. If the user is 12 or younger, the ticket costs $5. 
If the user is between 13 and 17, the ticket costs $7. 
If the user is 18 or older, the ticket costs $10. 
Use an if-elif-else statement to accomplish this.
"""

# Declare variable.
input_age = int(input("Enter your age: "))

# Check if variable greater than or equal to 18.
if input_age <= 12  :
    print("Ticket price: $5")
# Check if variable is between 13 and 18.
elif 13 <= input_age <= 17: 
    print("Ticket price: $7")
# Check variable is greater than or equal to 18.
elif input_age >= 18 :
    print("Ticket price: $10")
else: 
# If neither of the above conditions are met, print an error message.
    print("Something went wrong.")