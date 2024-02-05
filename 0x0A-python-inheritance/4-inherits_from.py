#!/usr/bin/python3
"""Defines function for inherited class."""


def inherits_from(obj, a_class):
    """Checks if object is an inherited instance of class.
    Args:
        obj (any): Object to check.
        a_class (type): The class to match the type of obj.
    Returns:
        True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
