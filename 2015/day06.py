import re
import numpy as np

def parse_line(s):
    p = re.compile("(.*?) (\d+),(\d+) through (\d+),(\d+)")
    return p.findall(s)[0]

with open("day06_input.txt", "r") as f:
    instructions = [parse_line(line.strip()) for line in f.readlines()]
    # print(instructions)

def run_instruct_q1(instruct):
    action, ax, ay, bx, by = instruct
    ax, ay, bx, by = int(ax), int(ay), int(bx), int(by)
    if action == "turn on":
        map[ay:by+1, ax:bx+1] = 1
    elif action == "turn off":
        map[ay:by+1, ax:bx+1] = 0
    elif action == "toggle":
        map[ay:by+1, ax:bx+1] = 1 - map[ay:by+1, ax:bx+1]
    else:
        raise NotImplementedError

def run_instruct_q2(instruct):
    action, ax, ay, bx, by = instruct
    ax, ay, bx, by = int(ax), int(ay), int(bx), int(by)
    if action == "turn on":
        map[ay:by+1, ax:bx+1] += 1
    elif action == "turn off":
        map[ay:by+1, ax:bx+1] -= 1
        # NOTE: map minimum is 0
        map[map < 0] = 0
    elif action == "toggle":
        map[ay:by+1, ax:bx+1] += 2
    else:
        raise NotImplementedError

# use numpy array for easier process
map = np.zeros([1000, 1000], dtype=int)
for instruct in instructions:
    run_instruct_q1(instruct)

print(sum([sum(line) for line in map]))

map = np.zeros([1000, 1000], dtype=int)
for instruct in instructions:
    run_instruct_q2(instruct)

print(sum([sum(line) for line in map]))
