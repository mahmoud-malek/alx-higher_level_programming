#!/usr/bin/python3
"""
MyList Module

This module defines the MyList class, which inherits
 from the built-in list class.
It provides a method to print the list in ascending order.

Example:
    my_list = MyList()
    my_list.append(3)
    my_list.append(1)
    my_list.append(2)
    my_list.print_sorted()  # Prints the list in ascending order
"""


class MyList(list):
    def print_sorted(self):
        """
        Print the list in ascending order.

        This method sorts the list in ascending order using the sorted function
        and then prints the sorted list.

        Args:
            None

        Returns:
            None
        """
        sorted_list = sorted(self)
        print(sorted_list)
