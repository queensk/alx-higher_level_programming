#!/usr/bin/python3
"""
This module has a class defining a Rectangle.
"""


class Rectangle:
    """
    Class defining Rectangle objects.
    """

    def __init__(self, width=0, height=0):
        """
        Method to initialize Rectangle class.

        Args:
            width: rectangle width.
            height: rectangle height.

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Method to get width.
        Return:
            returns width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Method to set width.
        Args:
            value: new width value
        Raise:
            TypeError: if width is not integer.
            TypeValue: if width is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Method to get height.
        Returns:
            height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Method to set height.
        Args:
            value: new height value.
        Raise:
            TypeError: height must be an integer.
            TypeValue: height must be >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
