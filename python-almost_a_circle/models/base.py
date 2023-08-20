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
    __nb_object = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__nb_object = self.__nb_object + 0
            self.id = self.__nb_object