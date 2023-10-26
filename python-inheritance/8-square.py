Rectangle = __import__('7-rectangle').Rectangle

"""
...
"""
class Square(Rectangle):
    """
    ...
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
    
    def area(self):
        return self.__size ** 2
    
    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
        

