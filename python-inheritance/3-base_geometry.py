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
