content = open("day16.txt").read().strip().split(",")
letters = list("abcdefghijklmnop")


def solve(lst):
    for move in content:
        if move[0] == 's':
            i = int(move[1:])
            lst = lst[-i:] + lst[:-i]
        elif move[0] == 'x':
            a, b = map(int, move[1:].split('/'))
            lst[a], lst[b] = lst[b], lst[a]
        elif move[0] == 'p':
            a, b = move[1:].split('/')
            ia = lst.index(a)
            ib = lst.index(b)
            lst[ia], lst[ib] = lst[ib], lst[ia]
    print(''.join(lst))


solve(letters)
