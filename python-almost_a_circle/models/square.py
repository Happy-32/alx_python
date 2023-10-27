"""
Square defines a python class that inherits from Rectangle
"""
from .rectangle import Rectangle
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    ....
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        ....
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        ......
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        ....
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def area(self):
        """
        ....
        """
        return self.size ** 2

    def display(self):
        """
        ....
        """
        for _ in range(self.y):
            print()
        for _ in range(self.size):
            print(" " * self.x + "#" * self.size)

    def update(self, *args, **kwargs):
        """
        ....
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                else:
                    setattr(self, key, value)

    def __str__(self):
        """
        ....
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
