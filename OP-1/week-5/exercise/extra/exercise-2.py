"""
Exercises 2: Tuples and Slicing
Create a tuple with three items: "apple", "banana", "cherry".
Print the second item in the tuple.
Slice the tuple to create a new tuple with the first two items.
Print the new tuple.
Try to modify the first item in the new tuple (you should get an error).
"""
# 1. Create a tuple with three items: "apple", "banana", "cherry".

tuple = ("apple", "banana", "cherry")

# 2. Print the second item in the tuple.

print(tuple[1])

# 3. Slice the tuple to create a new tuple with the first two items.

second_tuple = tuple[0:2]

# 4. Print the new tuple.

print(second_tuple)

# 5. Try to modify the first item in the new tuple (you should get an error).

second_tuple[0] = "pear"

# TypeError: 'tuple' object does not support item assignment