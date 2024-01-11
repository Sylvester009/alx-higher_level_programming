#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
        a function that computes the square value of all integers of a matrix.
    '''
    newList = []
    if len(matrix) == 0:
        return newList

    newList = [[i*i for i in j] for j in matrix]
    return newList
