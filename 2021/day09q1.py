from collections import defaultdict

file = open("inputs/day9.txt", "r")
test_file = open("inputs/day9_test.txt", "r")
# file = test_file

lines = file.readlines()
map = []

def get_line_lows(x):
    n = len(x)
    out = [False] * n

    if x[0] < x[1]: out[0] = True

    for i in range(1, n-1):
        if x[i] < x[i-1] and x[i] < x[i+1]: out[i] = True

    if x[n-1] < x[n-2]: out[n-1] = True

    return out

for line in lines:
    nums = list(line.strip())
    nums = [int(num) for num in nums]
    map.append(nums)

horizontal_lows = []
for line in map:
    horizontal_lows.append(get_line_lows(line))

# transpose map
map_T = list(zip(*map))
vertical_lows = []
for line in map_T:
    vertical_lows.append(get_line_lows(line))

vertical_lows_T = list(zip(*vertical_lows))

risk_level_sum = 0
for i in range(len(horizontal_lows)):
    for j in range(len(horizontal_lows[0])):
        if horizontal_lows[i][j] and vertical_lows_T[i][j]:
            risk_level_sum += map[i][j] + 1

print(risk_level_sum)
