#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        row = ""
        for j in range(len(matrix[i])):
            row += "{:d} ".format(matrix[i][j])
        print(row[:-1])