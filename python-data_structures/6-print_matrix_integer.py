#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    for row in matrix:
        i = 0
        for val in row:
            i += 1
            if i != len(row):
                print("{:d} ".format(val), end="")
            else:
                print("{:d}".format(val), end="")
        print()
