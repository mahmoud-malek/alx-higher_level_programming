#!/usr/bin/python3
"""Author: Mahmoud Abdelmalek"""


class Student:
    """
    Class Student that defines a student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in
                    self.__dict__.items() if key in attrs}

    def reload_from_jason(self, json):
        """Replace all attributes of the Student

        Args:
            json (dict): The key/value pairs to replace attributes with
        """
        for key, val, in json.items():
            setattr(self, key, val)
