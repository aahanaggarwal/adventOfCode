import math

file = open("inputs/day9.txt", "r")
test_file = open("inputs/day9_test.txt", "r")

lines = file.readlines()
map = []
for line in lines:
    map.append([int(num) for num in list(line.strip())])

remaining_points = set()
explored_points = set()

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] != 9: remaining_points.add((i, j))

def get_basin_size(point):
        x, y = point

        if x >= len(map) or x < 0: return 0
        if y >= len(map[0]) or y < 0: return 0
        if map[x][y] == 9: return 0
        if point in explored_points: return 0

        explored_points.add(point)
        
        neighbors = [
            get_basin_size((x-1, y)),
            get_basin_size((x+1, y)),
            get_basin_size((x, y-1)),
            get_basin_size((x, y+1))
        ]
        return sum(neighbors) + 1

sizes = []
while len(remaining_points) > 0:
    curr_point = remaining_points.pop()
    curr_size = get_basin_size(curr_point)
    sizes.append(curr_size)

print(math.prod(sorted(sizes)[-3:]))