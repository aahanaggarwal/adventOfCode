from collections import defaultdict
import heapq
import numpy as np

file = open("inputs/day15.txt", 'r')
test_file = open("inputs/day15_test.txt", 'r')
weird_file = open("inputs/day15_weird.txt", 'r')
# file = test_file
# file = weird_file

def add_modulo(a, d):
    y = []
    for x in a:
        y.append(x + d if x + d < 10 else x + d - 9)
    return y


map = [[int(x) for x in line[:-1]] for line in file.readlines()]

full_new_map = []
for i in range(5):
    new_row = []
    for j in range(5):
        new_map = []
        for line in map:
            new_line = add_modulo(line, i + j)
            new_map.append(new_line)
        new_row.append(new_map)
    full_new_map.append(np.concatenate(np.array(new_row, dtype=int), axis=1))
full_new_map = np.concatenate(np.array(full_new_map, dtype=int))
map = np.ndarray.tolist(full_new_map)

max_row = len(map) - 1
max_col = len(map[0]) - 1

dist = defaultdict(lambda: float('inf'))
visited = set()
source = (0, 0)
target = (max_row, max_col)
dist[source] = 0

def get_neighbors(point):
    x, y = point
    neighbors = []
    if x > 0:
        neighbors.append((x - 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if x < max_row:
        neighbors.append((x + 1, y))
    if y < max_col:
        neighbors.append((x, y + 1))

    return set(neighbors) - visited


to_visit = []
heapq.heappush(to_visit, (0, source))

def set_dist_to_target(point):
    if point in visited:
        return dist[point]

    neighbors = get_neighbors(point)
    for x_n, y_n in neighbors:
        alt = dist[point] + map[x_n][y_n]
        if alt < dist[(x_n, y_n)]:
            dist[(x_n, y_n)] = alt

    visited.add(point)


to_visit_set = set()
to_visit_set.add(source)
while len(to_visit) > 0 and target not in visited:
    _, curr = heapq.heappop(to_visit)
    to_visit_set.remove(curr)
    set_dist_to_target(curr)
    for neighbor in get_neighbors(curr):
        weight = dist[neighbor]
        if neighbor not in visited and neighbor not in to_visit_set:
            heapq.heappush(to_visit, (weight, neighbor))
            to_visit_set.add(neighbor)


print(dist[target])
