#!/usr/bin/python3
""" create a class that defines Square and control the atrribute size"""


class Square():
    """this is a class named Square"""

    def __init__(self, size=0):
        """
        initialize size otherwise displaying error message if the value of size is invalid
        attributes:
        __size: a private instance attribute
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
