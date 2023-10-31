#!/usr/bin/python3
"""
This module defines a function that multiplies two matrices using NumPy.

Functions:
    lazy_matrix_mul(m_a, m_b): Multiplies two matrices.

Example:
    >>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    array([[ 7, 10],
           [15, 22]])
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function to multiply two matrices using NumPy's matmul function.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Returns:
        numpy.ndarray: A new matrix representing the
                 multiplication of m_a by m_b.

    Example:
        >>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
        array([[ 7, 10],
               [15, 22]])
    """
    return (np.matmul(m_a, m_b))
