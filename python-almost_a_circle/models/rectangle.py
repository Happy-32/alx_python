#!/usr/bin/python3
"""
Base defines a python class 

-Base: class representing Base
"""
class Base:
    """
    __init__(self, id=None)- Attribute to chect if id is None

    __init__(id = None): initializes the Base object
    __nb_objects: a class level attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1 #Base allows you to access all class level attributes
            Base.id = self.__nb_objects


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
        super().__init__(id=None)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
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
        self.__width = width
    
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
        self.__height = height
    
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
        self.__x = x
    
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
        self.__y = y