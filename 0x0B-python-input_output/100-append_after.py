#!/usr/bin/python3

"""
a function that inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file

    Args:
        filename (str)
        search_string (str): The string to search for line.
        new_string (str): The text line to insert next lines
        after the search string.
    """
    with open(filename, 'r', encoding="UTF8") as file:
        text_lines = file.readlines()

    with open(filename, 'w', encoding="UTF8") as file:
        for lines in text_lines:
            file.write(lines)
            if search_string in lines:
                file.write(new_string)
