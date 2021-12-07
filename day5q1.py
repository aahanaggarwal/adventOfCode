file = open("inputs/day5.txt", "r")

line_segments = []

grid_size = (1000, 1000)
vertical_lines = []
horizontal_lines = []


for line in file:
    points = line.split(" -> ")
    x1, y1 = points[0].split(",")
    x2, y2 = points[1].split(",")
    y2 = y2.strip()

    if x1 == x2:
        vertical_lines.append((int(x1), int(y1), int(y2)))

    if y1 == y2:
        horizontal_lines.append((int(y1), int(x1), int(x2)))

grid = [[0 for x in range(grid_size[0])] for y in range(grid_size[1])]
for line in vertical_lines:
    print(line)
    x_pos = line[0]
    for i in range(min(line[1], line[2]), max(line[1], line[2]) + 1):
        grid[i][x_pos] += 1

for line in horizontal_lines:
    print(line)
    y_pos = line[0]
    for i in range(min(line[1], line[2]), max(line[1], line[2]) + 1):
        grid[y_pos][i] += 1

count = 0
for i in range(grid_size[0]):
    for j in range(grid_size[1]):
        if grid[i][j] > 1:
            count += 1

print(count)