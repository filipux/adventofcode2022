lines = open("09.txt").read().splitlines()

def getMove(hx, hy, tx, ty):
    sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)

    distx = abs(hx-tx)
    signx = sign(hx-tx)
    
    disty = abs(hy-ty)
    signy = sign(hy-ty)

    if distx == 2 and disty == 0:
        return (tx+signx, ty)
    elif disty == 2 and distx == 0:
        return(tx, ty+signy)
    elif distx + disty >= 3:
        return (tx+signx, ty+signy)
    return (tx, ty)

def snake(length):
    tailpositions = {}
    tails = [(0,0) for x in range(length)]

    for c in lines:
        dir, s = c.split(" ")
        step = int(s)
        r = {"R": (1,0), "U": (0,-1), "L": (-1,0), "D": (0,1)}
        dx, dy = r[dir]

        for r in range(step):
            tails[0] = (tails[0][0] + dx, tails[0][1] + dy)
            for i in range(1,len(tails)):
                tails[i] = getMove(*tails[i-1], *tails[i])
            tailpositions[tails[-1]] = True

    return len(tailpositions)

p1 = snake(2)
print("Part 1:", p1)

p2 = snake(10)
print("Part 2:", p2)
