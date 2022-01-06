#! /usr/bin/env python3

from IPython import embed
from collections import Counter
from functools import lru_cache

import sys
sys.setrecursionlimit(16385)

# read inputs
with open("day14_input.txt", "r") as f:
    line_input = f.readlines()[0].strip()

def parse_rule(rule):
    k, v = rule.split(" -> ")
    return k, v+k[1]

with open("day14_rules.txt", "r") as f:
    rule_list = [parse_rule(a.strip()) for a in f.readlines()]
    rules = {k:v for k, v in rule_list}

print(rules)

# process
def str2key(s):
    l2 = [a for a in s]
    l1 = [" "] + l2[:-1]
    return ["".join([a, b]) for a, b in zip(l1, l2)]

def count_pair_10th(pair):

    for i in range(10):
        new_list = [rules.get(k, k[1]) for k in str2key(pair)]
        pair = "".join(new_list)

    return Counter(pair[1:]), pair
record_pair_10th = {k: count_pair_10th(k) for k in rules}

@lru_cache(400)
# use cahce when recursive 
def count_pair_10th_xn(pair, n=4):
    if n == 1:
        return record_pair_10th[pair][0]

    _, s_input = record_pair_10th[pair]
    final_count = Counter()
    for k in str2key(s_input)[1:]:
        i_count = count_pair_10th_xn(k, n-1)
        final_count += i_count
    return  final_count

def count_str_10th_xn(s_input, n=4):
    # split str into pairs then count
    final_count = Counter()
    for k in str2key(s_input)[1:]:
        i_count = count_pair_10th_xn(k, n)
        final_count += i_count
    final_count[s_input[0]] += 1
    return final_count
    
# test
print("count pair x10")
print(count_pair_10th("ON"))
print("count pair x40")
print(count_pair_10th_xn("ON", 4))

# answer the questions
print("count string x10")
print(count_str_10th_xn(line_input, 1))
print("count string x40")
print(count_str_10th_xn(line_input, 4))

