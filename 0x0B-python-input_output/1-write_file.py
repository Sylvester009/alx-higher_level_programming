#!/usr/bin/python3

""" Defines a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """
    writes a string to a text file and
    return numbers of chareacter written
    Args:
        filename
        text
    """
    with open(filename, 'w', encoding="UTF8") as file:
        filecontent = file.write(text)
        return (filecontent)
