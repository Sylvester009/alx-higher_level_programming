#!/usr/bin/python3

"""
Defines a function that returns an object represented by
JSON String
"""


def from_json_string(my_str):
    """
    returns an object represented by JSON String

    Args:
        my_str: The object to be serialized to JSON.
    """
    import json

    return json.loads(my_str)
