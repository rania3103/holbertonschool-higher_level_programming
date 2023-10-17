#!/usr/bin/python3
"""Write a class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ this is the class"""

    def __init__(self, width, height):
        """initialize height and width"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculate the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ return the following rectangle description:
        [Rectangle] <width>/<height>"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
