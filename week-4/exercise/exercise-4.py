"""
Write a program that calculates the tax percentage based on gross pay, and then 
use this function in another function to calculate net pay. Remember that in net pay,
the employee receives 50 euros as transportation expenses. 
Here is the percentage scale: 
0-240 -> 0%
241-480 -> 15%
and above 481 -> 28%
"""

# Declare variable.
gross_pay = int(input("Enter the gross pay: "))

# Declare function.
def tax_percentage(gross_pay):
    # Check if gross pay is less than or equal to 240.
    if gross_pay <= 240:
        return 0
    # Check if gross pay is less than or equal to 480.
    elif gross_pay <= 480:
        return 15
    # Check if gross pay is greater than 480.
    elif gross_pay > 480:
        return 28

# Declare function. 
def net_pay(gross_pay):
    # Calculate net pay.
    net_pay = gross_pay - (gross_pay * tax_percentage(gross_pay) / 100) - 50
    # Return net pay.
    return net_pay

# Call function.
print(f"The net pay is {net_pay(gross_pay)} euros.")
