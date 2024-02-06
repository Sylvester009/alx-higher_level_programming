#!/usr/bin/python3

""" Defines a function that creates an Object from a JSON file"""


def load_from_json_file(filename):
    """
    creates an Object from a JSON file
    Args:
        filename
    """
    import json

    with open(filename) as file:
        return json.load(file)
