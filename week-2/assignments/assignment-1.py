

# Assignment 1 - Write a programm that sells tickets.

# Ask for user's age.
age = int(input("Enter your age: "))
# Check if user is within the valid range of 18 to 70.
if age < 18 or age > 70:
    print("Sorry, for security reasons we can't sell you a ticket.")
elif age < 25:
    is_student = input("Are you a student? (Enter 'yes' or 'no'): ").lower() == 'yes'
    has_membership = input("Do you have a membership card? (Enter 'yes' or 'no'): ").lower() == 'yes'
    if is_student and has_membership:
        if age % 2 == 1:
            print("It's your lucky day! You've won a free ticket!")
    if is_student or has_membership:
            print('Ticket price: €5')