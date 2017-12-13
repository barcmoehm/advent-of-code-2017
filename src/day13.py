with open("day13.txt") as file:
    content = file.read().strip().split("\n")
total = 0
for line in content:
    layer_depth, layer_range = map(int, line.split(": "))
    total += layer_range * layer_depth if layer_depth % ((layer_range - 1) * 2) == 0 else 0
print(total)
