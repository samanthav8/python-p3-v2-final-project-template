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


def create_child():
    name = input("What is the child's name? ")
    age = input("How old is the child? ")
    try:
        child = Child.create(name, int(age))
        print(f'{child.name} has been successfully enrolled to the daycare')
    except Exception as exc:
        print("There was an error enrolling the child: ", exc)


def update_child(child_id):
    if child := Child.find_by_id(child_id):
        try:
            name = input(f"Enter {child.name}'s new name. Press <enter> to keep current name : ")
            if name:
                child.name = name
            age = input(f"Enter {child.name}'s new age. Press <enter> to keep current age : ")
            if age:
                child.age = int(age)
            child.update()
            print(f'{child.name} has been successfully updated!')
        except Exception as exc:
            print(f"Sorry, there was an error updating {child.name}'s information. Please try again: ", exc)
    else:
        print(f'Sorry, no child found.')



def delete_child(child_id):
    if child := Child.find_by_id(child_id):
        child.delete()
        print(f'{child.name} has been unenrolled from the daycare.')
    else:
        print(f'Sorry, {child.name} could not be unenrolled.')

def create_toy(child):
    name = input("What is the toy's name? ")
    toy_type = input("What type of toy is it? ")
    condition = input("What condition is the toy in? ")
    
    try:
        toy = Toy.create(name, toy_type, condition, child.id)
        print(f'{toy.name} has been successfully added to {child.name}\'s toy box.')
    except Exception as exc:
        print(f"There was an error adding the toy to the toy box: {exc}")



def update_toy(toy_id):
    toy = Toy.find_by_id(toy_id)
    if toy:
        try:
            name = input(f"Enter the new name for {toy.name}. Press <enter> to keep current name : ")
            if name:
                toy.name = name
            toy_type = input(f"Enter the new type for {toy.name}. Press <enter> to keep current type : ")
            if toy_type:
                toy.toy_type = toy_type
            condition = input(f"Enter the new condition for {toy.name}. Press <enter> to keep current condition : ")
            if condition:
                toy.condition = condition

            toy.update()
            print(f'{toy.name} has been successfully updated in the toy box!')
        except Exception as exc:
            print(f"There was an error updating the toy's information: {exc}")
    else:
        print(f'Sorry, no toy found.')


def delete_toy(toy_id):
    if toy := Toy.find_by_id(toy_id):
        toy.delete()
        print(f'{toy.name} has been removed from the toy box')
    else:
        print(f'Sorry, {toy.name} could not be removed from the toy box.')
