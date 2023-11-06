#!/usr/bin/python3

"""A module that defines a function to lookup public
 attributes and methods of an object."""


def lookup(obj):
    """
    Return a list of public attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of public attributes and methods of the object.
    """

    all_attributes = dir(obj)
    public = [attr for attr in all_attributes if not attr.startswith('__')]
    return public
