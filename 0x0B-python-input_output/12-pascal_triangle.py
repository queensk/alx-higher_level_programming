#!/usr/bin/python3
"""
a function def pascal_triangle(n):
"""


def pascal_triangle(n):
    """
    A function returns a list of lists of integers
    representing the Pascal’s triangle of n:
    Args:
        n: Number
    Returns: list of lists.
    """
    t_row = [1]
    temp_l = [0]
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        triangle.append(t_row)
        t_row = [q+r for q, r in zip(t_row + temp_l, temp_l + t_row)]
    return triangle
