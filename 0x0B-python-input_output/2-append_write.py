#!/usr/bin/python3

"""
Defines a function that appends a string
at the end of a text file
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file

    Args:
        filename
        text

    Return: the number of characters added
    """

    with open(filename, 'a', encoding="UTF8") as file:
        filecontent = file.write(text)
        return(filecontent)
