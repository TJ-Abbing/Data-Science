"""
Create a Python class called Shop that simulates the management
of a shop's inventory. The class should have methods to add
products to the inventory, list the available products, calculate the
total value of the products, apply discounts, and display shop
information.
"""

# Creat Class Shop
class Shop:

    """
    Class Attributes:
    1. name: A string representing the name of the shop.
    2. city: A string representing the city where the shop is
    located.
    3. products: A list to store products with structured data. Each
    product is represented as a dictionary with attributes for
    name, price (in euros), and quantity in stock.
    """

    """
    Class Methods:
    __init__ (self, name, city): Initialize the shop's inventory with a
    name, a city, and an empty list of products.
    """
    # Class methods.
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.products = []

    """
    add_product(self, name, price, quantity): Add a product to the
    inventory. Each product should be represented as a dictionary with
    the following keys:
    name: The name of the product.
    price: The price of the product in euros.
    quantity: The quantity of the product in stock.
    Print: "{product_name} added to the inventory with a price of
    €{product_price} and a quantity of {product_quantity}."
    """
    def add_product(self, name, price, quantity):
        product = {"name": name, "price": price, "quantity": quantity}
        self.products.append(product)
        print(f"{name} added to the inventory with a price of €{price} and a quantity of {quantity}.")

    """
    list_products(self): List all the available products in the inventory.
    Display the products using the following format:

    Print:
    Available products in {shop_name} ({shop_city}):
    Name: {product_name}, Price: €{product_price}, Quantity:
    {product_quantity}
    Name: {product_name}, Price: €{product_price}, Quantity:
    {product_quantity}
    ... (for all products)
    If the inventory is empty, print "The shop's inventory is empty."
    """

    def list_products(self):
        if not self.products:
            print("The shop's inventory is empty.")
        else:
            print(f"Available products in {self.name} ({self.city}):")
            for product in self.products:
                print(f"Name: {product['name']}, Price: €{product['price']}, Quantity: {product['quantity']}")

    """
    calculate_total(self): Calculate the total value of all products in the
    inventory. The total value is calculated by summing the prices
    multiplied by the quantities of all products.
    Return: A float number which is the total value of products in the
    inventory in Euro.
    """

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product['price'] * product['quantity']
        return total

    """
    apply_discount(self, product_name, discount _ percent): Apply a
    discount to a specific product. The discount_percent should be a
    value between O and 100. Update the price of the product
    accordingly.
    Print: "{product_name} now has a {discount_percent}% discount.
    New price: €{new price}"
    """
    def apply_discount(self, product_name, discount_percent):
        for product in self.products:
            if product['name'] == product_name:
                product['price'] *= (100 - discount_percent) / 100
                print(f"{product_name} now has a {discount_percent}% discount. New price: €{product['price']}")

    """
    info(self): Display shop information, including the name, city, and
    details of the products in the inventory using
    the list_products method.
    Print:
    Shop Name: {shop_name}
    Shop Location: {shop_city}
    Products in Inventory:
    Name: {product _ name}, Price: €{product_price}, Quantity:
    {product_quantity}
    Name: {product _ name}, Price: €{product_price}, Quantity:
    {product_quantity}
    ... (for all products)
    """

    def info(self):
        print(f"Shop Name: {self.name}")
        print(f"Shop Location: {self.city}")
        print("Products in Inventory:")
        self.list_products()

# Create an instance of the Shop class
my_shop = Shop("My Shop", "Rotterdam")

# Example
my_shop.add_product("Laptop", 10.0, 5)
my_shop.add_product("Cellphone", 20.0, 3)
my_shop.add_product("Printer", 30.0, 2)

# List products in the inventory
my_shop.list_products()

# Calculate the total value of products in the inventory
total_value = my_shop.calculate_total()
print(total_value)

# Apply a discount to a product
my_shop.apply_discount("Cellphone", 10)

# List products again after applying a discount
my_shop.list_products()

# Display shop information using the info method
my_shop.info()


# Here is the output we are expecting to be printed from the examples:
"""
Laptop added to the inventory with a price of €10.0 and a quantity of 5.
Cellphone added to the inventory with a price of €20.0 and a quantity of 3.
Printer added to the inventory with a price of €30.0 and a quantity of 2.

Available products in My Shop (Rotterdam):
Name: Laptop, Price: €10.0, Quantity: 5
Name: Cellphone, Price: €20.0, Quantity: 3
Name: Printer, Price: €30.0, Quantity: 2

170.0

Cellphone now has a 10% discount. New price: €18.0

Available products in My Shop (Rotterdam):
Name: Laptop, Price: €10.0, Quantity: 5
Name: Cellphone, Price: €18.0, Quantity: 3
Name: Printer, Price: €30.0, Quantity: 2

Shop Name: My Shop
Shop Location: Rotterdam
Products in Inventory:
Available products in My Shop (Rotterdam):
Name: Laptop, Price: €10.0, Quantity: 5
Name: Cellphone, Price: €18.0, Quantity: 3
Name: Printer, Price: €30.0, Quantity: 2
"""