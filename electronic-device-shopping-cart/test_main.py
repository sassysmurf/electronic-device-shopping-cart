# Part 3: Run the Application


from main import Smartphone
from main import Laptop
from main import Tablet
from main import Cart

# Create Different Devices: Create at least 20 devices and add them to the device list,
# with varying names, prices, and stock quantities.

# smartphones

phone1 = Smartphone("iPhone 13", 700, 10, 24, 6.1, 20)
phone2 = Smartphone("Samsung Galaxy S24", 850, 12, 24, 6.2, 22)
phone3 = Smartphone("iPhone 15", 900, 15, 24, 6.1, 20)
phone4 = Smartphone("Google Pixel 8", 750, 10, 24, 6.2, 24)
phone5 = Smartphone("OnePlus 12", 800, 7, 24, 6.8, 18)
phone6 = Smartphone("Xiaomi 14", 680, 13, 24, 6.36, 21)

# laptops

laptop1 = Laptop("Macbook Pro", 3600, 8, 24, 8, 4.8)
laptop2 = Laptop("Dell XPS 15", 2200, 6, 24, 16, 5.0)
laptop3 = Laptop("HP Pavilion", 1100, 9, 24, 16, 4.2)
laptop4 = Laptop("Lenovo ThinkPad", 1500, 5, 24, 32, 4.5)
laptop5 = Laptop("Asus ZenBook", 1300, 8, 24, 16, 4.7)
laptop6 = Laptop("Acer Aspire", 850, 12, 24, 8, 3.8)
laptop7 = Laptop("MSI Gaming Laptop", 2400, 4, 24, 32, 5.2)

# tablets
tablet1 = Tablet("Samsung", 1200, 11, 24, 14.6, 700)
tablet2 = Tablet("iPad Air", 950, 9, 24, "2360x1640", 460)
tablet3 = Tablet("Samsung Galaxy Tab S9", 900, 8, 24, "2560x1600", 500)
tablet4 = Tablet("iPad Pro", 1400, 6, 24, "2732x2048", 466)
tablet5 = Tablet("Lenovo Tab P12", 550, 10, 24, "2944x1840", 615)
tablet6 = Tablet("Microsoft Surface Go", 700, 7, 24, "1920x1280", 544)
tablet7 = Tablet("Xiaomi Pad 6", 450, 14, 24, "2880x1800", 490)


devices = [phone1, laptop1, tablet1]
devices.extend([phone2, laptop2, tablet2])
devices.extend([
    phone3, phone4, phone5, phone6,
    laptop3, laptop4, laptop5, laptop6, laptop7,
    tablet3, tablet4, tablet5, tablet6, tablet7
])



cart = Cart()

# Show User Menu: Implement a simple menu-driven application that presents the following
# options to the user:
# #1 Show Devices: Display a list of all available devices with their details
# (name, price, stock, etc.).
# #2 Show Cart: Display the current items in the user's shopping cart.
# #3 Exit: Exit the program.

# Show Devices: When the user selects option #1 (Show Devices), the system
# will display all the available devices with their details (name, price, stock, etc.).
# Each device in the list will have a corresponding option to allow the user to
# choose which device they want to add to the cart.

# Show Cart: When the user selects option #2 (Show Cart), the system will display
# the devices that have been added to the cart along with their quantities and total price.


def show_menu():

    while True:
        print("1. Show Devices")
        print("2. Show cart")
        print("3. Exit program")
        print("4. Checkout")
        choice = input("Choose an option: ")

        if choice == "1":
            for index, device in enumerate(devices, start=1):
                print(index, type(device).__name__)
                device.display_info()

            try:
                device_choice = int(input("Choose a device: "))
                if device_choice >= 1 and device_choice <= len(devices):
                    selected_device = devices[device_choice - 1]
                    units = int(input("How many? "))
                    if units <=0:
                        print("Invalid quantity. Please enter a number greater than zero.")
                    else:
                        cart.add_device(selected_device, units)
                else:
                    print("Invalid device choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            cart.print_items()
            print(f"Total price: {cart.get_total_price():.2f}")
        elif choice == "3":
            print("Exiting program...")
            break
        elif choice == "4":
            cart.checkout()
        else:
            print("Invalid choice. Please try again.")

show_menu()







