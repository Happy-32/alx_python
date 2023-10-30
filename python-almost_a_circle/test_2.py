from models.square import Square

try:
    Square(-12)
    print("ValueError exception not raised")
    exit(1)
except ValueError as e:
    if str(e) != "width must be > 0":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)