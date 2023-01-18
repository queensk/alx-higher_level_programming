#!/usr/bin/python3
"""
Module has class Student that defines a student.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        initialize the student objects.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            d_list = {}

            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        d_list[satr] = obj[satr]
            return d_list

        return obj

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.
        """
        for atr in json:
            self.__dict__[atr] = json[atr]
