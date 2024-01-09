class VendingMachine:
    def __init__(self):
        self.items = {
            '1': {'name': 'Soda', 'price': 1.50, 'quantity': 10},
            '2': {'name': 'Chips', 'price': 1.00, 'quantity': 20},
            '3': {'name': 'Candy', 'price': 0.75, 'quantity': 15},
            '3': {'name': 'Chocolate milk', 'price': 2.00, 'quantity': 1}
        }

    def display_items(self):
        print("Available Items:")
        for code, item in self.items.items():
            print(f"{code}: {item['name']} - ${item['price']} - Quantity: {item['quantity']}")

    def buy_item(self):
        self.display_items()
        choice = input("Enter the code of the item you want to purchase: ")
        if choice in self.items:
            quantity = int(input("Enter the quantity: "))
            if self.items[choice]['quantity'] >= quantity:
                total_price = self.items[choice]['price'] * quantity
                print(f"Total price: ${total_price}")
                if input("Confirm purchase? (y/n): ").lower() == 'y':
                    self.items[choice]['quantity'] -= quantity
                    print(f"You purchased {quantity} {self.items[choice]['name']}(s). Enjoy!")
                else:
                    print("Transaction canceled.")
            else:
                print("Insufficient quantity available.")
        else:
            print("Invalid code.")

# Usage example:
vending_machine = VendingMachine()
vending_machine.buy_item()