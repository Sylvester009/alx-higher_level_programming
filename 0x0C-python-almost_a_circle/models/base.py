#!usr/bin/python3
# models/base.py

"""
Write a class Base that will
act as the base for the other
classes in the project.
"""

import json


class Base:
    """
    Base class to manage id attribute in all future classes
    """
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        method that returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
            return json.dumps(list_dictionaries)
