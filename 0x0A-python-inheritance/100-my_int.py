#!/usr/bin/python3
"""
A class MyInt that inherits from int.
"""


class MyInt(int):
    """
    MyInt that inherits from int.
    """
    def __init__(self, number):
        """
        initialize MyInt
        """
        self.number = number

    def __ne__(self, value):
        """
        Rebel to the not Equal Operator.
        """
        return (self.number == value)

    def __eq__(self, value):
        """
        Rebel to the Equal to Operator.
        """
        return (self.number != value)

    def __str__(self):
        """
        String representation of the given number.
        """
        return (str(self.number))
