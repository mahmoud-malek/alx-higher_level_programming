#!/usr/bin/python3
"""Author: Mahmoud Abdelmalek"""


def class_to_json(obj):
    """
    Function that returns the dictionary description with simple data structure
    """
    return obj.__dict__
