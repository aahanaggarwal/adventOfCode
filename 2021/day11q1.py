import numpy as np

file = open("inputs/day11.txt", 'r')
test_file = open("inputs/day11_test.txt", 'r')
# file = test_file
nums = [[int(num) for num in list(line)[:-1]] for line in file.readlines()]

nums = np.array(nums)

count = 0


def increase_by_1(r, c):
    if r < 0 or c < 0 or r > 9 or c > 9:
        return
    nums[r, c] += 1


def flash_for(flash_point):
    x, y = flash_point

    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            increase_by_1(x+r, y+c)
    nums[x, y] -= 1


for iter in range(100):
    nums += 1
    flashed_this_step = set()

    while True:
        flash_indices = np.array(np.where(np.ma.masked_greater(nums, 9) > 9))
        flash_points = set(map(tuple, flash_indices.T))
        flash_points = flash_points.difference(flashed_this_step)

        for flash_point in flash_points:
            flash_for(flash_point)

        if len(flash_points) == 0:
            break

        flashed_this_step = flashed_this_step.union(flash_points)

    count += len(flashed_this_step)
    nums[nums > 9] = 0


print(nums)
print(count)
