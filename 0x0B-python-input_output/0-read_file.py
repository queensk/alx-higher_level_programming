#!/usr/bin/python3
"""
A function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Function to read from a file.
    Args:
        filename: file to be read.
    Raises
        Exemption when file cant be opened.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
