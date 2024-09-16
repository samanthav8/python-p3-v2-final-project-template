#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.kid import Kid
from models.toy import Toy
import ipdb

def reset_database():
    Kid.drop_table()
    Kid.create_table()
    Toy.drop_table()
    Toy.create_table()

    sam = Kid.create("Sam", "3")
    ceci = Kid.create("Ceci", "4")

    buzz = Toy.create("Buzz", "Action figure", "New", "2")
    bear = Toy.create("Bear", "Stuffed Animal", "New", "1")
    barbie = Toy.create("Barbie", "Doll", "New", "1")
    barbie.delete()



reset_database()
ipdb.set_trace()
