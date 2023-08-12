def raise_exception():
    raise TypeError("This is a type exception")
    try:
        raise_exception()
    except TypeError as e:
        print("An exception occurred:", str(e))
