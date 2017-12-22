from collections import defaultdict


def connected(neighbours, start, seen=set()):
    if start in seen:
        return 0
    else:
        seen.add(start)
        return 1 + sum([connected(neighbours, n, seen) for n in neighbours[start]])


with open('day12.txt') as inp:
    programs = defaultdict(set)
    for line in inp:
        left, right = line.strip().split(' <-> ')
        programs[left] = set(right.split(', '))
        for p in programs[left]:
            programs[p].add(left)

print(connected(programs, '0'))