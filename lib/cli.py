# lib/cli.py

from helpers import (
    exit_program,
    list_children,
    create_child,
    update_child,
    delete_child,
    create_toy,
    update_toy,
    delete_toy
)

def border():
    print("\n" + "="*40 + "\n")

def line():
    print("\n")

def main_menu():
    while True:
        line()
        print("Welcome to the Daycare!")
        border()
        print("Please choose from the following options:")
        line()
        print("Type C or c to see the list of children")
        print("Type E or e to exit")

        choice = input("> ").lower()

        if choice == 'c':
            border()
            child_menu()
        elif choice == 'e':
            border()
            exit_program()
        else:
            print("Not a valid selection. Please try again")

def child_menu():
    while True:
        children = list_children()
        if children:
            border()
            print("Type the number to view the child's profile")
            print("Type A or a to add a new child")
            print("Type B or b to go back to the previous menu")
            print("Type E or e to exit")

            choice = input("> ").lower()

            if choice == 'a':
                border()
                create_child()
                line()
            elif choice == 'b':
                line()
                return  
            elif choice == 'e':
                line()
                exit_program()
            elif choice.isdigit() and 1 <= int(choice) <= len(children):
                child = children[int(choice) - 1] 
                border()
                child_details_menu(child)
            else:
                line()
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

        border()
        print("Type the number of a toy to view information about that toy")
        print("Type A or a to add a new toy")
        print("Type D or d to delete this child")
        print("Type U or u to update the child")
        print("Type B or b to go back to the children list")
        print("Type E or e to exit")

        choice = input("> ").lower()

        if choice == 'a':
            border()
            create_toy(child)
            line()
        elif choice == 'b':
            line()
            return  
        elif choice == 'u':
            border()
            update_child(child)
            line()
        elif choice == 'e':
            line()
            exit_program()
        elif choice.isdigit() and 1 <= int(choice) <= len(toys):
            toy = toys[int(choice) - 1]
            border()
            toy_details_menu(toy)
        elif choice == 'd':
            line()
            delete_child(child)
            return
        else:
            print("Not a valid selection. Please try again")

def toy_details_menu(toy):
    while True:
        print(f"Name: {toy.name}")
        print(f"Type of toy: {toy.toy_type}")
        print(f"Condition: {toy.condition}")
        border()
        print("Type D or d to delete this toy")
        print("Type U or u to update this toy")
        print("Type B or b to go back")
        print("Type E or e to exit")

        choice = input("> ").lower()

        if choice == 'd':
            line()
            delete_toy(toy)
            return
        elif choice == 'u':
            border()
            update_toy(toy)
            line()
        elif choice == 'b':
            line()
            return
        elif choice == 'e':
            line()
            exit_program()
        else:
            print("Not a valid selection. Please try again")


if __name__ == "__main__":
    main_menu()
