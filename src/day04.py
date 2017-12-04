def solve1(filename):
    with open(filename) as file:
        content = [line.strip().split() for line in file.readlines()]
        return [sum([li.count(s) for s in li]) == len(li) for li in content].count(True)


print(solve1("day04.txt"))
