file = open("inputs/day13.txt", 'r')
test_file = open("inputs/day13_test.txt", 'r')
file = test_file

lines = file.readlines()
points = set()
instructions = []

for line in lines:
    split = line.split()
    if len(split) == 0:
        continue
    if line.split()[0] == "fold":
        temp = line.split('=')
        axis = temp[0][-1]
        fold_at = int(temp[1][:-1])
        instructions.append((axis, fold_at))
    else:
        temp = line.split(',')
        x = int(temp[0])
        y = int(temp[1])
        points.add((x, y))

instruction = instructions[0]
new_points = set()
for point in points:
    x, y = point
    axis, fold_at = instruction
    if axis == 'y' and y > fold_at:
        diff = y - fold_at
        new_points.add((x, fold_at - diff))
    elif axis == 'x' and x > fold_at:
        diff = x - fold_at
        new_points.add((fold_at - diff, y))

    else:
        new_points.add(point)

print(new_points)
print(len(new_points))
