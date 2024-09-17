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

