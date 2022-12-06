import re

def readData():
    stacks = [[]]
    lines = open("05.txt").read().splitlines()
    for x in range(1, len(lines[0]), 4):
        stacks.append([])
        for y in range(0, len(lines)):
            v = lines[y][x]
            if v.isdigit(): break
            if v != " ": stacks[-1].insert(0, v)
            
    moves = [y for y in [list(map(int, re.findall("\d+", x))) for x in lines] if len(y) == 3]
    return (stacks, moves)


def crane(stacks, moves, inChunks):
    for (c,x,y) in moves:
        for r in range(0,c):
            index = r-c if inChunks else -1
            stacks[y].append(stacks[x].pop(index))

    return "".join([c[-1] for c in stacks[1:]])
    

stacks, moves = readData()
p1 = crane(stacks, moves, False)

stacks, moves = readData()
p2 = crane(stacks, moves, True)

print("Part 1:", p1)
print("Part 2:", p2)