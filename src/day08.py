COMPARE_OPERATORS = {
    '>': lambda x, y: x > y,
    '<': lambda x, y: x < y,
    '<=': lambda x, y: x <= y,
    '>=': lambda x, y: x >= y,
    '==': lambda x, y: x == y,
    '!=': lambda x, y: x != y
}

OPERATORS = {
    'inc': lambda x, y: x + y,
    'dec': lambda x, y: x - y
}

file = open("day08.txt").readlines()
nums = {}
highest = 0
for line in file:
    to_increment, op, num, cond, to_check, comp_op, num2 = line.split()
    if to_check not in nums:
        nums[to_check] = 0
    if to_increment not in nums:
        nums[to_increment] = 0
    if COMPARE_OPERATORS[comp_op](nums[to_check], int(num2)):
        nums[to_increment] = OPERATORS[op](nums[to_increment], int(num))

print(max([x for x in nums.values()]))


