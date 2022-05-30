#!/usr/bin/python3
'''this function allows to make a division between
a matrix and a divisor, the matrix must contain integer
or floating elements just as its divisor must be an
integer or floating number
add_integer(1, 2)'''


def matrix_divided(matrix, div):
    '''it must be evaluated if the div is an integer or
    float number and different from 0
    matrix is ​​evaluated that is a matrix and contains integers or floats'''
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (type(matrix) == list):
        a = []
        for i in matrix:
            a.append(len(i))
        a = set(a)
        if (len(a) == 1):
            matrice = []
            for row in matrix:
                listmatrix = []
                for element in row:
                    if isinstance(element, int) or isinstance(element, float):
                        listmatrix.append(round(element / div, 2))
                    else:
                        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                matrice.append(listmatrix)
            return matrice
        else:
            raise TypeError("Each row of the matrix must have the same size")
    else:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
