#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''a function that replaces all occurrences of an element
    by another in a new list'''
    newList = []

    for element in my_list:
        if element == search:
            newList.append(replace)
        else:
            newList.append(element)

    return newList
