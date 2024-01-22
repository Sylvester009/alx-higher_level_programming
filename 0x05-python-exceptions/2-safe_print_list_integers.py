#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first x integers in a list.

    Args:
        my_list: List containing elements of any type (integer, string, etc.).
        x (int): Number of elements to print.

    Returns:
        Number of integers printed.
    """
    elem_number = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            elem_number += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (elem_number)
