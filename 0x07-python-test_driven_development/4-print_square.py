#!/usr/bin/python3
"""
This module defines a function that prints a square.

Functions:
    print_square(size): Prints a square with the # character.

Example:
    >>> print_square(3)
    ###
    ###
    ###
"""


def print_square(size):
    """
    Function to print a square with the # character.

    Args:
        size (int): The height/width of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Prints:
        A square of the given size made up of # characters.

    Example:
        >>> print_square(3)
        ###
        ###
        ###
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
