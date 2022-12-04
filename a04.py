import re

lines = open("04.txt").read().splitlines()
v = [[int(y) for y in re.findall(r'\d+', x)] for x in lines]

p1 = p2 = 0
for x in v:
    a = set(range(x[0], x[1]+1))
    b = set(range(x[2], x[3]+1))
    if(a & b == a or a & b == b):
        p1 = p1 + 1
    if(len(a & b) > 0):
        p2 = p2 + 1

print("Part 1:", p1)
print("Part 2:", p2)
