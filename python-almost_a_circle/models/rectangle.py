#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base"""
from base import Base


class Rectangle(Base):
    """this is the class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize width,height,x,y and id
        super() is a builtin function that allow us to acces
        method of the Base class and then we can initialize
        id using __init__because id is a part of Base
        not Rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retrieve value of width """
        return self.__width

    @width.setter
    def width(self, width):
        """set value to width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """retrieve value of height """
        return self.__height

    @height.setter
    def height(self, height):
        """set value to height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """retrieve value of x """
        return self.__x

    @x.setter
    def x(self, x):
        """set value to x"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """retrieve value of y """
        return self.__y

    @y.setter
    def y(self, y):
        """set value to y"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """calculate the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """display the rectangle"""
        if self.__y > 0:
            for i in range(self.__y):
                print()
        for i in range(self.__height):
            if self.__x > 0:
                for i in range(self.__x):
                    print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """[Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
