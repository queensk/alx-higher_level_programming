#!/usr/bin/python3
"""
8-rectangle: class Rectangle from BaseGeomerty.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle inherits for class BaseGeometry.
    Attributes:
        width (int) width of the Rectangle.
        height (int) height of the Rectangle.
    Methods:
        __inti__ - initialise the Rectangle.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
