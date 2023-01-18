#!/usr/bin/python3
"""
Module that defines class Student that defines a student.
"""


class Student:
    """
    class describing Student instance.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Method to return dictionary description.
        """
        return self.__dict__.copy()
