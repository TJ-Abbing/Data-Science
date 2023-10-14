"""
Exercise 4:
Write a program that creates a set of at least 5 unique elements and then uses the "pop()" 
method to remove and print each element until the set is empty.
"""

# Declare set.
my_set = set()

# Add elements to set.
my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.add(4)
my_set.add(5)

# Remove elements and print them.
while my_set:
    element = my_set.pop()
    print(element)
