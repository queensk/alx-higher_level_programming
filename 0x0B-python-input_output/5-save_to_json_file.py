#!/usr/bin/python3
"""
Module with function that writes an Object to a text file,
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function Writes an object to a text file.
    Args:
        my_obj: object python data structure.
        filename: file to write.
    Raises:
        exemption when file cannot be append.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
