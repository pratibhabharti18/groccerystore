# grocery_inventory_management.py

# Initialize an empty inventory dictionary to store item information
inventory = {}

def add_item():
    print("Add a new item to the inventory.")
    item_name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))
    inventory[item_name] = {'quantity': quantity, 'price': price}
    print(f"{item_name} added to the inventory.")

def update_quantity():
    print("Update the quantity of an existing item.")
    item_name = input("Enter item name to update quantity: ")
    if item_name in inventory:
        new_quantity = int(input("Enter new quantity: "))
        inventory[item_name]['quantity'] = new_quantity
        print(f"Quantity updated for {item_name}.")
    else:
        print(f"Item not found in inventory.")

def view_inventory():
    print("View the current inventory.")
    print("\nCurrent Inventory:")
    for item_name, item_info in inventory.items():
        print(f"{item_name}: Quantity - {item_info['quantity']}, Price - {item_info['price']}")

def remove_item():
    print("Remove an item from the inventory.")
    item_name = input("Enter item name to remove: ")
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} removed from the inventory.")
    else:
        print(f"Item not found in inventory.")

# Main program loop
while True:
    # Display menu options
    print("\nMenu Options:")
    print("1. Add new item to inventory")
    print("2. Update existing item quantity")
    print("3. View current inventory")
    print("4. Remove item from inventory")
    print("5. Exit")

   
 # Get user input for menu selection
    choice = input("Enter your choice (1-5): ")

    # Process user input based on menu selection
    if choice == '1':
        add_item()
    elif choice == '2':
        update_quantity()
    elif choice == '3':
        view_inventory()
    elif choice == '4':
        remove_item()
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

