import re

with open("day09.txt") as file:
    content = [line.strip() for line in file]
    pattern = re.compile(r"<.*?>")
    pattern2 = re.compile("!.")
    for line in content:
        idx = 0
        count = 0
        depth = 0
        line = pattern2.sub("", line)
        line = pattern.sub("", line)
        while idx < len(line):
            if line[idx] == "{":
                depth += 1
                count += 1 * depth
            elif line[idx] == "}":
                depth -= 1
            idx += 1
        print(count)



