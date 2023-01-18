#!/usr/bin/python3
"""
finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Return a peak in a list of unsorted integers.
    """
    n = len(list_of_integers)
    if not n:
        return None
    elif n == 1:
        return list_of_integers[0]
    elif n == 2 or n == 3:
        return max(list_of_integers)

    mid = n // 2
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid:])
