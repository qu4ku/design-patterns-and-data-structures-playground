'''Interface Segregation Principle
Many client-specific interfaces are bettter than one general-purpose interface.

In other words, more extensive interaction interfaces are split into smaller
ones. The principle ensures classes only use the methods they need, reducing
overal redundancy.
'''

# The following example demonstrates a gneral-purpose interface:
class Animal():
    def walk(self):
        pass
    def swim(self):
        pass

class Cat(Animal):
    def walk(self):
        print('Struts')
    def fly(self):
        raise Exception("Cat's don't swim")

class Duck(Animal):
    def walk(self):
        print('Waddles')
    def swim(self):
        print('Floats')

# The child classes inherit from the parent Animal class, which contains walk
# and fly methods. Although both functions are aceptable for certain animals,
# some animals have redundant functionalities. 

# To handle the situation, split the interface into smaller sections:
class Walk():
    def walk(self):
        pass

class Swim(Walk):
    def swim(self):
        pass

class Cat(Wal):
    def walk(self):
        print('Struts')

class Duck(Swim):
    def walk(self):
        print('Waddles')
    def swim(self):
        print('Floats')

# The Fly class inherits from the Walk, providing additional functionality to
# appropriate child classes. The example satisfies the interface segregation
# principle. Adding another animal, such a fish, requires atomizing the interface
# further since fish can't walk
