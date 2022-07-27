'''Dependency Inversoin Principle
Depend upon abstractions, not concretions.

the principle aims to reduce connections between classes by adding an
abstraction layer. Moving dedpendencies to abstractions makes the code robust.
'''

# The following excample demonstrates class dependency wihotu an abstraction
# layer:
class LatinConvereter:
    def latin(self, name):
        print(f'{name} = "Felis catus"')
        return "Felis catus"

class Converter:
    def start(self):
        converter = LatinConvereter()
        converter.latin('Cat')

if __name__ = '__main__':
    converter = Converter()
    converter.start()

# The example has two classes:
# LatinConvereter uses an imaginary API to fetch the Latin name for an animal
# Converter is a high-level module that uses an instalnce of LatinConvereter
# and its functon to convert the provided name. The Converter heavily depends
# on the LatinConvereter class, which depends on the API. This approach violates
# the principle. The dependency inversion principle requires adding an
# abstraction interface layer betwen the two classes.
from abc import ABC

class NameConverter(ABC):
    def convert(self, name):
        pass

class LatinConvereter(NameConverter):
    def latin(self, name):
        print('Converting using Latin API')
        print(f'{name} = "Felis catus"')
        return "Felis catus"

class Converter:
    def __init__(self, converter: NameConverter):
        self.converter = converter
    def start(self):
        converter.convert('Cat')

if __name__ = '__main__':
    latin = LatinConvereter()
    converter = Converter(latin)
    converter.start()

# The Converter clas now depends on the NameConverter interfacve instead of
# on the LatinConverter directly. Future updates allow defining nam
# conversions using a different language and API through the NameConverter
# interface.

