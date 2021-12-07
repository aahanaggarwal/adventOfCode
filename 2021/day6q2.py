from collections import defaultdict


file = open("inputs/day6.txt", 'r')
nums_str = file.readline()

nums = nums_str.strip().split(',')
nums = [int(i) for i in nums]

test_nums = [3,4,3,1,2]
# nums = test_nums

nums = sorted(nums)
print(nums)

counts = defaultdict(int)
for num in nums:
    counts[num] += 1

day = 256

print(counts)

while day > 0:
    
    curr_keys = sorted(list(counts.keys()))
    if -1 in curr_keys:
        curr_keys.remove(-1)
    for num in curr_keys:
        counts[num-1] += counts[num]
        counts[num] = 0


    if counts[-1] > 0:
        counts[8] += counts[-1]
        counts[6] += counts[-1]
        counts[-1] = 0

    day -= 1

print(sum(counts.values()))