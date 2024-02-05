#!/usr/bin/python3
"""Defines a function that does class-checking."""


def is_same_class(obj, a_class):
    """checks if the object is an instance of the specified class
    Args:
        obj (any): Object to check.
        a_class (type): The class to match the type of obj.
    Returns:
        True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
