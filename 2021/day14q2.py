from collections import defaultdict

file = open("inputs/day14.txt", 'r')
test_file = open("inputs/day14_test.txt", 'r')
# file = test_file

template, rules_str = file.read().split("\n\n")
rules = set()
for rule_str in rules_str.split("\n"):
    if rule_str.strip() == "":
        break
    from_str, to = rule_str.split(" -> ")
    rules.add((from_str, to))

pairs = defaultdict(int)
overlaps = defaultdict(int)
for i in range(1, len(template)):
    pairs[template[i - 1] + template[i]] += 1

for step in range(40):
    new_pairs = defaultdict(int)
    for rule in rules:
        if rule[0] in pairs:
            new_pairs[rule[0][0] + rule[1]] += pairs[rule[0]]
            new_pairs[rule[1] + rule[0][1]] += pairs[rule[0]]

    pairs = new_pairs
    print(pairs, overlaps)

counts = defaultdict(float)
counts[template[0]] += 1
for key, val in pairs.items():
    counts[key[1]] += val

print(max(counts.values()) - min(counts.values()))
