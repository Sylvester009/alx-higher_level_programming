#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_set = set(my_list)
    num = 0

    for i in uniq_set:
        num += i

    return (num)
