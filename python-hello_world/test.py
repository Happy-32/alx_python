for i in range(10):
    for j in range(i + 1, 10):
        print("{:02}, ".format(i), end="")
        print("{:02}".format(j), end="")
        print("\n", end="")