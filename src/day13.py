with open("day13.txt") as file:
    content = file.read().strip().split("\n")
guards = {}
total = 0
for line in content:
    layer_depth, layer_range = map(int, line.split(": "))
    guards[layer_depth] = layer_range
    total += layer_range * layer_depth if layer_depth % ((layer_range - 1) * 2) == 0 else 0

wait = 0
caught = True
while caught:
    caught = False
    for i in guards.keys():
        r = guards[i]
        if (i + wait) % ((r - 1) * 2) == 0:
            caught = True
            wait += 1
            break

print(total)
print(wait)
