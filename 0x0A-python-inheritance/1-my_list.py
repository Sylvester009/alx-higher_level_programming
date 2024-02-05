#!/usr/bin/python3
"""Defines MyList class."""


class MyList(list):
    """Implements sorted printing for the list class."""

    def print_sorted(self):
        """prints the list, but in ascending sort."""
        print(sorted(self))
