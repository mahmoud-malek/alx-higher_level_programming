#!/usr/bin/python3

"""
This module defines a Rectangle class
"""


class Rectangle:
    """
    A Rectangle class with attributes width and height, and methods area,
    perimeter, __str__, __repr__, __del__, bigger_or_equal and square.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize Rectangle with width and height
        """
        self.width = width
        self.height = height
        self.print_symbol = '#'

    @property
    def width(self):
        """
        Retrieve the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the Rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the Rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return (str(self.print_symbol) * self.__width + '\n') * \
            self.__height.rstrip()

    def __repr__(self):
        """
        Return a string representation of the Rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
