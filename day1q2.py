# open file

file = open("inputs/day1.txt", "r")

# store each line as int in list
lines = [int(line) for line in file]

# take running sum every 3 elements
running_sums = []
for i in range(0, len(lines)):
    running_sums.append(sum(lines[i:i+3]))

print(running_sums)

# now check increasing
increasing = 0
for i in range(1, len(running_sums)):
    if running_sums[i] > running_sums[i-1]:
        increasing += 1

print(increasing)