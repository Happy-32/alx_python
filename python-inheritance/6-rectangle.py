"""
...
"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    ...
    """

    def __dir__(self):
        return [attr for attr in dir(type(self)) if attr != '__init_subclass__']

    def __init__(self, width, height):
        self.integer_validator("width",width)
        self.integer_validator("height",height)
        self.__width = width
        self.__height = height

