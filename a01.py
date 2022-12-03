lines = open("01.txt").read().split("\n\n")
elves = [x.splitlines() for x in lines]
elvesCalories = sorted([sum([int(y) for y in x]) for x in elves])

maxCalories = elvesCalories[-1]
topThreeMaxCalories = sum(elvesCalories[-3:])

print("Part 1:", maxCalories)
print("Part 2:", topThreeMaxCalories)