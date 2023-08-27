#!/usr/bin/python3
"""
Base defines a python class 

-Base: class representing Base
"""
class Base:
    """
    __init__(self, id=None)- Attribute to checK if id is None

    __init__(id = None): initializes the Base object
    __nb_objects: a class level attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1 #Base allows you to access all class level attributes
            self.id = Base.__nb_objects


class Rectangle(Base):
    """
    Rectangle represents a Rectangle object that inherits from the Base class

    Attributes:
        __width(int): Width of the rectangle
        __height(int): Height of the rectangle
        __x(int): maybe an x coordinate on the x-y plane
        __y(int): maybe a y coordinate on the x-y plane
    """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the Rectangle object.

        Args:
            width(int): Width of the rectangle (integer )
            height(int): height of the rectangle
            x(int): x coordinate of the rectangle
            y(int): y coordinate of the rectangle
            id(int): unique udentifier, default value of zero
        """
        Base.__init__(self,id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        else:
            self.__width = width

        if width <= 0:
            raise ValueError("width must be > 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        else:
            self.__height = height

        if height <= 0:
            raise ValueError("height must be > 0")

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        else:
            self.__x = x

        if x < 0:
            raise ValueError("x must be >= 0")

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        else:
            self.__y = y

        if y < 0:
            raise ValueError("y must be >= 0")
    
    @property
    def width(self):
        """
        Get the width of the rectangle

        Returns:
            int: The width of the rectangle
        """
        return self.__width
    
    @width.setter
    def width(self,width):
        """
        sets the width of the rectangle

        Returns:
            int: The width of the rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        else:
            self.__width = width

        
        if width <= 0:
            raise ValueError("width must be > 0")
    
    @property
    def height(self):
        """
        Get the height of the rectangle

        Returns:
            int: The height of the rectangle
        """
        return self.__height
    
    @height.setter
    def height(self,height):
        """
        sets the height of the rectangle

        Returns:
            int: The height of the rectangle
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        else:
            self.__height = height

        
        if height <= 0:
            raise ValueError("height must be > 0")
    
    @property
    def x(self):
        """
        Get the x coordinate of the rectangle

        Returns:
            int: The x coordinate of the rectangle
        """
        return self.__x
    
    @x.setter
    def x(self,x):
        """
        sets the x coordinate of the rectangle

        Returns:
            int: The x coordinate of the rectangle
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        else:
            self.__x = x


        if x < 0:
            raise ValueError("x must be >= 0")
    
    @property    
    def y(self):
        """
        Get the y coordinate of the rectangle

        Returns:
            int: The y coordinate of the rectangle
        """
        return self.__y
    
    @y.setter
    def y(self,y):
        """
        sets the y coordinate of the rectangle

        Returns:
            int: The y coordinate of the rectangle
        """
        
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        else:
            self.__y = y

        
        if y < 0:
            raise ValueError("y must be >= 0")
    
    def area(self):
        """
        Computes the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Returns a rectangle
        """
        # for j in range(self.height):
        #     print("#" * self.width)
        for i in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        print in stdout the Rectangle instance with the character # by taking care of x and y
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    
    def update(self, *args):
        """
        Assign an argument to each variable
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]