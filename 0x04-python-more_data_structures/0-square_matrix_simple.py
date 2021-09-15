#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix != None:
        new_matrix = [[n * n for n in a] for a in matrix]
        return new_matrix
    else:
        return
