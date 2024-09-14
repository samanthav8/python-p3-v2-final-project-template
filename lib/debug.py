#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.kid import Kid
from models.toy import Toy
import ipdb

Kid.drop_table()
Kid.create_table()
Toy.drop_table()
Toy.create_table()

Kid.create("Sam", "3")
Kid.create("Ceci", "4")
buzz = Toy.create("Buzz", "Action figure", "New", "2")
buzz.delete()

ipdb.set_trace()
