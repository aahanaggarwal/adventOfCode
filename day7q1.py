file = open("inputs/day7.txt", "r")

nums = [int(i) for i in file.readline().split(",")]

test_nums = [16,1,2,0,4,2,7,1,2,14]
nums = test_nums

best_candidate = -1
best_candidate_score = float("inf")
for candidate in nums:
    total = 0
    for other in nums:
        total += abs(candidate - other)
    if total < best_candidate_score:
        best_candidate = candidate
        best_candidate_score = total


print(best_candidate_score)