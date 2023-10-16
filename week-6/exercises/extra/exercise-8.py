"""
Exercise 8:
You are given a list of dictionaries, where each dictionary represents a student's information. 
Each student has a name, a list of grades, and an average grade. Write a Python program that does the following:

1. Calculates the average grade for each student.
2. Creates a new dictionary where the keys are student names, and the values are their average grades.
3. Returns the name of the student with the highest average grade.
"""

# Declare list of dictionaries.
students = [
    {
        "name": "John Doe",
        "grades": [80, 90, 100],
        "average_grade": 0
    },
    {
        "name": "Jane Doe",
        "grades": [70, 80, 90],
        "average_grade": 0
    },
    {
        "name": "Joe Doe",
        "grades": [60, 70, 80],
        "average_grade": 0
    }
]

# Declare function.
def handle_students(students):

    # Calculates the average grade for each student.
    for student in students:
        student["average_grade"] = sum(student["grades"]) / len(student["grades"])
        
    # Create a new dictionary where the keys are student names, and the values are their average grades.
    students_average_grade = {}

    for student in students:
        students_average_grade[student["name"]] = student["average_grade"]

    print(students_average_grade)

    # Returns the name of the student with the highest average grade.
    highest_average_grade = 0
    student_with_highest_average_grade = ""

    for student in students_average_grade:
        if students_average_grade[student] > highest_average_grade:
            highest_average_grade = students_average_grade[student]
            student_with_highest_average_grade = student

    return student_with_highest_average_grade

# Call function.
print(handle_students(students))
