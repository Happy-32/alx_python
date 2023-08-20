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

"""
Rectangle defines a class

-Rectangle: subclas that inherits from Super class Base
"""
class Rectangle(Base):
    """
    get_width, get_height, get_x, get_y: getter methods
    set_width, set_height, set_x, set_y: setter methods
    """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id=None)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def get_width(self):
        return self.__width
    
    def set_width(self,width):
        self.__width = width

    def get_height(self):
        return self.__height
    
    def set_height(self,height):
        self.__height = height

    def get_x(self):
        return self.__x
    
    def set_x(self,x):
        self.__x = x
    
    def get_y(self):
        return self.__y
    
    def set_y(self,y):
        self.__y = y