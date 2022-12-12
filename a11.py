import re

def play(rounds, bleh):

    #1. Parse input
    lines = iter(open("11.txt").read().splitlines())
    tryInt = lambda list: [int(x) if len(x) and x[0].isdigit() else x for x in list]
    monkeys = []
    multiplier = 1

    while True:
        monkey = {}
        next(lines) #Monkey 0:
        monkey["items"] = list(map(int,re.findall('\d+', next(lines)))) #   Starting items: 79, 98
        monkey["op"] = tryInt(next(lines).split(" "))[-2:] #   Operation: new = old * 19
        monkey["div"] = tryInt(next(lines).split(" "))[-1] #  Test: divisible by 23
        monkey["true"] = tryInt(next(lines).split(" "))[-1] #    If true: throw to monkey 1
        monkey["false"] = tryInt(next(lines).split(" "))[-1] #    If false: throw to monkey 4
        monkey["inspections"] = 0
        multiplier *= monkey["div"]
        monkeys.append(monkey)
        try: next(lines)
        except: break

    #2. Play!
    for round in range(rounds):
        for i, monkey in enumerate(monkeys):
            for worry in monkey["items"]:
                monkey["inspections"] = monkey["inspections"] + 1
                op, val = monkey["op"]
                
                if val == "old": val = worry

                if op == '*': worry = worry * val
                elif op == "+": worry = worry + val
                elif op == "-": worry = worry - val

                if bleh:
                    worry = worry % multiplier
                else:
                    worry = worry // 3

                throwto = monkey["false"] if worry % monkey["div"] else monkey["true"]
                monkeys[throwto]["items"].append(worry)
            monkey["items"] = []
    s = sorted([monkey["inspections"] for monkey in monkeys])
    return s[-1] * s[-2]


# calculate stuff
p1 = play(20, False)
print("Part 1:", p1)

p2 = play(10000, True)
print("Part 2:", p2)
