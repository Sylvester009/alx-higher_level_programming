#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Print x elements of a list.
    Args:
        my_list: List containing elements of any type (integer, string, etc.).
        x (int): Number of elements to print.
    Returns:
        Number of elements printed.
    """
    elem_number = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            elem_number += 1
        except IndexError:
            break
    print("")
    return (elem_number)
