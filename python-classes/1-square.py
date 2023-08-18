#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size


Try = Square(-89)
# # Try2 = Square("3")
# # Try3 = Square(-89)
# print(Try)
# print(Try2.size_isInt())
# print(Try2.size_lzero())

# print(Try2.size_isInt())
# print(Try2.size_lzero())
