import re

with open("day05_input.txt", "r") as f:
    strings = [line.strip() for line in f.readlines()]

def contains_3_vowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    k = [c for c in s if c in vowels]
    return len(k) >= 3

def contains_repeat(s):
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            return True
    else:
        return False

def not_contains_bad(s):
    bads = ["ab", "cd", "pq", "xy"]
    for b in bads:
        if b in s:
            return False
    else:
        return True

def is_good_string(s):
    return contains_3_vowels(s) and contains_repeat(s) and not_contains_bad(s)

def q2r1(s):
    p = re.compile(r"(..).*?(\1)")
    return len(p.findall(s)) > 0

def q2r2(s):
    p = re.compile(r"(.).(\1)")
    return len(p.findall(s)) > 0

def q2(s):
    return q2r1(s) and q2r2(s)


good_str = [s for s in strings if is_good_string(s)]
print(len(good_str))

good_str = [s for s in strings if q2(s)]
print(len(good_str))
