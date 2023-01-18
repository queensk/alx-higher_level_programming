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
        attrs_dict = self.__dict__.copy()
        if type(attrs) is list:

            for items in attrs:
                if type(items) is not str:
                    return attrs_dict

            d_list = {}

            for item in range(len(attrs)):
                for satt in attrs_dict:
                    if attrs[item] == satt:
                        d_list[satt] = attrs_dict[satt]
            return d_list

        return attrs_dict
