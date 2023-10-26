"""
Write a Python program that uses the math module to calculate the area of
a circle with radius f. The program should prompt the user for the radius and output the area of 
the circle rounded to 2 demical places.
"""

import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * (radius ** 2)

print("The area of the circle is: ", round(area, 2))