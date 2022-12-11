lines = open("07.txt").read().splitlines()

files = {"name":"/", "size":0, "isFolder":True, "children":[]}
curr = files

def addChild(parent, name, isFolder, size):
    child = {"name":name, "size":size, "isFolder":isFolder, "children":[], "parent": parent}
    parent["children"].append(child)
    return child

def updateFolderSizes(parent):
    size = 0
    folders = [c for c in parent["children"] if c["isFolder"]]
    for f in folders: updateFolderSizes(f)
    for child in parent["children"]: size += child["size"]
    parent["size"] = size

for row in lines:
    a,b,c = (row.split(" ")+ [""])[0:3]
    if a == "$":
        if b == "cd":
            if c == "..":
                curr = curr["parent"]
            elif c == "/":
                pass
            else:
                curr = addChild(curr, c, True, None)
        elif b == "ls":
            pass
    else:
        if a == "dir":
            pass
        elif a.isdigit():
            addChild(curr, b, False, int(a))


updateFolderSizes(files)

def part1(root):
    size = 0
    folders = [root]
    while len(folders) > 0:
        parent = folders.pop()
        folders = folders + [c for c in parent["children"] if c["isFolder"]]

        if parent["size"] <= 100000:
            size = size + parent["size"]
    
    return size
    
def part2(root, target):
    bestSize = root["size"]
    folders = [root]
    while len(folders) > 0:
        parent = folders.pop()
        folders = folders + [c for c in parent["children"] if c["isFolder"]]
        availableAfterDelete = 70000000 - root["size"] + parent["size"]
        if availableAfterDelete >= 30000000 and parent["size"] < bestSize:
            bestSize = parent["size"]
    
    return bestSize

p1 = part1(files)
print("p1", p1)

p2 = part2(files, p1)
print("p2", p2)
