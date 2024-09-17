# lib/cli.py

from helpers import (
    exit_program,
    list_kids,
    find_kid_by_name
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_kids()
        elif choice == "2":
            find_kid_by_name()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all kids")
    print("2. Find kid by name")


if __name__ == "__main__":
    main()
