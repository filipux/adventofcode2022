def points(f): return ord(f) - 96 if f.islower() else ord(f) - 38

lines = open("03.txt").read().splitlines()

rucksacks = [[set(x[:len(x)//2]), set(x[len(x)//2:])] for x in lines]
points1 = sum([points((r[0] & r[1]).pop()) for r in rucksacks])
print("Part 1:", points1)

chunks = [lines[i:i+3] for i in range(0,len(lines),3)]
points2 = sum([points((set(c[0]) & set(c[1]) & set(c[2])).pop()) for c in chunks])
print("Part 2:", points2)