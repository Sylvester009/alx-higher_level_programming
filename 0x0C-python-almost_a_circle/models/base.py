#!usr/bin/python3
# models/base.py

"""
Write a class Base that will
act as the base for the other
classes in the project.
"""


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
