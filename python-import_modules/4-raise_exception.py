#!/usr/bin/python3
def raise_exception():
    raise TypeError("This is an exception")
    try:
        raise_exception()
    except TypeError as e:
        print("An exception occurred:", str(e))
