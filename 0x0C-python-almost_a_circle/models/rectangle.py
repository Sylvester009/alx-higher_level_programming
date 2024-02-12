#!/usr/bin/python3
# models/rectangle.py

"""
Rectangle Class Module that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """defines a Class representing a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle object.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        self.__height = value

    @property
    def x(self):
        """Getter for the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x"""
        self.__x = value

    @property
    def y(self):
        """Getter for the y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y"""
        self.__y = value
