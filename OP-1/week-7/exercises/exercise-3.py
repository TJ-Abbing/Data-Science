""""
Create a Python class called Student with attributes for name, family name, student number, 
and a list of grades. 

It includes methods for calculating the average grade, displaying student 
information, add grade and a method checking if student is passing or not.

- add_grade method has one parameter as grade, and it adds given grade to the grades of 
student.
- is_passing method has one parameter as passing grade with default value of 5.0 and returns 
True or False.

Note: Use none value instead of the empty list as the default value for grades and make 
appropriate changes to have an empty list as default when the grades list is not given as 
argument.
OBJECT-ORIENTED PROG
"""

# Define class.
class Student:
    
        # Define constructor.
        def __init__(self, name, family_name, student, grades=None):
            self.name = name
            self.family_name = family_name
            self.student = student
            if grades is None:
                self.grades = []
            else:
                self.grades = grades

        # Define methods.
        def average_grade(self):
            if not self.grades:
                return 0
            else:
                return sum(self.grades) / len(self.grades)
        
        def display_student(self):
            return print(f"Name: {self.name}\nFamily name: {self.family_name}\nStudent number: {self.student}\nGrades: {self.grades}")
        
        def add_grade(self, grade):
            self.grades.append(grade)

        def is_passing(self, passing_grade=5.0):
            if self.average_grade() >= passing_grade:
                return True
            else: 
                return False

# Create instance.
student1 = Student("John", "Doe", 123456)
student2 = Student("Jane", "Doe", 654321, [7, 8, 9, 10, 10])

# Call methods.
student1.display_student()
print(student1.average_grade())
print(student1.is_passing())
student1.add_grade(10)
print(student1.average_grade())
print(student1.is_passing())

student2.display_student()
print(student2.average_grade())
print(student2.is_passing())
student2.add_grade(10)
print(student2.average_grade())
print(student2.is_passing())