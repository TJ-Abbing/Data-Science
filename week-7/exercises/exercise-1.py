"""
Create a class rectangle with the following attributes and methods:
Attributes:
length: a float representing the length of the rectangle
width: a float representing the width of the rectangle.
Methods:
_init_(self, length, width): a constructor that initializes the attributes with the given values.
area(self): a methode that calculates and returns the area of the rectangle.
perimeter(self): a methode that calculates and returns the perimeter of the rectangle.
"""

# Define class.
class Rectangle:
    
    # Define constructor.
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Define methods.
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2

rectangle = Rectangle(5, 10)
print(rectangle.area())
print(rectangle.perimeter())