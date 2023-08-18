#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.__size = size

    def size_isInt(self):
        try:
            if isinstance(self.__size, int):
                return self.__size
        except TypeError as te:
            print('size must be an integer')

    def size_lzero(self):
        try:
            if self.__size >= 0:
                return self.__size
        except TypeError as te:
            print("size must be >= 0")

Try = Square(-89)
Try2 = Square("3")
Try3 = Square(-89)
print(Try.size_isInt())
print(Try.size_lzero())

print(Try2.size_isInt())
print(Try2.size_lzero())

print(Try2.size_isInt())
print(Try2.size_lzero())
