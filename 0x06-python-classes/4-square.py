#!/usr/bin/python3

"""class that defines a square"""


class Square:
    """this represents a square"""

    def __init__(self, size=0):
        """Args:
        size: size of square
        """
        self.size = size

    @property
    def size(self):
        """method to get the size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """method to set the size of square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return (self.__size * self.__size)
