"""
Define functions to calculate the area and perimeter of these shapes.
"""

from math import pi

def circle_area(circle):
    return pi * circle.radius ** 2

def circle_perimeter(circle):
    return 2 * pi * circle.radius

def rectangle_area(rectangle):
    return rectangle.width * rectangle.height

def rectangle_perimeter(rectangle):
    return 2 * (rectangle.width + rectangle.height)

