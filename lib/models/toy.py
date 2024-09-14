# lib/models/toy.py
from models.__init__ import CURSOR, CONN
from models.kid import Kid

class Toy:
    def __init__(self, id, name, type, condition, kid_id):
        self.id = id
        self.name = name
        self.type = type
        self.condition = condition
        self.kid_id = kid_id

    @classmethod
    def create_table(cls):
        """ Create the toy table to store the attributes of the Toy instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS toys(
            id INTEGER PRIMARY KEY,
            name TEXT,
            type TEXT,
            condition TEXT,
            kid_id INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that stores Kid instances """
        sql = """
            DROP TABLE IF EXISTS toys;
        """
        CURSOR.execute(sql)
        CONN.commit()

