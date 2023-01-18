#!/usr/bin/python3
"""
A function that adds a new attribute to an object if it’s possible.
"""


def add_attribute(cls, name, value):
    """
    adds an new attribute if possible.
    """
    if hasattr(cls, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(cls, name, value)
