"""
Part 2: Implementing Classes
contact.py
In the contact.py module, create a class named Contact with the
following attributes and methods:
• Attributes:
o name (str): The name of the contact.
o email (str): The email address of the contact.
o phone_number (str): The phone number of the contact.
o creation_date (date): The creation date of the
contact, automatically set to the current date when
an instance is created.
"""

# Imports.
from datetime import datetime

# Declare class.
class Contact:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.creation_date = datetime.now()