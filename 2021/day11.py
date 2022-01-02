#! /usr/bin/env python3

from IPython import embed

# read inputs
with open("day11_input.txt", "r") as f:
    line_inputs = f.readlines()

matrix = [[int(a) for a in line.strip()] for line in line_inputs]
n_row = len(matrix)
n_col = len(matrix[0])

neighbors_delta = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1)
        ]

def is_valid(y, x):
    return y >= 0 and x >= 0 and y < n_row and x < n_col

def flash_neighbours(y, x):
    for d_y, d_x in neighbors_delta:
        y2, x2 = y+d_y, x+d_x
        if not is_valid(y2, x2):
            continue
        add_point(y2, x2)

def add_point(y, x):
    global matrix
    matrix[y][x] += 1
    if matrix[y][x] == 10:
        flash_neighbours(y, x)


def reset_matrix():
    global matrix
    n_flash = 0
    for y in range(n_row):
        for x in range(n_col):
            if matrix[y][x] >= 10:
                matrix[y][x] = 0
                n_flash += 1
    return n_flash


def scan_matrix():
    for y in range(n_row):
        for x in range(n_col):
            add_point(y, x)

    return reset_matrix()

total_flash = 0
for i in range(1000):
    n_flash = scan_matrix()
    total_flash += n_flash

    if i == 99:
        print("q1: 100 turns have {} flashes.".format(total_flash))

    if n_flash == n_row * n_col:
        print("q2: all synchronized at {} turn".format(i+1))
        break


