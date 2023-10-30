"""
Objective: The objective of this assignment is to develop a Contact
Management System. In this system, you will create a package
structure with two modules, 'contact.py' and 'contactbook.py', to
manage contacts. You will also create a main program in main.py'
to interact with the user and perform various operations on the
contacts, such as adding, viewing, and deleting.
"""

"""
Part 1: Creating Modules
1. Create a package named "contact_manager."
2. Inside the package, create two modules:
o contact.py: This module should define a Contact class
that has attributes called name, email, phone number,
and the creation date.
o contactbook.py: This module should define a
ContactBook class that manages a list of contacts and
provides methods to add, view, and delete contacts.
Remember to create your init_.py file.
"""

"""
Part 3: Creating the Main Program
In the main.py file (outside the package), you will create a main
program that interacts with the user and uses the classes defined in
the package.
• Import the Contact and ContactBook classes from the
contact_manager package.
• Create an instance of the ContactBook class named
contact book.
• Implement a while loop to create a simple menu-driven
interface for the user with the following options:
1. Add Contact: Prompt the user to enter contact
information and add it to the contact book.
2. View Contacts: Display the details of all contacts in the
contact book.
3. Delete Contact: Prompt the user to enter the name of
the contact to delete and remove it from the contact
book.
4. Exit: Exit the program.

Ensure that the program handles invalid choices and provides
appropriate feedback.
Example Usage:
Here's how the program should work:
• The user can add contacts with names, emails, and phone
numbers.
• The user can view the list of contacts with their creation
dates.
• The user can delete a contact by providing the contact's
name.
• The program should continue running until the user selects
the "Exit" option.
"""

# main.py (outside the package).
from contact_manager.contact import Contact
from contact_manager.contactbook import ContactBook

# Declare instance.
contact_book = ContactBook()

# Program loop.
while True:
    print("\nContact Management System")
    print("[1] Add Contact")
    print("[2] View Contacts")
    print("[3] Delete Contact")
    print("[4] Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the contact's name: ")
        email = input("Enter the contact's email: ")
        phone_number = input("Enter the contact's phone number: ")
        contact_book.add_contact(Contact(name, email, phone_number))
        print(f"Contact {name} added successfully.")

    elif choice == "2":
        print("Contacts:")
        contact_book.view_contacts()

    elif choice == "3":
        name = input("Enter the name of the contact to delete: ")
        result = contact_book.delete_contact(name)
        if not result:
            print(f"{name} was not found in contacts.")
        else:
            print(f"{name} has been deleted from contacts.")

    elif choice == "4":
        print("Thank you for using the Contact Management System, goodbye.")
        break

    else:
        print("Invalid choice. Please try again.")