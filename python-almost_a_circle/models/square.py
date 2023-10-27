"""
Square defines a python class that inherits from Rectangle
"""
from .rectangle import Rectangle
class Square(Rectangle):
    """
    ....
    """
    def __init__(self, size, x=0, y=0, id=None):
        if size <= 0:
            raise ValueError("size must be > 0")
        super().__init__(size, size, x, y, id)
        self.__size = size
        self.__x = x
        self.__y = y


    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            self.__size = size

        if size <= 0:
            raise ValueError("size must be > 0")
    
    def area(self):
        """
        Computes the area of the square
        """
        return self.__size * self.__size

    def display(self):
        """
        Displays the square as a series of '#' characters
        """
        for _ in range(self.y):
            print()
        for _ in range(self.size):
            print(" " * self.x + "#" * self.size)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square

        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                size = args[1]
                if size <= 0:
                    raise ValueError("size must be > 0")
                self.width = size
                self.height = size
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for i, value in kwargs.items():
                if i == "size":
                    if value <= 0:
                        raise ValueError("size must be > 0")
                setattr(self, i, value)
    
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"