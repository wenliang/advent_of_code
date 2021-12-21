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

def mark(blocks, num):
    def equal_to_zero(a, num):
        return a if a != num else 0
    return [[[equal_to_zero(a, num) for a in b ] for b in c] for c in blocks]

def check_block(block):
    # print(block)
    transposed = list(zip(*block))
    return any([sum(a) == 0 for a in block]) or any([sum(a)==0 for a in transposed])

def find_first_bingo(blocks, num_seq):
    for num in num_seq:
        # print(num)
        blocks = mark(blocks, num)
        blocks_matched = [block for block in blocks if check_block(block)]
        if len(blocks_matched) > 0:
            return blocks_matched[0], num

def find_last_bingo(blocks, num_seq):
    unmatched_blocks = list(range(n_block))
    for num in num_seq:
        blocks = mark(blocks, num)
        blocks_left = [b for b in blocks if not check_block(b)]
        if len(blocks) == 1 and len(blocks_left) == 0:
            return blocks[0], num
        else:
            blocks = blocks_left

def count_unmatched(block):
    # flatten the 2D block into 1D. then add it up
    return sum(list(chain.from_iterable(block)))

# Q1
block, num = find_first_bingo(blocks, num_seq)
sumed = count_unmatched(block)
print("Q1: last num {}\nfirst block: \n{}\nanswer: {}".format(num, block, num*sumed))

# Q2
block, num = find_last_bingo(blocks, num_seq)
sumed = count_unmatched(block)
print("Q2: last num {}\nlast block: \n{}\nanswer: {}".format(num, block, num*sumed))

