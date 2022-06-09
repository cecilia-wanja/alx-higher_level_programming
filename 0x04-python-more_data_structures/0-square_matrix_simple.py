#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    cols = len(matrix[0])
    list = []
    for x in range(rows):
        list2 = []
        for y in range(cols):
            list2.append(matrix[x][y]*matrix[x][y])
        list.append(list2)
    return list
