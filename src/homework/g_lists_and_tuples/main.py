#
import lists
from lists import get_lowest_list_value, get_highest_list_value

def main():
    while True:
        print("\nMenu:")
        print("1- Show the list low/high values")
        print("2- Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            numbers = []
            while True:
                try:
                    num = int(input("Enter a list value: "))
                    numbers.append(num)
                    if len(numbers) >= 3:
                        cont = input("Do you want to enter another value? (yes/no): ").strip().lower()
                        if cont != "yes":
                            break
                except ValueError:
                    print("Please enter a valid number.")

            if numbers:
                print(f"Lowest value: {get_lowest_list_value(numbers)}")
                print(f"Highest value: {get_highest_list_value(numbers)}")

        elif choice == "2":
            print("Existing program.")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")

main()