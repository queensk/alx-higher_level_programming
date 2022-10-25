#!/usr/bin/python3
"""
A class MyList that inherits from list.
"""


class MyList(list):
    """
    The class inherits from list.
    Attributes:
    Methods:
        def print_sorted(self): that prints the list,
        but sorted (ascending sort).
    """

    def print_sorted(self):
        """
        Method to print a list in ascending sort order.
        """
        print(sorted(self))
