#!/usr/bin/python3

""" Defines a function that reads a text file."""


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout.
    Args:
        filename
    """
    with open(filename, encoding="UTF8") as file:
        text = file.read()
        print(text, end="")
