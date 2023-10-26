"""
Import the package and modules in a script and use them to calculate the 
area and perimeter of a circle and a rectangle.
"""

from geometry.shapes import *
from geometry.measurements import *

circle = Circle(5)
rectangle = Rectangle(3, 4)

print(circle_area(circle))
print(circle_perimeter(circle))
print(rectangle_area(rectangle))
print(rectangle_perimeter(rectangle))