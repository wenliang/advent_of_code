
with open("day02_input.txt", "r") as f:
    sizes = [a.strip().split("x") for a in f.readlines()]
    sizes = [[int(a) for a in line] for line in sizes]

# print(sizes)

def calculate_wrap(s):
    l, h, w = s
    m = max(h, l, w)
    return 2*h*l + 2*l*w + 2*h*w + l*h*w/m

def calculate_ribbon(s):
    l, h, w = s
    m = max(h, l, w)
    return 2*(h+l+w -m) + l*h*w

total_wrap = sum([calculate_wrap(s) for s in sizes])
print(total_wrap)

total_ribbon = sum([calculate_ribbon(s) for s in sizes])
print(total_ribbon)
