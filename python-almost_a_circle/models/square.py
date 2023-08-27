from rectangle import Rectangle
class Square(Rectangle):
    """
    Defines a square class that inherits from rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(x, y, size, size, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"