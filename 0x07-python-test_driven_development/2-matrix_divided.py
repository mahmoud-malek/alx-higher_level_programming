#!/usr/bin/python3


"""
 This Moudule do some stuff :)
"""


def matrix_divided(matrix, div):
    """
    Function to divide all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
         Each sub-list represents a row in the matrix.
        div (int or float): The number by which to divide
         all elements of the matrix.

    Returns:
        list of lists: A new matrix with all elements divided by div.
         Each element is rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
         if rows in the matrix have different sizes,
          or if div is not an integer or float.
        ZeroDivisionError: If div is 0.

    Example:
        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 2)
        [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
