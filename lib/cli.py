# lib/cli.py

from helpers import (
    exit_program,
    list_children,
    find_child_by_name,
    find_child_by_id,
    create_child,
    update_child,
    delete_child,
    list_toys,
    find_toy_by_name,
    find_toy_by_id,
    create_toy,
    update_toy,
    delete_toy,
    list_child_toys
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_children()
        elif choice == "2":
            find_child_by_name()
        elif choice == "3":
            find_child_by_id()
        elif choice == "4":
            create_child()
        elif choice == "5":
            update_child()
        elif choice == "6":
            delete_child()
        elif choice == "7":
            list_toys()
        elif choice == "8":
            find_toy_by_name()
        elif choice == "9":
            find_toy_by_id()
        elif choice == "10":
            create_toy()
        elif choice == "11":
            update_toy()
        elif choice == "12":
            delete_toy()
        elif choice == "13":
            list_child_toys()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all children")
    print("2. Find child by name")
    print("3. Find child by id")
    print("4. Enroll child in daycare")
    print("5. Update your child's information")
    print("6. Unenroll your child from daycare")
    print("7. List all toys")
    print("8. Find toy by name")
    print("9. Find toy by id")
    print("10. Add a toy to the toy box")
    print("11. Update a toy's information")
    print("12. Remove a toy from the toy box")
    print("13. List all toys for a selected child")


if __name__ == "__main__":
    main()
