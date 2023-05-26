#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes square value of integars in matrix"""
    new_mat = []
    for blocks in matrix:
        new_mat += [list(map(lambda x: x**2, blocks))]
    return new_mat
