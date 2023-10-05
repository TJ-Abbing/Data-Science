"""
Write a Python program that calculates the average grade for a list of students.
You should define a function calculate_average_grade(grade) that takes a list of grades 
(in the form of dictionaries with "name" and "grade" keys) as input and returns the average grade. 
Use loops, conditional statements, and functions.
"""

# Declare dictionary
grades = [
    {"Name": "Alice", "Grade": 85},
    {"Name": "Bob", "Grade": 92},
    {"Name": "Charlie", "Grade": 78},
    {"Name": "David", "Grade": 88},
]

# Declare function
def calculate_average_grade(grade):
    total = 0
    for grade in grades:
        total += grade["Grade"]
    return total / len(grades)

# Call function
print(calculate_average_grade(grades))