import re
from functools import reduce


def match_len(x):
    return len(x) - 2


with open("day09.txt") as file:
    content = [line.strip() for line in file]
    pattern = re.compile(r"<.*?>")
    pattern2 = re.compile("!.")

    def add_lens(x, y) : return x + y

    for line in content:
        line = pattern2.sub("", line)
        garbage_count2 = reduce(add_lens, map(match_len, pattern.findall(line)))
        idx = 0
        count = 0
        depth = 0
        line = pattern.sub("", line)
        while idx < len(line):
            if line[idx] == "{":
                depth += 1
                count += 1 * depth
            elif line[idx] == "}":
                depth -= 1
            idx += 1
        print(count)
        print(garbage_count2)




