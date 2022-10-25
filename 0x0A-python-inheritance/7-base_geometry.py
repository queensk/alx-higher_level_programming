#!/usr/bin/python3
"""
class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """
    class BaseGeometry.
    Method:
        area: raises an Exception.
        integer_validator: validates value.
    """
    def area(self):
        """
        Area raises exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer validator to check the value.
        Args:
            name: string name.
            value: int value.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
