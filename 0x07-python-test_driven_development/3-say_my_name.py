#!/usr/bin/python3
"""
This module contains a function that prints first and last name.
"""
def say_my_name(first_name, last_name=""):
    """
    Function that prints My name is <first name> <last name>.

    Args:
        first_name: value of the first name.
        last_name: value of the last name.
    
    Returns:
        No return value.

        TypeError: If first_name or last_name is not a string

    
    """

    if not isinstance(first_name, str):
        TypeError ("first_name must be a string")
    
    if not isinstance(last_name, str):
        TypeError ("last_name must be a string")

    print(f"My name is {first_name} {last_name}")