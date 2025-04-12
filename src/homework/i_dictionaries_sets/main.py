#

import dictionary

def main():
    while True:
        print("\nInventory Menu")
        print("1 - Add or Update Item")
        print("2 - Delete Item")
        print("3 - Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            item = input("Enter item name: ")
            try:
                qty = int(input("Enter quantity to add/update: "))
                dictionary.add_inventory(item, qty)
                print(f"{item} updated. Current quantity: {dictionary.inventory[item]}")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "2":
            item = input("Enter item name to delete: ")
            if dictionary.remove_inventory_widget(item):
                print(f"{item} removed from inventory.")
            else:
                print(f"{item} not found.")
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()