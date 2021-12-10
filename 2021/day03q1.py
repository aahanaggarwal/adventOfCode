from collections import defaultdict

file = open("inputs/day3.txt", "r")

lines = file.readlines()

lines = [line.strip() for line in lines]

counts = defaultdict(int)

for line in lines:
    for index in range(len(line)):
        counts[index] += int(line[index])

ratios = []
for index in counts.keys():
    ratios.append(counts[index] / len(lines))

print(ratios)

epsilon = 0b101110100101
lambda1 = 0b010001011010

# convert to decimal
epsilon = 2981
lambda1 = 1114

print(epsilon*lambda1)