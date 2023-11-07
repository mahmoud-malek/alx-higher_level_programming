#!/usr/bin/python3

"""AUTOHR: MAHMOUD ABDEL MALEK """


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    pascal = []  # Initialize the Pascal's triangle as an empty list

    for i in range(n):
        row = []  # Initialize a new row for each iteration
        for j in range(i + 1):
            if j == 0 or j == i:
                # The first and last elements of each row are always 1
                row.append(1)
            else:
                # The other elements are the sum of the two elements
                #  above them in the previous row
                prev_row = pascal[i - 1]
                new_element = prev_row[j - 1] + prev_row[j]
                row.append(new_element)
        pascal.append(row)  # Add the row to the Pascal's triangle

    return pascal
