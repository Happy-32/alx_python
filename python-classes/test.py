#!/usr/bin/python3
Square = __import__('3-square').Square

try:
    my_square = Square(89)
    print(my_square.size)
    my_square.size = "89"
    print(my_square.size)
except Exception as e:
    print(e)
