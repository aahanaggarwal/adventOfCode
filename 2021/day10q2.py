import math

file = open("inputs/day10.txt", "r")
test_file = open("inputs/day10_test.txt", "r")
# file = test_file

lines = file.readlines()

points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

close_to_open = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

open_to_close = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

all_line_points = []

for line in lines:
    stack = []
    valid = True
    for char in line:
        if char in close_to_open.keys():
            top = stack[-1]
            if close_to_open[char] == top:
                stack.pop()
            else:
                valid = False
                break
        elif char != '\n':
            stack.append(char)

    if not valid:
        continue
    line_points = 0
    while len(stack) > 0:
        top = stack[-1]
        stack.pop()

        curr_points = points[open_to_close[top]]
        line_points = (line_points*5) + curr_points

    all_line_points.append(line_points)

all_line_points.sort()
print(all_line_points[len(all_line_points)//2])
