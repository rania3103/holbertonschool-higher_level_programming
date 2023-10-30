#!/usr/bin/python3
"""create a class Base"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
