# lib/cli.py

from helpers import (
    exit_program,
    list_kids,
    find_kid_by_name,
    find_kid_by_id,
    create_kid,
    update_kid
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
        elif choice == "3":
            find_kid_by_id()
        elif choice == "4":
            create_kid()
        elif choice == "5":
            update_kid()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all kids")
    print("2. Find kid by name")
    print("3. Find kid by id")
    print("4. Enroll kid in daycare")
    print("5. Update your kid's information")


if __name__ == "__main__":
    main()
