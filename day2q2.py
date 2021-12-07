file = open("inputs/day2.txt", "r")

lines = file.readlines()

depth = 0
distance = 0
aim = 0

for line in lines:
    [dir, dist] = line.split()
    if dir == "forward":
        distance += int(dist)
        depth += aim*int(dist)
    elif dir == "up":
        aim -= int(dist)
    elif dir == "down":
        aim += int(dist)

print(depth, distance)
print(depth*distance)