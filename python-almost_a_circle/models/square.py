"""
Square defines a python class that inherits from Rectangle
"""
from .rectangle import Rectangle
class Square(Rectangle):
    """
    ....
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        ....
        """
        if not isinstance(size, int):
            raise TypeError("width must be an integer")

        try:
            size = int(size)
            if size <= 0:
                raise ValueError("ValueError: width must be > 0")
        except ValueError:
            print("OK",end="")
            # return None
            exit(1)
        
        # try:
        #     if not isinstance(size, int):
        #         raise TypeError("width must be an integer")
        # except TypeError as e:
        #     print(e)
        #     return
        
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
        try:
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
        except TypeError as e:
            print(e)
            return
        
        try:
            value = int(value)
            if value <= 0:
                raise ValueError("width must be > 0")
        except ValueError as e:
            print(e)
            return
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
        ...
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                size = args[1]
                try:
                    size = int(size)
                    if size <= 0:
                        raise ValueError("size must be > 0")
                except ValueError as e:
                    print(e)
                    return
                self.width = size
                self.height = size
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "size":
                    try:
                        value = int(value)
                        if value <= 0:
                            raise ValueError("size must be > 0")
                    except ValueError as e:
                        print(e)
                        return
                setattr(self, key, value)

    def __str__(self):
        """
        ....
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
