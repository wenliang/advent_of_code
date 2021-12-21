#! /usr/bin/env python3


with open("day01_input.txt", "r") as f:
    lines_input = f.readlines()

lines = [int(a) for a in lines_input]
n_lines = len(lines)
part1 = lines[0:n_lines-1]
part2 = lines[1:n_lines]

compare = [1 for (a, b) in zip(part1, part2) if b>a]
print(len(compare))

##########################################
part1 = lines[0:n_lines-2]
part2 = lines[1:n_lines-1]
part3 = lines[2:n_lines]
sumed = [a+b+c for (a, b, c) in zip(part1, part2, part3)]

n_sumed = len(sumed)
p1 = sumed[0:n_sumed-1]
p2 = sumed[1:n_sumed]
compare = [1 for (a, b) in zip(p1, p2) if b>a]
print(len(compare))
