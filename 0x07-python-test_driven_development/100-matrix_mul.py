#!/usr/bin/python3
"""
    this is a module to multiply two matrices
"""
def matrix_mul(m_a, m_b):
    """
        this is a function to multiply two matrices
        with the condition that the number of columns
        of the first matrix must be equal to the number
        of rows of the second matrix
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    
    if type(m_a[0]) is not list:
        raise TypeError("m_a must be a list of lists")
    
    if type(m_b[0]) is not list:
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all([isinstance(j, (int, float)) for i in m_a for j in i]):
        raise TypeError("m_a should contain only integers or floats")
    
    if not all([isinstance(j, (int, float)) for i in m_b for j in i]):
        raise TypeError("m_b should contain only integers or floats")

    if not all([len(i) == len(m_a[0]) for i in m_a]):
        raise TypeError("each row of m_a must be of the same size")
    
    if not all([len(i) == len(m_b[0]) for i in m_b]):
        raise TypeError("each row of m_b must be of the same size")
    
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_list = []

    for item1 in m_a:
        tmp = []
        for i in range(len(m_b[0])):
            tmp.append(sum([(item1[j] * m_b[j][i]) for j in range(len(item1))]))
        new_list.append(tmp)
    return new_list