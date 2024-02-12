#!/usr/bin/python3
# models/square.py

from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a class representing a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square object.

        Args:
            size (int): size of the square.
            x (int, optional): The x-coordinate of the square. Defaults to 0.
            y (int, optional): The y-coordinate of the square. Defaults to 0.
            id (int, optional): Square ID. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        self.width = value
        self.height = value
        
    def __str__(self):
        """Return the string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
          self.id, self.x, self.y, self.width)

