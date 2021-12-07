file = open("inputs/day2.txt", "r")

lines = file.readlines()

depth = 0
distance = 0

for line in lines:
    [dir, dist] = line.split()
    if dir == "forward":
        depth += int(dist)
    elif dir == "up":
        distance -= int(dist)
    elif dir == "down":
        distance += int(dist)

print(depth, distance)
print(depth*distance)