#!/usr/bin/python3
"""
A class Square that inherits from Rectangle (9-rectangle.py).
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square inherits from Rectangle.
    Attributes:
        size (int): size of square.
    Methods:
        __init__ - initialise the square.
    """
    def __init__(self, size):
        """
        Initialize Square.
        """
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """
        Returns area of the square.
        """
        return (self.__size * self.__size)

    def __str__(self):
        """
        Returns the string representation of the square.
        """
        return ("[{}] {}/{}".format(type(self).__name__,
                                    self.__size, self.__size))
