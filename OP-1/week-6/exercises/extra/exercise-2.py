"""
Exercise 2: Accessing and Iterating Over Dictionaries
Create a dictionary called "phone_book" with the following key-value pairs:
"Alice": "555-1234"
"Bob": "555-5678"
"Charlie": "555-9999"
"""
phone_book = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

# Access the phone number for "Bob" and print it.
print(phone_book["Bob"])

# Iterate over the keys of "phone_book" and print them.
for entry in phone_book:
    print(entry)

# Iterate over the values of "phone_book" and print them.
for entry in phone_book.values():
    print(entry)

# Iterate over the key-value pairs of "phone_book" and print them.
for key, value in phone_book.items():
    print(key, value)
