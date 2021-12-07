# open file
file = open("inputs/day1.txt", "r")

# store each line as int in list
lines = [int(line) for line in file]

increasing = 0
for i in range(1, len(lines)):
    if lines[i] > lines[i-1]:
        increasing += 1

print(increasing)