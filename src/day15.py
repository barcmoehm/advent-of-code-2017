import itertools


def next_value(v, factor, multiple=1):
    while True:
        v = (v * factor) % 2147483647
        if v % multiple == 0:
            yield v


def compare(a, b):
    return bin(a)[-16:] == bin(b)[-16:]


factor_a = 16807
factor_b = 48271
a, b = next_value(679, factor_a, 4),  next_value(771, factor_b, 8)
count = 0
for a, b in itertools.islice(zip(a, b), 5000000):
    if compare(a, b):
        count += 1


print(count)
