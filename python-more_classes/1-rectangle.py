#!/usr/bin/python
""" define a class Rectangle with private instance
attribute width/height"""


class Rectangle:
    """ this is the class Rectangle"""

    def __init__(self, width=0, height=0):
        """initialize width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set value to width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """"retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ set value to height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
