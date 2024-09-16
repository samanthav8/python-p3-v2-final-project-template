# lib/models/toy.py
from models.__init__ import CURSOR, CONN
from models.kid import Kid

class Toy:

    all = {}

    def __init__(self, name, type, condition, kid_id, id=None):
        self.id = id
        self.name = name
        self.type = type
        self.condition = condition
        self.kid_id = kid_id

    def __repr__(self):
        return (
            f"<Toy {self.id}: {self.name}, {self.type}, {self.condition}, " +
            f"Kid ID: , {self.kid_id}>"
        )
    

    @classmethod
    def create_table(cls):
        """ Create the toy table to store the attributes of the Toy instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS toys(
            id INTEGER PRIMARY KEY,
            name TEXT,
            type TEXT,
            condition TEXT,
            kid_id INTEGER,
            FOREIGN KEY (kid_id) REFERENCES kids(id))
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

    def save(self):
        """ Insert a new row with the name,type, condition, and kid values of the current Toy instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key
        """
        sql = """
            INSERT INTO toys (name, type, condition, kid_id)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.type, self.condition, self.kid_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, type, condition, kid_id):
        """ Initialize a new Toy instance and save the object to the database """
        toy = cls(name, type, condition, kid_id)
        toy.save()
        return toy
    
    def update(self):
        """Update the table row corresponding to the current Toy instance."""
        sql = """
            UPDATE toys
            SET name = ?, type = ?, condition = ?, kid_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.type, self.condition, self.kid_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Toy instance"""
        sql = """
            DELETE FROM toys
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Toy object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        toy = cls.all.get(row[0])
        if toy:
            # ensure attributes match row values in case local object was modified
            toy.name = row[1]
            toy.type = row[2]
            toy.condition = row[3]
            toy.kid_id = row[4]
        else:
            # not in dictionary, create new instance and add to dictionary
            toy = cls(row[1], row[2], row[3], row[4])
            toy.id = row[0]
            cls.all[toy.id] = toy
        return toy
    
    @classmethod
    def get_all(cls):
        """Return a list containing a Toy object per row in the table"""
        sql = """
            SELECT *
            FROM toys
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Toy object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM toys
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None


    @classmethod
    def find_by_name(cls, name):
        """Return a Toy object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM toys
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None