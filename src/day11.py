input = [line.strip().split(",")for line in open("day11.txt").readlines()][0]
x = 0
y = 0
highest = 0
for d in input:
    if d == "n":
        x -= 1
        y -= 1
    elif d == "ne":
        x -= 1
    elif d == "nw":
        y -= 1
    elif d == "se":
        y += 1
    elif d == "sw":
        x += 1
    elif d == "s":
        x += 1
        y += 1
    val = abs(x) + abs(y) - min(abs(x), abs(y))
    highest = max(highest, val)
print(abs(x) + abs(y) - min(abs(x), abs(y)))
print(highest)


