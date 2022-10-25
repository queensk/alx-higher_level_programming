#!/usr/bin/python3
"""
9-rectangle.py - class Rectangle that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle inheritance from BaseGeometry.
    Attributs:
        width (int): width of rectangle.
        height (int): height of rectangle.
    Methods:
        __init__ - initialises the Rectangle.
    """
    def __init__(self, width, height):
        """
        initialize the Rectangle object.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of a rectangle.
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        Returns a string of rectangle details.
        """
        return ("[{}] {}/{}".format(type(self).__name__,
                                    self.__width, self.__height))
