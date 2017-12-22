content = [line.strip().split() for line in open("day7.txt").readlines()]
programs = []
tops = set()
for line in content:
    programs.append(line[0])
    if '->' in line:
        i = line.index('->')
        children = [c.strip(',') for c in line[i + 1:]]
        for c in children:
            tops.add(c)

for p in programs:
    if p not in tops:
        print(p)


