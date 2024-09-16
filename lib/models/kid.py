# lib/models/kid.py
from models.__init__ import CURSOR, CONN

class Kid:

    all={}


    def __init__(self, name, age, id=None,):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Kid {self.id}: {self.name}, {self.age}>"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if isinstance(age, int) and age > 0:
            self._age = age
        else:
            raise ValueError("Age must be a positive integer")

    @classmethod
    def create_table(cls):
        """ Create a new table to presist the attributes of the Kid instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS kids(
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Kid instances """
        sql = """
            DROP TABLE IF EXISTS kids;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and age values of the current Kid instance.
        Update object id attribute using the primary key value of new row.
        """
        sql = """
            INSERT INTO kids (name, age)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.age))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self


    @classmethod
    def create(cls, name, age):
        """ Initialize a new Kid instance and save the object to the database """
        kid = cls(name, age)
        kid.save()
        return kid
    
    def update(self):
        """Update the table row corresponding to the current Kid instance."""
        sql = """
            UPDATE kids
            SET name = ?, age = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.age, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Kid instance +
        delete the dictionary entry + reassign id attribute"""


        sql = """
            DELETE FROM kids
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Kid object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        kid = cls.all.get(row[0])
        if kid:
            # ensure attributes match row values in case local object was modified
            kid.name = row[1]
            kid.age = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            kid = cls(row[1], row[2])
            kid.id = row[0]
            cls.all[kid.id] = kid
        return kid
    
    @classmethod
    def get_all(cls):
        """Return a list containing a Kid object per row in the table"""
        sql = """
            SELECT *
            FROM kids
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return a Kid object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM kids
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """Return a Kid object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM kids
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def toys(self):
        """Return list of toys associated with current department"""
        from models.toy import Toy
        sql = """
            SELECT * FROM toys
            WHERE kid_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Toy.instance_from_db(row) for row in rows
        ]
