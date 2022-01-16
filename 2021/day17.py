from itertools import accumulate

min_x = 257
max_x = 286
min_y = -101
max_y = -57

vy_max = 10000
step_max = 10000

def check_valid_vy(vy, step_max=step_max, min_y=min_y, max_y=max_y):
    vys = list(range(vy, vy-step_max, -1))
    distances = list(accumulate(vys))
    distances_valid = [a for a in distances if a>=min_y and a <=max_y]
    if len(distances_valid) > 0:
        return max(distances)
    else:
        return 0

heights = [check_valid_vy(vy) for vy in range(vy_max)]
print(max(heights))
