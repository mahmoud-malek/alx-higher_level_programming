#!/usr/bin/python3
"""Check if an object is an instance or inherited instance of a class."""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        True if obj is an instance or inherited instance of
         a_class, False otherwise.
    """
    return isinstance(obj, a_class)
