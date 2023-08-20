#!/usr/bin/python3
class Base:
    __nb_object = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__nb_object = self.__nb_object + 0
            self.id = self.__nb_object