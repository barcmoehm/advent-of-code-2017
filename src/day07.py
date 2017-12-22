from collections import defaultdict

content = [line.strip().split() for line in open("day7.txt").readlines()]
programs = []
tops = set()
weights = {}
children = defaultdict(list)

for line in content:
    programs.append(line[0])
    weights[line[0]] = int(line[1].strip('()'))

    if '->' in line:
        i = line.index('->')
        temp = children[programs[-1]] = [c.strip(',') for c in line[i + 1:]]
        for t in temp:
            tops.add(t)

for p in programs:
    if p not in tops:
        root = p


def unbalanced(children, weights, root):
    expected = None
    wsum = weights[root]
    for c in children[root]:
        c_weight = unbalanced(children, weights, c)
        wsum += c_weight
        if expected is None:
            expected = c_weight
        elif expected != c_weight:
            print(expected - (c_weight - weights[c]))
    return wsum


unbalanced(children, weights, root)
