from collections import Counter

with open("day03_input.txt", "r") as f:
    instructions = [a for a in f.readline().strip()]

def move_1(instruction, pos):
    neighbours = {
            ">": (pos[0]+1, pos[1]),
            "<": (pos[0]-1, pos[1]),
            "^": (pos[0], pos[1]+1),
            "v": (pos[0], pos[1]-1),
            }
    return neighbours[instruction]


def moves_q1(instructions):
    visited = [(0, 0)]
    pos = (0, 0)
    for i in instructions:
        pos = move_1(i, pos)
        visited.append(pos)

    return Counter(visited)

def moves_q2(instructions):
    visited = [(0, 0)]
    pos = [(0, 0), (0, 0)]
    for i, instru in enumerate(instructions):
        pos[i%2] = move_1(instru, pos[i%2])
        visited.append(pos[i%2])

    return Counter(visited)
        
count = moves_q1(instructions)
print(len(count))
count = moves_q2(instructions)
print(len(count))
