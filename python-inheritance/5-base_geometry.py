"""
.....
"""

class meta_class(type):
    def __dir__(cls):
        return [attr for attr in super().__dir__() if attr != "__init_subclass__"] 


class BaseGeometry(metaclass=meta_class):
    """
    An Empty class
    """
    def __dir__(cls) -> None:
        return_array = super().__dir__()
        return_dir = []
        for i in return_array:
            if i != "__init_subclass__":
                return_dir.append(i)
        return return_dir

    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
