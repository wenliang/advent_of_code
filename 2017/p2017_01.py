with open("p2018_01_input.txt", "r") as f:
    line = f.readline()
N = len(line)-1
delta = int(N/2)
# print(N)
line2 = "{}{}".format(line[:-1], line[:delta])
# print(line2)
sum = 0
for i in range(N):
    c1 = line2[i]
    c2 = line2[i+delta]
    if c1 == c2:
        sum += int(c1)
print(sum)
