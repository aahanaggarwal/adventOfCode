from collections import defaultdict
from enum import Enum
from typing import List

file = open("inputs/day12.txt", 'r')
test_file = open("inputs/day12_test.txt", 'r')
test_file2 = open("inputs/day12_test2.txt", 'r')
test_file3 = open("inputs/day12_test3.txt", 'r')

lines = file.readlines()


class CaveType(Enum):
    START = "start"
    END = "end"
    BIG = 1
    SMALL = 2


def node_type(node: str) -> CaveType:
    if node == "end":
        return CaveType.END
    if node == "start":
        return CaveType.START
    if node == node.upper():
        return CaveType.BIG
    return CaveType.SMALL


map = defaultdict(set)
for line in lines:
    one, two = line[:-1].split("-")
    map[one].add(two)
    map[two].add(one)


# really straightforward dfs solution, don't think i need memo because we
# are always exploring a diff path


def ways_to_end(node: str, curr_path: List[str]) -> int:
    if node_type(node) == CaveType.END:
        return 1
    if node_type(node) == CaveType.SMALL and node in curr_path:
        return 0
    if node_type(node) == CaveType.START and node in curr_path:
        return 0

    # now i am at some node which I can explore from
    # go through all neighbors, and add their vals

    curr_ways = 0
    new_path = curr_path + [node]

    for neighbor in map[node]:
        # list copy always gets me, anticipated it this time
        curr_ways += ways_to_end(neighbor, new_path.copy())

    return curr_ways


print(map)
print(ways_to_end("start", []))
