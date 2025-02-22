#
from unittest import result
import repetition

def main():
    repetition.get_factorial(1)
    repetition.sum_odd_numbers(1)
    while True:
        print("Homework 3 Menu")
        print("1 - Factorial")
        print("2 - Sum odd numbers")
        print("3 - Exit")

        option = input("Select an Option: ")

        if option == '1':
            num = int(input("Enter a number: "))
            print("The factorial of", num, "is", repetition.get_factorial(num))
        elif option == '2':
            num = int(input("Enter a number: "))
            print("The sum of odd numbers up to", num, "is", repetition.sum_odd_numbers(num))
        elif option == '3':
            print("Do you wish to continue?")

        
main()
    
