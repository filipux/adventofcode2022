lines = open("02.txt").read().splitlines()
points = {
    'A X': 3+1,
    'A Y': 6+2,
    'A Z': 0+3,
    'B X': 0+1,
    'B Y': 3+2,
    'B Z': 6+3,
    'C X': 6+1,
    'C Y': 0+2,
    'C Z': 3+3
    }
total1 = sum([points[x] for x in lines])
print("Part 1:", total1)

points2 = {
    'A X': 3+0,
    'A Y': 1+3,
    'A Z': 2+6,
    'B X': 1+0,
    'B Y': 2+3,
    'B Z': 3+6,
    'C X': 2+0,
    'C Y': 3+3,
    'C Z': 1+6
    }
total2 = sum([points2[x] for x in lines])
print("Part 2:", total2)
