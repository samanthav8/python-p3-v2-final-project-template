# lib/helpers.py
from models.kid import Kid
from models.toy import Toy


def exit_program():
    print("Goodbye!")
    exit()

def list_kids():
    kids = Kid.get_all()
    for kid in kids:
        print(kid)

def find_kid_by_name():
    name = input("Enter the kid's name: ")
    kid = Kid.find_by_name(name)
    print(kid) if kid else print(
        f'There is no {name} in this daycare'
    )

def find_kid_by_id():
    id_ = input("Enter the Kid's id: ")
    kid = Kid.find_by_id(id_)
    print(kid) if kid else print(f'There is no kid with the id of {id_}')

def create_kid():
    name = input("What is the kids name?")
    age = input("How old is your kid?")
    try:
        kid = Kid.create(name, int(age))
        print(f'{kid} has been successfully added to the daycare')
    except Exception as exc:
        print("Error in enrolling your kid: ", exc)


def update_kid():
    id_ = input("Enter the kid's id: ")
    if kid := Kid.find_by_id(id_):
        try:
            name = input("Enter the kid's new name: ")
            kid.name = name
            age = input("Enter the kid's new age: ")
            kid.age = int(age)  # Convert age to an integer

            kid.update()
            print(f'Success: {kid}')
        except Exception as exc:
            print("Error updating kids information: ", exc)
    else:
        print(f'Kid with the id of {id_} not found')


def delete_kid():
    id_ = input("Enter the kid's id: ")
    if kid := Kid.find_by_id(id_):
        kid.delete()
        print(f'Kid with the of {id_} has been deleted')
    else:
        print(f'Kid with the id of {id_} not found')
