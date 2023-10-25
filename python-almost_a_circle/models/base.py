#!/usr/bin/python3
"""create a class Base"""


class Base:
    """this the class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize id in case of id is not none otherwise
        we increment nb_objects and assign its value to id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
