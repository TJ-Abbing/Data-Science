"""
Instructions
In this assignment, we want to practice lists and tuples with other concepts we have learned so far.
Imagine that we have two lists.
I. A listwhere the firstelement is always a string represen€ngthe name Of the course, and the second is a list of tuples.
Each tuple represents a student and has 3 elements, which are the first name, last name, and student number of each
student.
2. The second list also always has a string thatsaysthe name of the course asthe first element, and the second element is
a list Of lists.
Each inner list will be a list with two elements, the student number (an integer) and the student's grade float).
Here in the attached Python file, I have created these two lists for you, with some elements already inserted into them, so that
you have an idea of what these lists look like.
In this assignment, we will have 3 levels Of indexing. I recommend that you 100k at the line Of code that I mentioned as a HINT to
get an idea of what we are g•effng with each level of indexing.
Now that we understood what Our lists are, I want you to:
• Create a function to add new students to this list, taking a course student list, first name, last name, and
student number as parameters. It will first check if the student is already in the list or not, if so it will
return this string: "Student is already enrolled in this course. If not, it adds the student to the list and
returns this string • Student successfully added to course.
• Create a function that removes a student from this list. The function takes a course students list and a
student number as parameters and returns this string: • Student was successfully removed from the
course, if it finds the student, otherwise it returns this string •There is no student with this student
number in this course.
• Create a function that adds grades to the course grade list, taking the student number and the grade as
parameters. This function will have two different types of functionality. First, it checks if the student
number given as argument already has a grade in the grade list or not. If there is already a grade
registered for this student number, it will update the grade and return this string: •Grade was
successfully updated•. Otherwise, it will add the student and the grade to the list.
• Create a function that calculates the class average grade taking the grade list as a parameter. This
function first checks if there are any grades in the grades list or not. If there are no grades, it will return
this string: •There are no grades in the grade list yet•. Otherwise, it calculates the average for the class
and returns this string: •The average grade of this course is 6.8• (replace 6.8 with your calculated
average).
P.S. To calculate the average, you need to sum all the grades and divide it by the number of students.
Tip: Don't forget to use the len() function.
"""