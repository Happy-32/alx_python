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
    # def __init__(self, size=0):
    #     if not isinstance(size, int):
    #         raise TypeError("size must be an integer")
    #     elif size < 0:
    #         raise ValueError("size must be >= 0")
    #     else:
    #         self.__size = size

    def __init__(self, size=0):
        self.__size = size

    def size_isInt(self):
        try:
            if not isinstance(self.__size, int):
                return self.__size
        except TypeError:
            print('size must be an integer')

    def size_lzero(self):
        try:
            if self.__size < 0:
                print("size must be an >= 0")
        except ValueError:
            print("size must be >= 0")


