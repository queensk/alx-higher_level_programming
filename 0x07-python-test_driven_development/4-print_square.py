#!/usr/bin/python3
"""
This module is composed by a function that prints a square with the character #
"""


def print_square(size):
    """
    prints a square string with value #
    Args:
        size: Size of the square to print

    Returns:
        No retune

    Raises:
        TypeError: If size is not an integer number



    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for item in range(size):
        print("#" * size)
