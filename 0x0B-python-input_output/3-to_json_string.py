#!/usr/bin/python3

"""
Defines a function that returns the JSON representation
"""


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)

    Args:
        my_obj: The object to be serialized to JSON.
    Returns:
        The JSON representation of the object as a string.
    """
    import json

    return json.dumps(myobj)
