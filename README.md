# Daycare Toy Tracker CLI

This Daycare Toy Tracker CLI is a command line interface app that is designed to manage all of the children and their toys within the daycare. It allows the daycare staff to manager information about the children in the daycare along with their toys. It allows daycare staff to add, update, and remove children from the database as well as add, update, remove, and assign toys to the children in which they belong to in order to keep the toy box organized. 

## Features
The main features in the CLI app are:
-Managing Children: Adding, updating, deleting, and listing the children that are currently enrolled in the daycare. For each child, their name and age is recorded. 
-Managing Toys: Adding, updating, deleting, and listing toys that are in the daycare's toy box. Each toy is assigned to the child who brought the toy to the daycare. The name, type, condtion, and child_id are recorded for each toy. 

## Installation 
1. Clone the repository: git clone https://github.com/samanthav8/python-p3-v2-final-project-template
2. Install dependencies: pipenv install
3. Activate the virtual environment: pipenv shell
4. Seed the database: python lib/seed.py

## Usage
1. Run the CLI Application: python lib/cli.py
2. Follow the CLI instructions to manage the children and toys

## CLI Functions

exit_program()
Exits the program and prints a goodbye message.

list_children()
Lists all children currently enrolled in the daycare.

create_child()
Adds a new child to the daycare.

update_child()
Updates the information of a child.

delete_child()
Unenrolls a child from the daycare.

create_toy()
Adds a new toy to the toy box and is associated with a child.

update_toy()
Updates the information of a toy.

delete_toy()
Removes a toy from the toy box.

## Models
-Child
Attributes: name(string), age(integer)
Methods
create(name, age): Creates a new child.
update(): Updates the child’s information.
delete(): Deletes the child.
toys(): Lists all toys belonging to the child.

-Toy
Attributes: name(string), type(string), conditon(string), child_id(integer)
Methods
create(name, toy_type, condition, child_id): Creates a new toy.
update(): Updates the toy’s information.
delete(): Removes the toy.

##Credits
The template for this project was forked and clone from https://github.com/learn-co-curriculum/python-p3-v2-final-project-template