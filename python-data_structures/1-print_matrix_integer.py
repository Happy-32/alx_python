#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # for row in matrix:
        # print(" ".join(str(element) for element in row), end="\n")
    
    for i in matrix:
        row = ""
        for j in i:
            row += "{:d}".format(j) + " "
        print(row[:-1])