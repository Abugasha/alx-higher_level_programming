#!/usr/bin/python3
"""
This file multiplies two matrix
Written by: daorejuela1
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function automatically ident text.

    Args:
        ma_a: first matrix.
        ma_b: second matrix.

    Returns:
        matrix with mult value.

    Raises:
        TypeError: if matrices are empty
        doesnt have int/float or
        cant multiply.
    """
    result = np.matmul(m_a, m_b)
    return result
