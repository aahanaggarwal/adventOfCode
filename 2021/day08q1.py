file = open("inputs/day8.txt", "r")

lines = file.readlines()
output_values = []

for line in lines:
    line = line.strip()
    line = line.split("|")
    output_values.append(line[1].split())

unique_digit_lens = [2, 4, 3, 7]

count = 0
for output_value in output_values:
    for string in output_value:
        if len(string) in unique_digit_lens:
            count += 1

print(count)