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

def main_menu():
    while True:
        print("Welcome to the Daycare!")
        print("Please choose from the following options")
        print("Type C or c to see the list of children")
        print("Type E or e to exit")

        choice = input("> ").lower()

        if choice == 'c':
            child_menu()
        elif choice == 'e':
            exit_program()
        else:
            print("Invalid choice. Please try again.")

def child_menu():
    while True:
        children = list_children()
        if children:
            print("Type the number to view the child's profile")
            print("Type A or a to add a new child")
            print("Type B or b to go back to the previous menu")
            print("Type E or e to exit")

            choice = input("> ").lower()

            if choice == 'a':
                create_child()
            elif choice == 'b':
                return  
            elif choice == 'e':
                exit_program()
            elif choice.isdigit() and 1 <= int(choice) <= len(children):
                child = children[int(choice) - 1] 
                child_details_menu(child)
            else:
                print("Invalid choice. Please try again.")
        else:
            return  

def child_details_menu(child):
    while True:
        print(f"{child.name}'s Daycare Profile")
        print(f"Age: {child.age}")
        print("Toys:")
        toys = child.toys()
        if toys:
            for i, toy in enumerate(toys, start=1):
                print(f"{i}. {toy.name}")
        else:
            print(f"{child.name} has no toys in the toy box")

        print("Type the number of a toy to view information about that toy")
        print("Type A or a to add a new toy")
        print("Type D or d to delete a toy")
        print("Type U or u to update the child")
        print("Type B or b to go back to the children list")
        print("Type E or e to exit")

        choice = input("> ").lower()

        if choice == 'a':
            create_toy(child)
        elif choice == 'b':
            return  
        elif choice == 'u':
            update_child(child.id)
        elif choice == 'e':
            exit_program()
        elif choice.isdigit() and 1 <= int(choice) <= len(toys):
            toy = toys[int(choice) - 1]
            pass
        elif choice == 'd':
            toy_index = input("Enter the number of the toy to remove from the toy box: ")
            if toy_index.isdigit() and 1 <= int(toy_index) <= len(toys):
                toy_to_delete = toys[int(toy_index) - 1]
                toy_to_delete.delete()
                print(f"{toy_to_delete.name} has been removed from the toy box.")
            else:
                print("No toy exists with that number. Please try again")
        else:
            print("Invalid choice. Please try again.")

# def main():
#    while True:
#        menu()
#        choice = input("> ")
#        if choice == "0":
#            exit_program()
#        elif choice == "1":
#            list_children()
#        elif choice == "2":
#            find_child_by_name()
#        elif choice == "3":
#            find_child_by_id()
#        elif choice == "4":
#            create_child()
#        elif choice == "5":
#            update_child()
#        elif choice == "6":
#            delete_child()
#        elif choice == "7":
#            list_toys()
#        elif choice == "8":
#            find_toy_by_name()
#        elif choice == "9":
#            find_toy_by_id()
#        elif choice == "10":
#            create_toy()
#        elif choice == "11":
#            update_toy()
#        elif choice == "12":
#            delete_toy()
#        elif choice == "13":
#            list_child_toys()
#        else:
#            print("Invalid choice. Please try again!")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all children")
    print("2. Find child by name")
    print("3. Find child by id")
    print("4. Enroll child in daycare")
    print("5. Update a child's information")
    print("6. Unenroll a child from daycare")
    print("7. List all toys")
    print("8. Find toy by name")
    print("9. Find toy by id")
    print("10. Add a toy to the toy box")
    print("11. Update a toy's information")
    print("12. Remove a toy from the toy box")
    print("13. List all toys for a selected child")


if __name__ == "__main__":
    main_menu()
