#!/usr/bin/python3
"""
Square model defines a square based on its size

-Square: a class that represents the square
"""
class Square:
    """
    Attributes:
    -size(int): the size of the square which should be an integer

    Methods:
    -__init__(size=0): Initializes the square object 
    """
    def __init__(self, size=0):
        self.__size = size

    def size_isInt(self):
        try:
            if isinstance(self.__size, int):
                return self.__size
        except TypeError:
            print('size must be an integer')

    def size_lzero(self):
        try:
            if self.__size > 0:
                return self.__size
        except ValueError:
            print("size must be >= 0")

    def area(self):
        area = self.__size * self.__size
        return area