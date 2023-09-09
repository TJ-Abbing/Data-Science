# Prompt the user to enter a year
year = int(input("Enter a year: "))

# Check if the year is divisible by 400
if year % 400 == 0:
    # If the year is divisible by 400, it is a leap year
    print("The year is a leap year")
# Check if the year is divisible by 100
elif year % 100 == 0:
    # If the year is divisible by 100 but not by 400, it is not a leap year
    print("The year is not a leap year")
# Check if the year is divisible by 4
elif year % 4 == 0:
    # If the year is divisible by 4 but not by 100, it is a leap year
    print("The year is a leap year")
else:
    # If the year is not divisible by 4, it is not a leap year
    print("The year is not a leap year")
