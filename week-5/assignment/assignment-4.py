# Defining lists and tuples
course_students = ["Python for applied data science", [("Bob", "Smith", 100234), ("John", "Snow", 100235)]]

course_grades_draft = ["Python for applied data science", []]

course_grades = ["Python for applied data science", [[100234, 5.6], [100235, 8.0]]]

"""
Instructions

In this assignment, we want to practice lists and tuples with other concepts we have
learned so far.
Imagine that we have two lists.

1. A list where the first element is always a string representing the name of the
course, and the second is a list of tuples.
Each tuple represents a student and has 3 elements, which are the first name, last
name, and student number of each student.

2. The second list also always has a string that says the name of the course as the
first element, and the second element is a list of lists.
Each inner list will be a list with two elements, the student number (an integer) and
the student's grade (a float).
Here in the attached Python file, I have created these two lists for you, with some elements
already inserted into them, so that you have an idea of what these lists look like.
In this assignment, we will have 3 levels of indexing. I recommend that you look at the line
of code that I mentioned as a HINT to get an idea of what we are getting with each level of
indexing.

Now that we understood what our lists are, I want you to:

Create a function to add new students to this list, taking a course student list,
first name, last name, and student number as parameters. It will first check if the
student is already in the list or not, if so it will return this string: "Student is
already enrolled in this course". If not, it adds the student to the list and returns
this string "Student successfully added to course".
"""

# Create a function to add new students to this list, taking a course student list, first name, last name, and student number as parameters.
def add_student(course_students, first_name, last_name, student_number):
    # It will first check if the student is already in the list or not, if so it will return this string: "Student is already enrolled in this course".
    for student in course_students[1]:
        if student[2] == student_number:
            return "Student is already enrolled in this course"
    # If not, it adds the student to the list and returns this string "Student successfully added to course".
    course_students[1].append((first_name, last_name, student_number))
    return "Student successfully added to the course"

# Call the function.
print(add_student(course_students, "Bob", "Smith", 100234))
print(add_student(course_students, "Alice", "Cordon", 100236))

"""
Create a function that removes a student from this list. The function takes a
course students list and a student number as parameters and returns this string:
"Student was successfully removed from the course", if it finds the student,
otherwise it returns this string "There is no student with this student number in
this course.
"""

# Create a function that removes a student from this list.
def remove_student(course_students, student_number):
    # Returns this string: "Student was successfully removed from the course", If it finds the student.
    for student in course_students[1]:
        if student[2] == student_number:
            course_students[1].remove(student)
            return "Student was successfully removed from the course"
    # Otherwise it returns this string "There is no student with this student number in this course.
    return "There is no student with this student number in this course"

# Call the function.
print(remove_student(course_students, 100237))
print(remove_student(course_students, 100234))

"""
Create a function that adds grades to the course grade list, taking the student
number and the grade as parameters. This function will have two different types
of functionality. First, it checks if the student number given as argument already
has a grade in the grade list or not. If there is already a grade registered for this
student number, it will update the grade and return this string: "Grade was
successfully updated". Otherwise, it will add the student and the grade to the
list.
"""

# Create a function that adds grades to the course grade list, taking the student number and the grade as parameters.
def add_grade(course_grades, student_number, grade):
    # Check if the student number given as an argument already has a grade in the grade list or not.
    for student_grade in course_grades[1]:
        if student_grade[0] == student_number:
            # If there is already a grade registered for this student number, it will update the grade and return this string: "Grade was successfully updated".
            student_grade[1] = grade
            return "Grade was successfully updated"
    # Otherwise, it will add the student and the grade to the list.
    course_grades[1].append([student_number, grade])
    return "Grade added successfully"

# Call the function.
print(add_grade(course_grades, 100234, 7.0))
print(add_grade(course_grades, 100236, 8.6))
# print(add_grade(course_grades_draft, 100234, 7.0))
# print(add_grade(course_grades_draft, 100236, 8.6))

"""
Create a function that calculates the class average grade taking the grade list as a
parameter. This function first checks if there are any grades in the grades list or
not. If there are no grades, it will return this string: "There are no grades in the
grade list yet". Otherwise, it calculates the average for the class and returns this
string: "The average grade of this course is 6.8" (replace 6.8 with your calculated
average).
"""

# Create a function that calculates the class average grade taking the grade list as a parameter.
def class_average(course_grades):
    # First, checks if there are any grades in the grades list or not.
    if len(course_grades[1]) == 0:
        return "There are no grades in the grade list yet"
    else:
        # Calculates the average for the class.
        total_grades = sum([grade[1] for grade in course_grades[1]])
        average = total_grades / len(course_grades[1])
        return f"The average grade of this course is {average:.1f}"

# Call the function.
print(class_average(course_grades_draft))
print(class_average(course_grades))

# Print the course students and grades.
# print(course_students) # This will print both the name of the course and the list of tuples that has students' information.
# print(course_students[0]) # This will print the name of the course
# print(course_students[1]) #  This will print the list of tuples that has students' information.
# (course_students[1][0]) # This will print the information of the first student in the list.
# print(course_students[1][0][2]) # This will print the student number of the first student in the list.