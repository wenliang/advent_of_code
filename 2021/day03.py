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
c_gamma, c_epsilon = list(zip(*counts))

b_gamma = "0b{}".format("".join(c_gamma))
b_epsil = "0b{}".format("".join(c_epsilon))
print("gamma in binary: {}, epsilon in binary: {}".format(b_gamma, b_epsil))

# convert binary numbers to integer
i_gamma = int(b_gamma, 2)
i_epsil = int(b_epsil, 2)
print("gamma: {}, epsilon: {}, power consumption: {}".format(i_gamma, i_epsil, i_gamma*i_epsil))

#############################################################
# life support rating

def count_most_least_char(lines, index):
    collect = [line[index] for line in lines]
    counts = Counter(collect)
    return ["1", "0"] if counts["1"] >= counts["0"] else ["0", "1"]

def filter_lines(lines, most_or_least):
    assert most_or_least in [0, 1]

    for i in range(n_char_per_line):
        check_char = count_most_least_char(lines, i)[most_or_least]
        left_lines = [line for line in lines if line[i] == check_char]
        if len(left_lines) == 1:
            return left_lines[0]
        if len(left_lines) == 0:
            print("nothing left. something wrong. break here")
            1/0
        lines = left_lines

    print("nothing left. something wrong. break here")
    1/0


b_oxygen_gen_rating = "0b{}".format("".join(filter_lines(lines, 0)))
b_co2_scrubber_rating = "0b{}".format("".join(filter_lines(lines, 1)))

print("oxgen: {}, co2: {}".format(b_oxygen_gen_rating, b_co2_scrubber_rating))

i_oxygen = int(b_oxygen_gen_rating, 2)
i_co2 = int(b_co2_scrubber_rating, 2)

print("oxygen: {}, co2: {}, life support: {}".format(i_oxygen, i_co2, i_oxygen*i_co2))

