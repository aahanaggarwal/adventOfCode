import math

file = open("inputs/day10.txt", "r")
test_file = open("inputs/day10_test.txt", "r")
# file = test_file

lines = file.readlines()

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

total_points = 0

close_to_open = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

for line in lines:
    stack = []
    for char in line:
        if char in close_to_open.keys():
            top = stack[-1]
            if close_to_open[char] == top:
                stack.pop()
            else:
                total_points += points[char]
                break
        else:
            stack.append(char)

print(total_points)
