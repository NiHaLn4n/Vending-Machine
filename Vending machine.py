class Item:
    def __init__(self, code, name, category, price, stock):
        # To initialize the item with its code, name, category, price, and stock level
        self.code = code  # To store the item code
        self.name = name  # To store the item name
        self.category = category  # To store the item category
        self.price = price  # To store the item price
        self.stock = stock  # To store the item stock level

    def dispense(self):
        # To dispense the item if it is in stock
        if self.stock > 0:  # To check if the item is in stock
            self.stock -= 1  # To reduce stock by one
            return True  # To return True indicating successful dispense
        return False  # To return False if the item is out of stock

class VendingMachine:
    def __init__(self, name):
        # To initialize the vending machine with a name and a list of items
        self.name = name  # To store the vending machine name
        self.items = [  # To store the list of items in the vending machine
            Item('1', 'Coca-Cola', 'Drink', 2.50, 10),
            Item('2', 'Pepsi', 'Drink', 2.50, 10),
            Item('3', 'Orange Juice', 'Drink', 2.00, 8),
            Item('4', 'Milkshake', 'Snack', 3.00, 5),
            Item('5', 'Red Bull', 'Drink', 1.00, 20),
            Item('6', 'Frappuccino', 'Drink', 5.00, 10),
            Item('7', 'Coffee', 'Hot Drink', 2.50, 12)
        ]
        self.balance = 0.0  # To initialize the balance to zero

    def display_menu(self):
        # To display the menu of items available in the vending machine
        print(f"\n--- Welcome to {self.name}! ---")
        for item in self.items:  # To loop through each item
            print(f"{item.code}: {item.name} ({item.category}) - {item.price:.2f} AED | Stock: {item.stock}")

    def get_item_by_code(self, code):
        # To retrieve an item from the vending machine by its code
        for item in self.items:  # To loop through each item
            if item.code == code:  # To check if the item code matches
                return item  # To return the item if found
        return None  # To return None if the item is not found

    def insert_money(self, amount):
        # To insert money into the vending machine and update the balance
        self.balance += amount  # To increase balance by the inserted amount
        print(f"Balance: {self.balance:.2f} AED")

    def calculate_change(self, item_price):
        # To calculate the change to be returned to the user
        change = self.balance - item_price  # To calculate change
        self.balance = 0  # To reset the balance after giving change
        return change  # To return the change

    def select_item(self, code):
        # To select an item based on its code and process the purchase
        item = self.get_item_by_code(code)  # To get the item by code
        if item:
            if item.stock == 0:  # To check if the item is out of stock
                print("Item out of stock.")
            elif self.balance < item.price:  # To check if there are insufficient funds
                print("Insufficient funds.")
            else:
                self.balance -= item.price  # To deduct item price from balance
                if item.dispense():  # To attempt to dispense the item
                    print(f"Dispensing {item.name}...")
                    change = self.calculate_change(item.price)  # To calculate change
                    if change > 0:
                        print(f"Change: {change:.2f} AED")  # To print the change if any
                else:
                    print("Failed to dispense item.")
        else:
            print("Invalid item code.")  # To print error if item code is invalid

    def run(self):
        # To run the main loop of the vending machine
        while True:
            self.display_menu()  # To display the menu
            code = input("Enter item code: ").strip().upper()  # To get item code from user
            amount = float(input("Insert money: "))  # To get money from user
            self.insert_money(amount)  # To insert the money
            self.select_item(code)  # To select and dispense the item
            if input("Make another purchase? (yes/no): ").strip().lower() != "yes":
                print(f"Thank you for using {self.name}. Goodbye!")
                break  # To exit the loop if user doesn't want to make another purchase

# To create and run the vending machine
vending_machine = VendingMachine("Snack Corner")  # To create a vending machine
vending_machine.run()  # To run the vending machine

