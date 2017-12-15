def next_value(v, factor):
    return (v * factor) % 2147483647


def compare(a, b):
    return bin(a)[-16:] == bin(b)[-16:]


factor_a = 16807
factor_b = 48271

a, b = 679,  771
count = 0
for i in range(0, 40000000):
    a = next_value(a, factor_a)
    b = next_value(b, factor_b)
    if compare(a, b):
        count += 1

print(count)
