#! /usr/bin/env python3

with open("day02_input.txt", "r") as f:
    lines_input = f.readlines()

def split_str(s):
    a, b = s.split(" ")
    return (a, int(b))
lines = [split_str(l) for l in  lines_input]

#################################################3

x, y = 0, 0

def forward(a):
    global x
    x += a

def up(a):
    global y
    y -= a

def down(a):
    global y
    y += a

funs = {"forward": forward, "up": up, "down": down}

for fname, n in lines:
    funs[fname](n)

print(x, y, x*y)

###################################################
x, y, aim = 0, 0, 0 

def forward_v2(a):
    global x, y, aim
    x += a
    y += aim*a

def up_v2(a):
    global aim 
    aim -= a

def down_v2(a):
    global aim
    aim += a

funs_v2 = {"forward": forward_v2, "up": up_v2, "down": down_v2}
for fname, n in lines:
    funs_v2[fname](n)
print(x, y, x*y)
