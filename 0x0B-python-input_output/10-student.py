#!/usr/bin/python3
"""
A class Student that defines a student.
"""


class Student:
    """
    Student class defines student objects.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        Args:
            attrs: attributes to get from dictionary.
        """
        if type(attrs) is list:
            attrs_dict = self.__dict__.copy()
            for items in attrs_dict:
                if type(items) is not str:
                    return items

            d_list = {}

            for item in range(len(attrs)):
                for satt in items:
                    if attrs[item] == satt:
                        d_list[satt] = items[satt]
            return d_list

        return items
