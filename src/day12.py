from collections import defaultdict


def connected(neighbours, start, seen=set()):
    if start in seen:
        return 0
    else:
        seen.add(start)
        return 1 + sum([connected(neighbours, n, seen) for n in neighbours[start]])


def connected_group(neighbours, start, seen=set()):
    if start in seen:
        return seen
    else:
        seen.add(start)
        # print(seen)
        for child in neighbours[start]:
            seen = connected_group(neighbours, child, seen)
        # print(seen)
        return seen


programs = defaultdict(set)
with open('day12.txt') as content:
    for line in content:
        left, right = line.strip().split(' <-> ')
        programs[left] = set(right.split(', '))
        [programs[p].add(left) for p in programs[left]]

print(connected(programs, '0'))

groups = set()
for key in programs.keys():
    # hashable (immutable) set
    groups.add(frozenset(connected_group(programs, key)))

print(len(groups))
