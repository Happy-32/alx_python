def raise_exception_msg(message=""):
    raise NameError(message)
    try:
        raise_exception_msg("This is a name exception")
    except NameError as e:
        print("An exception occurred:", str(e))
