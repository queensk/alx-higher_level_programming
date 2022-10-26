#!/usr/bin/python3
"""
Module with functions that return a JSON string:
"""
import json


def from_json_string(my_str):
    """
    A function that returns an object (Python data structure)
    represented by a JSON string
    Args:
        my_str: string to be input.
    Returns:
        an object (Python data structure) represented by a JSON string.
    """
    return json.dumps(my_str)
