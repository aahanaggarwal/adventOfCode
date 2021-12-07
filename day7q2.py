file = open("inputs/day7.txt", "r")

nums = [int(i) for i in file.readline().split(",")]

test_nums = [16,1,2,0,4,2,7,1,2,14]
# nums = test_nums

costs = [0, 1]
for i in range(2, max(nums) + 1):
    costs.append(costs[i - 1] + i)


best_candidate = -1
best_candidate_score = float("inf")
for candidate in range(0, max(nums) + 1):
    total = 0
    for other in nums:
        total += costs[abs(candidate - other)]

    if total < best_candidate_score:
        best_candidate = candidate
        best_candidate_score = total

    print(candidate, total)

print("best candidate: ", best_candidate)
print("best candidate score: ", best_candidate_score)