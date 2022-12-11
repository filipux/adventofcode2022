lines = open("10.txt").read().splitlines()

crt = ['#' for x in range(240)]
cycles = 0
x = 1
p1 = 0

def cycle():
    global cycles, p1, crt
    if (cycles-20) % 40 == 0: p1 += cycles*x
    if abs(cycles % 40 - x) <= 1: crt[cycles % 240] = '#'
    else: crt[cycles % 240] = ' '
    cycles += 1

for d in lines:
    op, val = (d.split(" ")+[""])[:2]
    if op == "addx":
        cycle()
        cycle()
        x += int(val)
    elif op == "noop":
        cycle()

print("Part 1:", p1)
print("Part 2:")
for i, x in enumerate(crt):
    if i % 40 == 0: print("")
    print(x, end='')
