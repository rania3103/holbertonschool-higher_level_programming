#!/usr/bin/python3
"""Create a function def pascal_triangle(n): that returns a list of lists
of integers representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """this is the function"""
    pascal = []
    if n <= 0:
        return pascal
    else:
        for i in range(n):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                elif i >= 2:
                    row.append(pascal[i - 1][j] + pascal[i - 1][j - 1])
            pascal.append(row)
    return pascal
