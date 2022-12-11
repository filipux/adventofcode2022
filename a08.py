

lines = [list(map(int, list(x))) for x in open("08_test.txt").read().splitlines()]
vis = [[0 for x in range(len(lines[0]))] for x in range(len(lines))]

def rotate():
    global lines, vis
    lines = [list(x) for x in list(zip(*lines[::-1]))]
    vis = [list(x) for x in list(zip(*vis[::-1]))]

def look():
    for y in range(len(lines)):
        vis[y][0] = vis[y][-1] = 1
        for x in range(len(lines[0])):
            if vis[y][x] == 1 or lines[y][x] > max(lines[y][0:x]):
                vis[y][x] = 1   

look()
rotate()
look()
rotate()
look()
rotate()
look()
rotate()

p1 = str(vis).count("1")
print("Part 1:", p1)


# I guess beam could be used to solve p1 too?

def beam(x, y, dx, dy):
    count = 0
    value = lines[y][x]
    xrange = range(len(lines[0]))
    yrange = range(len(lines))
    while True:
        x += dx
        y += dy
        if x not in xrange or y not in yrange: return count
        count += 1
        if lines[y][x] >= value: return count
        
p2 = 0
for y, row in enumerate(lines):
    for x, c in enumerate(row):
        value = lines[y][x]
        a = beam(x,y,-1,0)
        b = beam(x,y,+1,0)
        c = beam(x,y,0,-1)
        d = beam(x,y,0,+1)
        p2 = max(p2, a*b*c*d)

print("Part 2:", p2)