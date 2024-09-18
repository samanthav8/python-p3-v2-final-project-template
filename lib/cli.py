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
            print("Not a valid selection. Please try again")

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
                print("Not a valid selection. Please try again")
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
        print("Type D or d to delete this child")
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
            toy_details_menu(toy)
        elif choice == 'd':
            delete_child(child.id)
            return
        else:
            print("Not a valid selection. Please try again")

def toy_details_menu(toy):
    while True:
        print(f"Name: {toy.name}")
        print(f"Type of toy: {toy.toy_type}")
        print(f"Condition: {toy.condition}")
        print("Type D or d to delete this toy")
        print("Type U or u to update this toy")
        print("Type B or b to go back")
        print("Type E or e to exit")

        choice = input("> ").lower()

        if choice == 'd':
            delete_toy(toy.id)
            return
        elif choice == 'u':
            update_toy(toy.id)
        elif choice == 'b':
            return
        elif choice == 'e':
            exit_program()
        else:
            print("Not a valid selection. Please try again")


if __name__ == "__main__":
    main_menu()
