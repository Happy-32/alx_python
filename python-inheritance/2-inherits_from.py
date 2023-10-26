def inherits_from(obj, a_class):
    # return issubclass(type(obj), a_class)
    # Check if obj is an instance of a subclass of a_class
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
    