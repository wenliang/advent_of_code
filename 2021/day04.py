#! /usr/bin/env python3

with open("day04_input.txt", "r") as f:
    line_inputs = f.readlines()

num_seq = [int(a) for a in line_inputs[0].split(",")]

lines = [a.strip().split() for a in line_inputs[1:]]
n_block = int(len(lines) / 6)
blocks = [lines[a*6+1:(a+1)*6] for a in range(n_block)]

# print(blocks)

# size of blocks elements
n_block = len(blocks)
n_row = 5
n_col = 5
# same size as blocks
matched = [[[False for i_col in range(n_col)] for i_row in range(n_row)] for i_block in range(n_block)]

def mark(num):
    for i_block in range(n_block):
        for i_row in range(n_row):
            for i_col in range(n_col):
                if int(blocks[i_block][i_row][i_col]) == num:
                    # print("matched {} {} {}".format(i_block, i_row, i_col))
                    matched[i_block][i_row][i_col] = True 


def check_block(block):
    # print(block)
    transposed = list(zip(*block))
    return any([all(a) for a in block]) or any([all(a) for a in transposed])

def find_first_bingo():
    for num in num_seq:
        # print(num)
        mark(num)
        for i_block, block in enumerate(blocks):
            if check_block(matched[i_block]):
                return i_block, num

def find_last_bingo():
    unmatched_blocks = list(range(n_block))
    for num in num_seq:
        mark(num)
        for i_block, block in enumerate(blocks):
            if i_block in unmatched_blocks and check_block(matched[i_block]):
                unmatched_blocks.remove(i_block)
                if len(unmatched_blocks) == 0:
                    print(matched[i_block])
                    return i_block, num
        print(unmatched_blocks)

def count_unmatched(block, block_match):
    sumed = 0
    for i_row in range(n_row):
        for i_col in range(n_col):
            if not block_match[i_row][i_col]:
                sumed += int(block[i_row][i_col])
    return sumed

# Q1
# i_block, num = find_first_bingo()
# sumed = count_unmatched(blocks[i_block], matched[i_block])
# print(num, i_block, num*sumed)

# Q2
i_block, num = find_last_bingo()
sumed = count_unmatched(blocks[i_block], matched[i_block])
print(num, i_block, num*sumed)

