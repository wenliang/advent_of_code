
from collections import Counter


with open("day06_input.txt", "r") as f:
    raw_input = [a for a in f.readlines()]

lanternfish_internal_timers = [int(a) for a in raw_input[0].split(",")]

count = dict(Counter(lanternfish_internal_timers))
print(count)

def next_day_v2(count):
    number_of_zeros = count.get(0, 0)
    new_count = {}
    for c in range(0, 8):
        new_count[c] = count.get(c+1, 0)
    new_count[8] = number_of_zeros
    new_count[6] += number_of_zeros
    return new_count

# Q1
n_day = 80
# Q2
n_day = 256

for day in range(n_day):
    count = next_day_v2(count)
    print(count)

print(count)
print(sum(count.values()))
