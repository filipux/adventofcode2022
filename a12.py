lines = open("12.txt").read().splitlines()

valid = set()

for y, row in enumerate(lines):
    for x, c in enumerate(row):
        valid.add((x,y))
        if c == 'S': start = (x,y)
        if c == 'E': end = (x,y)

def height(n):
    x,y = n
    c = lines[y][x]
    if c == 'S': return 0
    if c == 'E': return ord('z') - ord('a')
    return ord(c) - ord('a')

def search(end):
    stack = [end]
    steps = {end:0}
    while len(stack) > 0:
        cur = x,y = stack.pop()
        neighbours = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
        
        for n in neighbours:
            if n in valid and height(cur) - height(n) <= 1:
                if not n in steps or steps[cur] + 1 < steps[n]:
                    stack.append(n)
                    steps[n] = steps[cur] + 1

    return steps


steps = search(end)

p1 = steps[start]
p2 = min([steps[x] for x in steps.keys() if height(x) == 0])

print("Part 1:", p1) 
print("Part 2:", p2) 
