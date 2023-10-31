#!/usr/bin/python3
"""
This module defines a function that prints a text with
 two new lines after each '.', '?', and ':'.

Functions:
    text_indentation(text): Prints a text with
    two new lines after each '.', '?', and ':'.

Example:
    >>> text_indentation("Hello. How are you?")
    Hello.

    How are you?
"""


def text_indentation(text):
    """
    Function to print a text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.

    Prints:
        The given text, but with two new lines after each '.', '?', and ':'.

    Example:
        >>> text_indentation("Hello. How are you?")
        Hello.

        How are you?
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
