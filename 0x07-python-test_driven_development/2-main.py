#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
try:
    print(matrix_divided(matrix, 0))
except Exception as e:
    print(e)
try:
    print(matrix_divided(matrix, 2.889))
except Exception as e:
    print(e)
try:
    print(matrix_divided([[1, 2, 3], [4, 5, 'a']], 3))
except Exception as e:
    print(e)
try:
    print(matrix_divided("[[1, 2, 3], [4, 5, 'a']]", 3))
except Exception as e:
    print(e)
try:
    print(matrix_divided([[1, 2, 3], [4, 5, 'a']], "school"))
except Exception as e:
    print(e)
