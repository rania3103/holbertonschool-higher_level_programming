#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for row in matrix:
        new.append(list(map(lambda x: x ** 2, row)))
    return (new)
