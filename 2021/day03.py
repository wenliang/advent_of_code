#! /usr/bin/env python3

from collections import Counter

with open("day03_input.txt", "r") as f:
    lines_input = f.readlines()

n_char_per_line = 12

# 1000x12
lines = [[char for char in line.strip()] for line in lines_input]
# 12x1000
groups = list(zip(*lines))

#############################################################
# first scan
def count_most_least(group):
    counts = Counter(group)
    return ("1", "0") if counts["1"] >= counts["0"] else ("0", "1")

counts = [count_most_least(g) for g in groups]
parameters = list(zip(*counts))

b_para = ["0b{}".format("".join(c_para)) for c_para in parameters]
print("gamma in binary: {}, epsilon in binary: {}".format(b_para[0], b_para[1]))

# convert binary numbers to integer
i_para = [int(b, 2) for b in b_para]
print("gamma: {}, epsilon: {}, power consumption: {}".format(i_para[0], i_para[1], i_para[0]*i_para[1]))

#############################################################
# life support rating

# NOTE: cannot reuse the group above. because it is changing after each filter.

def filter_lines(lines, most_or_least):
    assert most_or_least in [0, 1]

    if len(lines) == 1:
        return lines[0]
    if len(lines) == 0:
        print("nothing left. something wrong. break here")
        1/0

    g1 = [line[0] for line in lines]
    check_char = count_most_least(g1)[most_or_least]
    left_lines = [line[1:] for line in lines if line[0] == check_char]
    # NOTE: use recursive way
    return [check_char] + filter_lines(left_lines, most_or_least)

b_paras =  ["0b{}".format("".join(filter_lines(lines, i))) for i in range(2)]
print("oxgen: {}, co2: {}".format(b_paras[0], b_paras[1]))

i_paras = [int(para, 2) for para in b_paras]
print("oxygen: {}, co2: {}, life support: {}".format(i_paras[0], i_paras[1], i_paras[0]*i_paras[1]))

