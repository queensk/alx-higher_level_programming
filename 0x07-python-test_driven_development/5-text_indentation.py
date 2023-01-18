#!/usr/bin/python3
"""
Module composed by a function that prints 2 new lines after ".?:" characters
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines,
    after each of these characters: ., ? and :

    Args:
        text: string input parameter

    Returns:
        No return

    Raises:
        TypeError: If text is not a string

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end="")
