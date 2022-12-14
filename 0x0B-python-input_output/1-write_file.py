#!/usr/bin/python3
"""
A function that writes a string to a text file (UTF8).
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and,
    returns the number of characters written.
    Args:
        filename: filename
        text: text to write
    Raises:
        Exemption: When the file cant be opened.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
