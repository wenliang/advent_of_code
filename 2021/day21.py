from collections import Counter
from functools import lru_cache

def get_deterministic_dice():
    i = 0
    counts = 0
    while True:
        s = []
        for j in range(3):
            i = 1 if i==100 else i+1
            counts += 1
            s.append(i)
        yield sum(s), counts

def get_current_position(p1, dice):
    return (p1+dice-1) % 10 + 1

def q1():
    # NOTE: this is my input
    position = [8, 2]
    scores = [0, 0]

    gamer = 0
    for d, counts in get_deterministic_dice():
        position[gamer] = get_current_position(position[gamer], d)
        scores[gamer] += position[gamer]
        # print("gamer {}, dice {}, scores {}, position {}".format(gamer+1, d, scores[gamer], position[gamer]))

        if scores[gamer] >= 1000:
            print("q1 final, position {} -> scores {}".format(position, scores))
            if gamer == 0:
                print("Q1: winner 1, {}*{} = {}".format(scores[1], counts, scores[1]*counts))
                return
            else:
                print("Q1: winner 0, {}*{} = {}".format(scores[0], counts, scores[0]*counts))
                return

        gamer = (gamer+1) % 2

def quantum_3rolls_freq():
    a = []
    for i1 in range(1, 4):
        for i2 in range(1, 4):
            for i3 in range(1, 4):
                a.append(i1+i2+i3)
    return Counter(a)
# the odds of 3 rolls
rolls = quantum_3rolls_freq()
print(rolls)

@lru_cache(40000)
def p1_move(p1, s1, p2, s2):
    total = [0, 0]
    for step, r2 in rolls.items():
        p, s = p1, s1
        p = (p + step - 1) % 10 + 1
        s += p

        if s >= 21:
            total[0] += r2
        else:
            t1 = p2_move(p, s, p2, s2)
            total = [a+b*r2 for a, b in zip(total, t1)]
    return total

@lru_cache(40000)
def p2_move(p1, s1, p2, s2):
    total = [0, 0]
    for step, r2 in rolls.items():
        p, s = p2, s2
        p = (p + step - 1) % 10 + 1
        s += p

        if s >= 21:
            total[1] += r2
        else:
            t1 = p1_move(p1, s1, p, s)
            total = [a+b*r2 for a, b in zip(total, t1)]
    return total

def q2():


    # test input
    # positions = (4, 8)
    # my input
    positions = (8, 2)
    wins = p1_move(positions[0], 0, positions[1], 0)
    
    print("Q2: {}".format(wins))


q1()
q2()
