# lib/helpers.py
from models.child import Child
from models.toy import Toy


def exit_program():
    print("Have a nice day!")
    exit()

def list_children():
    children = Child.get_all()
    if children:
        print("Here are all children currently enrolled in the daycare:")
        for i,child in enumerate(children, start=1):
            print(f"{i}. {child.name}")
        return children
    else:
        print("There are no children enrolled in the daycare at this moment.")

def find_child_by_name():
    name = input("Please enter the child's name: ")
    child = Child.find_by_name(name)
    print(child) if child else print(
        f'Sorry, there is no child named {name} in our daycare.'
    )

def find_child_by_id():
    id_ = input("Please enter the child's id: ")
    child = Child.find_by_id(id_)
    print(child) if child else print(f'Sorry, there is no child with the id of {id_}')

def create_child():
    name = input("What is the child's name? ")
    age = input("How old is the child? ")
    try:
        child = Child.create(name, int(age))
        print(f'{child.name} has been successfully enrolled to the daycare')
    except Exception as exc:
        print("There was an error enrolling the child: ", exc)


def update_child():
    id_ = input("Please enter the child's id: ")
    if child := Child.find_by_id(id_):
        try:
            name = input("Enter the child's new name: ")
            child.name = name
            age = input("Enter the child's new age: ")
            child.age = int(age)  # Convert age to an integer

            child.update()
            print(f'{child.name} has been successfully updated!')
        except Exception as exc:
            print("Sorry, there was an error updating {child.name}'s information. Please try again: ", exc)
    else:
        print(f'Sorry, no child found with the id of {id_}.')


def delete_child():
    id_ = input("Please enter the child's id: ")
    if child := Child.find_by_id(id_):
        child.delete()
        print(f'{child.name} has been unenrolled from the daycare.')
    else:
        print(f'Sorry, no child found with the id of {id_}.')

def list_toys():
    toys = Toy.get_all()
    if toys:
        print("Here are all the toys in the toy box:")
        for toy in toys:
            print(toy)
    else:
        print("The toy box is empty.")

def find_toy_by_name():
    name = input("Please enter the toy's name: ")
    toy = Toy.find_by_name(name)
    print(toy) if toy else print(
        f'Sorry, there is no toy named {name} in the toy box.'
    )

def find_toy_by_id():
    id_ = input("Please enter the toy's id: ")
    toy = Toy.find_by_id(id_)
    print(toy) if toy else print(f'Sorry, there is no toy with the id of {id_}.')

def create_toy():
    name = input("What is the toy's name?")
    type = input("What type of toy is it?")
    condition = input("What condition is the toy in?")
    child_id = input("Which child does this toy belong to? Please enter the child's id: ")
    try:
        toy = Toy.create(name, type, condition, int(child_id))
        print(f'{toy.name} has been successfully added to the toy box')
    except Exception as exc:
        print("There was an error adding {toy.name} to the toy box:  ", exc)

def update_toy():
    id_ = input("Please enter the toy's id: ")
    if toy := Toy.find_by_id(id_):
        try:
            name = input("Enter the toy's new name: ")
            toy.name = name
            type = input("Enter the toy's new type: ")
            toy.type = type
            condition = input("Enter the toy's new condition:")
            toy.condition = condition
            child_id = input("Enter the child's id who now owns the toy:")
            toy.child_id = int(child_id)

            toy.update()
            print(f'{toy.name} has been updated in the toy box!')
        except Exception as exc:
            print("There was an error updating the toy's information: ", exc)
    else:
        print(f'Sorry, no toy found with the id of {id_}.')

def delete_toy():
    id_ = input("Please enter the toy's id: ")
    if toy := Toy.find_by_id(id_):
        toy.delete()
        print(f'{toy.name} has been removed from the toy box')
    else:
        print(f'Sorry, no toy found with the id of {id_}.')


def list_child_toys():
    child_id = input("Please enter the child's id: ")
    child = Child.find_by_id(child_id)
    
    if child:
        toys = child.toys()
        if toys:
            print(f"Toys belonging to {child.name}:")
            for toy in toys:
                print(toy)
        else:
            print(f"{child.name} doesn't have any toys.")
    else:
        print(f"Sorry, no child found with the id of {child_id}.")
