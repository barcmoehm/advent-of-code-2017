def solve1(filename):
    with open(filename) as file:
        content = [int(line.strip()) for line in file]

    idx = 0
    steps = 0
    while 0 <= idx < len(content):
        i = idx
        idx += content[idx]
        content[i] += 1
        steps += 1
    return steps


def solve2(filename):
    with open(filename) as file:
        content = [int(line.strip()) for line in file]

    idx = 0
    steps = 0
    while 0 <= idx < len(content):
        i = idx
        idx += content[idx]
        content[i] += 1 if content[i] < 3 else -1
        steps += 1
    return steps


print(solve1("day05.txt"))
print(solve2("day05.txt"))
