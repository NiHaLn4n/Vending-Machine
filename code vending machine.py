# Define the vending machine menu
menu = [
    {"code": "1", "item": "Chocolate", "price": 1.50},
    {"code": "2", "item": "Chips", "price": 2.00},
    {"code": "3", "item": "Coffee", "price": 1.25},
    {"code": "4", "item": "Biscuit", "price": 1.00},
    {"code": "5", "item": "Juice", "price": 2.50},
]

def display_menu():
    """Displays the vending machine menu."""
    print("\n--- Vending Machine Menu ---")
    print("Code | Item        | Price ($)")
    print("----------------------------")
    for item in menu:
        print(f"{item['code']:4} | {item['item']:10} | {item['price']:.2f}")
    print("----------------------------")

def select_item():
    """Prompts the user to select an item by its code."""
    while True:
        code = input("Enter the code of the item you'd like to purchase: ").strip()
        for item in menu:
            if item["code"] == code:
                return item
        print("Invalid code. Please enter a valid code from the menu.")

def process_payment(price):
    """Processes payment using coins or cash."""
    total_inserted = 0
    print(f"The item costs ${price:.2f}. Insert cash or coins.")
    while total_inserted < price:
        try:
            inserted = float(input(f"Insert money (total inserted: ${total_inserted:.2f}): "))
            if inserted > 0:
                total_inserted += inserted
            else:
                print("Please insert a positive amount.")
        except ValueError:
            print("Invalid input. Please insert valid cash or coin amounts.")
    return total_inserted - price

def make_suggestion(selected_item):
    """Suggests an additional purchase based on the selected item."""
    suggestions = {
        "Coffee": "Biscuit",
        "Chips": "Juice",
        "Chocolate": "Water",
        "Biscuit": "Juice",
        "Juice": "Chips"
    }
    suggestion = suggestions.get(selected_item["item"])
    if suggestion:
        print(f"Suggestion: How about pairing your {selected_item['item']} with a {suggestion}?")

def main():
    """Main function to run the vending machine."""
    print("Welcome to the Vending Machine!")
    while True:
        display_menu()
        selected_item = select_item()
        print(f"You selected {selected_item['item']} for ${selected_item['price']:.2f}.")
        
        change = process_payment(selected_item["price"])
        print(f"Dispensing {selected_item['item']}... Enjoy!")
        
        if change > 0:
            print(f"Your change is ${change:.2f}.")
        else:
            print("No change due. Thank you for the exact payment!")
        
        make_suggestion(selected_item)
        
        another_purchase = input("Would you like to make another purchase? (yes/no): ").strip().lower()
        if another_purchase != "yes":
            print("Thank you for using the Vending Machine. Goodbye!")
            break

# Start the program
if __name__ == "__main__":
    main()