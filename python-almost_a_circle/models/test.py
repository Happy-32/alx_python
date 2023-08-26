class Base:

    __nb_objects__ = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            None

class Rectangle(Base):

    def __init__(self, width, height, x, y, id=None):
        Base.__init__(self,id)
        self.width = width
        self.height = height
        self.x = x
        self.y= y

# b1 = Base(3)
# print(b1.id)
# r1 = Rectangle(4,5,0,0)
# print(r1.id)
# print(help(Rectangle))