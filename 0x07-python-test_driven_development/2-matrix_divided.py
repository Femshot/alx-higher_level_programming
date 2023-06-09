#!/usr/bin/python3
"""Module containing a function matrix_divided"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix (list of list): list of list of int or float
        div (int/float): integer or float to divide for

    Raises:
        TypeError: Exception if elements in matrix and div are not integer or
            float, if rows in the matrix aren't the same size
        ZeroDivisionError: Exception if div is 0

    Return:
        The result to divide matrix by div
    """

    if type(div) not in [int, float] or div + 1 == div or div != div:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is list:
        new_matrix = [x[:] for x in matrix]
        for i in range(len(matrix)):
            if i <= len(matrix) - 2 and len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError("Each row of the matrix must have the same" +
                                " size")
            for j in range(len(matrix[i])):
                if type(matrix[i][j]) not in [int, float] or\
                        matrix[i][j] + 1 == matrix[i][j]:
                    raise TypeError("matrix must be a matrix (list of lists)" +
                                    " of integers/floats")
                else:
                    div_num = round(matrix[i][j] / div, 2)
                    if type(div_num) not in [int, float] or div_num != div_num:
                        raise TypeError("matrix must be a matrix (list of " +
                                        "lists)" + " of integers/floats")
                    new_matrix[i][j] = div_num
    else:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    return new_matrix
