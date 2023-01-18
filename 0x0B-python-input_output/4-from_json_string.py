#!/usr/bin/python3
"""
Module with function that returns an object (Python data structure)
represented by a JSON string:
"""
import json


def from_json_string(my_str):
    """
    Function that returns an object by a JSON representation.
    Args:
        my_str: string object.
    Returns:
        an object.
    Raise:
        Exemption: when the string can't be decoded.
    """
    return json.loads(my_str)
