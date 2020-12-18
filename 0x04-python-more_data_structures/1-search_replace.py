#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixc = []
    for n in matrix:
        matrixf = list(map(lambda x: x ** 2, n))
        matrixc.append(matrixf)
    return matrixc
