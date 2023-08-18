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
    def __init__(self, size):
        self.__size = size
