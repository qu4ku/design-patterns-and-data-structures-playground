""" Singe-Responsibility Principle
There should never be more than one reason for a class to change
"""

# A class with multiple reponsibilities
class Animal:
    # property constructor
    def __init__(self, name):
        self.name = name

    #property representation
    def __repr__(self):
        return f'Animal(name="{self.name})'

    # database management
    def save(animal):
        print(f'Save {animal} to the database')

if __name__ == '__main__':
    # property instatiation
    a = Animal('Cat')
    # saving property to a database
    Animal.save(a)

# when making any changes to the save() method, the changes happens in the
# Animal classs. When making property changes, the modifications also occur
# in the Animal class

# a class responsible for property management
class Animal:
    def __init__(self, name):
        self.name = name
    def __repr__:
        return f'Animal(name="{self.name}")'

# a class responsible for database management
class AnimalDB:
    def save(animal):
        print(f'Save {animal} to the database')

if __name__ == '__main__':
    a = Animal('Cat')
    db = AnimalDB()
    db.save(a)
