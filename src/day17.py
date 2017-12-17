lst = [0]
steps = 335
pos = 0
for i in range(2017):
    pos = (pos + steps) % len(lst) + 1
    lst.insert(pos, i + 1)
print(lst, pos)
print(lst[pos+1])