from itertools import accumulate

min_x = 257
max_x = 286
min_y = -101
max_y = -57

vy_max = 10000
vx_max = max_x+1
step_max = 10000

def check_valid_vy(vy, step_max=step_max, min_y=min_y, max_y=max_y):
    vys = list(range(vy, vy-step_max, -1))
    distances = list(accumulate(vys))
    steps_valid = [i+1 for i, a in enumerate(distances) if a>=min_y and a <=max_y]
    if len(steps_valid) > 0:
        return vy, max(distances), steps_valid
    else:
        return 0

def check_valid_vx(vx, step_max=step_max, min_x=min_x, max_x=max_x):
    vxs = list(range(vx, vx-step_max, -1))
    vxs = [a if a>=0 else 0 for a in vxs]
    distances = list(accumulate(vxs))
    steps_valid = [i+1 for i, a in enumerate(distances) if a>=min_x and a <=max_x]
    if len(steps_valid) > 0:
        return vx, steps_valid
    else:
        return 0

# NOTE: the possible velocity of y could be negative in q2
all_vys = [check_valid_vy(vy) for vy in range(min_y, vy_max)]
vys = [(a[0], a[2]) for a in all_vys if a != 0]

all_vxs = [check_valid_vx(vx) for vx in range(vx_max)]
vxs = [a for a in all_vxs if a != 0]

print([(a[0], len(a[1])) for a in vys])
print([(a[0], len(a[1])) for a in vxs])

# q1
heights = [a[1] for a in all_vys if a!=0]
print(max(heights))

# q2 
valid_start = []
for vy, steps_y in vys:
    for vx, steps_x in vxs:
        set_y = set(steps_y)
        set_x = set(steps_x)
        if len(set_y.intersection(set_x)) > 0:
            valid_start.append((vx, vy))

# print(valid_start)
print(len(valid_start))

