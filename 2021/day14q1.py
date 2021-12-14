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

for step in range(10):
    additions = []
    for rule in rules:
        index = template.find(rule[0])
        sub_template = template

        while index != -1:
            print(rule, index)
            additions.append((rule[1], index + (len(template) - len(sub_template))))
            sub_template = sub_template[index + 1:]
            index = sub_template.find(rule[0])

    additions.sort(key=lambda x: x[1])
    print(template, additions)

    for i, addition in enumerate(additions):
        index_to_add = addition[1] + 1 + i
        letter_to_add = addition[0]
        template = template[:index_to_add] + letter_to_add + template[index_to_add:]

template = list(template)
print(len(template))
letters = set(template)
counts = []
for letter in letters:
    counts.append(template.count(letter))

print(max(counts) - min(counts))
