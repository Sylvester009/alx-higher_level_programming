#!/usr/bin/python3
"""Writing a LockedClass."""


class LockedClass:
    """
    prevents the user from dynamically creating new instance attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
