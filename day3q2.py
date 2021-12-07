from collections import defaultdict

file = open("inputs/day3.txt", "r")

lines = file.readlines()

lines = [line.strip() for line in lines]

one = []
zero = []
master = lines.copy()
index = 0

while len(master) > 1:

    for line in master:
        if line[index] == '0':
            zero.append(line)
        else:
            one.append(line)

    if len(zero) > len(one):
        master = zero.copy()
    else:
        master = one.copy()

    zero = []
    one = []
    index += 1
print(master[0])

one = []
zero = []
master = lines.copy()
index = 0

while len(master) > 1:

    for line in master:
        if line[index] == '0':
            zero.append(line)
        else:
            one.append(line)

    if len(zero) <= len(one):
        master = zero.copy()
    else:
        master = one.copy()

    zero = []
    one = []
    index += 1
print(master[0])