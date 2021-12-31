#! /usr/bin/env python3

from IPython import embed

from copy import deepcopy
from time import sleep

# read inputs
with open("day25_input.txt", "r") as f:
    line_inputs = f.readlines()

matrix = [[a for a in line.strip()] for line in line_inputs]
# print(lines[:3])
n_y = len(matrix)
n_x = len(matrix[0])

# q1
def next_right():
    empty_matrix = deepcopy(matrix)
    n = 0
    for y in range(n_y):
        for x in range(n_x):
            if empty_matrix[y][x] == ">":
                x2 = (x+1) % n_x
                # empty_matrix will not be changed
                next_position = empty_matrix[y][x2]
                if next_position == ".":
                    n += 1
                    # swap
                    matrix[y][x2] = ">"
                    matrix[y][x] = "."
                
    return n

def next_down():
    empty_matrix = deepcopy(matrix)
    n = 0
    for y in range(n_y):
        for x in range(n_x):
            if empty_matrix[y][x] == "v":
                y2 = (y+1) % n_y
                # empty_matrix will not be changed
                next_position = empty_matrix[y2][x]
                if next_position == ".":
                    n += 1
                    # swap
                    matrix[y][x] = "."
                    matrix[y2][x] = "v"
                
    return n

def display():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    for line in matrix:
        print("".join(line))

for n in range(1000):
    moves_right = next_right()
    moves_down  = next_down()
    display()
    sleep(0.2)

    if moves_right + moves_down == 0:
        print(n+1)
        break
