#
import i_dictionaries_sets
from src.homework.i_dictionaries_sets import get_p_distance_matrix

def get_input_lists():
    n = int(input("Enter number of DNA strings (<=10): "))
    dna_lists = []
    for i in range(n):
        dna_string = input(f"Enter DNA string {i+1} (ex: TTTC...): ").strip().upper()
        dna_lists.append(list(dna_string))
    return dna_lists

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{val:.5f}" for val in row))

def main():
    while True:
        print("\n1 - Get p distance matrix\n2 - Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            lists = get_input_lists()
            matrix = get_p_distance_matrix(lists)
            print_matrix(matrix)
        elif choice == '2':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()