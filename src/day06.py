def solve1(fname):
    with open(fname) as file:
        content = list(map(int, [line.split() for line in file][0]))
    seen = {}
    cycles = 0
    while tuple(content) not in seen:
        seen[tuple(content)] = cycles
        i, val = max(enumerate(content), key=lambda k: (k[1], -k[0]))
        content[i] = 0
        while val:
            i = (i+1)%len(content)
            content[i] += 1
            val -= 1
        cycles += 1
    print("total:", len(seen), cycles)
    print("size:", cycles - seen[tuple(content)])

solve1("day06.txt")
