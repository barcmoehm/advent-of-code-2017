n = 0
steps = 335
pos = 0
for i in range(1, 50000001):
    pos = (pos + steps) % i + 1
    if pos == 1:
        n = i
print(n)



