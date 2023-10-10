"""
Exercises 4:
Write a function that takes a list of numbers as input and returns the product of all the numbers.
"""

# Declare list.
list = [1, 2, 3, 4]

# Declare function.
def product_of_list(list):
    product = 1
    for item in list:
        product *= item
    return product

# Print result.
print(product_of_list(list))