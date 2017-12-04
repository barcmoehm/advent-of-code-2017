def solve1(filename):
    with open(filename) as file:
        content = [line.strip().split() for line in file.readlines()]
        return [sum([li.count(s) for s in li]) == len(li) for li in content].count(True)


def solve2(filename):
    count = 0
    with open(filename) as file:
        content = [line.strip().split() for line in file.readlines()]
        for line in content:
            sort = ["".join(sorted(s)) for s in line]
            if len(sort) == len(set(sort)):
                count += 1

    return count


print(solve1("day04.txt"))
print(solve2("day04.txt"))