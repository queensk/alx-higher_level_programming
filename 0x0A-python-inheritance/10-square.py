#!/usr/bin/python3
"""
A class Square that inherits from Rectangle (9-rectangle.py):
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from square.
    Attributes:
        size (int): width of square.
    Methods:
        __init__ - initializes the square.
    """
    def __init__(self, size):
        """
        Initialize the square
        """
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """
        Return the area of the square.
        """
        return (self.__size * self.__size)

    def __str__(self):
        """
        Returns the string representation of the square.
        """
        return ("[{}] {}/{}".format("Rectangle",
                                    self.__size, self.__size))
