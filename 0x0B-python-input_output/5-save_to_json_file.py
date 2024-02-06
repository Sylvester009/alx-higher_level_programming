#!/usr/bin/python3

""" Defines a function that writes an Object to a text file"""


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file
    Args:
        my_obj: object to write
        filename
    """
    import json

    with open(filename, 'w') as file:
        return file.write(json.dumps(my_obj))
