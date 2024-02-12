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
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format('width'))
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format('height'))
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Getter for the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Getter for the y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        returns the area value of the Rectangle instance.
        """
        return (self.__width * self.__height)

    def display(self):
        """Print the Rectangle instance using '#' characters."""
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the string representation of the Rectangle
        class instance.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:
        Args:
            1st arg: id attribute
            2nd arg: width attribute
            3rd arg: height attribute
            4th arg: x attribute
            5th arg: y attribute
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
 
    def to_dictionary(self):
        """Return dictionary representation of Rectangle instance."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
