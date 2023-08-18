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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        area = self.__size * self.__size
        return area