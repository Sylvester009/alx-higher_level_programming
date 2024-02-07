#!/usr/bin/python3

"""
Pascal Triangle.
"""


def pascal_triangle(n):
    """
    Function  that returns a list of lists of integers
    representing the Pascal’s triangle
    Args:
        n (int): always an integer.
    Return:
        a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = []
    for i in range(n):
        row = [1]

        if i > 1:
            prevRow = triangle[i - 1]
            for x in range(1, i):
                row.append(prevRow[x - 1] + prevRow[x])

        if i > 0:
            row.append(1)

        triangle.append(row)

    return triangle
