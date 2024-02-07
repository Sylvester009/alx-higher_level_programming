#!/usr/bin/python3

"""
Defines a function that returns the dictionary description.
"""


def class_to_json(obj):
    """
    Class to JSON
    Args:
        obj: instance of class
    """
    return obj.__dict__
