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

#############
# Q2

from collections import Counter
from itertools import chain

def is_valid(y, x):
    return y >= 0 and x >= 0 and y < n_row and x < n_col

def should_skip(height):
    return height == 9 or type(height) == str

matrix = [[int(a) for a in line.strip()] for line in line_inputs]

def mark_basin(y, x, basin_name):
    print(y, x, basin_name)
    if not is_valid(y, x):
        return
    if should_skip(matrix[y][x]):
        return

    matrix[y][x] = basin_name

    # check neighbours recursively
    neighbours = [(y-1, x), (y+1, x), (y, x+1), (y, x-1)]
    for y1, x1 in neighbours:
        mark_basin(y1, x1, basin_name)

i_basin = 0
for i_row in range(n_row):
    for i_col in range(n_col):
        if not should_skip(matrix[i_row][i_col]):
            i_basin += 1
            basin_name = "b{:03d}".format(i_basin)
            mark_basin(i_row, i_col, basin_name)


count = Counter(chain(*matrix))
del count[9]
size_basins = sorted(count.values(), reverse=True)

print(size_basins[0] * size_basins[1] * size_basins[2])

embed()
