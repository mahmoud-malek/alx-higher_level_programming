#!/usr/bin/python3
"""
class base
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ instantiation with size """
        self.__size = size
        super().__init__(self.__size, self.__size)
