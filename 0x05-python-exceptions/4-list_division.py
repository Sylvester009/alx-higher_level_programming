#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """divides element by element 2 lists.
    Args:
        my_list_1 (list): 1st list that contain any type (integer, string, etc.).
        my_list_2 (list): 2nd list that contain any type (integer, string, etc.).
        list_length (int): The number of elements to divide.
    Returns:
       new list (length = list_length) with all divisions
    """
    new_list = []
    for i in range(0, list_length):
        try:
            num = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            num = 0
        except ZeroDivisionError:
            print("division by 0")
            num = 0
        except IndexError:
            print("out of range")
            num = 0
        finally:
            new_list.append(num)
    return (new_list)
