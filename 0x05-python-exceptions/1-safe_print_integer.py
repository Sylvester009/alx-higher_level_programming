#!/usr/bin/python3

def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format().
        value: Any type (integer, string, etc.).
        
    Returns:
        True if value has been correctly printed, otherwise False.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
