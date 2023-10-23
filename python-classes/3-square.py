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

    -size(): to access the size attribute of the Square object
    -area(): to compute the area of the square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self,value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        if isinstance(self.size, int):
            return self.size * self.size
        else:
            raise TypeError("size must be an integer")
