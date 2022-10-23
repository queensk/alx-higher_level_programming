#!/usr/bin/python3
"""
Module defines a rectangle class.
"""


class Rectangle:
    """
    Class that defines rectangle object.
    """

    def __init__(self, width=0, height=0):
        """
        Method to initialize class Rectangle object.
        Args:
            width: rectangle width.
            height: rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Width getter method.
        Returns:
            Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width setter method.
        Args:
            value: Rectangle width.
        Raise:
            TypeError: if width is not an integer.
            TypeValue: if width is is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Height getter method.
        Returns:
            Height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Height setter method.
        Args:
            value: The new height value.
        Raise:
            TypeError: if height is not an integer
            TypeValue: if height is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    def area(self):
        """
        Methods to calculate the area.
        Returns:
            rectangle area.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Methods to calculate the perimeter.
        Returns:
            rectangle perimeter.
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (2 * self.height) + (2 * self.width)
