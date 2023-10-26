#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base"""
Base = __import__("Base").base


class Rectangle(Base):
    """this is the class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize width,height,x,y and id"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        """super() is a builtin function that allow us to acces
        method of the Base class and then we can initialize id using __init__
        because id is a part of Base not Rectangle"""
        super().__init__(id)

    @property
    def width(self, width):
        """retrieve value of width """
        return self.__width

    @width.setter
    def width(self, width):
        """set value to width"""
        self.__width = width

    @property
    def height(self, height):
        """retrieve value of height """
        return self.__height

    @height.setter
    def height(self, height):
        """set value to height"""
        self.__height = height

    @property
    def x(self, x):
        """retrieve value of x """
        return self.__x

    @x.setter
    def x(self, x):
        """set value to x"""
        self.__x = x

    @property
    def y(self, y):
        """retrieve value of y """
        return self.__y

    @y.setter
    def y(self, y):
        """set value to y"""
        self.__y = y
