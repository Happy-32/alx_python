from rectangle import Rectangle
class Square(Rectangle):
    """
    Defines a square class that inherits from rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        if size <= 0:
            raise ValueError("size must be > 0")
        super().__init__(x, y, size, size, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    
s1 = Square(5)
print(s1)
print(s1.area())
s1.display()