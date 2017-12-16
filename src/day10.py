def reverse_sublist(lst, start, end):
    sublist = [lst[i % len(lst)] for i in range(start, end)]
    reverse = list(reversed(sublist))
    j = 0
    for i in range(start, end):
        lst[i % len(lst)] = reverse[j]
        j += 1
    return lst


numbers = [i for i in range(0, 256)]
lengths = [[int(d) for d in line.strip().split(",")] for line in open("day10.txt").readlines()][0]
pos = 0
skip = 0
#print(numbers)
for l in lengths:
    start = pos
    end = pos + l
    numbers = reverse_sublist(numbers, start, end)
    #print(numbers)
    pos += (l + skip)
    skip += 1

print(numbers[0] * numbers[1])