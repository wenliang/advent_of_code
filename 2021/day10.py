#! /usr/bin/env python3

from IPython import embed

# read inputs
with open("day10_input.txt", "r") as f:
    line_inputs = f.readlines()

lines = [[a for a in line.strip()] for line in line_inputs]
# print(lines[:3])

# constants
part1 = [a for a in "([{<"]
part2 = [a for a in ")]}>"]
pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
        }

########################################
# q1
scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
        }

def find_1st_bad(l):
    stack = []
    for c in l:
        if c in part1:
            stack.append(c)
        elif c in part2:
            exp_c = pairs[stack.pop()]
            if c != exp_c:
                return scores[c]
    return 0

bad_1st = [find_1st_bad(l) for l in lines]
print(bad_1st)
print(sum(bad_1st))

########################################
# q2
scores_q2 = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
        }

def find_uncompleted(l):
    stack = []
    for c in l:
        if c in part1:
            stack.append(c)
        elif c in part2:
            exp_c = pairs[stack.pop()]
            if c != exp_c:
                return None

    # stack should be all part1
    rights = [scores_q2[pairs[a]]*5**i for i,a in enumerate(stack)]
    return sum(rights)

scores = [find_uncompleted(l) for l in lines]
scores_valid = [s for s in scores if s]
scores = sorted(scores_valid)
print(scores[int(len(scores)/2)])
embed()

