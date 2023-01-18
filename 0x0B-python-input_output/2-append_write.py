#!/usr/bin/python3
"""
A function that appends a string at the end of a text file (UTF8).
"""


def append_write(filename="", text=""):
    """
    Function appends a string at the end of a text file (UTF8) and,
    returns the number of characters added.
    Args:
        filename: Name of file to open.
        text: Text to be appended to the end of the text file.
    Returns:
        the number of characters added.
    Raise:
        exemption when file can't be opened.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
