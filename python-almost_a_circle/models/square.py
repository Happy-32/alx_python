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
    
    def area(self):
        """
        Computes the area of the square
        """
        return self.width * self.width

    def display(self):
        """
        Displays the square as a series of '#' characters
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
    
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"