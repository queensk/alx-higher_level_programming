#!/usr/bin/python3
"""
A function that returns True
if the object is exactly an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    Function that return True if object is and instance of a class.
    Args:
        obj: The object instance of the class.
        a_class: The class declaration.
    Returns:
        True: if the object is an instance of a class.
        False: if object is not an instance of a class.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
