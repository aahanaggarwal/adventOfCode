from collections import defaultdict
import heapq
from functools import lru_cache

file = open("inputs/day15.txt", 'r')
test_file = open("inputs/day15_test.txt", 'r')
weird_file = open("inputs/day15_weird.txt", 'r')
# file = test_file
file = weird_file

map = [[int(x) for x in line[:-1]] for line in file.readlines()]
max_row = max_col = len(map) - 1

dist = defaultdict(lambda: float('inf'))
visited = set()
source = (0, 0)
target = (max_row, max_col)
dist[source] = 0

@lru_cache(maxsize=32)
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

    return neighbors


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


while len(to_visit) > 0:
    _, curr = heapq.heappop(to_visit)
    set_dist_to_target(curr)
    for neighbor in get_neighbors(curr):
        if neighbor not in visited:
            heapq.heappush(to_visit, (dist[neighbor], neighbor))


print(dist[target])
