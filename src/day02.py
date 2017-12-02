def checkSum1(fname):
    with open(fname) as file:
        content = file.readlines()

    sum = 0
    content = [line.strip().split() for line in content]
    for line in content:
        
        line= list(map(int, line))
        sum += (max(line) - min(line))
    print(sum)
    return sum


checkSum1('day02.txt')
