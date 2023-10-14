"""
Create a class called BankAccount with the following attributes and methods:
Attributes:
balance: a float representing the amount of money in the account.
Methods:
_init_(self, balance): a constructor that initializes the balance attribute with the given value.
deposit(self, amount): a method that deposits the given amount in the account.
withdraw(self, amount): a method that withdraws the given amount from the account.
get_balance(self): a method that returns the current balance of the account.
"""

# Define class.
class BankAccount:

    # Define constructor.
    def __init__(self, balance):
        self.balance = balance

    # Define methods.
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
    
    def get_balance(self):
        return self.balance
    
# Create object.
account = BankAccount(1000)
print(account.get_balance())
account.deposit(500)
print(account.get_balance())
account.withdraw(1000)
print(account.get_balance())