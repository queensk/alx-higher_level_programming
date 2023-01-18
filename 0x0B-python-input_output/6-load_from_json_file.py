#!/usr/bin/python3
"""
Module with function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Function Create object from a JSON file.
    Args:
        filename: json file to be opened.
    Returns:
        json object from json file.
    Raises:
        Exemption when file cant be opened.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
