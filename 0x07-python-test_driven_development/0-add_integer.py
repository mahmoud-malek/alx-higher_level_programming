#!/usr/bin/python3

""" This module defines addition function for integers"""


def add_integer(a, b=98):
    """Return sum of a and b
    any floats are castaed to int

    Raises:
        TypeError: if either a or b is not integer and not float
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
