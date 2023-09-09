# Assignment 1 - Write a programm that sells tickets.

# Ask for user's age.
age = int(input("Enter your age: "))

# Check if user is within the invalid age range (younger than 18 or older than 70). If true (=in invalid range), deny access.
if age < 18 or age > 70:

    print("Sorry, for security reasons we can't sell you a ticket.")

# If user is over 25, ticket price is €15.
elif age >= 25:
    print('Ticket price: €15')

# Check if user is younger than 25. 
elif age < 25:

    # If true, ask if user is a student & if user has a membership card.
    is_student = input("Are you a student? (Enter 'yes' or 'no'): ").lower() == 'yes'
    has_membership = input("Do you have a membership card? (Enter 'yes' or 'no'): ").lower() == 'yes'

    # Check if false (=not a student and not a member). If false, ticket price is €10.
    if not is_student and not has_membership:
        print('Ticket price: €10')  

    # Check if user is both a student and member. 
    if is_student and has_membership:

        # If true, check if user's age is an odd number. If false (=even number), ticket price is €5.
        if not age % 2 == 1:
            print('Ticket price: €5')   
        # If false (=odd number), give user a free ticket.
        else:
            print("It's your lucky day! You've won a free ticket!")

    # If false (=student and / or member), check if user is either a student or a member. If true, ticket price is €5.
    elif is_student or has_membership:
        print('Ticket price: €5')   