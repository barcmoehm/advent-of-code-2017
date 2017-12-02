def checkSum1(fname):
    with open(fname) as file:
        content = file.readlines()

    sum = 0
    content = [[int(d) for d in line.strip().split()] for line in content]
    for line in content:
        sum += (max(line) - min(line))
    print(sum)
    return sum

def checkSum2(fname):
    with open(fname) as file:
        content = file.readlines()
    sum = 0
    content = [[int(d) for d in line.strip().split()] for line in content]
    for line in content:
        size = len(line)
        flag = False
        for i in range(0, size):
            for j in range(0, size):
                part1 = max(line[i], line[j])
                part2 = min(line[i], line[j])
                if(i != j and not flag and (part1%part2 == 0)):
                    sum+= part1//part2
                    flag = True
    return sum

checkSum1('day02.txt')
checkSum2('day02.txt')

