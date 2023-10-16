#!/usr/bin/python3
"""write a class Rectangle wwith 2 private instance attributes
and 2 public instance methods and print rectangle"""


class Rectangle:
    """this is the class Rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialize width and height & increment
        each new instance instantiation"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ calculate the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """calculate perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        """print rectangle with #"""
        ch = ""
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    ch += "#"
                if i != self.__height - 1:
                    ch += "\n"
            return ch

    def __repr__(self):
        """ return a string representation of the
        rectangle to be able to recreate
        a new instance by using eval()"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Print the message Bye rectangle...
        when an instance of Rectangle is deleted
        & decrement each deletion of an instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
