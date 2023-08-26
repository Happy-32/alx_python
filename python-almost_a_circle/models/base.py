#!/usr/bin/python3
"""
Base defines a python class 

-Base: class representing Base
"""
class Base:
    """
    __init__(self, id=None)- Attribute to chect if id is None

    __init__(id = None): initializes the Base object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        elif id == None:
            Base.__nb_objects += 1 #Base allows you to access all class level attributes
            Base.id = self.__nb_objects

b1 = Base()
print(b1.id)

b2 = Base()
print(b2.id)

b3 = Base()
print(b3.id)

b4 = Base(12)
print(b4.id)

b5 = Base()
print(b5.id)