"""
Part 2: Implementing Classes
contactbook.py
In the contactbook.py module, create a class named ContactBook
with the following attributes and methods:
• Attributes:
o contacts (list): A list to store instances of the Contact
class.
• Methods:
o add_contact(self, contact): Add a new contact to the
contact book.
o view_contacts(self): Display the details of all contacts
in the contact book.
0 delete_contact(self, name): Delete a contact from the contact book based on the contact's name.
"""

# Declare class.
class ContactBook:
    
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone_number}, Created on: {contact.creation_date}")

    def delete_contact(self, name):
        for contact in self.contacts:
            if name == contact.name:
                self.contacts.remove(contact)
                return True
        return False