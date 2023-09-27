"""
Expats are highly skilled migrants who work in the Netherlands and have some tax
reduction on their salary for 5 years.
If you are an expat, 30% of your salary is not taxed.
"""

"""
1. Write a program that asks for this information at the beginning and stores it in
variables.
• What is your name?
• What is your age?
• What is your monthly salary?
• How many days a week do you work?
"""

# Declare variables.
name = input("What is your name? ")
age = int(input("What is your age? "))
salary = int(input("What is your monthly salary? "))
days = int(input("How many days a week do you work? "))

"""
2. Write a function called 'isExpat' that returns True if the person is an expat,
otherwise returns False.
These are the rules for being an expat:
If you are under 18, you are not an expat.
If you are under 35 and your salary is over 3000, you are an expat.
If you are over 35 and your salary is over 5000, you are an expat.
In all other cases, you are not an expat.
"""

# Declare function.
def isExpat(age, salary):
    # Check if age is under 18.
    if age < 18:
        return False
    # Check if age is under 35 and salary is over 3000.
    elif age < 35 and salary > 3000:
        return True
    # Check if age is over 35 and salary is over 5000.
    elif age > 35 and salary > 5000:
        return True
    # In all other cases, return False.
    else:
        return False

# print("The employee is an expat." if isExpat(age, salary) else "The employee is not an expat.")

"""
3.
Write a function called 'tax deduction' that calculates the amount of tax to be
deducted from the salary.

Remember to check at the beginning of the function whether the employee is an
expat or not. Use the function you wrote earlier within your function to check. If
the employee is an expat, you have to reduce the salary to 70 percent of the
total, because as we said before, 30 percent of the salary is not taxed.
Then check if the salary is below 3000, the amount deducted will be 15 percent.
If the salary is greater than or equal to 3000 and less than 4000, 20 percent will
be deducted.
If the salary is greater or equal to 4000 and less than 6000, 30 percent will be
deducted from the salary.
Finally, if the salary is 6000 and above, 40 percent is deducted.
"""

# Declare function. 
def tax_deduction(age, salary):
    # Check if employee is an expat.
    if isExpat(age, salary):
        salary = salary * 0.7
    # Check if salary is below 3000.
    if salary < 3000:
        return salary * 0.85
    # Check if salary is greater than or equal to 3000 and less than 4000.
    elif salary >= 3000 and salary < 4000:
        return salary * 0.8
    # Check if salary is greater than or equal to 4000 and less than 6000.
    elif salary >= 4000 and salary < 6000:
        return salary * 0.7
    # Check if salary is 6000 and above.
    elif salary >= 6000:
        return salary * 0.6
    
# print(f"The amount of tax to be deducted from the salary is {tax_deduction(age, salary)}.")

"""
4. Write a function called 'net_salary' that will first deduct tax from the gross amount
by calling 'tax_deduction' function and then it will add transportation and internet
costs to it.

Internet cost is fixed amount and it is 30.
Transportation cost is calculated based on number of days and salary. If the
salary is less than 5000, 10 Euro will be paid for each day and for the salaries
above, 5 Euro.
Remember to calculate the monthly transportation costs. Let us assume that we
have 4 weeks in a month and you have already asked for the number of days the
employee works per week.
In the end, the function will return the net salary to be paid.
"""

# Declare function.
def net_salary(age, salary, days):
    # Calculate net salary.
    net_salary = tax_deduction(age, salary) + 30 + (days * 4 * 10 if salary < 5000 else days * 4 * 5)
    return net_salary

# print(f"The net salary to be paid is {net_salary(age, salary, days)}.")

"""
5. Write a function called 'info' that returns a string like this, replacing Bob with the
employee's name and the number with the net salary.

"Dear Bob, this month your net salary is 4800 Euros."
At the end of the program, simply call the 'info' function and print the string to see the
string in the output.
"""

# Declare function.
def info(name, net_salary):
    # Return string.
    return f"Dear {name}, this month your net salary is {net_salary} Euros."

# Call function.
print(info(name, net_salary(age, salary, days)))