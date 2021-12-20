#! /usr/bin/env python3

with open("day03_input.txt", "r") as f:
    lines_input = f.readlines()

n_char_per_line = 12


#############################################################
# first scan
n_ones = [0] * n_char_per_line
n_zeros = [0] * n_char_per_line
for line in lines_input:
    for i, char in enumerate(line):
        if char == "1":
            n_ones[i] += 1
        elif char == "0":
            n_zeros[i] += 1
        else:
            pass # this is \n
            # print("{} not supported".format(char))

print("count of ones: {}".format(n_ones))
print("count of zeros: {}".format(n_zeros))

#  calculate gamma / epsilon
b_gamma = "0b"
b_epsil = "0b"

for i in range(n_char_per_line):
    if n_ones[i] > n_zeros[i]:
        b_gamma += "1"
        b_epsil += "0"
    else:
        b_gamma += "0"
        b_epsil += "1"

print("gamma in binary: {}, epsilon in binary: {}".format(b_gamma, b_epsil))

# convert binary numbers to integer
i_gamma = int(b_gamma, 2)
i_epsil = int(b_epsil, 2)

print("gamma: {}, epsilon: {}, power consumption: {}".format(i_gamma, i_epsil, i_gamma*i_epsil))

#############################################################
# life support rating

def count_most_common(lines, index):
    n_1 = 0
    n_0 = 0
    for line in lines:
        if line[index] == "1":
            n_1 += 1
        elif line[index] == "0":
            n_0 += 1
    if n_1 >= n_0:
        return "1"
    else:
        return "0"

def count_least_common(lines, index):
    n_1 = 0
    n_0 = 0
    for line in lines:
        if line[index] == "1":
            n_1 += 1
        elif line[index] == "0":
            n_0 += 1
    if n_1 >= n_0:
        return "0"
    else:
        return "1"

def filter_lines(lines, search_method):
    # remove the 0b in the beginning of bit_criteria
    for i in range(n_char_per_line):
        left_lines = []
        check_char = search_method(lines, i)
        for line in lines:
            if line[i] == check_char:
                left_lines.append(line)
        if len(left_lines) == 1:
            return left_lines[0]
        if len(left_lines) == 0:
            print("nothing left. something wrong. break here")
            1/0
        lines = left_lines
        left_lines = []

    print("nothing left. something wrong. break here")
    1/0

b_oxygen_gen_rating = "0b{}".format(filter_lines(lines_input, count_most_common))
b_co2_scrubber_rating = "0b{}".format(filter_lines(lines_input, count_least_common))

print("oxgen: {}, co2: {}".format(b_oxygen_gen_rating, b_co2_scrubber_rating))

i_oxygen = int(b_oxygen_gen_rating, 2)
i_co2 = int(b_co2_scrubber_rating, 2)

print("oxygen: {}, co2: {}, life support: {}".format(i_oxygen, i_co2, i_oxygen*i_co2))

