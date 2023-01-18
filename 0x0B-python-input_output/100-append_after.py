#!/usr/bin/python3
"""
A function that inserts a line of text to a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function that insert a new line of text of a file.
    Args:
        filename: filename to be read.
        search_string: string to search.
        new_string: steam to append.
    """
    res_line = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            res_line += [line]
            if line.find(search_string) != -1:
                res_line += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(res_line))
