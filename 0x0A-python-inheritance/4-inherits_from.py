#!/usr/bin/python3
"""
A function that returns True,
if the object is an instance of a class,
that inherited (directly or indirectly),
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Function to check an object,
    is an instance of a class (directly or Indirectly).
    Args:
        obj: The object of a class to test.
        a_class: The class description of an object.
    Returns:
        True: of object is an instance (directly or indirectly).
        False: if object is not an instance.
    """
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
