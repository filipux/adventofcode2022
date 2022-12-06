text = open("06.txt").read().splitlines().pop()

def findUniqueSequence(text, count):
    for i in range(0, len(text)-count+1):
        chars = text[i:i+count]
        if len(set(chars)) == count:
            return i+count

p1 = findUniqueSequence(text, 4)
print("Part 1:", p1)

p2 = findUniqueSequence(text, 14)
print("Part 2:", p2)