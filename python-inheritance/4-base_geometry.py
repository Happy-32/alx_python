"""
.....
"""

class BaseGeometry:
    """
    .....
    """

    def __dir__(self):
        return [attr for attr in dir(type(self)) if attr != '__init_subclass__']

    def area(self):
        raise Exception("area() is not implemented")