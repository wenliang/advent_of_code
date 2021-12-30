#! /usr/bin/env python3

import numpy as np
from IPython import embed

# read inputs
with open("day09_input.txt", "r") as f:
    line_inputs = f.readlines()

matrix = np.matrix([[int(a) for a in line.strip()] for line in line_inputs])
# print(matrix)

n_row, n_col = matrix.shape

edge_row = np.array([True for i in range(n_col)])
edge_col = np.array([[True] for i in range(n_row)])

compare_down  = np.vstack([matrix[0:-1] < matrix[1:], edge_row])
compare_up    = np.vstack([edge_row, matrix[0:-1] > matrix[1:]])
compare_left  = np.hstack([matrix[:, :-1] < matrix[:, 1:], edge_col])
compare_right = np.hstack([edge_col, matrix[:, :-1] > matrix[:, 1:]])
compare_v = np.logical_and(compare_down, compare_up)
compare_h = np.logical_and(compare_left, compare_right)
low_point_bool = np.logical_and(compare_h, compare_v)
low_point_int = np.where(low_point_bool, 1, 0)

addup = np.multiply(matrix, low_point_int).sum() + low_point_int.sum()
print("q1: {}".format(addup))

embed()
