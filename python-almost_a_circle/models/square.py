#!/usr/bin/python3
"""Write the class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this is the square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """use all attributes of Rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """[Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """retrieve  the value of size"""
        return self.width

    @size.setter
    def size(self, size):
        """assign size to width and height"""
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = size
        self.height = size
