#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        row = ""
        for j in i:
            row += str(j) + " "
        print(row[:-1])