#!/usr/bin/python3
"""
This module defines a function that multiplies two matrices.

Functions:
    matrix_mul(m_a, m_b): Multiplies two matrices.

Example:
    >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    [[7, 10], [15, 22]]
"""


def matrix_mul(m_a, m_b):
    """
    Function to multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Returns:
        list of lists of ints/floats: A new matrix representing
                the multiplication of m_a by m_b.

    Raises:
        TypeError: If either m_a or m_b is not a list of lists of
                 integers/floats, if either m_a or m_b is empty,
                  or if either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.

    Example:
        >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
        [[7, 10], [15, 22]]
    """
    # Check if m_a and m_b are lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a) or not \
            all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b \
         must be a list of lists")

    # Check if m_a and m_b are not empty
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    # Check if elements of m_a and m_b are integers or floats
    for row in m_a:
        if not all(isinstance(val, (int, float)) for val in row):
            raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if not all(isinstance(val, (int, float)) for val in row):
            raise TypeError("m_b should contain only integers or floats")

    # Check if m_a and m_b are rectangles
    if len(set(len(row) for row in m_a)) != 1 or \
            len(set(len(row) for row in m_b)) != 1:
        raise TypeError("Each row of m_a must be of the same size or \
            each row of m_b must be of the same size")

    # Check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
