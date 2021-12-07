file = open("inputs/day6.txt", 'r')
nums_str = file.readline()

nums = nums_str.strip().split(',')
nums = [int(i) for i in nums]

test_nums = [3,4,3,1,2]
# nums = test_nums

day = 80

while day > 0:
    new_fish = 0
    nums = [i-1 for i in nums]
    for i, num in enumerate(nums):
        if num == -1:
            nums[i] = 6
            new_fish += 1
    new_fish_arr = [8] * new_fish
    nums.extend(new_fish_arr)
    day -= 1

print(len(nums))