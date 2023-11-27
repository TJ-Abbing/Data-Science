# Create a dictionary called phone_book
phone_book = {"Alice": "555-1234", "Bob": "555-5678", "Charlie": "555-9999"}

# Print the phone number for Bob
print(phone_book["Bob"])

# Iterate over the keys of phone_book and print each one
for key in phone_book:
    print(key)

# Iterate over the values of phone_book and print each one
for value in phone_book.values():
    print(value)

# Iterate over the key-value pairs of phone_book and print each one
for key, value in phone_book.items():
    print(key, value)