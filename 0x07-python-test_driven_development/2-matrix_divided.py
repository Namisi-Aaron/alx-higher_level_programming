#!/usr/bin/python3
"""matrix_divided module"""

def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    new_matrix = []
    for i in matrix:
        for j in i:
            if not isinstance(j, (float,int)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
            if not all(len(i) == len(matrix[0]) for i in matrix):
                raise TypeError("Each row of the matrix must have the same size")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            new_matrix[i][j] = round((j/div), 2)
    return new_matrix
