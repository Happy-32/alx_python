"""
.....
"""

class BaseGeometry:
    def __dir__(self):
        return [attr for attr in dir(type(self)) if attr != '__init_subclass__']
