#! /usr/bin/env python3

from itertools import chain

with open("day04_input.txt", "r") as f:
    line_inputs = f.readlines()

num_seq = [int(a) for a in line_inputs[0].split(",")]

lines = [[int(b) for b in a.strip().split()] for a in line_inputs[1:]]
n_block = int(len(lines) / 6)
blocks = [lines[a*6+1:(a+1)*6] for a in range(n_block)]

# print(blocks)

# size of blocks elements
n_block = len(blocks)
n_row = 5
n_col = 5
# same size as blocks

def mark(num, blocks):
    def equal_to_zero(a, num):
        return a if a != num else 0
    return [[[equal_to_zero(a, num) for a in b ] for b in c] for c in blocks]

def check_block(block):
    # print(block)
    transposed = list(zip(*block))
    return any([sum(a) == 0 for a in block]) or any([sum(a)==0 for a in transposed])

def find_first_bingo(blocks):
    for num in num_seq:
        # print(num)
        blocks = mark(num, blocks)
        for i_block, block in enumerate(blocks):
            if check_block(blocks[i_block]):
                return i_block, num

def find_last_bingo(blocks):
    unmatched_blocks = list(range(n_block))
    for num in num_seq:
        blocks = mark(num, blocks)
        blocks_left = [b for b in blocks if not check_block(b)]
        if len(blocks) == 1 and len(blocks_left) == 0:
            return blocks[0], num
        else:
            blocks = blocks_left

def count_unmatched(block):
    return sum(list(chain.from_iterable(block)))

# Q1
# block, num = find_first_bingo(blocks)
# sumed = count_unmatched(block)
# print(num, i_block, num*sumed)

# Q2
block, num = find_last_bingo(blocks)
sumed = count_unmatched(block)
print(num, num*sumed)

