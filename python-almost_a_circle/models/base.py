#!/usr/bin/python3
"""
Base defines a python class 

-Base: class representing Base
"""
class Base:
    """
    __init__(self, id=None)- Attribute to chect if id is None

    __init__(id = NOne): initializes the Base object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1 #Base allows you to access all class level attributes
            Base.id = self.__nb_objects