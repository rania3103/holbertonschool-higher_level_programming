#!/usr/bin/python3
"""create a class Square that defines a square with a private instance size"""


class Square():
    """this is a class named square"""

    def __init__(self, __size):
        """Instantiation with size (no type/value verification)"""
        self.__size = __size
