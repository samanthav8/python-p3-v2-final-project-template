from models.__init__ import CONN, CURSOR
from models.child import Child
from models.toy import Toy

def seed_database():
    Child.drop_table()
    Child.create_table()
    Toy.drop_table()
    Toy.create_table()

    Child.create("Sam", 3)
    Child.create("Ceci", 4)
    Child.create("Justin", 4)
    Child.create("Alyssa", 2)

    Toy.create("Buzz", "Action figure", "New", 3)
    Toy.create("Bear", "Stuffed Animal", "New", 1)
    Toy.create("Barbie", "Doll", "New", 1)

seed_database()