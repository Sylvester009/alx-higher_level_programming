#!/usr/bin/python3

"""class that defines a square"""


class Square:
    """this represents a square"""

    def __init__(self, size):
        """Args:
        size: size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
