#!/usr/bin/python3
def raise_exception_msg(message=""):
    raise NameError(message)
    try:
        raise_exception_msg("This is an exception")
    except NameError as e:
        print("An exception occurred:", str(e))
