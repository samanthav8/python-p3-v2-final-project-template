# lib/helpers.py
from models.child import Child
from models.toy import Toy


def exit_program():
    print("Goodbye!")
    exit()

def list_children():
    children = Child.get_all()
    for child in children:
        print(child)

def find_child_by_name():
    name = input("Enter the child's name: ")
    child = Child.find_by_name(name)
    print(child) if child else print(
        f'There is no {name} in this daycare'
    )

def find_child_by_id():
    id_ = input("Enter the child's id: ")
    child = Child.find_by_id(id_)
    print(child) if child else print(f'There is no child with the id of {id_}')

def create_child():
    name = input("What is the child's name?")
    age = input("How old is your child?")
    try:
        child = Child.create(name, int(age))
        print(f'{child} has been successfully added to the daycare')
    except Exception as exc:
        print("Error in enrolling your child: ", exc)


def update_child():
    id_ = input("Enter the child's id: ")
    if child := Child.find_by_id(id_):
        try:
            name = input("Enter the child's new name: ")
            child.name = name
            age = input("Enter the child's new age: ")
            child.age = int(age)  # Convert age to an integer

            child.update()
            print(f'Success: {child}')
        except Exception as exc:
            print("Error updating child's information: ", exc)
    else:
        print(f'Child with the id of {id_} not found')


def delete_child():
    id_ = input("Enter the child's id: ")
    if child := Child.find_by_id(id_):
        child.delete()
        print(f'Child with the id of {id_} has been deleted')
    else:
        print(f'Child with the id of {id_} not found')

def list_toys():
    toys = Toy.get_all()
    for toy in toys:
        print(toy)

def find_toy_by_name():
    name = input("Enter the toy's name: ")
    toy = Toy.find_by_name(name)
    print(toy) if toy else print(
        f'There is no toy named {name} in the toy box'
    )

def find_toy_by_id():
    id_ = input("Enter the Toy's id: ")
    toy = Toy.find_by_id(id_)
    print(toy) if toy else print(f'There is no toy with the id of {id_}')

def create_toy():
    name = input("What is the toy's name?")
    type = input("What type of toy is it?")
    condition = input("What condition is the toy in?")
    child_id = input("Who's toy is it? Please enter the child's id: ")
    try:
        toy = Toy.create(name, type, condition, int(child_id))
        print(f'{toy} has been successfully added to the toy box')
    except Exception as exc:
        print("Could not add the toy into the toy box ", exc)

def update_toy():
    id_ = input("Enter the toy's id: ")
    if toy := Toy.find_by_id(id_):
        try:
            name = input("Enter the toy's new name: ")
            toy.name = name
            type = input("Enter the toy's new type: ")
            toy.type = type
            condition = input("Enter the toy's new condition:")
            toy.condition = condition
            child_id = input("Enter the child's id in which the toy now belongs to:")
            toy.child_id = int(child_id)

            toy.update()
            print(f'{toy.name} has been updated!')
        except Exception as exc:
            print("Error updating toy's information: ", exc)
    else:
        print(f'Toy with the id of {id_} not found')

def delete_toy():
    id_ = input("Enter the toy's id: ")
    if toy := Toy.find_by_id(id_):
        toy.delete()
        print(f'{toy.name} has been removed from the toy box')
    else:
        print(f'Toy with the id of {id_} not found')


def list_child_toys():
    child_id = input("Enter the child's id: ")
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
        print(f"No child found with id {child_id}")
