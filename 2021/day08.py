#! /usr/bin/env python3

from collections import Counter
from itertools import chain

# read inputs
with open("day08_input.txt", "r") as f:
    line_inputs = f.readlines()

lines = [a.split("|") for a in line_inputs]

# constants
seg2num = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9
        }


def find_s1_s4_s7(s_train):
    seg_train = s_train.strip().split()
    lens = [2, 4, 3] 
    return [[s for s in seg_train if len(s) == l][0] for l in lens]

def get_map_char(s_train):
    count = Counter(s_train.replace(" ", ""))

    s1, s4, s7 = find_s1_s4_s7(s_train)

    trans = {6: lambda x: "b",
            4: lambda x: "e",
            9: lambda x: "f",
            8: lambda x: "c" if x in s1 else "a",
            7: lambda x: "d" if x in s4 else "g" }

    trans_char = {k: trans[v](k) for k, v in count.items()}
    trans_char[" "] = " "

    return trans_char

def wrong_str2num(s_train, s_test):
    trans_char = get_map_char(s_train)
    segments = ["".join(sorted(a)) for a in "".join([trans_char[a] for a in s_test.strip()]).split()]
    return [seg2num[a] for a in segments]


# Q1
single_numbers = [wrong_str2num(k, v) for k, v in lines]
counts = Counter(chain.from_iterable(single_numbers))
# print(counts)
print(sum([counts[i] for i in [1, 4, 7, 8]]))
    
# Q2
def combine_num(nums):
    return nums[0]*1000 + nums[1]*100 + nums[2]*10 + nums[3]
combined_numbers = [combine_num(a) for a in single_numbers]
print(sum(combined_numbers))
