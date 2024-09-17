# lib/cli.py

from helpers import (
    exit_program,
    list_kids,
    find_kid_by_name,
    find_kid_by_id,
    create_kid,
    update_kid,
    delete_kid,
    list_toys,
    find_toy_by_name,
    find_toy_by_id,
    create_toy,
    update_toy,
    delete_toy,
    list_kid_toys
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
        elif choice == "6":
            delete_kid()
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
            list_kid_toys()
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
    print("6. Unenroll your kid's from daycare")
    print("7. List all toys")
    print("8. Find toy by name")
    print("9. Find toy by id")
    print("10. Add a toy to the toy box")
    print("11. Update a toy's information")
    print("12. Remove a toy from the toy box")
    print("13. List all toys for a selected kid")


if __name__ == "__main__":
    main()
