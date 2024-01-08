#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_new = ()
    tuple_1st = tuple_a + (0, 0)
    tuple_2nd = tuple_b + (0, 0)
    tuple_new = tuple_1st[0] + tuple_2nd[0], tuple_1st[1] + tuple_2nd[1]
    return tuple_new
