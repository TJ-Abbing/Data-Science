# Create a list of days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Prompt the user to enter a number representing the day of the week
currentDay = int(input("Enter a number: "))

# Check if the entered number is within the valid range (0 to 6)
if 0 <= currentDay < len(days):
    # If the number is valid, print the corresponding day of the week
    print(days[currentDay])
else:
    # If the number is not valid, print an error message
    print("Invalid input")