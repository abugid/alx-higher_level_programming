#!/usr/bin/python3
"""
    This is a module to multiply two matrices using the module numpy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
        This is a function used to multiply two matrices
        with the help of numpy
    """
    return numpy.matmul(m_a, m_b)
