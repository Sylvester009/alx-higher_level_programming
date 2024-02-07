#!/usr/bin/python3

"""
Defines a class Student
"""


class Student:
    """
    Class that defines a Student
    """
    def __init__(self, first_name, last_name, age):
        """
        instance initialization
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student
        """
        if attrs is None:
            return self.__dict__
        if not isinstance(attrs, list):
            return self.__dict__
        if not (isinstance(attrs[elems], str) for elems in attrs):
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}

    def reload_from_json(self, json):
        for dictkey, dictvalue in json.items():
            setattr(self, dictkey, dictvalue)
