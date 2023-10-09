"""
Write a Python program to manage phone contacts.
Implement a dictionary where each contact has a name (string) as
key and a set of phone numbers (strings) as value. Implement the
following functions
"""

contacts = {}  # Dictionary to store contacts

"""
• add_contact(name, phone_number):
Adds a phone number to the contact with the given name. If the
contact doesn't exist, create a new one.
"""

# def add_contact(name, phone_number):
    

"""
• remove_contact(name):
Removes a contact by name.
When the contact is removed, it prints this message: "Contact
{name} has been removed". If it was not among the contacts, it
prints: "Contact {name} not found".
"""

# def remove_contact(name): 
    

"""
• remove_number(name, phone_number):
Removes a number from the given contact.
The function checks if the name is in contacts or not, if not it prints:
"Contact {name} not found".
And if the contact was among the contacts, then if the number was
among the given contact's numbers, it deletes the number and
prints: "Phone number {phone number} has been removed from
contact {name}", otherwise it prints: "Phone number:
{phone_number} is not one of {name}ls numbers."
"""

# def remove_number(name, phone_number):
    

"""
• find_contact(name):
Finds and prints the phone numbers associated with a given name.
The function prints "Contact: {name}" on one line and each number
on the next line. And if the name wasn't in the contacts, it prints:
"Contact {name} not found".
"""

# def find_contact(name):
    

"""
• list_contacts():
Lists all contacts and their phone numbers.
If the contacts are empty, it prints: "No contact found".
Otherwise, it creates a list of numbers belonging to each contact
and prints the name of the contact in each line, and the list of
numbers in front of the name.
"""

# def list_contacts():
