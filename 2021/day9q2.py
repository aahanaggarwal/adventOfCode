from collections import defaultdict

file = open("inputs/day9.txt", "r")
test_file = open("inputs/day9_test.txt", "r")

lines = file.readlines()
map = []

map_of_nines = []
for line in lines:
    nums = list(line.strip())
    nums = [int(num) for num in nums]
    nines = [num == 9 for num in nums]
    map_of_nines.append(nines)
    print(nines)
    map.append(nums)

remaining_points = set()
explored_points = set()

for i in range(len(map)):
    for j in range(len(map[i])):
        if not map_of_nines[i][j]: remaining_points.add((i, j))

sizes = []

while len(remaining_points) > 0:

    def get_basin_size(point):
        x, y = point
        if x >= len(map) or x < 0: return 0
        if y >= len(map[0]) or y < 0: return 0

        if point in explored_points or point not in remaining_points: return 0

        remaining_points.remove(point)
        explored_points.add(point)

        neighbors = [
            get_basin_size((x-1, y)),
            get_basin_size((x+1, y)),
            get_basin_size((x, y-1)),
            get_basin_size((x, y+1))
        ]

        return sum(neighbors) + 1

    curr_point = remaining_points.pop()
    remaining_points.add(curr_point)
    curr_size = get_basin_size(curr_point)
    sizes.append(curr_size)

sizes = sorted(sizes)
print(sizes[-1] * sizes[-2] * sizes[-3])