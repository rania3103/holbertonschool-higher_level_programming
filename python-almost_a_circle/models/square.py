#!/usr/bin/python3
"""Write the class Square that inherits from Rectangle"""
from rectangle import Rectangle


class Square(Rectangle):
    """this is the square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """use all attributes of Rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """[Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
