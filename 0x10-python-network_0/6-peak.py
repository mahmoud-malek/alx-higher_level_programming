#!/usr/bin/python3

""" a module that defines a function to find a peak """


def find_peak(list_of_integers):
    """ this is a function to get the peak """

    ls = list_of_integers
    start = 0
    end = len(ls) - 1

    while (start < end):
        mid = int(start + (end - start) // 2)

        if ls[mid] < ls[mid + 1]:
            start = mid + 1
        else:
            end = mid
    if start < 0 or start > len(ls)-1:
        return None
    return ls[start]
