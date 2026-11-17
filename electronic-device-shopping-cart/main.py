# Electronic Device Shopping Cart
#
# This file shows a shopping cart system for electronic devices.
# The inheritance concept of Object-Oriented Programming (OOP) is  implemented.
# This system will allow customers to browse and purchase electronic
# devices such as smartphones, laptops, and tablets, while also managing
# stock and applying discounts.

# Part 1: Concept & Design
# We are building an electronic device store where customers can browse,
# add items to their cart, and purchase devices. Each device type has
# its own unique properties, but all devices share some common attributes
# such as name, price, and stock.

# System Overview:

# The store will offer different types of devices: Smartphones, Laptops, and Tablets.
# Each device will have common attributes like name, price, and stock, and unique attributes
# for each device type.
# Customers will be able to add devices to their shopping cart, specify quantities,
# and proceed to checkout.

# Device Types:

# Smartphone: Contains attributes like screen size and battery life.
# Laptop: Contains attributes like RAM size and processor speed.
# Tablet: Contains attributes like screen resolution and weight.

# Methods to Implement:

# Display Device Information: Show the name, price, and availability of each device.
# Add Devices to Cart: Allow the customer to specify the quantity of a device to add to their
# shopping cart.
# Checkout: Calculate the total price of items in the cart and reduce the stock of devices purchased.

# Part 2: Implementation Steps

# Step 1: Create a Base Class - Device

# Create a parent class called Device that defines common attributes and behaviors for all devices.
# Attributes:
# name: The name of the device (e.g., "iPhone 13", "MacBook Pro").
# price: The price of the device.
# stock: The number of units available in the store.
# warranty_period: The warranty period for the device in months.

# Methods:
# __init__(self, name, price, stock, warranty)

class Device:
    def __init__(self, name, price, stock, warranty):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty = warranty

# display_info(self): Displays the basic details of the device (name, price, stock, warranty).

    def display_info(self):
        print(f'{self.name} {self.price} {self.stock} {self.warranty}')

# __str__(self): Displays the basic details of the device (name, price, stock, warranty).
    def __str__(self):
        return (f'Name: {self.name} Price: {self.price}\n'
                f' In stock: {self.stock} Warranty: {self.warranty}')

# apply_discount(self,discount_percentage): Reduces the price by a specified discount percentage.
    def apply_discount(self,discount_percentage):
        discount = self.price * discount_percentage / 100
        final_price = self.price - discount
        print(f"Price: {self.price:.2f}")
        print(f"Discount ({discount_percentage}%): {discount:.2f}")
        print(f"Price to pay: {final_price:.2f}")

# is_available(self,amount): Checks if the device is available in the required quantity.
# Returns True if available, False otherwise.
    def is_available(self,amount):
        if self.stock >= amount:
            return True
        else:
            return False

# reduce_stock(self,amount): Reduces the stock by the specified quantity when a purchase is made.
    def reduce_stock(self,amount):
        if self.is_available(amount):
            self.stock -= amount
            return True
        else:
            return False
# This class should serve as the foundation for all other types of devices.


# Step 2: Create Derived Classes for Specific Device Types

# Using inheritance, create three subclasses: Smartphone, Laptop, and Tablet.
# Each subclass should inherit from Device and have its own additional attributes and methods.

# Smartphone (Inherits from Device):
# Attributes:
# screen_size: The size of the screen in inches.
# battery_life: The battery life in hours.

class Smartphone(Device):
    def __init__(self, name, price, stock, warranty,screen_size, battery_life):
        super().__init__(name, price, stock, warranty)
        self.screen_size = screen_size
        self.battery_life = battery_life

# Methods:
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Stock: {self.stock}")
        print(f"Warranty period: {self.warranty} months")
        print(f"Screen size: {self.screen_size} inches")
        print(f"Battery: {self.battery_life} hours")

# __str__(self): String representation of Smartphone
    def __str__(self):
        return(f'Name: {self.name} Price: {self.price} In stock {self.stock}\n'
               f' Warranty: {self.warranty}\n'
               f'Screen size: {self.screen_size} Battery life: {self.battery_life}')

# make_call(self): Simulates making a call.
    def make_call(self):
        print("Making a call...")
# install_app(self): Simulates installing an app.
    def install_app(self):
        print ("Installing an app...")

# Laptop (Inherits from Device):
# Attributes:
# ram_size: The amount of RAM in GB.
# processor_speed: The speed of the processor in GHz.

class Laptop(Device):
    def __init__(self, name, price, stock, warranty,
                 ram_size, processor_speed):
        super().__init__(name, price, stock, warranty)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

# Methods:
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Stock: {self.stock}")
        print(f"Warranty period: {self.warranty} months")
        print(f"RAM: {self.ram_size} GB")
        print(f"Processor speed: {self.processor_speed} GHz")

# __str__(self): String representation of Laptop
    def __str__(self):
        return (f'Name: {self.name} Price: {self.price} In stock {self.stock}\n'
                f'Warranty: {self.warranty} RAM size: {self.ram_size}\n'
                f'Processor speed: {self.processor_speed}')
# run_program(self): Simulates running a program on the laptop.
    def run_program(self):
        print("Running a program...")
# use_keyboard(self): Simulates typing on the keyboard.
    def use_keyboard(self):
        print("Typing on a keyboard...")


# Tablet (Inherits from Device):
# Attributes:
# screen_resolution: The screen resolution (e.g., "2048x1536").
# weight: The weight of the tablet in grams.
class Tablet(Device):
    def __init__(self, name, price, stock, warranty, screen_resolution, weight):
        super().__init__(name, price, stock, warranty)
        self.screen_resolution = screen_resolution
        self.weight = weight

# Methods:
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Stock: {self.stock}")
        print(f"Warranty period: {self.warranty} months")
        print(f"Screen resolution: {self.screen_resolution}")
        print(f"Weight: {self.weight} grams")

# __str__(self): String representation of Tablet
    def __str__(self):
        return (f'Name: {self.name} Price: {self.price} In stock {self.stock}\n'
                f'Warranty: {self.warranty}\n'
                f'Screen Resolution: {self.screen_resolution} Weight: {self.weight}')

# browse_internet(self): Simulates browsing the internet.
    def browse_internet(self):
        print("Browsing the internet...")
# use_touchscreen(self): Simulates using the touchscreen for navigation.
    def use_touchscreen(self):
        print("Using touchscreen for navigation...")

# Each subclass should override or extend the display_info() method to show relevant
# details specific to that device type.

# Step 3: Create the Cart and Purchase System
# Now, create a shopping cart system that allows customers to manage their cart and
# proceed to checkout.

# Cart Class:
# Attributes:
# items: A list of tuples, where each tuple contains a device and the amount being purchased.
# total_price: The total price of all devices in the cart.

class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0

# Methods:
# add_device(self, device, amount): Adds a specified quantity of a device to the cart
# if it’s available in stock and updates the total_price.
    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            self.total_price += device.price * amount
        else:
            print("Not enough stock available!")

# remove_device(self, device, amount): Removes a specified quantity of a device from
# the cart and updates the total_price.
    def remove_device(self, device, amount):
        if (device, amount) in self.items:
            self.items.remove((device, amount))
            self.total_price -= device.price * amount
        else:
            print("Device not found in cart!")

# get_total_price(self): Retrieves the total price in the cart.
    def get_total_price(self):
        return self.total_price

# print_items(self): Prints all devices with their amounts in the cart.
    def print_items(self):
        if not self.items:
            print("Your cart is empty!")
        else:
            for device, amount in self.items:
                print("Name:", device.name, "Quantity:", amount, "Price:", device.price)


# checkout(self): Ensures all devices in the cart are available in the specified quantity.
# If they are, reduce the stock and print a receipt.
    def checkout(self):
        all_available = True

        if not self.items:
            print("Your cart is empty!")
            return

        for device, amount in self.items:
            if device.is_available(amount):
                print("Available")
            else:
                all_available = False
                print("Unavailable")
        if all_available:

            for device, amount in self.items:
                device.reduce_stock(amount)
            self.print_items()
            print("Checkout successful!")

            self.items = []
            self.total_price = 0

        else:
            print("Checkout failed. Not enough stock!")

# Part 3: Run the Application
# check test_main.py