from collections import Counter

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
    p1 += dice
    return (p1-1) % 10 + 1

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

q1()

def quantum_3rolls_freq():
    a = []
    for i1 in range(1, 4):
        for i2 in range(1, 4):
            for i3 in range(1, 4):
                a.append(i1+i2+i3)
    return Counter(a)

def q2():
    wins = [0, 0]

    # the odds of 3 rolls
    rolls = quantum_3rolls_freq()

    def move_x1(gamer, positions, scores, repeat=1):
        for step, r2 in rolls.items():
            position = (positions[gamer]+step-1)%10 + 1
            score = scores[gamer] + position
            if score >= 21:
                wins[gamer] += repeat*r2
                print("winner {}, position {}, scores {}, repeat: {}".format(gamer+1, position, score, repeat*r2))
                # this world will stop
            else:
                if gamer == 0:
                    gamer_2 = 1
                    positions = (position, positions[1])
                    scores = (score, scores[1])
                else:
                    gamer_2 = 0
                    positions = (positions[0], position)
                    scores = (scores[0], score)
                # print("continue {}, positions {}, scores {}".format(gamer_2, positions, scores))
                move_x1(gamer_2, positions, scores, repeat*r2)
    gamer = 0
    # my input
    positions = (8, 2)
    # test input
    positions = (4, 8)
    scores = (0, 0)
    move_x1(gamer, positions, scores, repeat=1)
    
    print(wins)

q2()

    
